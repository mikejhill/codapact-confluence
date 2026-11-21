"""Markdown in, Markdown out: Confluence page, blog post and comment bodies as Markdown.

Confluence stores bodies as Atlassian Document Format (ADF), and also offers ``storage``
(XHTML) and ``wiki``. With ``--doc-format markdown`` (the default;
``CONFLUENCE_DOC_FORMAT`` sets it too):

* a ``body`` given as a Markdown string, or as ``{"representation": "markdown", "value":
  ...}``, is sent as ADF (``atlas_doc_format``);
* commands that take ``--body-format`` ask for ``atlas_doc_format`` unless you choose
  another format, and every ADF body in a response comes back as
  ``{"representation": "markdown", "value": ...}`` (under the key ``markdown``).

``--doc-format adf`` sends and returns bodies unchanged. Conversion uses adflux with its
Confluence profile: macros (``::toc``, ``:::info``, ``:jira[KEY-1]``...), emoticons,
layouts. ``uvx adflux syntax`` documents the dialect; ``uvx adflux macros NAME`` shows a
macro's parameters.
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Any

from adflux import to_adf, to_markdown

PROFILE = "confluence"
ADF = "atlas_doc_format"
CHOICES = ("markdown", "adf")


def _adf_body(markdown: str) -> dict[str, str]:
    return {"representation": ADF, "value": json.dumps(to_adf(markdown, PROFILE), ensure_ascii=False)}


def to_wire(value: Any, key: str | None = None) -> Any:
    """Convert Markdown bodies to ADF bodies, recursively."""
    if key == "body" and isinstance(value, str):
        return _adf_body(value)
    if isinstance(value, dict):
        if value.get("representation") == "markdown" and isinstance(value.get("value"), str):
            return _adf_body(value["value"])
        return {k: to_wire(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return [to_wire(v, key) for v in value]
    return value


def is_adf(value: Any) -> bool:
    """Whether ``value`` is an ADF document."""
    return isinstance(value, dict) and value.get("type") == "doc" and isinstance(value.get("content"), list)


def from_wire(value: Any) -> Any:
    """Convert ADF bodies (and bare ADF documents) in ``value`` to Markdown, recursively."""
    if is_adf(value):
        return to_markdown(value, PROFILE)
    if isinstance(value, dict):
        if value.get("representation") == ADF and isinstance(value.get("value"), str) and value["value"]:
            return {**value, "representation": "markdown", "value": to_markdown(value["value"], PROFILE)}
        out: dict[str, Any] = {}
        for k, v in value.items():
            converted = from_wire(v)
            if k == ADF and isinstance(converted, dict) and converted.get("representation") == "markdown":
                out["markdown"] = converted
            else:
                out[k] = converted
        return out
    if isinstance(value, list):
        return [from_wire(v) for v in value]
    return value


class MarkdownHook:
    """Call hook that converts bodies between Markdown and ADF."""

    def __init__(self, markdown: str | None = None) -> None:
        self.markdown = markdown

    def before(self, operation: Any, arguments: dict[str, Any]) -> dict[str, Any]:
        if self.markdown is not None:
            request = arguments.get("body")
            if not isinstance(request, dict):
                raise ValueError("--markdown is for commands that send a page, post or comment body")
            arguments = {**arguments, "body": {**request, "body": self.markdown}}
        out = {k: to_wire(v) if isinstance(v, dict | list) else v for k, v in arguments.items()}
        names = {p.name for p in getattr(operation, "params", ())}
        if "body_format" in names and out.get("body_format") is None:
            out["body_format"] = ADF
        return out

    def after(self, operation: Any, result: Any) -> Any:
        del operation
        return from_wire(result)


class Extension:
    """``cli.extensions`` entry: the ``--doc-format`` option."""

    def __init__(self, runtime: Any) -> None:
        self.prefix = getattr(runtime, "env_prefix", "CONFLUENCE")

    def add_options(self, group: argparse._ArgumentGroup, hidden: bool) -> None:
        group.add_argument(
            "--doc-format",
            choices=CHOICES,
            default=argparse.SUPPRESS,
            help=argparse.SUPPRESS
            if hidden
            else f"bodies as markdown (default) or raw adf JSON (env {self.prefix}_DOC_FORMAT)",
        )
        group.add_argument(
            "--markdown",
            metavar="TEXT|@FILE|@-",
            default=argparse.SUPPRESS,
            help=argparse.SUPPRESS
            if hidden
            else "the body to send, as Markdown text, @file, or @- for stdin (instead of --body JSON)",
        )

    def format(self, args: argparse.Namespace) -> str:
        chosen = getattr(args, "doc_format", None) or os.environ.get(f"{self.prefix}_DOC_FORMAT") or "markdown"
        if chosen not in CHOICES:
            raise ValueError(f"{self.prefix}_DOC_FORMAT must be markdown or adf")
        return chosen

    def hooks(self, args: argparse.Namespace) -> list[Any]:
        markdown = _read(getattr(args, "markdown", None))
        if self.format(args) != "markdown":
            if markdown is not None:
                raise ValueError("--markdown needs --doc-format markdown")
            return []
        return [MarkdownHook(markdown)]

    def notes(self) -> list[str]:
        return [
            "Bodies are Markdown in and out: --markdown TEXT|@file|@- sets the body to send; "
            "responses return "
            "body.markdown.value. --doc-format adf keeps ADF JSON. Dialect: uvx adflux syntax; "
            "macros: uvx adflux macros NAME.",
        ]


def _read(value: str | None) -> str | None:
    if value is None:
        return None
    if value == "@-":
        import sys

        return sys.stdin.read()
    if value.startswith("@"):
        from pathlib import Path

        return Path(value[1:]).read_text(encoding="utf-8")
    return value


def extension(runtime: Any) -> Extension:
    """Factory named in ``cli.extensions``."""
    return Extension(runtime)
