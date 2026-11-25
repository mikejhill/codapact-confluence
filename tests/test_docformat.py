"""The --doc-format / --markdown extension (hand-written, shipped as codapact_confluence._docformat)."""

from __future__ import annotations

import argparse
import json
from types import SimpleNamespace

import pytest

from codapact_confluence import _docformat as docformat

TOC = {"type": "extension", "attrs": {"extensionType": "com.atlassian.confluence.macro.core", "extensionKey": "toc", "parameters": {"macroParams": {}}}}


def op(*params: str) -> SimpleNamespace:
    return SimpleNamespace(name="op", params=tuple(SimpleNamespace(name=p) for p in params))


def test_markdown_body_is_sent_as_adf() -> None:
    sent = docformat.MarkdownHook().before(op("body"), {"body": {"title": "T", "body": "::toc"}})
    body = sent["body"]["body"]
    assert body["representation"] == "atlas_doc_format"
    assert json.loads(body["value"])["content"] == [TOC]
    again = docformat.MarkdownHook().before(op("body"), {"body": {"body": {"representation": "markdown", "value": "::toc"}}})
    assert again["body"]["body"] == body


def test_reads_ask_for_adf_and_return_markdown() -> None:
    hook = docformat.MarkdownHook()
    assert hook.before(op("id", "body_format"), {"id": 1})["body_format"] == "atlas_doc_format"
    assert hook.before(op("id", "body_format"), {"id": 1, "body_format": "storage"})["body_format"] == "storage"
    page = {"id": "1", "body": {"atlas_doc_format": {"representation": "atlas_doc_format", "value": json.dumps({"type": "doc", "version": 1, "content": [TOC]})}}}
    out = hook.after(op(), page)
    assert out["body"] == {"markdown": {"representation": "markdown", "value": "::toc\n"}}


def test_markdown_option_sets_the_body() -> None:
    sent = docformat.MarkdownHook("# Hi").before(op("body"), {"body": {"title": "T"}})
    assert sent["body"]["title"] == "T"
    assert json.loads(sent["body"]["body"]["value"])["content"][0]["type"] == "heading"
    with pytest.raises(ValueError, match="--markdown"):
        docformat.MarkdownHook("x").before(op("id"), {"id": 1})


def test_doc_format_adf_turns_conversion_off() -> None:
    extension = docformat.extension(SimpleNamespace(env_prefix="CONFLUENCE"))
    assert extension.hooks(argparse.Namespace(doc_format="adf")) == []
    assert len(extension.hooks(argparse.Namespace())) == 1
