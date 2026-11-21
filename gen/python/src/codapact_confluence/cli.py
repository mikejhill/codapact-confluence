"""Command line interface generated from the command model. Do not edit."""

# ruff: noqa: E501
from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Any

from codapact.runtime.cli import (  # noqa: F401
    CliRuntime,
    binary_value,
    compact,
    integer,
    json_value,
    number,
)

from .client import Client
from .client import _model as _api_model

RUNTIME = CliRuntime(program='codapact-confluence', env_prefix='CONFLUENCE', version='0.1.0', distribution='codapact-confluence', api_name='The Confluence Cloud REST API v2', api_version='2.0.0', model=_api_model, auth_plugin='', auth_config={'basic': {'check': 'get_spaces', 'docs': 'Use your Atlassian account email as the username and an API token as the password (create one at https://id.atlassian.com/manage-profile/security/api-tokens).'}, 'session': {'check': 'get_spaces', 'docs': 'For sites where API tokens are disabled: signs in through a browser window and sends the session cookies.', 'browser': {'login_url': '{base_url}/wiki', 'cookies': ['tenant.session.token'], 'headers': {'X-Atlassian-Token': 'no-check'}, 'signin_hosts': ['id.atlassian.com', '*.okta.com']}}}, extensions=('codapact_confluence._docformat:extension',))
RAW = argparse.RawDescriptionHelpFormatter



def _run_admin_key_get(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({})
    return client.admin_key.get(**kwargs)


def _run_admin_key_enable(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'duration_in_minutes': args.p_duration_in_minutes})
    return client.admin_key.enable(**kwargs)


def _run_admin_key_disable(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({})
    RUNTIME.confirm(args, 'admin-key disable')
    return client.admin_key.disable(**kwargs)


def _run_ancestors_list_whiteboard(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit})
    return client.ancestors.list_whiteboard(**kwargs)


def _run_ancestors_list_database(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit})
    return client.ancestors.list_database(**kwargs)


def _run_ancestors_list_smart_link(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit})
    return client.ancestors.list_smart_link(**kwargs)


def _run_ancestors_list_folder(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit})
    return client.ancestors.list_folder(**kwargs)


def _run_ancestors_list_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit})
    return client.ancestors.list_page(**kwargs)


def _run_app_properties_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.app_properties.list(**kwargs)


def _run_app_properties_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_property_key', 'PROPERTY_KEY (or --property-key)')
    kwargs = compact({'property_key': getattr(args, 'p_property_key', None)})
    return client.app_properties.get(**kwargs)


def _run_app_properties_put(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_property_key', 'PROPERTY_KEY (or --property-key)')
    kwargs = compact({'property_key': getattr(args, 'p_property_key', None), 'body': args.p_body})
    return client.app_properties.put(**kwargs)


def _run_app_properties_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_property_key', 'PROPERTY_KEY (or --property-key)')
    kwargs = compact({'property_key': getattr(args, 'p_property_key', None)})
    RUNTIME.confirm(args, 'app-properties delete')
    return client.app_properties.delete(**kwargs)


def _run_attachment_list_attachments(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'sort': args.p_sort, 'cursor': args.p_cursor, 'status': args.p_status, 'media_type': args.p_media_type, 'filename': args.p_filename, 'limit': args.p_limit})
    return client.attachment.list_attachments(**kwargs)


def _run_attachment_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'version': args.p_arg_version, 'include_labels': args.p_include_labels, 'include_properties': args.p_include_properties, 'include_operations': args.p_include_operations, 'include_versions': args.p_include_versions, 'include_version': args.p_include_version, 'include_collaborators': args.p_include_collaborators})
    return client.attachment.get(**kwargs)


def _run_attachment_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'purge': args.p_purge})
    RUNTIME.confirm(args, 'attachment delete')
    return client.attachment.delete(**kwargs)


def _run_attachment_list_blogpost_attachments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'sort': args.p_sort, 'cursor': args.p_cursor, 'status': args.p_status, 'media_type': args.p_media_type, 'filename': args.p_filename, 'limit': args.p_limit})
    return client.attachment.list_blogpost_attachments(**kwargs)


def _run_attachment_list_custom_content_attachments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'sort': args.p_sort, 'cursor': args.p_cursor, 'status': args.p_status, 'media_type': args.p_media_type, 'filename': args.p_filename, 'limit': args.p_limit})
    return client.attachment.list_custom_content_attachments(**kwargs)


def _run_attachment_list_label_attachments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.attachment.list_label_attachments(**kwargs)


def _run_attachment_list_page_attachments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'sort': args.p_sort, 'cursor': args.p_cursor, 'status': args.p_status, 'media_type': args.p_media_type, 'filename': args.p_filename, 'limit': args.p_limit})
    return client.attachment.list_page_attachments(**kwargs)


def _run_attachment_get_thumbnail(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'version': args.p_arg_version, 'height': args.p_height, 'width': args.p_width})
    return client.attachment.get_thumbnail(**kwargs)


def _run_blog_post_list_blog_posts(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'id': args.p_id, 'space_id': args.p_space_id, 'sort': args.p_sort, 'status': args.p_status, 'title': args.p_title, 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.blog_post.list_blog_posts(**kwargs)


def _run_blog_post_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'private': args.p_private, 'space_id': args.p_space_id, 'status': args.p_status, 'title': args.p_title, 'body': args.p_body, 'created_at': args.p_created_at})
    return client.blog_post.create(**kwargs)


def _run_blog_post_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'get_draft': args.p_get_draft, 'status': args.p_status, 'version': args.p_arg_version, 'include_labels': args.p_include_labels, 'include_properties': args.p_include_properties, 'include_operations': args.p_include_operations, 'include_likes': args.p_include_likes, 'include_versions': args.p_include_versions, 'include_version': args.p_include_version, 'include_favorited_by_current_user_status': args.p_include_favorited_by_current_user_status, 'include_webresources': args.p_include_webresources, 'include_collaborators': args.p_include_collaborators})
    return client.blog_post.get(**kwargs)


def _run_blog_post_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.blog_post.update(**kwargs)


def _run_blog_post_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'purge': args.p_purge, 'draft': args.p_draft})
    RUNTIME.confirm(args, 'blog-post delete')
    return client.blog_post.delete(**kwargs)


def _run_blog_post_list_label_blog_posts(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'space_id': args.p_space_id, 'body_format': args.p_body_format, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.blog_post.list_label_blog_posts(**kwargs)


def _run_blog_post_get_blog_posts_in_space(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'sort': args.p_sort, 'status': args.p_status, 'title': args.p_title, 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.blog_post.get_blog_posts_in_space(**kwargs)


def _run_children_get_whiteboard_direct(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.children.get_whiteboard_direct(**kwargs)


def _run_children_get_database_direct(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.children.get_database_direct(**kwargs)


def _run_children_get_smart_link_direct(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.children.get_smart_link_direct(**kwargs)


def _run_children_get_folder_direct(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.children.get_folder_direct(**kwargs)


def _run_children_list_child_pages(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.children.list_child_pages(**kwargs)


def _run_children_get_child_custom_content(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.children.get_child_custom_content(**kwargs)


def _run_children_get_page_direct(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.children.get_page_direct(**kwargs)


def _run_classification_level_list_classification_levels(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({})
    return client.classification_level.list_classification_levels(**kwargs)


def _run_classification_level_get_space_default(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.classification_level.get_space_default(**kwargs)


def _run_classification_level_put_space_default(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.classification_level.put_space_default(**kwargs)


def _run_classification_level_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    RUNTIME.confirm(args, 'classification-level delete')
    return client.classification_level.delete(**kwargs)


def _run_classification_level_get_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'status': args.p_status})
    return client.classification_level.get_page(**kwargs)


def _run_classification_level_put_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.classification_level.put_page(**kwargs)


def _run_classification_level_post_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'status': args.p_status})
    return client.classification_level.post_page(**kwargs)


def _run_classification_level_get_blog_post(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'status': args.p_status})
    return client.classification_level.get_blog_post(**kwargs)


def _run_classification_level_put_blog_post(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.classification_level.put_blog_post(**kwargs)


def _run_classification_level_post_blog_post(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'status': args.p_status})
    return client.classification_level.post_blog_post(**kwargs)


def _run_classification_level_get_whiteboard(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.classification_level.get_whiteboard(**kwargs)


def _run_classification_level_put_whiteboard(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.classification_level.put_whiteboard(**kwargs)


def _run_classification_level_post_whiteboard(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'status': args.p_status})
    return client.classification_level.post_whiteboard(**kwargs)


def _run_classification_level_get_database(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.classification_level.get_database(**kwargs)


def _run_classification_level_put_database(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.classification_level.put_database(**kwargs)


def _run_classification_level_post_database(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'status': args.p_status})
    return client.classification_level.post_database(**kwargs)


def _run_comment_list_attachment_comments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort, 'version': args.p_arg_version})
    return client.comment.list_attachment_comments(**kwargs)


def _run_comment_list_custom_content_comments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.comment.list_custom_content_comments(**kwargs)


def _run_comment_list_page_footer_comments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'status': args.p_status, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.list_page_footer_comments(**kwargs)


def _run_comment_list_page_inline_comments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'status': args.p_status, 'resolution_status': args.p_resolution_status, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.list_page_inline_comments(**kwargs)


def _run_comment_list_blog_post_footer_comments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'status': args.p_status, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.list_blog_post_footer_comments(**kwargs)


def _run_comment_list_blog_post_inline_comments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'status': args.p_status, 'resolution_status': args.p_resolution_status, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.list_blog_post_inline_comments(**kwargs)


def _run_comment_list_footer_comments(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'body_format': args.p_body_format, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.list_footer_comments(**kwargs)


def _run_comment_create_footer(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'blog_post_id': args.p_blog_post_id, 'page_id': args.p_page_id, 'parent_comment_id': args.p_parent_comment_id, 'attachment_id': args.p_attachment_id, 'custom_content_id': args.p_custom_content_id, 'body': args.p_body})
    return client.comment.create_footer(**kwargs)


def _run_comment_get_footer(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'body_format': args.p_body_format, 'version': args.p_arg_version, 'include_properties': args.p_include_properties, 'include_operations': args.p_include_operations, 'include_likes': args.p_include_likes, 'include_versions': args.p_include_versions, 'include_version': args.p_include_version})
    return client.comment.get_footer(**kwargs)


def _run_comment_update_footer(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'version': args.p_arg_version, 'body': args.p_body, 'links': args.p_links})
    return client.comment.update_footer(**kwargs)


def _run_comment_delete_footer(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None)})
    RUNTIME.confirm(args, 'comment delete-footer')
    return client.comment.delete_footer(**kwargs)


def _run_comment_get_footer_children(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.get_footer_children(**kwargs)


def _run_comment_list_inline_comments(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'body_format': args.p_body_format, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.list_inline_comments(**kwargs)


def _run_comment_create_inline(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'blog_post_id': args.p_blog_post_id, 'page_id': args.p_page_id, 'parent_comment_id': args.p_parent_comment_id, 'body': args.p_body, 'inline_comment_properties': args.p_inline_comment_properties})
    return client.comment.create_inline(**kwargs)


def _run_comment_get_inline(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'body_format': args.p_body_format, 'version': args.p_arg_version, 'include_properties': args.p_include_properties, 'include_operations': args.p_include_operations, 'include_likes': args.p_include_likes, 'include_versions': args.p_include_versions, 'include_version': args.p_include_version})
    return client.comment.get_inline(**kwargs)


def _run_comment_update_inline(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'version': args.p_arg_version, 'body': args.p_body, 'resolved': args.p_resolved})
    return client.comment.update_inline(**kwargs)


def _run_comment_delete_inline(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None)})
    RUNTIME.confirm(args, 'comment delete-inline')
    return client.comment.delete_inline(**kwargs)


def _run_comment_get_inline_children(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.comment.get_inline_children(**kwargs)


def _run_content_convert_ids_to_content_types(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'content_ids': args.p_content_ids})
    return client.content.convert_ids_to_content_types(**kwargs)


def _run_content_permissions_get_page_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.content_permissions.get_page_restriction_state(**kwargs)


def _run_content_permissions_set_page_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'state': args.p_state})
    return client.content_permissions.set_page_restriction_state(**kwargs)


def _run_content_permissions_get_blog_post_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.content_permissions.get_blog_post_restriction_state(**kwargs)


def _run_content_permissions_set_blog_post_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'state': args.p_state})
    return client.content_permissions.set_blog_post_restriction_state(**kwargs)


def _run_content_permissions_get_database_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.content_permissions.get_database_restriction_state(**kwargs)


def _run_content_permissions_set_database_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'state': args.p_state})
    return client.content_permissions.set_database_restriction_state(**kwargs)


def _run_content_permissions_get_whiteboard_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.content_permissions.get_whiteboard_restriction_state(**kwargs)


def _run_content_permissions_set_whiteboard_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'state': args.p_state})
    return client.content_permissions.set_whiteboard_restriction_state(**kwargs)


def _run_content_permissions_get_folder_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.content_permissions.get_folder_restriction_state(**kwargs)


def _run_content_permissions_set_folder_restriction_state(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'state': args.p_state})
    return client.content_permissions.set_folder_restriction_state(**kwargs)


def _run_content_permissions_list_page_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_permissions.list_page_permissions(**kwargs)


def _run_content_permissions_set_page_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.set_page_permissions(**kwargs)


def _run_content_permissions_add_page_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.add_page_permissions(**kwargs)


def _run_content_permissions_delete_page_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'allow_self_lockout': args.p_allow_self_lockout})
    RUNTIME.confirm(args, 'content-permissions delete-page-permissions')
    return client.content_permissions.delete_page_permissions(**kwargs)


def _run_content_permissions_list_blog_post_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_permissions.list_blog_post_permissions(**kwargs)


def _run_content_permissions_set_blog_post_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.set_blog_post_permissions(**kwargs)


def _run_content_permissions_add_blog_post_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.add_blog_post_permissions(**kwargs)


def _run_content_permissions_delete_blog_post_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'allow_self_lockout': args.p_allow_self_lockout})
    RUNTIME.confirm(args, 'content-permissions delete-blog-post-permissions')
    return client.content_permissions.delete_blog_post_permissions(**kwargs)


def _run_content_permissions_list_database_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_permissions.list_database_permissions(**kwargs)


def _run_content_permissions_set_database_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.set_database_permissions(**kwargs)


def _run_content_permissions_add_database_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.add_database_permissions(**kwargs)


def _run_content_permissions_delete_database_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'allow_self_lockout': args.p_allow_self_lockout})
    RUNTIME.confirm(args, 'content-permissions delete-database-permissions')
    return client.content_permissions.delete_database_permissions(**kwargs)


def _run_content_permissions_list_whiteboard_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_permissions.list_whiteboard_permissions(**kwargs)


def _run_content_permissions_set_whiteboard_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.set_whiteboard_permissions(**kwargs)


def _run_content_permissions_add_whiteboard_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.add_whiteboard_permissions(**kwargs)


def _run_content_permissions_delete_whiteboard_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'allow_self_lockout': args.p_allow_self_lockout})
    RUNTIME.confirm(args, 'content-permissions delete-whiteboard-permissions')
    return client.content_permissions.delete_whiteboard_permissions(**kwargs)


def _run_content_permissions_list_folder_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_permissions.list_folder_permissions(**kwargs)


def _run_content_permissions_set_folder_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.set_folder_permissions(**kwargs)


def _run_content_permissions_add_folder_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'allow_self_lockout': args.p_allow_self_lockout, 'permissions': args.p_permissions})
    return client.content_permissions.add_folder_permissions(**kwargs)


def _run_content_permissions_delete_folder_permissions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'operation': args.p_operation, 'principal_type': args.p_principal_type, 'principal_id': args.p_principal_id, 'allow_self_lockout': args.p_allow_self_lockout})
    RUNTIME.confirm(args, 'content-permissions delete-folder-permissions')
    return client.content_permissions.delete_folder_permissions(**kwargs)


def _run_content_properties_list_attachment(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_attachment_id', 'ATTACHMENT_ID (or --attachment-id)')
    kwargs = compact({'attachment_id': getattr(args, 'p_attachment_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_attachment(**kwargs)


def _run_content_properties_create_attachment_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_attachment_id', 'ATTACHMENT_ID (or --attachment-id)')
    kwargs = compact({'attachment_id': getattr(args, 'p_attachment_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_attachment_property(**kwargs)


def _run_content_properties_get_attachment_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_attachment_id', 'ATTACHMENT_ID (or --attachment-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'attachment_id': getattr(args, 'p_attachment_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_attachment_by_id(**kwargs)


def _run_content_properties_update_attachment_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_attachment_id', 'ATTACHMENT_ID (or --attachment-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'attachment_id': getattr(args, 'p_attachment_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_attachment_property(**kwargs)


def _run_content_properties_delete_attachment_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_attachment_id', 'ATTACHMENT_ID (or --attachment-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'attachment_id': getattr(args, 'p_attachment_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-attachment-property')
    return client.content_properties.delete_attachment_property(**kwargs)


def _run_content_properties_list_blogpost(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_blogpost_id', 'BLOGPOST_ID (or --blogpost-id)')
    kwargs = compact({'blogpost_id': getattr(args, 'p_blogpost_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_blogpost(**kwargs)


def _run_content_properties_create_blogpost_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_blogpost_id', 'BLOGPOST_ID (or --blogpost-id)')
    kwargs = compact({'blogpost_id': getattr(args, 'p_blogpost_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_blogpost_property(**kwargs)


def _run_content_properties_get_blogpost_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_blogpost_id', 'BLOGPOST_ID (or --blogpost-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'blogpost_id': getattr(args, 'p_blogpost_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_blogpost_by_id(**kwargs)


def _run_content_properties_update_blogpost_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_blogpost_id', 'BLOGPOST_ID (or --blogpost-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'blogpost_id': getattr(args, 'p_blogpost_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_blogpost_property(**kwargs)


def _run_content_properties_delete_blogpost_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_blogpost_id', 'BLOGPOST_ID (or --blogpost-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'blogpost_id': getattr(args, 'p_blogpost_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-blogpost-property')
    return client.content_properties.delete_blogpost_property(**kwargs)


def _run_content_properties_list_custom_content(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_custom_content_id', 'CUSTOM_CONTENT_ID (or --custom-content-id)')
    kwargs = compact({'custom_content_id': getattr(args, 'p_custom_content_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_custom_content(**kwargs)


def _run_content_properties_create(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_custom_content_id', 'CUSTOM_CONTENT_ID (or --custom-content-id)')
    kwargs = compact({'custom_content_id': getattr(args, 'p_custom_content_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create(**kwargs)


def _run_content_properties_get_custom_content_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_custom_content_id', 'CUSTOM_CONTENT_ID (or --custom-content-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'custom_content_id': getattr(args, 'p_custom_content_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_custom_content_by_id(**kwargs)


def _run_content_properties_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_custom_content_id', 'CUSTOM_CONTENT_ID (or --custom-content-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'custom_content_id': getattr(args, 'p_custom_content_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update(**kwargs)


def _run_content_properties_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_custom_content_id', 'CUSTOM_CONTENT_ID (or --custom-content-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'custom_content_id': getattr(args, 'p_custom_content_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete')
    return client.content_properties.delete(**kwargs)


def _run_content_properties_list_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_page_id', 'PAGE_ID (or --page-id)')
    kwargs = compact({'page_id': getattr(args, 'p_page_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_page(**kwargs)


def _run_content_properties_create_page_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_page_id', 'PAGE_ID (or --page-id)')
    kwargs = compact({'page_id': getattr(args, 'p_page_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_page_property(**kwargs)


def _run_content_properties_get_page_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_page_id', 'PAGE_ID (or --page-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'page_id': getattr(args, 'p_page_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_page_by_id(**kwargs)


def _run_content_properties_update_page_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_page_id', 'PAGE_ID (or --page-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'page_id': getattr(args, 'p_page_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_page_property(**kwargs)


def _run_content_properties_delete_page_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_page_id', 'PAGE_ID (or --page-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'page_id': getattr(args, 'p_page_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-page-property')
    return client.content_properties.delete_page_property(**kwargs)


def _run_content_properties_list_whiteboard(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_whiteboard(**kwargs)


def _run_content_properties_create_whiteboard_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_whiteboard_property(**kwargs)


def _run_content_properties_get_whiteboard_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_whiteboard_id', 'WHITEBOARD_ID (or --whiteboard-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'whiteboard_id': getattr(args, 'p_whiteboard_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_whiteboard_by_id(**kwargs)


def _run_content_properties_update_whiteboard_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_whiteboard_id', 'WHITEBOARD_ID (or --whiteboard-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'whiteboard_id': getattr(args, 'p_whiteboard_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_whiteboard_property(**kwargs)


def _run_content_properties_delete_whiteboard_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_whiteboard_id', 'WHITEBOARD_ID (or --whiteboard-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'whiteboard_id': getattr(args, 'p_whiteboard_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-whiteboard-property')
    return client.content_properties.delete_whiteboard_property(**kwargs)


def _run_content_properties_list_database(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_database(**kwargs)


def _run_content_properties_create_database_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_database_property(**kwargs)


def _run_content_properties_get_database_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_database_id', 'DATABASE_ID (or --database-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'database_id': getattr(args, 'p_database_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_database_by_id(**kwargs)


def _run_content_properties_update_database_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_database_id', 'DATABASE_ID (or --database-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'database_id': getattr(args, 'p_database_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_database_property(**kwargs)


def _run_content_properties_delete_database_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_database_id', 'DATABASE_ID (or --database-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'database_id': getattr(args, 'p_database_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-database-property')
    return client.content_properties.delete_database_property(**kwargs)


def _run_content_properties_list_smart_link(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_smart_link(**kwargs)


def _run_content_properties_create_smart_link_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_smart_link_property(**kwargs)


def _run_content_properties_get_smart_link_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_embed_id', 'EMBED_ID (or --embed-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'embed_id': getattr(args, 'p_embed_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_smart_link_by_id(**kwargs)


def _run_content_properties_update_smart_link_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_embed_id', 'EMBED_ID (or --embed-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'embed_id': getattr(args, 'p_embed_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_smart_link_property(**kwargs)


def _run_content_properties_delete_smart_link_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_embed_id', 'EMBED_ID (or --embed-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'embed_id': getattr(args, 'p_embed_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-smart-link-property')
    return client.content_properties.delete_smart_link_property(**kwargs)


def _run_content_properties_list_folder(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_folder(**kwargs)


def _run_content_properties_create_folder_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_folder_property(**kwargs)


def _run_content_properties_get_folder_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_folder_id', 'FOLDER_ID (or --folder-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'folder_id': getattr(args, 'p_folder_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_folder_by_id(**kwargs)


def _run_content_properties_update_folder_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_folder_id', 'FOLDER_ID (or --folder-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'folder_id': getattr(args, 'p_folder_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_folder_property(**kwargs)


def _run_content_properties_delete_folder_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_folder_id', 'FOLDER_ID (or --folder-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'folder_id': getattr(args, 'p_folder_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-folder-property')
    return client.content_properties.delete_folder_property(**kwargs)


def _run_content_properties_list_comment(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'key': args.p_key, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.content_properties.list_comment(**kwargs)


def _run_content_properties_create_comment_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.content_properties.create_comment_property(**kwargs)


def _run_content_properties_get_comment_by_id(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.content_properties.get_comment_by_id(**kwargs)


def _run_content_properties_update_comment_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.content_properties.update_comment_property(**kwargs)


def _run_content_properties_delete_comment_property(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_comment_id', 'COMMENT_ID (or --comment-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'comment_id': getattr(args, 'p_comment_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'content-properties delete-comment-property')
    return client.content_properties.delete_comment_property(**kwargs)


def _run_custom_content_get_by_type_in_blog_post(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'type_': args.p_type, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit, 'body_format': args.p_body_format})
    return client.custom_content.get_by_type_in_blog_post(**kwargs)


def _run_custom_content_get_by_type(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'type_': args.p_type, 'id': args.p_id, 'space_id': args.p_space_id, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit, 'body_format': args.p_body_format})
    return client.custom_content.get_by_type(**kwargs)


def _run_custom_content_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'type_': args.p_type, 'status': args.p_status, 'space_id': args.p_space_id, 'page_id': args.p_page_id, 'blog_post_id': args.p_blog_post_id, 'custom_content_id': args.p_custom_content_id, 'title': args.p_title, 'body': args.p_body})
    return client.custom_content.create(**kwargs)


def _run_custom_content_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'version': args.p_arg_version, 'include_labels': args.p_include_labels, 'include_properties': args.p_include_properties, 'include_operations': args.p_include_operations, 'include_versions': args.p_include_versions, 'include_version': args.p_include_version, 'include_collaborators': args.p_include_collaborators})
    return client.custom_content.get(**kwargs)


def _run_custom_content_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.custom_content.update(**kwargs)


def _run_custom_content_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'purge': args.p_purge})
    RUNTIME.confirm(args, 'custom-content delete')
    return client.custom_content.delete(**kwargs)


def _run_custom_content_get_by_type_in_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'type_': args.p_type, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit, 'body_format': args.p_body_format})
    return client.custom_content.get_by_type_in_page(**kwargs)


def _run_custom_content_get_by_type_in_space(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'type_': args.p_type, 'cursor': args.p_cursor, 'limit': args.p_limit, 'body_format': args.p_body_format})
    return client.custom_content.get_by_type_in_space(**kwargs)


def _run_data_policies_get_metadata(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({})
    return client.data_policies.get_metadata(**kwargs)


def _run_data_policies_list_spaces(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'ids': args.p_ids, 'keys': args.p_keys, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.data_policies.list_spaces(**kwargs)


def _run_database_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'private': args.p_private, 'space_id': args.p_space_id, 'title': args.p_title, 'parent_id': args.p_parent_id})
    return client.database.create(**kwargs)


def _run_database_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'include_collaborators': args.p_include_collaborators, 'include_direct_children': args.p_include_direct_children, 'include_operations': args.p_include_operations, 'include_properties': args.p_include_properties})
    return client.database.get(**kwargs)


def _run_database_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    RUNTIME.confirm(args, 'database delete')
    return client.database.delete(**kwargs)


def _run_database_list_fields(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'cursor': args.p_cursor, 'if_none_match': args.p_if_none_match})
    return client.database.list_fields(**kwargs)


def _run_database_list_views(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'cursor': args.p_cursor, 'if_none_match': args.p_if_none_match})
    return client.database.list_views(**kwargs)


def _run_database_list_entries(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'cursor': args.p_cursor, 'if_none_match': args.p_if_none_match, 'sort': args.p_sort, 'filter': args.p_filter})
    return client.database.list_entries(**kwargs)


def _run_database_get_entry(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    RUNTIME.require(args, 'p_entry_id', 'ENTRY_ID (or --entry-id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'entry_id': getattr(args, 'p_entry_id', None), 'if_none_match': args.p_if_none_match})
    return client.database.get_entry(**kwargs)


def _run_descendants_list_whiteboard(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'depth': args.p_depth, 'cursor': args.p_cursor})
    return client.descendants.list_whiteboard(**kwargs)


def _run_descendants_list_database(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'depth': args.p_depth, 'cursor': args.p_cursor})
    return client.descendants.list_database(**kwargs)


def _run_descendants_list_smart_link(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'depth': args.p_depth, 'cursor': args.p_cursor})
    return client.descendants.list_smart_link(**kwargs)


def _run_descendants_list_folder(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'depth': args.p_depth, 'cursor': args.p_cursor})
    return client.descendants.list_folder(**kwargs)


def _run_descendants_list_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'limit': args.p_limit, 'depth': args.p_depth, 'cursor': args.p_cursor})
    return client.descendants.list_page(**kwargs)


def _run_folder_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'space_id': args.p_space_id, 'title': args.p_title, 'parent_id': args.p_parent_id})
    return client.folder.create(**kwargs)


def _run_folder_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'include_collaborators': args.p_include_collaborators, 'include_direct_children': args.p_include_direct_children, 'include_operations': args.p_include_operations, 'include_properties': args.p_include_properties})
    return client.folder.get(**kwargs)


def _run_folder_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    RUNTIME.confirm(args, 'folder delete')
    return client.folder.delete(**kwargs)


def _run_label_list_attachment_labels(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'prefix': args.p_prefix, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.label.list_attachment_labels(**kwargs)


def _run_label_list_blog_post_labels(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'prefix': args.p_prefix, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.label.list_blog_post_labels(**kwargs)


def _run_label_list_custom_content_labels(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'prefix': args.p_prefix, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.label.list_custom_content_labels(**kwargs)


def _run_label_list_labels(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'label_id': args.p_label_id, 'prefix': args.p_prefix, 'cursor': args.p_cursor, 'sort': args.p_sort, 'limit': args.p_limit})
    return client.label.list_labels(**kwargs)


def _run_label_list_page_labels(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'prefix': args.p_prefix, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.label.list_page_labels(**kwargs)


def _run_label_list_space_labels(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'prefix': args.p_prefix, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.label.list_space_labels(**kwargs)


def _run_label_list_space_content_labels(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'prefix': args.p_prefix, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.label.list_space_content_labels(**kwargs)


def _run_like_get_blog_post_count(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.like.get_blog_post_count(**kwargs)


def _run_like_list_blog_post_users(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.like.list_blog_post_users(**kwargs)


def _run_like_get_page_count(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.like.get_page_count(**kwargs)


def _run_like_list_page_users(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.like.list_page_users(**kwargs)


def _run_like_get_footer_count(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.like.get_footer_count(**kwargs)


def _run_like_list_footer_users(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.like.list_footer_users(**kwargs)


def _run_like_get_inline_count(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.like.get_inline_count(**kwargs)


def _run_like_list_inline_users(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.like.list_inline_users(**kwargs)


def _run_operation_list_attachment_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_attachment_operations(**kwargs)


def _run_operation_list_blog_post_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_blog_post_operations(**kwargs)


def _run_operation_list_custom_content_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_custom_content_operations(**kwargs)


def _run_operation_list_page_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_page_operations(**kwargs)


def _run_operation_list_whiteboard_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_whiteboard_operations(**kwargs)


def _run_operation_list_database_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_database_operations(**kwargs)


def _run_operation_list_smart_link_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_smart_link_operations(**kwargs)


def _run_operation_list_folder_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_folder_operations(**kwargs)


def _run_operation_list_space_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_space_operations(**kwargs)


def _run_operation_list_footer_comment_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_footer_comment_operations(**kwargs)


def _run_operation_list_inline_comment_operations(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.operation.list_inline_comment_operations(**kwargs)


def _run_page_list_label_pages(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'space_id': args.p_space_id, 'body_format': args.p_body_format, 'sort': args.p_sort, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.page.list_label_pages(**kwargs)


def _run_page_list_pages(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'id': args.p_id, 'space_id': args.p_space_id, 'sort': args.p_sort, 'status': args.p_status, 'title': args.p_title, 'body_format': args.p_body_format, 'subtype': args.p_subtype, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.page.list_pages(**kwargs)


def _run_page_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'embedded': args.p_embedded, 'private': args.p_private, 'root_level': args.p_root_level, 'space_id': args.p_space_id, 'status': args.p_status, 'title': args.p_title, 'parent_id': args.p_parent_id, 'body': args.p_body, 'subtype': args.p_subtype})
    return client.page.create(**kwargs)


def _run_page_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'get_draft': args.p_get_draft, 'status': args.p_status, 'version': args.p_arg_version, 'include_labels': args.p_include_labels, 'include_properties': args.p_include_properties, 'include_operations': args.p_include_operations, 'include_likes': args.p_include_likes, 'include_versions': args.p_include_versions, 'include_version': args.p_include_version, 'include_favorited_by_current_user_status': args.p_include_favorited_by_current_user_status, 'include_webresources': args.p_include_webresources, 'include_collaborators': args.p_include_collaborators, 'include_direct_children': args.p_include_direct_children})
    return client.page.get(**kwargs)


def _run_page_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.page.update(**kwargs)


def _run_page_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'purge': args.p_purge, 'draft': args.p_draft})
    RUNTIME.confirm(args, 'page delete')
    return client.page.delete(**kwargs)


def _run_page_update_title(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'status': args.p_status, 'title': args.p_title})
    return client.page.update_title(**kwargs)


def _run_page_get_pages_in_space(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'depth': args.p_depth, 'sort': args.p_sort, 'status': args.p_status, 'title': args.p_title, 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.page.get_pages_in_space(**kwargs)


def _run_redactions_post_redact_page(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'created_at': args.p_created_at, 'clean_history': args.p_clean_history, 'version_number': args.p_version_number, 'body': args.p_body, 'title': args.p_title})
    return client.redactions.post_redact_page(**kwargs)


def _run_redactions_post_redact_blog(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'created_at': args.p_created_at, 'clean_history': args.p_clean_history, 'version_number': args.p_version_number, 'body': args.p_body, 'title': args.p_title})
    return client.redactions.post_redact_blog(**kwargs)


def _run_smart_link_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'space_id': args.p_space_id, 'title': args.p_title, 'parent_id': args.p_parent_id, 'embed_url': args.p_embed_url})
    return client.smart_link.create(**kwargs)


def _run_smart_link_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'include_collaborators': args.p_include_collaborators, 'include_direct_children': args.p_include_direct_children, 'include_operations': args.p_include_operations, 'include_properties': args.p_include_properties})
    return client.smart_link.get(**kwargs)


def _run_smart_link_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    RUNTIME.confirm(args, 'smart-link delete')
    return client.smart_link.delete(**kwargs)


def _run_space_list_spaces(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'ids': args.p_ids, 'keys': args.p_keys, 'type_': args.p_type, 'status': args.p_status, 'labels': args.p_labels, 'favorited_by': args.p_favorited_by, 'not_favorited_by': args.p_not_favorited_by, 'sort': args.p_sort, 'description_format': args.p_description_format, 'include_icon': args.p_include_icon, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.space.list_spaces(**kwargs)


def _run_space_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'name': args.p_name, 'key': args.p_key, 'alias': args.p_alias, 'description': args.p_description, 'role_assignments': args.p_role_assignments, 'copy_space_access_configuration': args.p_copy_space_access_configuration, 'create_private_space': args.p_create_private_space, 'template_key': args.p_template_key})
    return client.space.create(**kwargs)


def _run_space_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'description_format': args.p_description_format, 'include_icon': args.p_include_icon, 'include_operations': args.p_include_operations, 'include_properties': args.p_include_properties, 'include_permissions': args.p_include_permissions, 'include_role_assignments': args.p_include_role_assignments, 'include_labels': args.p_include_labels})
    return client.space.get(**kwargs)


def _run_space_permission_transition_list_space_permission_combinations(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.space_permission_transition.list_space_permission_combinations(**kwargs)


def _run_space_permission_transition_generate_space_permission_combinations(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({})
    return client.space_permission_transition.generate_space_permission_combinations(**kwargs)


def _run_space_permission_transition_bulk_assign_space_permission_roles(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'assignments': args.p_assignments, 'space_selection': args.p_space_selection})
    return client.space_permission_transition.bulk_assign_space_permission_roles(**kwargs)


def _run_space_permission_transition_bulk_remove_space_permission_access(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'permission_combination_ids': args.p_permission_combination_ids, 'space_selection': args.p_space_selection})
    return client.space_permission_transition.bulk_remove_space_permission_access(**kwargs)


def _run_space_permission_transition_get_task_status(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_task_id', 'TASK_ID (or --task-id)')
    kwargs = compact({'task_id': getattr(args, 'p_task_id', None)})
    return client.space_permission_transition.get_task_status(**kwargs)


def _run_space_permissions_list_assignments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.space_permissions.list_assignments(**kwargs)


def _run_space_permissions_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.space_permissions.list(**kwargs)


def _run_space_properties_list(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_space_id', 'SPACE_ID (or --space-id)')
    kwargs = compact({'space_id': getattr(args, 'p_space_id', None), 'key': args.p_key, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.space_properties.list(**kwargs)


def _run_space_properties_create(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_space_id', 'SPACE_ID (or --space-id)')
    kwargs = compact({'space_id': getattr(args, 'p_space_id', None), 'key': args.p_key, 'value': args.p_value})
    return client.space_properties.create(**kwargs)


def _run_space_properties_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_space_id', 'SPACE_ID (or --space-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'space_id': getattr(args, 'p_space_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    return client.space_properties.get(**kwargs)


def _run_space_properties_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_space_id', 'SPACE_ID (or --space-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'space_id': getattr(args, 'p_space_id', None), 'property_id': getattr(args, 'p_property_id', None), 'key': args.p_key, 'value': args.p_value, 'version': args.p_arg_version})
    return client.space_properties.update(**kwargs)


def _run_space_properties_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_space_id', 'SPACE_ID (or --space-id)')
    RUNTIME.require(args, 'p_property_id', 'PROPERTY_ID (or --property-id)')
    kwargs = compact({'space_id': getattr(args, 'p_space_id', None), 'property_id': getattr(args, 'p_property_id', None)})
    RUNTIME.confirm(args, 'space-properties delete')
    return client.space_properties.delete(**kwargs)


def _run_space_roles_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'space_id': args.p_space_id, 'role_type': args.p_role_type, 'principal_id': args.p_principal_id, 'principal_type': args.p_principal_type, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.space_roles.list(**kwargs)


def _run_space_roles_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'name': args.p_name, 'description': args.p_description, 'space_permissions': args.p_space_permissions})
    return client.space_roles.create(**kwargs)


def _run_space_roles_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    return client.space_roles.get(**kwargs)


def _run_space_roles_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'name': args.p_name, 'description': args.p_description, 'space_permissions': args.p_space_permissions, 'anonymous_reassignment_role_id': args.p_anonymous_reassignment_role_id, 'guest_reassignment_role_id': args.p_guest_reassignment_role_id})
    return client.space_roles.update(**kwargs)


def _run_space_roles_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    RUNTIME.confirm(args, 'space-roles delete')
    return client.space_roles.delete(**kwargs)


def _run_space_roles_get_mode(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({})
    return client.space_roles.get_mode(**kwargs)


def _run_space_roles_list_assignments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'role_id': args.p_role_id, 'role_type': args.p_role_type, 'principal_id': args.p_principal_id, 'principal_type': args.p_principal_type, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.space_roles.list_assignments(**kwargs)


def _run_space_roles_set_assignments(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body': args.p_body})
    return client.space_roles.set_assignments(**kwargs)


def _run_task_list_tasks(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'body_format': args.p_body_format, 'include_blank_tasks': args.p_include_blank_tasks, 'status': args.p_status, 'task_id': args.p_task_id, 'space_id': args.p_space_id, 'page_id': args.p_page_id, 'blogpost_id': args.p_blogpost_id, 'created_by': args.p_created_by, 'assigned_to': args.p_assigned_to, 'completed_by': args.p_completed_by, 'created_at_from': args.p_created_at_from, 'created_at_to': args.p_created_at_to, 'due_at_from': args.p_due_at_from, 'due_at_to': args.p_due_at_to, 'completed_at_from': args.p_completed_at_from, 'completed_at_to': args.p_completed_at_to, 'cursor': args.p_cursor, 'limit': args.p_limit})
    return client.task.list_tasks(**kwargs)


def _run_task_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format})
    return client.task.get(**kwargs)


def _run_task_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'body': args.p_body})
    return client.task.update(**kwargs)


def _run_user_create_bulk_lookup(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'account_ids': args.p_account_ids})
    return client.user.create_bulk_lookup(**kwargs)


def _run_user_check_access_by_email(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'emails': args.p_emails})
    return client.user.check_access_by_email(**kwargs)


def _run_user_invite_by_email(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'emails': args.p_emails})
    return client.user.invite_by_email(**kwargs)


def _run_version_list_attachment_versions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.version.list_attachment_versions(**kwargs)


def _run_version_list_attachment_details(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_attachment_id', 'ATTACHMENT_ID (or --attachment-id)')
    RUNTIME.require(args, 'p_version_number', 'VERSION_NUMBER (or --version-number)')
    kwargs = compact({'attachment_id': getattr(args, 'p_attachment_id', None), 'version_number': getattr(args, 'p_version_number', None)})
    return client.version.list_attachment_details(**kwargs)


def _run_version_list_blog_post_versions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.version.list_blog_post_versions(**kwargs)


def _run_version_list_blog_post_details(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_blogpost_id', 'BLOGPOST_ID (or --blogpost-id)')
    RUNTIME.require(args, 'p_version_number', 'VERSION_NUMBER (or --version-number)')
    kwargs = compact({'blogpost_id': getattr(args, 'p_blogpost_id', None), 'version_number': getattr(args, 'p_version_number', None)})
    return client.version.list_blog_post_details(**kwargs)


def _run_version_list_page_versions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.version.list_page_versions(**kwargs)


def _run_version_list_page_details(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_page_id', 'PAGE_ID (or --page-id)')
    RUNTIME.require(args, 'p_version_number', 'VERSION_NUMBER (or --version-number)')
    kwargs = compact({'page_id': getattr(args, 'p_page_id', None), 'version_number': getattr(args, 'p_version_number', None)})
    return client.version.list_page_details(**kwargs)


def _run_version_list_custom_content_versions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_custom_content_id', 'CUSTOM_CONTENT_ID (or --custom-content-id)')
    kwargs = compact({'custom_content_id': getattr(args, 'p_custom_content_id', None), 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.version.list_custom_content_versions(**kwargs)


def _run_version_list_custom_content_details(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_custom_content_id', 'CUSTOM_CONTENT_ID (or --custom-content-id)')
    RUNTIME.require(args, 'p_version_number', 'VERSION_NUMBER (or --version-number)')
    kwargs = compact({'custom_content_id': getattr(args, 'p_custom_content_id', None), 'version_number': getattr(args, 'p_version_number', None)})
    return client.version.list_custom_content_details(**kwargs)


def _run_version_list_footer_comment_versions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.version.list_footer_comment_versions(**kwargs)


def _run_version_list_footer_comment_details(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    RUNTIME.require(args, 'p_version_number', 'VERSION_NUMBER (or --version-number)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'version_number': getattr(args, 'p_version_number', None)})
    return client.version.list_footer_comment_details(**kwargs)


def _run_version_list_inline_comment_versions(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'body_format': args.p_body_format, 'cursor': args.p_cursor, 'limit': args.p_limit, 'sort': args.p_sort})
    return client.version.list_inline_comment_versions(**kwargs)


def _run_version_list_inline_comment_details(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    RUNTIME.require(args, 'p_version_number', 'VERSION_NUMBER (or --version-number)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'version_number': getattr(args, 'p_version_number', None)})
    return client.version.list_inline_comment_details(**kwargs)


def _run_whiteboard_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'private': args.p_private, 'space_id': args.p_space_id, 'title': args.p_title, 'parent_id': args.p_parent_id, 'template_key': args.p_template_key, 'locale': args.p_locale})
    return client.whiteboard.create(**kwargs)


def _run_whiteboard_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None), 'include_collaborators': args.p_include_collaborators, 'include_direct_children': args.p_include_direct_children, 'include_operations': args.p_include_operations, 'include_properties': args.p_include_properties})
    return client.whiteboard.get(**kwargs)


def _run_whiteboard_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_id', 'ID (or --id)')
    kwargs = compact({'id': getattr(args, 'p_id', None)})
    RUNTIME.confirm(args, 'whiteboard delete')
    return client.whiteboard.delete(**kwargs)

def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    common = argparse.ArgumentParser(add_help=False)
    RUNTIME.add_global_options(common, hidden=True)
    parser = RUNTIME.parser(
        description="This document describes Confluence's v2 APIs. This is intended to be an\niteration on the existing Confluence Cloud REST API with improvements in both\nendpoint definitions and performance.",
        epilog="credentials:\n  basic: set CONFLUENCE_BASIC_USERNAME and CONFLUENCE_BASIC_PASSWORD, CONFLUENCE_BASIC_COMMAND, or run 'codapact-confluence auth login'\n  session: custom; set CONFLUENCE_AUTH_PLUGIN=package.module:factory",
        examples=['codapact-confluence ancestors list-whiteboard ID'],
    )
    commands = parser.add_subparsers(dest="command", metavar="COMMAND", required=True)
    g_admin_key = commands.add_parser('admin-key', help='disable, enable, get', description="Run 'codapact-confluence admin-key COMMAND --help' for a command's options and examples.")
    g_admin_key_commands = g_admin_key.add_subparsers(dest="g_admin_key", metavar="COMMAND", required=True)
    c = g_admin_key_commands.add_parser('get', parents=[common], help='Get Admin Key', description='Returns information about the admin key if one is currently enabled for the\ncalling user within the site.\n\n**[Permissions](https://support.atlassian.com/user-management/docs/give-users-\nadmin-permissions/#Centralized-user-management-content) required**: User must\nbe an organization or site admin.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence admin-key get']), formatter_class=RAW)
    c.set_defaults(handler=_run_admin_key_get, flags={}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_admin_key'})
    c = g_admin_key_commands.add_parser('enable', parents=[common], help='Enable Admin Key', description='Enables admin key access for the calling user within the site. If an admin key\nalready exists for the user, a new one will be issued with an updated\nexpiration time.\n\n**Note:** The `durationInMinutes` field within the request body is optional.\nIf the request body is empty or if the `durationInMinutes` is set to 0\nminutes, a new admin key will be issued to the calling user with a default\nduration of 10 minutes.\n\n**[Permissions](https://support.atlassian.com/user-management/docs/give-users-\nadmin-permissions/#Centralized-user-management-content) required**: User must\nbe an organization or site admin.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence admin-key enable', 'codapact-confluence admin-key enable --dry-run']), formatter_class=RAW)
    c.add_argument('--duration-in-minutes', dest='p_duration_in_minutes', type=integer, metavar='DURATION_IN_MINUTES', help='The requested duration of admin key access in minutes, up to a maximum of 60 minutes, after which the issued admin key will automatically expire.')
    c.set_defaults(handler=_run_admin_key_enable, flags={'body.duration_in_minutes': '--duration-in-minutes'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'enable_admin_key'})
    c = g_admin_key_commands.add_parser('disable', parents=[common], help='Disable Admin Key', description='Disables admin key access for the calling user within the site.\n\n**[Permissions](https://support.atlassian.com/user-management/docs/give-users-\nadmin-permissions/#Centralized-user-management-content) required**: User must\nbe an organization or site admin.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence admin-key disable --dry-run', 'codapact-confluence admin-key disable --yes']), formatter_class=RAW)
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_admin_key_disable, flags={}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'disable_admin_key'})
    g_ancestors = commands.add_parser('ancestors', help='list-database, list-folder, list-page, … (5 commands)', description="Run 'codapact-confluence ancestors COMMAND --help' for a command's options and examples.")
    g_ancestors_commands = g_ancestors.add_subparsers(dest="g_ancestors", metavar="COMMAND", required=True)
    c = g_ancestors_commands.add_parser('list-whiteboard', parents=[common], help='Get all ancestors of whiteboard', description="Returns all ancestors for a given whiteboard by ID in top-to-bottom order\n(that is, the highest ancestor is the first item in the response payload). The\nnumber of results is limited by the `limit` parameter and additional results\n(if available) will be available by calling this endpoint with the ID of first\nancestor in the response payload.\n\nThis endpoint returns minimal information about each ancestor. To fetch more\ndetails, use a related endpoint, such as [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the whiteboard and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence ancestors list-whiteboard ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results. (default: 25)")
    c.set_defaults(handler=_run_ancestors_list_whiteboard, flags={'id': '--id', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_ancestors'})
    c = g_ancestors_commands.add_parser('list-database', parents=[common], help='Get all ancestors of database', description="Returns all ancestors for a given database by ID in top-to-bottom order (that\nis, the highest ancestor is the first item in the response payload). The\nnumber of results is limited by the `limit` parameter and additional results\n(if available) will be available by calling this endpoint with the ID of first\nancestor in the response payload.\n\nThis endpoint returns minimal information about each ancestor. To fetch more\ndetails, use a related endpoint, such as [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the database and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence ancestors list-database ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results. (default: 25)")
    c.set_defaults(handler=_run_ancestors_list_database, flags={'id': '--id', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_ancestors'})
    c = g_ancestors_commands.add_parser('list-smart-link', parents=[common], help='Get all ancestors of Smart Link in content tree', description="Returns all ancestors for a given Smart Link in the content tree by ID in top-\nto-bottom order (that is, the highest ancestor is the first item in the\nresponse payload). The number of results is limited by the `limit` parameter\nand additional results (if available) will be available by calling this\nendpoint with the ID of first ancestor in the response payload.\n\nThis endpoint returns minimal information about each ancestor. To fetch more\ndetails, use a related endpoint, such as [Get Smart Link in the content tree\nby id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nsmart-link/#api-embeds-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the Smart Link in the content tree and its corresponding\nspace", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence ancestors list-smart-link ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results. (default: 25)")
    c.set_defaults(handler=_run_ancestors_list_smart_link, flags={'id': '--id', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_smart_link_ancestors'})
    c = g_ancestors_commands.add_parser('list-folder', parents=[common], help='Get all ancestors of folder', description="Returns all ancestors for a given folder by ID in top-to-bottom order (that\nis, the highest ancestor is the first item in the response payload). The\nnumber of results is limited by the `limit` parameter and additional results\n(if available) will be available by calling this endpoint with the ID of first\nancestor in the response payload.\n\nThis endpoint returns minimal information about each ancestor. To fetch more\ndetails, use a related endpoint, such as [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-folders-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the folder and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence ancestors list-folder ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help="Maximum number of items per result to return. If more results exist, call the endpoint with the highest ancestor's ID to fetch the next set of results. (default: 25)")
    c.set_defaults(handler=_run_ancestors_list_folder, flags={'id': '--id', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_ancestors'})
    c = g_ancestors_commands.add_parser('list-page', parents=[common], help='Get all ancestors of page', description="Returns all ancestors for a given page by ID in top-to-bottom order (that is,\nthe highest ancestor is the first item in the response payload). The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available by calling this endpoint with the ID of first\nancestor in the response payload.\n\nThis endpoint returns minimal information about each ancestor. To fetch more\ndetails, use a related endpoint, such as [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence ancestors list-page ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help="Maximum number of pages per result to return. If more results exist, call this endpoint with the highest ancestor's ID to fetch the next set of results. (default: 25)")
    c.set_defaults(handler=_run_ancestors_list_page, flags={'id': '--id', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_ancestors'})
    g_app_properties = commands.add_parser('app-properties', help='delete, get, list, put', description="Run 'codapact-confluence app-properties COMMAND --help' for a command's options and examples.")
    g_app_properties_commands = g_app_properties.add_subparsers(dest="g_app_properties", metavar="COMMAND", required=True)
    c = g_app_properties_commands.add_parser('list', parents=[common], help='Get Forge app properties.', description='Gets Forge app properties. This API can only be accessed using\n**[asApp()](https://developer.atlassian.com/platform/forge/apis-\nreference/fetch-api-product.requestconfluence/#method-signature)** requests\nfrom Forge.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence app-properties list']), formatter_class=RAW)
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor represents the last returned property key. It will be included in the response body as the next link. Use this key to request the next set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of app properties per result to return. If more results exist, use the last returned property key from the Link field in the response body as a cursor to retrieve the next set of results. (default: 50)')
    c.set_defaults(handler=_run_app_properties_list, flags={'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_forge_app_properties'})
    c = g_app_properties_commands.add_parser('get', parents=[common], help='Get a Forge app property by key.', description='Gets a Forge app property by property key. This API can only be accessed using\n**[asApp()](https://developer.atlassian.com/platform/forge/apis-\nreference/fetch-api-product.requestconfluence/#method-signature)** requests\nfrom Forge.', usage='%(prog)s PROPERTY_KEY [options]', epilog=RUNTIME.command_epilog(['codapact-confluence app-properties get PROPERTY_KEY']), formatter_class=RAW)
    c.add_argument('p_property_key', metavar='PROPERTY_KEY', nargs='?', default=argparse.SUPPRESS, help='The key of the property')
    c.add_argument('--property-key', dest='p_property_key', default=argparse.SUPPRESS, metavar='PROPERTY_KEY', help='same as PROPERTY_KEY')
    c.set_defaults(handler=_run_app_properties_get, flags={'property_key': '--property-key'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_forge_app_property'})
    c = g_app_properties_commands.add_parser('put', parents=[common], help='Create or update a Forge app property.', description='Creates or updates a Forge app property. This API can only be accessed using\n**[asApp()](https://developer.atlassian.com/platform/forge/apis-\nreference/fetch-api-product.requestconfluence/#method-signature)** requests\nfrom Forge.', usage='%(prog)s PROPERTY_KEY --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence app-properties put PROPERTY_KEY --body @body.json', 'codapact-confluence app-properties put PROPERTY_KEY --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_property_key', metavar='PROPERTY_KEY', nargs='?', default=argparse.SUPPRESS, help='The key of the property')
    c.add_argument('--property-key', dest='p_property_key', default=argparse.SUPPRESS, metavar='PROPERTY_KEY', help='same as PROPERTY_KEY')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True)
    c.set_defaults(handler=_run_app_properties_put, flags={'property_key': '--property-key', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'put_forge_app_property'})
    c = g_app_properties_commands.add_parser('delete', parents=[common], help='Deletes a Forge app property.', description='Deletes a Forge app property. This API can only be accessed using\n**[asApp()](https://developer.atlassian.com/platform/forge/apis-\nreference/fetch-api-product.requestconfluence/#method-signature)** requests\nfrom Forge.', usage='%(prog)s PROPERTY_KEY [options]', epilog=RUNTIME.command_epilog(['codapact-confluence app-properties delete PROPERTY_KEY --dry-run', 'codapact-confluence app-properties delete PROPERTY_KEY --yes']), formatter_class=RAW)
    c.add_argument('p_property_key', metavar='PROPERTY_KEY', nargs='?', default=argparse.SUPPRESS, help='The key of the property')
    c.add_argument('--property-key', dest='p_property_key', default=argparse.SUPPRESS, metavar='PROPERTY_KEY', help='same as PROPERTY_KEY')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_app_properties_delete, flags={'property_key': '--property-key'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_forge_app_property'})
    g_attachment = commands.add_parser('attachment', help='delete, get, get-thumbnail, … (8 commands)', description="Run 'codapact-confluence attachment COMMAND --help' for a command's options and examples.")
    g_attachment_commands = g_attachment.add_subparsers(dest="g_attachment", metavar="COMMAND", required=True)
    c = g_attachment_commands.add_parser('list-attachments', parents=[common], help='Get attachments', description='Returns all attachments. The number of results is limited by the `limit`\nparameter and additional results (if available) will be available through the\n`next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the container of the attachment.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment list-attachments']), formatter_class=RAW)
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'trashed'], help='Filter the results to attachments based on their status. By default, `current` and `archived` are used.')
    c.add_argument('--media-type', dest='p_media_type', metavar='MEDIA_TYPE', help='Filters on the mediaType of attachments. Only one may be specified.')
    c.add_argument('--filename', dest='p_filename', metavar='FILENAME', help='Filters on the file-name of attachments. Only one may be specified.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 50)')
    c.set_defaults(handler=_run_attachment_list_attachments, flags={'sort': '--sort', 'cursor': '--cursor', 'status': '--status', 'media_type': '--media-type', 'filename': '--filename', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachments'})
    c = g_attachment_commands.add_parser('get', parents=[common], help='Get attachment by id', description="Returns a specific attachment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment's container.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help="The ID of the attachment to be returned. If you don't know the attachment's ID, use Get attachments for page/blogpost/custom content.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.")
    c.add_argument('--include-labels', dest='p_include_labels', action=argparse.BooleanOptionalAction, help='Includes labels associated with this attachment in the response. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this attachment in the response. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this attachment in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-versions', dest='p_include_versions', action=argparse.BooleanOptionalAction, help='Includes versions associated with this attachment in the response. (default: False)')
    c.add_argument('--include-version', dest='p_include_version', action=argparse.BooleanOptionalAction, help='Includes the current version associated with this attachment in the response. (default: True)')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the attachment. (default: False)')
    c.set_defaults(handler=_run_attachment_get, flags={'id': '--id', 'version': '--arg-version', 'include_labels': '--include-labels', 'include_properties': '--include-properties', 'include_operations': '--include-operations', 'include_versions': '--include-versions', 'include_version': '--include-version', 'include_collaborators': '--include-collaborators'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_by_id'})
    c = g_attachment_commands.add_parser('delete', parents=[common], help='Delete attachment', description='Delete an attachment by id.\n\nDeleting an attachment moves the attachment to the trash, where it can be\nrestored later. To permanently delete an attachment (or "purge" it), the\nendpoint must be called on a **trashed** attachment with the following param\n`purge=true`.\n\n**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-\nconfluences-roles/) required**: Permission to view the container of the\nattachment. Permission to delete attachments in the space. [`manage/content`](\nhttps://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-\npermissions/#api-space-permissions-get) permission for the space (if\nattempting to purge).\n\n**Note:** To find the display name for each permission ID, call the [Get\navailable space\npermissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) API.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment delete ID --dry-run', 'codapact-confluence attachment delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the attachment to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--purge', dest='p_purge', action=argparse.BooleanOptionalAction, help='If attempting to purge the attachment. (default: False)')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_attachment_delete, flags={'id': '--id', 'purge': '--purge'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_attachment'})
    c = g_attachment_commands.add_parser('list-blogpost-attachments', parents=[common], help='Get attachments for blog post', description='Returns the attachments of specific blog post. The number of results is\nlimited by the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the blog post and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment list-blogpost-attachments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which attachments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'trashed'], help='Filter the results to attachments based on their status. By default, `current` and `archived` are used.')
    c.add_argument('--media-type', dest='p_media_type', metavar='MEDIA_TYPE', help='Filters on the mediaType of attachments. Only one may be specified.')
    c.add_argument('--filename', dest='p_filename', metavar='FILENAME', help='Filters on the file-name of attachments. Only one may be specified.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 50)')
    c.set_defaults(handler=_run_attachment_list_blogpost_attachments, flags={'id': '--id', 'sort': '--sort', 'cursor': '--cursor', 'status': '--status', 'media_type': '--media-type', 'filename': '--filename', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blogpost_attachments'})
    c = g_attachment_commands.add_parser('list-custom-content-attachments', parents=[common], help='Get attachments for custom content', description='Returns the attachments of specific custom content. The number of results is\nlimited by the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the custom content and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment list-custom-content-attachments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content for which attachments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'trashed'], help='Filter the results to attachments based on their status. By default, `current` and `archived` are used.')
    c.add_argument('--media-type', dest='p_media_type', metavar='MEDIA_TYPE', help='Filters on the mediaType of attachments. Only one may be specified.')
    c.add_argument('--filename', dest='p_filename', metavar='FILENAME', help='Filters on the file-name of attachments. Only one may be specified.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 50)')
    c.set_defaults(handler=_run_attachment_list_custom_content_attachments, flags={'id': '--id', 'sort': '--sort', 'cursor': '--cursor', 'status': '--status', 'media_type': '--media-type', 'filename': '--filename', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_attachments'})
    c = g_attachment_commands.add_parser('list-label-attachments', parents=[common], help='Get attachments for label', description='Returns the attachments of specified label. The number of results is limited\nby the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment list-label-attachments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the label for which attachments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_attachment_list_label_attachments, flags={'id': '--id', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_label_attachments'})
    c = g_attachment_commands.add_parser('list-page-attachments', parents=[common], help='Get attachments for page', description='Returns the attachments of specific page. The number of results is limited by\nthe `limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment list-page-attachments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which attachments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'trashed'], help='Filter the results to attachments based on their status. By default, `current` and `archived` are used.')
    c.add_argument('--media-type', dest='p_media_type', metavar='MEDIA_TYPE', help='Filters on the mediaType of attachments. Only one may be specified.')
    c.add_argument('--filename', dest='p_filename', metavar='FILENAME', help='Filters on the file-name of attachments. Only one may be specified.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 50)')
    c.set_defaults(handler=_run_attachment_list_page_attachments, flags={'id': '--id', 'sort': '--sort', 'cursor': '--cursor', 'status': '--status', 'media_type': '--media-type', 'filename': '--filename', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_attachments'})
    c = g_attachment_commands.add_parser('get-thumbnail', parents=[common], help='Download attachment thumbnail by id', description="Redirects the client to a URL that serves an attachment thumbnail's binary\ndata.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment's container.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence attachment get-thumbnail ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help="The ID of the attachment to be returned. If you don't know the attachment's ID, use Get attachments for page/blogpost/custom content.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.")
    c.add_argument('--height', dest='p_height', type=integer, metavar='HEIGHT', help='Allows you to define the thumbnail height.')
    c.add_argument('--width', dest='p_width', type=integer, metavar='WIDTH', help='Allows you to define the thumbnail width.')
    c.set_defaults(handler=_run_attachment_get_thumbnail, flags={'id': '--id', 'version': '--arg-version', 'height': '--height', 'width': '--width'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_thumbnail_by_id'})
    g_blog_post = commands.add_parser('blog-post', help='create, delete, get, … (7 commands)', description="Run 'codapact-confluence blog-post COMMAND --help' for a command's options and examples.")
    g_blog_post_commands = g_blog_post.add_subparsers(dest="g_blog_post", metavar="COMMAND", required=True)
    c = g_blog_post_commands.add_parser('list-blog-posts', parents=[common], help='Get blog posts', description="Returns all blog posts. The number of results is limited by the `limit`\nparameter and additional results (if available) will be available through the\n`next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\nblog posts that the user has permission to view will be returned.", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence blog-post list-blog-posts']), formatter_class=RAW)
    c.add_argument('--id', dest='p_id', action="append", type=integer, metavar='ID', help='Filter the results based on blog post ids. Multiple blog post ids can be specified as a comma-separated list.')
    c.add_argument('--space-id', dest='p_space_id', action="append", type=integer, metavar='SPACE_ID', help='Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'deleted', 'trashed'], help='Filter the results to blog posts based on their status. By default, `current` is used.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Filter the results to blog posts based on their title.')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of blog posts per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_blog_post_list_blog_posts, flags={'id': '--id', 'space_id': '--space-id', 'sort': '--sort', 'status': '--status', 'title': '--title', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_posts'})
    c = g_blog_post_commands.add_parser('create', parents=[common], help='Create blog post', description='Creates a new blog post in the space specified by the spaceId.\n\nBy default this will create the blog post as a non-draft, unless the status is\nspecified as draft. If creating a non-draft, the title must not be empty.\n\nCurrently only supports the storage representation specified in the\nbody.representation enums below', usage='%(prog)s --space-id SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence blog-post create --space-id SPACE_ID', 'codapact-confluence blog-post create --space-id SPACE_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--private', dest='p_private', action=argparse.BooleanOptionalAction, help='The blog post will be private. Only the user who creates this blog post will have permission to view and edit one. (default: False)')
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', required=True, help='ID of the space')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft'], help='The status of the blog post, specifies if the blog post will be created as a new blog post or a draft')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Title of the blog post, required if creating non-draft.')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON")
    c.add_argument('--created-at', dest='p_created_at', metavar='CREATED_AT', help='Created date of the blog post in the format of "yyyy-MM-ddTHH:mm:ss.SSSZ".')
    c.set_defaults(handler=_run_blog_post_create, flags={'private': '--private', 'body.space_id': '--space-id', 'body.status': '--status', 'body.title': '--title', 'body.body': '--body', 'body.created_at': '--created-at'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_blog_post'})
    c = g_blog_post_commands.add_parser('get', parents=[common], help='Get blog post by id', description='Returns a specific blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence blog-post get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the blog post to be returned. If you don't know the blog post ID, use Get blog posts and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format', 'view', 'export_view', 'anonymous_export_view', 'styled_view', 'editor'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--get-draft', dest='p_get_draft', action=argparse.BooleanOptionalAction, help='Retrieve the draft version of this blog post. (default: False)')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'trashed', 'deleted', 'historical', 'draft'], help='Filter the blog post being retrieved by its status.')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.")
    c.add_argument('--include-labels', dest='p_include_labels', action=argparse.BooleanOptionalAction, help='Includes labels associated with this blog post in the response. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this blog post in the response. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this blog post in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-likes', dest='p_include_likes', action=argparse.BooleanOptionalAction, help='Includes likes associated with this blog post in the response. (default: False)')
    c.add_argument('--include-versions', dest='p_include_versions', action=argparse.BooleanOptionalAction, help='Includes versions associated with this blog post in the response. (default: False)')
    c.add_argument('--include-version', dest='p_include_version', action=argparse.BooleanOptionalAction, help='Includes the current version associated with this blog post in the response. (default: True)')
    c.add_argument('--include-favorited-by-current-user-status', dest='p_include_favorited_by_current_user_status', action=argparse.BooleanOptionalAction, help='Includes whether this blog post has been favorited by the current user. (default: False)')
    c.add_argument('--include-webresources', dest='p_include_webresources', action=argparse.BooleanOptionalAction, help='Includes web resources that can be used to render blog post content on a client. (default: False)')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the blog post. (default: False)')
    c.set_defaults(handler=_run_blog_post_get, flags={'id': '--id', 'body_format': '--body-format', 'get_draft': '--get-draft', 'status': '--status', 'version': '--arg-version', 'include_labels': '--include-labels', 'include_properties': '--include-properties', 'include_operations': '--include-operations', 'include_likes': '--include-likes', 'include_versions': '--include-versions', 'include_version': '--include-version', 'include_favorited_by_current_user_status': '--include-favorited-by-current-user-status', 'include_webresources': '--include-webresources', 'include_collaborators': '--include-collaborators'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_by_id'})
    c = g_blog_post_commands.add_parser('update', parents=[common], help='Update blog post', description='Update a blog post by id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post and its corresponding space. Permission to\nupdate blog posts in the space.', usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence blog-post update ID --body @body.json', 'codapact-confluence blog-post update ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the blog post to be updated. If you don't know the blog post ID, use Get Blog Posts and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id*, status*, title*, body*, version*, space_id, created_at (* required). Schema: codapact-confluence describe blog-post update')
    c.set_defaults(handler=_run_blog_post_update, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_blog_post'})
    c = g_blog_post_commands.add_parser('delete', parents=[common], help='Delete blog post', description='Delete a blog post by id.\n\nBy default this will delete blog posts that are non-drafts. To delete a blog\npost that is a draft, the endpoint must be called on a draft with the\nfollowing param `draft=true`. Discarded drafts are not sent to the trash and\nare permanently deleted.\n\nDeleting a blog post that is not a draft moves the blog post to the trash,\nwhere it can be restored later. To permanently delete a blog post (or "purge"\nit), the endpoint must be called on a **trashed** blog post with the following\nparam `purge=true`.\n\n**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-\nconfluences-roles/) required**: Permission to view the blog post and its\ncorresponding space. Permission to delete blog posts in the space. [`manage/co\nntent`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nspace-permissions/#api-space-permissions-get) permission for the space (if\nattempting to purge).\n\n**Note:** To find the display name for each permission ID, call the [Get\navailable space\npermissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) API.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence blog-post delete ID --dry-run', 'codapact-confluence blog-post delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--purge', dest='p_purge', action=argparse.BooleanOptionalAction, help='If attempting to purge the blog post. (default: False)')
    c.add_argument('--draft', dest='p_draft', action=argparse.BooleanOptionalAction, help='If attempting to delete a blog post that is a draft. (default: False)')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_blog_post_delete, flags={'id': '--id', 'purge': '--purge', 'draft': '--draft'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_blog_post'})
    c = g_blog_post_commands.add_parser('list-label-blog-posts', parents=[common], help='Get blog posts for label', description='Returns the blogposts of specified label. The number of results is limited by\nthe `limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence blog-post list-label-blog-posts ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the label for which blog posts should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--space-id', dest='p_space_id', action="append", type=integer, metavar='SPACE_ID', help='Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of blog posts per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_blog_post_list_label_blog_posts, flags={'id': '--id', 'space_id': '--space-id', 'body_format': '--body-format', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_label_blog_posts'})
    c = g_blog_post_commands.add_parser('get-blog-posts-in-space', parents=[common], help='Get blog posts in space', description="Returns all blog posts in a space. The number of results is limited by the\n`limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission) and\nview the space. Only blog posts that the user has permission to view will be\nreturned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence blog-post get-blog-posts-in-space ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which blog posts should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'deleted', 'trashed'], help='Filter the results to blog posts based on their status. By default, `current` is used.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Filter the results to blog posts based on their title.')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of blog posts per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_blog_post_get_blog_posts_in_space, flags={'id': '--id', 'sort': '--sort', 'status': '--status', 'title': '--title', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_posts_in_space'})
    g_children = commands.add_parser('children', help='get-child-custom-content, get-database-direct, get-folder-direct, … (7 commands)', description="Run 'codapact-confluence children COMMAND --help' for a command's options and examples.")
    g_children_commands = g_children.add_subparsers(dest="g_children", metavar="COMMAND", required=True)
    c = g_children_commands.add_parser('get-whiteboard-direct', parents=[common], help='Get direct children of a whiteboard', description="Returns all children for given whiteboard id in the content tree. The number\nof results is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each child. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\ncontent that the user has permission to view will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence children get-whiteboard-direct ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the parent whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_children_get_whiteboard_direct, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_direct_children'})
    c = g_children_commands.add_parser('get-database-direct', parents=[common], help='Get direct children of a database', description="Returns all children for given database id in the content tree. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each child. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\ncontent that the user has permission to view will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence children get-database-direct ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the parent database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_children_get_database_direct, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_direct_children'})
    c = g_children_commands.add_parser('get-smart-link-direct', parents=[common], help='Get direct children of a Smart Link', description="Returns all children for given smart link id in the content tree. The number\nof results is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each child. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\ncontent that the user has permission to view will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence children get-smart-link-direct ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the parent smart link.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_children_get_smart_link_direct, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_smart_link_direct_children'})
    c = g_children_commands.add_parser('get-folder-direct', parents=[common], help='Get direct children of a folder', description="Returns all children for given folder id in the content tree. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each child. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\ncontent that the user has permission to view will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence children get-folder-direct ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the parent folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_children_get_folder_direct, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_direct_children'})
    c = g_children_commands.add_parser('list-child-pages', parents=[common], help='[deprecated] Get child pages', description="Returns all child pages for given page id. The number of results is limited by\nthe `limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\npages that the user has permission to view will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence children list-child-pages ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the parent page. If you don't know the page ID, use Get pages and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_children_list_child_pages, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': True, 'operation': 'get_child_pages'})
    c = g_children_commands.add_parser('get-child-custom-content', parents=[common], help='Get child custom content', description="Returns all child custom content for given custom content id. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\ncustom content that the user has permission to view will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence children get-child-custom-content ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the parent custom content. If you don't know the custom content ID, use Get custom-content and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_children_get_child_custom_content, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_child_custom_content'})
    c = g_children_commands.add_parser('get-page-direct', parents=[common], help='Get direct children of a page', description="Returns all children for given page id in the content tree. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each child. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\ncontent that the user has permission to view will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence children get-page-direct ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the parent page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_children_get_page_direct, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_direct_children'})
    g_classification_level = commands.add_parser('classification-level', help='delete, get-blog-post, get-database, … (16 commands)', description="Run 'codapact-confluence classification-level COMMAND --help' for a command's options and examples.")
    g_classification_level_commands = g_classification_level.add_subparsers(dest="g_classification_level", metavar="COMMAND", required=True)
    c = g_classification_level_commands.add_parser('list-classification-levels', parents=[common], help='Get list of classification levels', description="Returns a list of [classification levels](https://developer.atlassian.com/clou\nd/admin/dlp/rest/intro/#Classification%20level) available.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission).", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level list-classification-levels']), formatter_class=RAW)
    c.set_defaults(handler=_run_classification_level_list_classification_levels, flags={}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_classification_levels'})
    c = g_classification_level_commands.add_parser('get-space-default', parents=[common], help='Get space default classification level', description="Returns the [default classification\nlevel](https://support.atlassian.com/security-and-access-policies/docs/what-\nis-a-default-classification-level/) for a specific space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the space.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level get-space-default ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which default classification level should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_classification_level_get_space_default, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_default_classification_level'})
    c = g_classification_level_commands.add_parser('put-space-default', parents=[common], help='Update space default classification level', description="Update the [default classification\nlevel](https://support.atlassian.com/security-and-access-policies/docs/what-\nis-a-default-classification-level/) for a specific space.\n\n**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-\nconfluences-roles/) required**: Permission to access the Confluence site ('Can\nuse' global permission) and\n[`manage/space`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) permission for the space.\n\n**Note:** To find the display name for each permission ID, call the [Get\navailable space\npermissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) API.", usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level put-space-default ID --body @body.json', 'codapact-confluence classification-level put-space-default ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which default classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id* (* required). Schema: codapact-confluence describe classification-level put-space-default')
    c.set_defaults(handler=_run_classification_level_put_space_default, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'put_space_default_classification_level'})
    c = g_classification_level_commands.add_parser('delete', parents=[common], help='Delete space default classification level', description="Returns the [default classification\nlevel](https://support.atlassian.com/security-and-access-policies/docs/what-\nis-a-default-classification-level/) for a specific space.\n\n**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-\nconfluences-roles/) required**: Permission to access the Confluence site ('Can\nuse' global permission) and\n[`manage/space`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) permission for the space.\n\n**Note:** To find the display name for each permission ID, call the [Get\navailable space\npermissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) API.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level delete ID --dry-run', 'codapact-confluence classification-level delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which default classification level should be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_classification_level_delete, flags={'id': '--id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_space_default_classification_level'})
    c = g_classification_level_commands.add_parser('get-page', parents=[common], help='Get page classification level', description="Returns the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the page. 'Permission to edit the page is required if\ntrying to view classification level for a draft.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level get-page ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which classification level should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft', 'archived'], help='Status of page from which classification level will fetched. (default: current)')
    c.set_defaults(handler=_run_classification_level_get_page, flags={'id': '--id', 'status': '--status'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_classification_level'})
    c = g_classification_level_commands.add_parser('put-page', parents=[common], help='Update page classification level', description="Updates the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to edit the page.", usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level put-page ID --body @body.json', 'codapact-confluence classification-level put-page ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id*, status* (* required). Schema: codapact-confluence describe classification-level put-page')
    c.set_defaults(handler=_run_classification_level_put_page, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'put_page_classification_level'})
    c = g_classification_level_commands.add_parser('post-page', parents=[common], help='Reset page classification level', description="Resets the [classification level](https://developer.atlassian.com/cloud/admin/\ndlp/rest/intro/#Classification%20level) for a specific page for the space\n[default classification level](https://support.atlassian.com/security-and-\naccess-policies/docs/what-is-a-default-classification-level/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the page.", usage='%(prog)s ID --status {current,draft} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level post-page ID --status current', 'codapact-confluence classification-level post-page ID --status current --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft'], required=True, help='Status of the content.')
    c.set_defaults(handler=_run_classification_level_post_page, flags={'id': '--id', 'body.status': '--status'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'post_page_classification_level'})
    c = g_classification_level_commands.add_parser('get-blog-post', parents=[common], help='Get blog post classification level', description="Returns the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the blog post. 'Permission to edit the blog post is\nrequired if trying to view classification level for a draft.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level get-blog-post ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which classification level should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft', 'archived'], help='Status of blog post from which classification level will fetched. (default: current)')
    c.set_defaults(handler=_run_classification_level_get_blog_post, flags={'id': '--id', 'status': '--status'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_classification_level'})
    c = g_classification_level_commands.add_parser('put-blog-post', parents=[common], help='Update blog post classification level', description="Updates the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to edit the blog post.", usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level put-blog-post ID --body @body.json', 'codapact-confluence classification-level put-blog-post ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id*, status* (* required). Schema: codapact-confluence describe classification-level put-blog-post')
    c.set_defaults(handler=_run_classification_level_put_blog_post, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'put_blog_post_classification_level'})
    c = g_classification_level_commands.add_parser('post-blog-post', parents=[common], help='Reset blog post classification level', description="Resets the [classification level](https://developer.atlassian.com/cloud/admin/\ndlp/rest/intro/#Classification%20level) for a specific blog post for the space\n[default classification level](https://support.atlassian.com/security-and-\naccess-policies/docs/what-is-a-default-classification-level/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the blog post.", usage='%(prog)s ID --status {current,draft} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level post-blog-post ID --status current', 'codapact-confluence classification-level post-blog-post ID --status current --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft'], required=True, help='Status of the content.')
    c.set_defaults(handler=_run_classification_level_post_blog_post, flags={'id': '--id', 'body.status': '--status'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'post_blog_post_classification_level'})
    c = g_classification_level_commands.add_parser('get-whiteboard', parents=[common], help='Get whiteboard classification level', description="Returns the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the whiteboard.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level get-whiteboard ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard for which classification level should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_classification_level_get_whiteboard, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_classification_level'})
    c = g_classification_level_commands.add_parser('put-whiteboard', parents=[common], help='Update whiteboard classification level', description="Updates the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to edit the whiteboard.", usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level put-whiteboard ID --body @body.json', 'codapact-confluence classification-level put-whiteboard ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id*, status* (* required). Schema: codapact-confluence describe classification-level put-whiteboard')
    c.set_defaults(handler=_run_classification_level_put_whiteboard, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'put_whiteboard_classification_level'})
    c = g_classification_level_commands.add_parser('post-whiteboard', parents=[common], help='Reset whiteboard classification level', description="Resets the [classification level](https://developer.atlassian.com/cloud/admin/\ndlp/rest/intro/#Classification%20level) for a specific whiteboard for the\nspace [default classification level](https://support.atlassian.com/security-\nand-access-policies/docs/what-is-a-default-classification-level/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the whiteboard.", usage='%(prog)s ID --status {current} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level post-whiteboard ID --status current', 'codapact-confluence classification-level post-whiteboard ID --status current --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--status', dest='p_status', choices=['current'], required=True, help='Status of the content.')
    c.set_defaults(handler=_run_classification_level_post_whiteboard, flags={'id': '--id', 'body.status': '--status'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'post_whiteboard_classification_level'})
    c = g_classification_level_commands.add_parser('get-database', parents=[common], help='Get database classification level', description="Returns the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the database.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level get-database ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database for which classification level should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_classification_level_get_database, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_classification_level'})
    c = g_classification_level_commands.add_parser('put-database', parents=[common], help='Update database classification level', description="Updates the [classification level](https://developer.atlassian.com/cloud/admin\n/dlp/rest/intro/#Classification%20level) for a specific database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to edit the database.", usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level put-database ID --body @body.json', 'codapact-confluence classification-level put-database ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id*, status* (* required). Schema: codapact-confluence describe classification-level put-database')
    c.set_defaults(handler=_run_classification_level_put_database, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'put_database_classification_level'})
    c = g_classification_level_commands.add_parser('post-database', parents=[common], help='Reset database classification level', description="Resets the [classification level](https://developer.atlassian.com/cloud/admin/\ndlp/rest/intro/#Classification%20level) for a specific database for the space\n[default classification level](https://support.atlassian.com/security-and-\naccess-policies/docs/what-is-a-default-classification-level/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\n'Permission to access the Confluence site ('Can use' global permission) and\npermission to view the database.", usage='%(prog)s ID --status {current} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence classification-level post-database ID --status current', 'codapact-confluence classification-level post-database ID --status current --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database for which classification level should be updated.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--status', dest='p_status', choices=['current'], required=True, help='Status of the content.')
    c.set_defaults(handler=_run_classification_level_post_database, flags={'id': '--id', 'body.status': '--status'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'post_database_classification_level'})
    g_comment = commands.add_parser('comment', help='create-footer, create-inline, delete-footer, … (18 commands)', description="Run 'codapact-confluence comment COMMAND --help' for a command's options and examples.")
    g_comment_commands = g_comment.add_subparsers(dest="g_comment", metavar="COMMAND", required=True)
    c = g_comment_commands.add_parser('list-attachment-comments', parents=[common], help='Get attachment comments', description='Returns the comments of the specific attachment. The number of results is\nlimited by the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment and its corresponding containers.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-attachment-comments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment for which comments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help='Version number of the attachment to retrieve comments for. If no version provided, retrieves comments for the latest version.')
    c.set_defaults(handler=_run_comment_list_attachment_comments, flags={'id': '--id', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort', 'version': '--arg-version'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_comments'})
    c = g_comment_commands.add_parser('list-custom-content-comments', parents=[common], help='Get custom content comments', description='Returns the comments of the specific custom content. The number of results is\nlimited by the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content and its corresponding containers.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-custom-content-comments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content for which comments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_comment_list_custom_content_comments, flags={'id': '--id', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_comments'})
    c = g_comment_commands.add_parser('list-page-footer-comments', parents=[common], help='Get footer comments for page', description='Returns the root footer comments of specific page. The number of results is\nlimited by the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-page-footer-comments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which footer comments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'trashed', 'deleted', 'historical', 'draft'], help='Filter the footer comment being retrieved by its status.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_list_page_footer_comments, flags={'id': '--id', 'body_format': '--body-format', 'status': '--status', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_footer_comments'})
    c = g_comment_commands.add_parser('list-page-inline-comments', parents=[common], help='Get inline comments for page', description='Returns the root inline comments of specific page. The number of results is\nlimited by the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-page-inline-comments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which inline comments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'trashed', 'deleted', 'historical', 'draft'], help='Filter the inline comment being retrieved by its status.')
    c.add_argument('--resolution-status', dest='p_resolution_status', action="append", choices=['resolved', 'open', 'dangling', 'reopened'], help='Filter the inline comment being retrieved by its resolution status.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of inline comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_list_page_inline_comments, flags={'id': '--id', 'body_format': '--body-format', 'status': '--status', 'resolution_status': '--resolution-status', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_inline_comments'})
    c = g_comment_commands.add_parser('list-blog-post-footer-comments', parents=[common], help='Get footer comments for blog post', description='Returns the root footer comments of specific blog post. The number of results\nis limited by the `limit` parameter and additional results (if available) will\nbe available through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the blog post and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-blog-post-footer-comments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which footer comments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'deleted', 'trashed', 'historical', 'draft'], help='Filter the footer comment being retrieved by its status.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_list_blog_post_footer_comments, flags={'id': '--id', 'body_format': '--body-format', 'status': '--status', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_footer_comments'})
    c = g_comment_commands.add_parser('list-blog-post-inline-comments', parents=[common], help='Get inline comments for blog post', description='Returns the root inline comments of specific blog post. The number of results\nis limited by the `limit` parameter and additional results (if available) will\nbe available through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the blog post and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-blog-post-inline-comments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which inline comments should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'deleted', 'trashed', 'historical', 'draft'], help='Filter the inline comment being retrieved by its status.')
    c.add_argument('--resolution-status', dest='p_resolution_status', action="append", choices=['resolved', 'open', 'dangling', 'reopened'], help='Filter the inline comment being retrieved by its resolution status.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of inline comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_list_blog_post_inline_comments, flags={'id': '--id', 'body_format': '--body-format', 'status': '--status', 'resolution_status': '--resolution-status', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_inline_comments'})
    c = g_comment_commands.add_parser('list-footer-comments', parents=[common], help='Get footer comments', description='Returns all footer comments. The number of results is limited by the `limit`\nparameter and additional results (if available) will be available through the\n`next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the container and its corresponding space.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-footer-comments']), formatter_class=RAW)
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_list_footer_comments, flags={'body_format': '--body-format', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_comments'})
    c = g_comment_commands.add_parser('create-footer', parents=[common], help='Create footer comment', description='Create a footer comment.\n\nThe footer comment can be made against several locations: - at the top level\n(specifying pageId or blogPostId in the request body) - as a reply (specifying\nparentCommentId in the request body) - against an attachment (note: this is\ndifferent than the comments added via the attachment properties page on the\nUI, which are referred to as version comments) - against a custom content\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to create comments in the space.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment create-footer --blog-post-id BLOG_POST_ID', 'codapact-confluence comment create-footer --blog-post-id BLOG_POST_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--blog-post-id', dest='p_blog_post_id', metavar='BLOG_POST_ID', help='ID of the containing blog post, if intending to create a top level footer comment. Do not provide if creating a reply.')
    c.add_argument('--page-id', dest='p_page_id', metavar='PAGE_ID', help='ID of the containing page, if intending to create a top level footer comment. Do not provide if creating a reply.')
    c.add_argument('--parent-comment-id', dest='p_parent_comment_id', metavar='PARENT_COMMENT_ID', help='ID of the parent comment, if intending to create a reply. Do not provide if creating a top level comment.')
    c.add_argument('--attachment-id', dest='p_attachment_id', metavar='ATTACHMENT_ID', help='ID of the attachment, if intending to create a comment against an attachment.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', metavar='CUSTOM_CONTENT_ID', help='ID of the custom content, if intending to create a comment against a custom content.')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON")
    c.set_defaults(handler=_run_comment_create_footer, flags={'body.blog_post_id': '--blog-post-id', 'body.page_id': '--page-id', 'body.parent_comment_id': '--parent-comment-id', 'body.attachment_id': '--attachment-id', 'body.custom_content_id': '--custom-content-id', 'body.body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_footer_comment', 'requires_one_of': [['--blog-post-id', '--page-id', '--parent-comment-id', '--attachment-id', '--custom-content-id', '--body']]})
    c = g_comment_commands.add_parser('get-footer', parents=[common], help='Get footer comment by id', description='Retrieves a footer comment by id\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the container and its corresponding space.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment get-footer COMMENT_ID']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment to be retrieved.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format', 'view', 'export_view', 'anonymous_export_view', 'styled_view', 'editor'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.")
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this footer comment in the response. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this footer comment in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-likes', dest='p_include_likes', action=argparse.BooleanOptionalAction, help='Includes likes associated with this footer comment in the response. (default: False)')
    c.add_argument('--include-versions', dest='p_include_versions', action=argparse.BooleanOptionalAction, help='Includes versions associated with this footer comment in the response. (default: False)')
    c.add_argument('--include-version', dest='p_include_version', action=argparse.BooleanOptionalAction, help='Includes the current version associated with this footer comment in the response. (default: True)')
    c.set_defaults(handler=_run_comment_get_footer, flags={'comment_id': '--comment-id', 'body_format': '--body-format', 'version': '--arg-version', 'include_properties': '--include-properties', 'include_operations': '--include-operations', 'include_likes': '--include-likes', 'include_versions': '--include-versions', 'include_version': '--include-version'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_comment_by_id'})
    c = g_comment_commands.add_parser('update-footer', parents=[common], help='Update footer comment', description='Update a footer comment. This can be used to update the body text of a\ncomment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to create comments in the space.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment update-footer COMMENT_ID --arg-version @arg-version.json', 'codapact-confluence comment update-footer COMMENT_ID --arg-version @arg-version.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment to be retrieved.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='JSON object with number, message. Schema: codapact-confluence describe comment update-footer')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON")
    c.add_argument('--links', dest='p_links', type=json_value, metavar="JSON", help='JSON object with base. Schema: codapact-confluence describe comment update-footer')
    c.set_defaults(handler=_run_comment_update_footer, flags={'comment_id': '--comment-id', 'body.version': '--arg-version', 'body.body': '--body', 'body.links': '--links'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_footer_comment', 'requires_one_of': [['--arg-version', '--body', '--links']]})
    c = g_comment_commands.add_parser('delete-footer', parents=[common], help='Delete footer comment', description='Deletes a footer comment. This is a permanent deletion and cannot be reverted.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to delete comments in the space.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment delete-footer COMMENT_ID --dry-run', 'codapact-confluence comment delete-footer COMMENT_ID --yes']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment to be retrieved.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_comment_delete_footer, flags={'comment_id': '--comment-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_footer_comment'})
    c = g_comment_commands.add_parser('get-footer-children', parents=[common], help='Get children footer comments', description='Returns the children footer comments of specific comment. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment get-footer-children ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the parent comment for which footer comment children should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_get_footer_children, flags={'id': '--id', 'body_format': '--body-format', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_comment_children'})
    c = g_comment_commands.add_parser('list-inline-comments', parents=[common], help='Get inline comments', description='Returns all inline comments. The number of results is limited by the `limit`\nparameter and additional results (if available) will be available through the\n`next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment list-inline-comments']), formatter_class=RAW)
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_list_inline_comments, flags={'body_format': '--body-format', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_comments'})
    c = g_comment_commands.add_parser('create-inline', parents=[common], help='Create inline comment', description='Create an inline comment. This can be at the top level (specifying pageId or\nblogPostId in the request body) or as a reply (specifying parentCommentId in\nthe request body). Note the inlineCommentProperties object in the request body\nis used to select the text the inline comment should be tied to. This is what\ndetermines the text highlighting when viewing a page in Confluence.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to create comments in the space.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment create-inline --blog-post-id BLOG_POST_ID', 'codapact-confluence comment create-inline --blog-post-id BLOG_POST_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--blog-post-id', dest='p_blog_post_id', metavar='BLOG_POST_ID', help='ID of the containing blog post, if intending to create a top level footer comment. Do not provide if creating a reply.')
    c.add_argument('--page-id', dest='p_page_id', metavar='PAGE_ID', help='ID of the containing page, if intending to create a top level footer comment. Do not provide if creating a reply.')
    c.add_argument('--parent-comment-id', dest='p_parent_comment_id', metavar='PARENT_COMMENT_ID', help='ID of the parent comment, if intending to create a reply. Do not provide if creating a top level comment.')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON")
    c.add_argument('--inline-comment-properties', dest='p_inline_comment_properties', type=json_value, metavar="JSON", help='Object describing the text to highlight on the page/blog post. Only applicable for top level inline comments (not replies) and required in that case. JSON object with text_selection, text_selection_match_count, text_selection_match_index. Schema: codapact-confluence describe comment create-inline')
    c.set_defaults(handler=_run_comment_create_inline, flags={'body.blog_post_id': '--blog-post-id', 'body.page_id': '--page-id', 'body.parent_comment_id': '--parent-comment-id', 'body.body': '--body', 'body.inline_comment_properties': '--inline-comment-properties'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_inline_comment', 'requires_one_of': [['--blog-post-id', '--page-id', '--parent-comment-id', '--body', '--inline-comment-properties']]})
    c = g_comment_commands.add_parser('get-inline', parents=[common], help='Get inline comment by id', description='Retrieves an inline comment by id\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment get-inline COMMENT_ID']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment to be retrieved.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format', 'view', 'export_view', 'anonymous_export_view', 'styled_view', 'editor'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.")
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this inline comment in the response. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this inline comment in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-likes', dest='p_include_likes', action=argparse.BooleanOptionalAction, help='Includes likes associated with this inline comment in the response. (default: False)')
    c.add_argument('--include-versions', dest='p_include_versions', action=argparse.BooleanOptionalAction, help='Includes versions associated with this inline comment in the response. (default: False)')
    c.add_argument('--include-version', dest='p_include_version', action=argparse.BooleanOptionalAction, help='Includes the current version associated with this inline comment in the response. (default: True)')
    c.set_defaults(handler=_run_comment_get_inline, flags={'comment_id': '--comment-id', 'body_format': '--body-format', 'version': '--arg-version', 'include_properties': '--include-properties', 'include_operations': '--include-operations', 'include_likes': '--include-likes', 'include_versions': '--include-versions', 'include_version': '--include-version'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_comment_by_id'})
    c = g_comment_commands.add_parser('update-inline', parents=[common], help='Update inline comment', description='Update an inline comment. This can be used to update the body text of a\ncomment and/or to resolve the comment\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to create comments in the space.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment update-inline COMMENT_ID --arg-version @arg-version.json', 'codapact-confluence comment update-inline COMMENT_ID --arg-version @arg-version.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment to be retrieved.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='JSON object with number, message. Schema: codapact-confluence describe comment update-inline')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON")
    c.add_argument('--resolved', dest='p_resolved', action=argparse.BooleanOptionalAction, help='Resolved state of the comment. Set to true to resolve the comment, set to false to reopen it. If')
    c.set_defaults(handler=_run_comment_update_inline, flags={'comment_id': '--comment-id', 'body.version': '--arg-version', 'body.body': '--body', 'body.resolved': '--resolved'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_inline_comment', 'requires_one_of': [['--arg-version', '--body', '--resolved']]})
    c = g_comment_commands.add_parser('delete-inline', parents=[common], help='Delete inline comment', description='Deletes an inline comment. This is a permanent deletion and cannot be\nreverted.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to delete comments in the space.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment delete-inline COMMENT_ID --dry-run', 'codapact-confluence comment delete-inline COMMENT_ID --yes']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment to be deleted.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_comment_delete_inline, flags={'comment_id': '--comment-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_inline_comment'})
    c = g_comment_commands.add_parser('get-inline-children', parents=[common], help='Get children inline comments', description='Returns the children inline comments of specific comment. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence comment get-inline-children ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the parent comment for which inline comment children should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format type to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--sort', dest='p_sort', choices=['created-date', '-created-date', 'modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of footer comments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_comment_get_inline_children, flags={'id': '--id', 'body_format': '--body-format', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_comment_children'})
    g_content = commands.add_parser('content', help='convert-ids-to-content-types', description="Run 'codapact-confluence content COMMAND --help' for a command's options and examples.")
    g_content_commands = g_content.add_subparsers(dest="g_content", metavar="COMMAND", required=True)
    c = g_content_commands.add_parser('convert-ids-to-content-types', parents=[common], help='Convert content ids to content types', description='Converts a list of content ids into their associated content types. This is\nuseful for users migrating from v1 to v2 who may have stored just content ids\nwithout their associated type. This will return types as they should be used\nin v2. Notably, this will return `inline-comment` for inline comments and\n`footer-comment` for footer comments, which is distinct from them both being\nrepresented by `comment` in v1.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the requested content. Any content that the user does not\nhave permission to view or does not exist will map to `null` in the response.', usage='%(prog)s --content-ids @content-ids.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content convert-ids-to-content-types --content-ids @content-ids.json', 'codapact-confluence content convert-ids-to-content-types --content-ids @content-ids.json --dry-run']), formatter_class=RAW)
    c.add_argument('--content-ids', dest='p_content_ids', type=json_value, metavar="JSON", required=True, help='The content ids to convert. They may be provided as strings or numbers.')
    c.set_defaults(handler=_run_content_convert_ids_to_content_types, flags={'body.content_ids': '--content-ids'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'convert_content_ids_to_content_types'})
    g_content_permissions = commands.add_parser('content-permissions', help='add-blog-post-permissions, add-database-permissions, add-folder-permissions, … (30 commands)', description="Run 'codapact-confluence content-permissions COMMAND --help' for a command's options and examples.")
    g_content_permissions_commands = g_content_permissions.add_subparsers(dest="g_content_permissions", metavar="COMMAND", required=True)
    c = g_content_permissions_commands.add_parser('get-page-restriction-state', parents=[common], help='Get page restriction state', description='Returns the restriction state of a page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions get-page-restriction-state ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_content_permissions_get_page_restriction_state, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_restriction_state'})
    c = g_content_permissions_commands.add_parser('set-page-restriction-state', parents=[common], help='Set page restriction state', description='Sets the restriction state of a page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the page or administer the space.', usage='%(prog)s ID --state {OPEN,EDIT_RESTRICTED,VIEW_RESTRICTED} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-page-restriction-state ID --state OPEN', 'codapact-confluence content-permissions set-page-restriction-state ID --state OPEN --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--state', dest='p_state', choices=['OPEN', 'EDIT_RESTRICTED', 'VIEW_RESTRICTED'], required=True)
    c.set_defaults(handler=_run_content_permissions_set_page_restriction_state, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.state': '--state'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_page_restriction_state'})
    c = g_content_permissions_commands.add_parser('get-blog-post-restriction-state', parents=[common], help='Get blog post restriction state', description='Returns the restriction state of a blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions get-blog-post-restriction-state ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_content_permissions_get_blog_post_restriction_state, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_restriction_state'})
    c = g_content_permissions_commands.add_parser('set-blog-post-restriction-state', parents=[common], help='Set blog post restriction state', description='Sets the restriction state of a blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the blog post or administer the space.', usage='%(prog)s ID --state {OPEN,EDIT_RESTRICTED,VIEW_RESTRICTED} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-blog-post-restriction-state ID --state OPEN', 'codapact-confluence content-permissions set-blog-post-restriction-state ID --state OPEN --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--state', dest='p_state', choices=['OPEN', 'EDIT_RESTRICTED', 'VIEW_RESTRICTED'], required=True)
    c.set_defaults(handler=_run_content_permissions_set_blog_post_restriction_state, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.state': '--state'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_blog_post_restriction_state'})
    c = g_content_permissions_commands.add_parser('get-database-restriction-state', parents=[common], help='Get database restriction state', description='Returns the restriction state of a database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions get-database-restriction-state ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_content_permissions_get_database_restriction_state, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_restriction_state'})
    c = g_content_permissions_commands.add_parser('set-database-restriction-state', parents=[common], help='Set database restriction state', description='Sets the restriction state of a database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the database or administer the space.', usage='%(prog)s ID --state {OPEN,EDIT_RESTRICTED,VIEW_RESTRICTED} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-database-restriction-state ID --state OPEN', 'codapact-confluence content-permissions set-database-restriction-state ID --state OPEN --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--state', dest='p_state', choices=['OPEN', 'EDIT_RESTRICTED', 'VIEW_RESTRICTED'], required=True)
    c.set_defaults(handler=_run_content_permissions_set_database_restriction_state, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.state': '--state'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_database_restriction_state'})
    c = g_content_permissions_commands.add_parser('get-whiteboard-restriction-state', parents=[common], help='Get whiteboard restriction state', description='Returns the restriction state of a whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the whiteboard.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions get-whiteboard-restriction-state ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_content_permissions_get_whiteboard_restriction_state, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_restriction_state'})
    c = g_content_permissions_commands.add_parser('set-whiteboard-restriction-state', parents=[common], help='Set whiteboard restriction state', description='Sets the restriction state of a whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the whiteboard or administer the space.', usage='%(prog)s ID --state {OPEN,EDIT_RESTRICTED,VIEW_RESTRICTED} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-whiteboard-restriction-state ID --state OPEN', 'codapact-confluence content-permissions set-whiteboard-restriction-state ID --state OPEN --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--state', dest='p_state', choices=['OPEN', 'EDIT_RESTRICTED', 'VIEW_RESTRICTED'], required=True)
    c.set_defaults(handler=_run_content_permissions_set_whiteboard_restriction_state, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.state': '--state'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_whiteboard_restriction_state'})
    c = g_content_permissions_commands.add_parser('get-folder-restriction-state', parents=[common], help='Get folder restriction state', description='Returns the restriction state of a folder.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the folder.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions get-folder-restriction-state ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_content_permissions_get_folder_restriction_state, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_restriction_state'})
    c = g_content_permissions_commands.add_parser('set-folder-restriction-state', parents=[common], help='Set folder restriction state', description='Sets the restriction state of a folder.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the folder or administer the space.', usage='%(prog)s ID --state {OPEN,EDIT_RESTRICTED,VIEW_RESTRICTED} [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-folder-restriction-state ID --state OPEN', 'codapact-confluence content-permissions set-folder-restriction-state ID --state OPEN --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--state', dest='p_state', choices=['OPEN', 'EDIT_RESTRICTED', 'VIEW_RESTRICTED'], required=True)
    c.set_defaults(handler=_run_content_permissions_set_folder_restriction_state, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.state': '--state'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_folder_restriction_state'})
    c = g_content_permissions_commands.add_parser('list-page-permissions', parents=[common], help='Get page permissions', description='Returns the direct content permissions on a page with optional filtering by\noperation, principal-type, and principal-id. Results are cursor-paginated (max\n250 per page).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions list-page-permissions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation (`read` or `update`).')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type (`user` or `group`). May be used without `principal-id` to return all permissions for that type.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help="Opaque cursor for pagination. Use the value from the previous response's `_links.next`.")
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of permission entries to return. Must be between 1 and 250. (default: 100)')
    c.set_defaults(handler=_run_content_permissions_list_page_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_permissions'})
    c = g_content_permissions_commands.add_parser('set-page-permissions', parents=[common], help='Set page permissions', description='Replaces all direct content permissions on a page with the provided set. Any\npermissions not included in the request body are removed.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the page or administer the space.', usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-page-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions set-page-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions set-page-permissions')
    c.set_defaults(handler=_run_content_permissions_set_page_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_page_permissions'})
    c = g_content_permissions_commands.add_parser('add-page-permissions', parents=[common], help='Add page permissions', description="Adds or replaces direct content permissions for the specified principals on a\npage. Permissions for other principals are preserved; use `PUT` to replace all\npermissions at once.\n\nA principal can hold only one `read` or `update` permission. Adding `read` for\na principal that currently has `update` downgrades that principal to `read`;\nadding `update` upgrades them. If the same request contains both operations\nfor a principal, `update` takes precedence.\n\nReasserting a principal's existing permission is idempotent and returns a\nsuccessful response without creating a duplicate entry.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the page or administer the space.", usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions add-page-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions add-page-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions add-page-permissions')
    c.set_defaults(handler=_run_content_permissions_add_page_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'add_page_permissions'})
    c = g_content_permissions_commands.add_parser('delete-page-permissions', parents=[common], help='Delete page permissions', description="Deletes direct content permissions from a page. Filters narrow the deletion\nscope; omitting all filters deletes all direct permissions.\n\nThe following filter combinations are supported: - No filters: deletes all\ndirect permissions. - `principal-type` + `principal-id`: deletes the\nprincipal's direct `read` or `update` permission. - `operation` + `principal-\ntype` + `principal-id`: deletes the permission only when its operation\nmatches.\n\nProviding `operation` without `principal-type`/`principal-id`, or providing\nonly one of `principal-type`/`principal-id`, returns a 400 error.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the page or administer the space.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions delete-page-permissions ID --dry-run', 'codapact-confluence content-permissions delete-page-permissions ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation. Must be provided together with `principal-type` and `principal-id`.')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type. Must be provided together with `principal-id`.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_permissions_delete_page_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'allow_self_lockout': '--allow-self-lockout'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_page_permissions'})
    c = g_content_permissions_commands.add_parser('list-blog-post-permissions', parents=[common], help='Get blog post permissions', description='Returns the direct content permissions on a blog post with optional filtering\nby operation, principal-type, and principal-id. Results are cursor-paginated\n(max 250 per page).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions list-blog-post-permissions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation (`read` or `update`).')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type (`user` or `group`). May be used without `principal-id` to return all permissions for that type.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help="Opaque cursor for pagination. Use the value from the previous response's `_links.next`.")
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of permission entries to return. Must be between 1 and 250. (default: 100)')
    c.set_defaults(handler=_run_content_permissions_list_blog_post_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_permissions'})
    c = g_content_permissions_commands.add_parser('set-blog-post-permissions', parents=[common], help='Set blog post permissions', description='Replaces all direct content permissions on a blog post with the provided set.\nAny permissions not included in the request body are removed.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the blog post or administer the space.', usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-blog-post-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions set-blog-post-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions set-blog-post-permissions')
    c.set_defaults(handler=_run_content_permissions_set_blog_post_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_blog_post_permissions'})
    c = g_content_permissions_commands.add_parser('add-blog-post-permissions', parents=[common], help='Add blog post permissions', description="Adds or replaces direct content permissions for the specified principals on a\nblog post. Permissions for other principals are preserved; use `PUT` to\nreplace all permissions at once.\n\nA principal can hold only one `read` or `update` permission. Adding `read` for\na principal that currently has `update` downgrades that principal to `read`;\nadding `update` upgrades them. If the same request contains both operations\nfor a principal, `update` takes precedence.\n\nReasserting a principal's existing permission is idempotent and returns a\nsuccessful response without creating a duplicate entry.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the blog post or administer the space.", usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions add-blog-post-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions add-blog-post-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions add-blog-post-permissions')
    c.set_defaults(handler=_run_content_permissions_add_blog_post_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'add_blog_post_permissions'})
    c = g_content_permissions_commands.add_parser('delete-blog-post-permissions', parents=[common], help='Delete blog post permissions', description='Deletes direct content permissions from a blog post. See `DELETE\n/pages/{id}/permissions` for filter semantics.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the blog post or administer the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions delete-blog-post-permissions ID --dry-run', 'codapact-confluence content-permissions delete-blog-post-permissions ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation. Must be provided together with `principal-type` and `principal-id`.')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type. Must be provided together with `principal-id`.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_permissions_delete_blog_post_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'allow_self_lockout': '--allow-self-lockout'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_blog_post_permissions'})
    c = g_content_permissions_commands.add_parser('list-database-permissions', parents=[common], help='Get database permissions', description='Returns the direct content permissions on a database with optional filtering.\nResults are cursor-paginated (max 250 per page).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions list-database-permissions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation (`read` or `update`).')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type (`user` or `group`). May be used without `principal-id` to return all permissions for that type.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help="Opaque cursor for pagination. Use the value from the previous response's `_links.next`.")
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of permission entries to return. Must be between 1 and 250. (default: 100)')
    c.set_defaults(handler=_run_content_permissions_list_database_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_permissions'})
    c = g_content_permissions_commands.add_parser('set-database-permissions', parents=[common], help='Set database permissions', description='Replaces all direct content permissions on a database with the provided set.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the database or administer the space.', usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-database-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions set-database-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions set-database-permissions')
    c.set_defaults(handler=_run_content_permissions_set_database_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_database_permissions'})
    c = g_content_permissions_commands.add_parser('add-database-permissions', parents=[common], help='Add database permissions', description="Adds or replaces direct content permissions for the specified principals on a\ndatabase. Permissions for other principals are preserved; use `PUT` to replace\nall permissions at once.\n\nA principal can hold only one `read` or `update` permission. Adding `read` for\na principal that currently has `update` downgrades that principal to `read`;\nadding `update` upgrades them. If the same request contains both operations\nfor a principal, `update` takes precedence.\n\nReasserting a principal's existing permission is idempotent and returns a\nsuccessful response without creating a duplicate entry.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the database or administer the space.", usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions add-database-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions add-database-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions add-database-permissions')
    c.set_defaults(handler=_run_content_permissions_add_database_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'add_database_permissions'})
    c = g_content_permissions_commands.add_parser('delete-database-permissions', parents=[common], help='Delete database permissions', description='Deletes direct content permissions from a database. See `DELETE\n/pages/{id}/permissions` for filter semantics.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the database or administer the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions delete-database-permissions ID --dry-run', 'codapact-confluence content-permissions delete-database-permissions ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation. Must be provided together with `principal-type` and `principal-id`.')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type. Must be provided together with `principal-id`.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_permissions_delete_database_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'allow_self_lockout': '--allow-self-lockout'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_database_permissions'})
    c = g_content_permissions_commands.add_parser('list-whiteboard-permissions', parents=[common], help='Get whiteboard permissions', description='Returns the direct content permissions on a whiteboard with optional\nfiltering. Results are cursor-paginated (max 250 per page).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the whiteboard.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions list-whiteboard-permissions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation (`read` or `update`).')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type (`user` or `group`). May be used without `principal-id` to return all permissions for that type.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help="Opaque cursor for pagination. Use the value from the previous response's `_links.next`.")
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of permission entries to return. Must be between 1 and 250. (default: 100)')
    c.set_defaults(handler=_run_content_permissions_list_whiteboard_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_permissions'})
    c = g_content_permissions_commands.add_parser('set-whiteboard-permissions', parents=[common], help='Set whiteboard permissions', description='Replaces all direct content permissions on a whiteboard with the provided set.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the whiteboard or administer the space.', usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-whiteboard-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions set-whiteboard-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions set-whiteboard-permissions')
    c.set_defaults(handler=_run_content_permissions_set_whiteboard_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_whiteboard_permissions'})
    c = g_content_permissions_commands.add_parser('add-whiteboard-permissions', parents=[common], help='Add whiteboard permissions', description="Adds or replaces direct content permissions for the specified principals on a\nwhiteboard. Permissions for other principals are preserved; use `PUT` to\nreplace all permissions at once.\n\nA principal can hold only one `read` or `update` permission. Adding `read` for\na principal that currently has `update` downgrades that principal to `read`;\nadding `update` upgrades them. If the same request contains both operations\nfor a principal, `update` takes precedence.\n\nReasserting a principal's existing permission is idempotent and returns a\nsuccessful response without creating a duplicate entry.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the whiteboard or administer the space.", usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions add-whiteboard-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions add-whiteboard-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions add-whiteboard-permissions')
    c.set_defaults(handler=_run_content_permissions_add_whiteboard_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'add_whiteboard_permissions'})
    c = g_content_permissions_commands.add_parser('delete-whiteboard-permissions', parents=[common], help='Delete whiteboard permissions', description='Deletes direct content permissions from a whiteboard. See `DELETE\n/pages/{id}/permissions` for filter semantics.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the whiteboard or administer the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions delete-whiteboard-permissions ID --dry-run', 'codapact-confluence content-permissions delete-whiteboard-permissions ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation. Must be provided together with `principal-type` and `principal-id`.')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type. Must be provided together with `principal-id`.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_permissions_delete_whiteboard_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'allow_self_lockout': '--allow-self-lockout'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_whiteboard_permissions'})
    c = g_content_permissions_commands.add_parser('list-folder-permissions', parents=[common], help='Get folder permissions', description='Returns the direct content permissions on a folder with optional filtering.\nResults are cursor-paginated (max 250 per page).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the folder.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions list-folder-permissions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation (`read` or `update`).')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type (`user` or `group`). May be used without `principal-id` to return all permissions for that type.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help="Opaque cursor for pagination. Use the value from the previous response's `_links.next`.")
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of permission entries to return. Must be between 1 and 250. (default: 100)')
    c.set_defaults(handler=_run_content_permissions_list_folder_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_permissions'})
    c = g_content_permissions_commands.add_parser('set-folder-permissions', parents=[common], help='Set folder permissions', description='Replaces all direct content permissions on a folder with the provided set.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the folder or administer the space.', usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions set-folder-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions set-folder-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions set-folder-permissions')
    c.set_defaults(handler=_run_content_permissions_set_folder_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_folder_permissions'})
    c = g_content_permissions_commands.add_parser('add-folder-permissions', parents=[common], help='Add folder permissions', description="Adds or replaces direct content permissions for the specified principals on a\nfolder. Permissions for other principals are preserved; use `PUT` to replace\nall permissions at once.\n\nA principal can hold only one `read` or `update` permission. Adding `read` for\na principal that currently has `update` downgrades that principal to `read`;\nadding `update` upgrades them. If the same request contains both operations\nfor a principal, `update` takes precedence.\n\nReasserting a principal's existing permission is idempotent and returns a\nsuccessful response without creating a duplicate entry.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the folder or administer the space.", usage='%(prog)s ID --permissions @permissions.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions add-folder-permissions ID --permissions @permissions.json', 'codapact-confluence content-permissions add-folder-permissions ID --permissions @permissions.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    c.add_argument('--permissions', dest='p_permissions', type=json_value, metavar="JSON", required=True, help='JSON array of objects with operation*, principals* (* required). Schema: codapact-confluence describe content-permissions add-folder-permissions')
    c.set_defaults(handler=_run_content_permissions_add_folder_permissions, flags={'id': '--id', 'allow_self_lockout': '--allow-self-lockout', 'body.permissions': '--permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'add_folder_permissions'})
    c = g_content_permissions_commands.add_parser('delete-folder-permissions', parents=[common], help='Delete folder permissions', description='Deletes direct content permissions from a folder. See `DELETE\n/pages/{id}/permissions` for filter semantics.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the folder or administer the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-permissions delete-folder-permissions ID --dry-run', 'codapact-confluence content-permissions delete-folder-permissions ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--operation', dest='p_operation', choices=['read', 'update'], help='Filter by operation. Must be provided together with `principal-type` and `principal-id`.')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['user', 'group'], help='Filter by principal type. Must be provided together with `principal-id`.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filter by principal ID. Must be provided together with `principal-type`.')
    c.add_argument('--allow-self-lockout', dest='p_allow_self_lockout', action=argparse.BooleanOptionalAction, help="If `false` (default), the request is rejected when it would remove the calling user's own edit access. (default: False)")
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_permissions_delete_folder_permissions, flags={'id': '--id', 'operation': '--operation', 'principal_type': '--principal-type', 'principal_id': '--principal-id', 'allow_self_lockout': '--allow-self-lockout'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_folder_permissions'})
    g_content_properties = commands.add_parser('content-properties', help='create, create-attachment-property, create-blogpost-property, … (45 commands)', description="Run 'codapact-confluence content-properties COMMAND --help' for a command's options and examples.")
    g_content_properties_commands = g_content_properties.add_subparsers(dest="g_content_properties", metavar="COMMAND", required=True)
    c = g_content_properties_commands.add_parser('list-attachment', parents=[common], help='Get content properties for attachment', description='Retrieves all Content Properties tied to a specified attachment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment.', usage='%(prog)s ATTACHMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-attachment ATTACHMENT_ID']), formatter_class=RAW)
    c.add_argument('p_attachment_id', metavar='ATTACHMENT_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment for which content properties should be returned.')
    c.add_argument('--attachment-id', dest='p_attachment_id', default=argparse.SUPPRESS, metavar='ATTACHMENT_ID', help='same as ATTACHMENT_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_attachment, flags={'attachment_id': '--attachment-id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_content_properties'})
    c = g_content_properties_commands.add_parser('create-attachment-property', parents=[common], help='Create content property for attachment', description='Creates a new content property for an attachment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the attachment.', usage='%(prog)s ATTACHMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-attachment-property ATTACHMENT_ID --key KEY', 'codapact-confluence content-properties create-attachment-property ATTACHMENT_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_attachment_id', metavar='ATTACHMENT_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment to create a property for.')
    c.add_argument('--attachment-id', dest='p_attachment_id', default=argparse.SUPPRESS, metavar='ATTACHMENT_ID', help='same as ATTACHMENT_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_attachment_property, flags={'attachment_id': '--attachment-id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_attachment_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-attachment-by-id', parents=[common], help='Get content property for attachment by id', description='Retrieves a specific Content Property by ID that is attached to a specified\nattachment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment.', usage='%(prog)s ATTACHMENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-attachment-by-id ATTACHMENT_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_attachment_id', metavar='ATTACHMENT_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property to be returned')
    c.add_argument('--attachment-id', dest='p_attachment_id', default=argparse.SUPPRESS, metavar='ATTACHMENT_ID', help='same as ATTACHMENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_attachment_by_id, flags={'attachment_id': '--attachment-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-attachment-property', parents=[common], help='Update content property for attachment by id', description='Update a content property for attachment by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the attachment.', usage='%(prog)s ATTACHMENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-attachment-property ATTACHMENT_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-attachment-property ATTACHMENT_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_attachment_id', metavar='ATTACHMENT_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--attachment-id', dest='p_attachment_id', default=argparse.SUPPRESS, metavar='ATTACHMENT_ID', help='same as ATTACHMENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-attachment-property')
    c.set_defaults(handler=_run_content_properties_update_attachment_property, flags={'attachment_id': '--attachment-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_attachment_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-attachment-property', parents=[common], help='Delete content property for attachment by id', description='Deletes a content property for an attachment by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to attachment the page.', usage='%(prog)s ATTACHMENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-attachment-property ATTACHMENT_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-attachment-property ATTACHMENT_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_attachment_id', metavar='ATTACHMENT_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--attachment-id', dest='p_attachment_id', default=argparse.SUPPRESS, metavar='ATTACHMENT_ID', help='same as ATTACHMENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_attachment_property, flags={'attachment_id': '--attachment-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_attachment_property_by_id'})
    c = g_content_properties_commands.add_parser('list-blogpost', parents=[common], help='Get content properties for blog post', description='Retrieves all Content Properties tied to a specified blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post.', usage='%(prog)s BLOGPOST_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-blogpost BLOGPOST_ID']), formatter_class=RAW)
    c.add_argument('p_blogpost_id', metavar='BLOGPOST_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which content properties should be returned.')
    c.add_argument('--blogpost-id', dest='p_blogpost_id', default=argparse.SUPPRESS, type=integer, metavar='BLOGPOST_ID', help='same as BLOGPOST_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_blogpost, flags={'blogpost_id': '--blogpost-id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blogpost_content_properties'})
    c = g_content_properties_commands.add_parser('create-blogpost-property', parents=[common], help='Create content property for blog post', description='Creates a new property for a blogpost.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the blog post.', usage='%(prog)s BLOGPOST_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-blogpost-property BLOGPOST_ID --key KEY', 'codapact-confluence content-properties create-blogpost-property BLOGPOST_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_blogpost_id', metavar='BLOGPOST_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post to create a property for.')
    c.add_argument('--blogpost-id', dest='p_blogpost_id', default=argparse.SUPPRESS, type=integer, metavar='BLOGPOST_ID', help='same as BLOGPOST_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_blogpost_property, flags={'blogpost_id': '--blogpost-id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_blogpost_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-blogpost-by-id', parents=[common], help='Get content property for blog post by id', description='Retrieves a specific Content Property by ID that is attached to a specified\nblog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post.', usage='%(prog)s BLOGPOST_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-blogpost-by-id BLOGPOST_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_blogpost_id', metavar='BLOGPOST_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property being requested')
    c.add_argument('--blogpost-id', dest='p_blogpost_id', default=argparse.SUPPRESS, type=integer, metavar='BLOGPOST_ID', help='same as BLOGPOST_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_blogpost_by_id, flags={'blogpost_id': '--blogpost-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blogpost_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-blogpost-property', parents=[common], help='Update content property for blog post by id', description='Update a content property for blog post by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the blog post.', usage='%(prog)s BLOGPOST_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-blogpost-property BLOGPOST_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-blogpost-property BLOGPOST_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_blogpost_id', metavar='BLOGPOST_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--blogpost-id', dest='p_blogpost_id', default=argparse.SUPPRESS, type=integer, metavar='BLOGPOST_ID', help='same as BLOGPOST_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-blogpost-property')
    c.set_defaults(handler=_run_content_properties_update_blogpost_property, flags={'blogpost_id': '--blogpost-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_blogpost_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-blogpost-property', parents=[common], help='Delete content property for blogpost by id', description='Deletes a content property for a blogpost by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the blog post.', usage='%(prog)s BLOGPOST_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-blogpost-property BLOGPOST_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-blogpost-property BLOGPOST_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_blogpost_id', metavar='BLOGPOST_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--blogpost-id', dest='p_blogpost_id', default=argparse.SUPPRESS, type=integer, metavar='BLOGPOST_ID', help='same as BLOGPOST_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_blogpost_property, flags={'blogpost_id': '--blogpost-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_blogpost_property_by_id'})
    c = g_content_properties_commands.add_parser('list-custom-content', parents=[common], help='Get content properties for custom content', description='Retrieves Content Properties tied to a specified custom content.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content.', usage='%(prog)s CUSTOM_CONTENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-custom-content CUSTOM_CONTENT_ID']), formatter_class=RAW)
    c.add_argument('p_custom_content_id', metavar='CUSTOM_CONTENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content for which content properties should be returned.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', default=argparse.SUPPRESS, type=integer, metavar='CUSTOM_CONTENT_ID', help='same as CUSTOM_CONTENT_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_custom_content, flags={'custom_content_id': '--custom-content-id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_content_properties'})
    c = g_content_properties_commands.add_parser('create', parents=[common], help='Create content property for custom content', description='Creates a new content property for a piece of custom content.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the custom content.', usage='%(prog)s CUSTOM_CONTENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create CUSTOM_CONTENT_ID --key KEY', 'codapact-confluence content-properties create CUSTOM_CONTENT_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_custom_content_id', metavar='CUSTOM_CONTENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content to create a property for.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', default=argparse.SUPPRESS, type=integer, metavar='CUSTOM_CONTENT_ID', help='same as CUSTOM_CONTENT_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create, flags={'custom_content_id': '--custom-content-id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_custom_content_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-custom-content-by-id', parents=[common], help='Get content property for custom content by id', description='Retrieves a specific Content Property by ID that is attached to a specified\ncustom content.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page.', usage='%(prog)s CUSTOM_CONTENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-custom-content-by-id CUSTOM_CONTENT_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_custom_content_id', metavar='CUSTOM_CONTENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property being requested.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', default=argparse.SUPPRESS, type=integer, metavar='CUSTOM_CONTENT_ID', help='same as CUSTOM_CONTENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_custom_content_by_id, flags={'custom_content_id': '--custom-content-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update', parents=[common], help='Update content property for custom content by id', description='Update a content property for a piece of custom content by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the custom content.', usage='%(prog)s CUSTOM_CONTENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update CUSTOM_CONTENT_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update CUSTOM_CONTENT_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_custom_content_id', metavar='CUSTOM_CONTENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', default=argparse.SUPPRESS, type=integer, metavar='CUSTOM_CONTENT_ID', help='same as CUSTOM_CONTENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update')
    c.set_defaults(handler=_run_content_properties_update, flags={'custom_content_id': '--custom-content-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_custom_content_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete', parents=[common], help='Delete content property for custom content by id', description='Deletes a content property for a piece of custom content by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the custom content.', usage='%(prog)s CUSTOM_CONTENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete CUSTOM_CONTENT_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete CUSTOM_CONTENT_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_custom_content_id', metavar='CUSTOM_CONTENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', default=argparse.SUPPRESS, type=integer, metavar='CUSTOM_CONTENT_ID', help='same as CUSTOM_CONTENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete, flags={'custom_content_id': '--custom-content-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_custom_content_property_by_id'})
    c = g_content_properties_commands.add_parser('list-page', parents=[common], help='Get content properties for page', description='Retrieves Content Properties tied to a specified page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page.', usage='%(prog)s PAGE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-page PAGE_ID']), formatter_class=RAW)
    c.add_argument('p_page_id', metavar='PAGE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which content properties should be returned.')
    c.add_argument('--page-id', dest='p_page_id', default=argparse.SUPPRESS, type=integer, metavar='PAGE_ID', help='same as PAGE_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_page, flags={'page_id': '--page-id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_content_properties'})
    c = g_content_properties_commands.add_parser('create-page-property', parents=[common], help='Create content property for page', description='Creates a new content property for a page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the page.', usage='%(prog)s PAGE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-page-property PAGE_ID --key KEY', 'codapact-confluence content-properties create-page-property PAGE_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_page_id', metavar='PAGE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page to create a property for.')
    c.add_argument('--page-id', dest='p_page_id', default=argparse.SUPPRESS, type=integer, metavar='PAGE_ID', help='same as PAGE_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_page_property, flags={'page_id': '--page-id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_page_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-page-by-id', parents=[common], help='Get content property for page by id', description='Retrieves a specific Content Property by ID that is attached to a specified\npage.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page.', usage='%(prog)s PAGE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-page-by-id PAGE_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_page_id', metavar='PAGE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property being requested.')
    c.add_argument('--page-id', dest='p_page_id', default=argparse.SUPPRESS, type=integer, metavar='PAGE_ID', help='same as PAGE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_page_by_id, flags={'page_id': '--page-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-page-property', parents=[common], help='Update content property for page by id', description='Update a content property for a page by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the page.', usage='%(prog)s PAGE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-page-property PAGE_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-page-property PAGE_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_page_id', metavar='PAGE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--page-id', dest='p_page_id', default=argparse.SUPPRESS, type=integer, metavar='PAGE_ID', help='same as PAGE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-page-property')
    c.set_defaults(handler=_run_content_properties_update_page_property, flags={'page_id': '--page-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_page_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-page-property', parents=[common], help='Delete content property for page by id', description='Deletes a content property for a page by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the page.', usage='%(prog)s PAGE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-page-property PAGE_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-page-property PAGE_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_page_id', metavar='PAGE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--page-id', dest='p_page_id', default=argparse.SUPPRESS, type=integer, metavar='PAGE_ID', help='same as PAGE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_page_property, flags={'page_id': '--page-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_page_property_by_id'})
    c = g_content_properties_commands.add_parser('list-whiteboard', parents=[common], help='Get content properties for whiteboard', description='Retrieves Content Properties tied to a specified whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the whiteboard.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-whiteboard ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard for which content properties should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_whiteboard, flags={'id': '--id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_content_properties'})
    c = g_content_properties_commands.add_parser('create-whiteboard-property', parents=[common], help='Create content property for whiteboard', description='Creates a new content property for a whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the whiteboard.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-whiteboard-property ID --key KEY', 'codapact-confluence content-properties create-whiteboard-property ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard to create a property for.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_whiteboard_property, flags={'id': '--id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_whiteboard_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-whiteboard-by-id', parents=[common], help='Get content property for whiteboard by id', description='Retrieves a specific Content Property by ID that is attached to a specified\nwhiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the whiteboard.', usage='%(prog)s WHITEBOARD_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-whiteboard-by-id WHITEBOARD_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_whiteboard_id', metavar='WHITEBOARD_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property being requested.')
    c.add_argument('--whiteboard-id', dest='p_whiteboard_id', default=argparse.SUPPRESS, type=integer, metavar='WHITEBOARD_ID', help='same as WHITEBOARD_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_whiteboard_by_id, flags={'whiteboard_id': '--whiteboard-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-whiteboard-property', parents=[common], help='Update content property for whiteboard by id', description='Update a content property for a whiteboard by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the whiteboard.', usage='%(prog)s WHITEBOARD_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-whiteboard-property WHITEBOARD_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-whiteboard-property WHITEBOARD_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_whiteboard_id', metavar='WHITEBOARD_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--whiteboard-id', dest='p_whiteboard_id', default=argparse.SUPPRESS, type=integer, metavar='WHITEBOARD_ID', help='same as WHITEBOARD_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-whiteboard-property')
    c.set_defaults(handler=_run_content_properties_update_whiteboard_property, flags={'whiteboard_id': '--whiteboard-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_whiteboard_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-whiteboard-property', parents=[common], help='Delete content property for whiteboard by id', description='Deletes a content property for a whiteboard by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the whiteboard.', usage='%(prog)s WHITEBOARD_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-whiteboard-property WHITEBOARD_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-whiteboard-property WHITEBOARD_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_whiteboard_id', metavar='WHITEBOARD_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--whiteboard-id', dest='p_whiteboard_id', default=argparse.SUPPRESS, type=integer, metavar='WHITEBOARD_ID', help='same as WHITEBOARD_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_whiteboard_property, flags={'whiteboard_id': '--whiteboard-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_whiteboard_property_by_id'})
    c = g_content_properties_commands.add_parser('list-database', parents=[common], help='Get content properties for database', description='Retrieves Content Properties tied to a specified database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-database ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database for which content properties should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_database, flags={'id': '--id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_content_properties'})
    c = g_content_properties_commands.add_parser('create-database-property', parents=[common], help='Create content property for database', description='Creates a new content property for a database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the database.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-database-property ID --key KEY', 'codapact-confluence content-properties create-database-property ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database to create a property for.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_database_property, flags={'id': '--id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_database_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-database-by-id', parents=[common], help='Get content property for database by id', description='Retrieves a specific Content Property by ID that is attached to a specified\ndatabase.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database.', usage='%(prog)s DATABASE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-database-by-id DATABASE_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_database_id', metavar='DATABASE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property being requested.')
    c.add_argument('--database-id', dest='p_database_id', default=argparse.SUPPRESS, type=integer, metavar='DATABASE_ID', help='same as DATABASE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_database_by_id, flags={'database_id': '--database-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-database-property', parents=[common], help='Update content property for database by id', description='Update a content property for a database by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the database.', usage='%(prog)s DATABASE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-database-property DATABASE_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-database-property DATABASE_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_database_id', metavar='DATABASE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--database-id', dest='p_database_id', default=argparse.SUPPRESS, type=integer, metavar='DATABASE_ID', help='same as DATABASE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-database-property')
    c.set_defaults(handler=_run_content_properties_update_database_property, flags={'database_id': '--database-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_database_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-database-property', parents=[common], help='Delete content property for database by id', description='Deletes a content property for a database by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the database.', usage='%(prog)s DATABASE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-database-property DATABASE_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-database-property DATABASE_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_database_id', metavar='DATABASE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--database-id', dest='p_database_id', default=argparse.SUPPRESS, type=integer, metavar='DATABASE_ID', help='same as DATABASE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_database_property, flags={'database_id': '--database-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_database_property_by_id'})
    c = g_content_properties_commands.add_parser('list-smart-link', parents=[common], help='Get content properties for Smart Link in the content tree', description='Retrieves Content Properties tied to a specified Smart Link in the content\ntree.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the Smart Link in the content tree.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-smart-link ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree for which content properties should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of Smart Links per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_smart_link, flags={'id': '--id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_smart_link_content_properties'})
    c = g_content_properties_commands.add_parser('create-smart-link-property', parents=[common], help='Create content property for Smart Link in the content tree', description='Creates a new content property for a Smart Link in the content tree.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the Smart Link in the content tree.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-smart-link-property ID --key KEY', 'codapact-confluence content-properties create-smart-link-property ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree to create a property for.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_smart_link_property, flags={'id': '--id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_smart_link_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-smart-link-by-id', parents=[common], help='Get content property for Smart Link in the content tree by id', description='Retrieves a specific Content Property by ID that is attached to a specified\nSmart Link in the content tree.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the Smart Link in the content tree.', usage='%(prog)s EMBED_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-smart-link-by-id EMBED_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_embed_id', metavar='EMBED_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property being requested.')
    c.add_argument('--embed-id', dest='p_embed_id', default=argparse.SUPPRESS, type=integer, metavar='EMBED_ID', help='same as EMBED_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_smart_link_by_id, flags={'embed_id': '--embed-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_smart_link_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-smart-link-property', parents=[common], help='Update content property for Smart Link in the content tree by id', description='Update a content property for a Smart Link in the content tree by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the Smart Link in the content tree.', usage='%(prog)s EMBED_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-smart-link-property EMBED_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-smart-link-property EMBED_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_embed_id', metavar='EMBED_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--embed-id', dest='p_embed_id', default=argparse.SUPPRESS, type=integer, metavar='EMBED_ID', help='same as EMBED_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-smart-link-property')
    c.set_defaults(handler=_run_content_properties_update_smart_link_property, flags={'embed_id': '--embed-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_smart_link_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-smart-link-property', parents=[common], help='Delete content property for Smart Link in the content tree by id', description='Deletes a content property for a Smart Link in the content tree by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the Smart Link in the content tree.', usage='%(prog)s EMBED_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-smart-link-property EMBED_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-smart-link-property EMBED_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_embed_id', metavar='EMBED_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--embed-id', dest='p_embed_id', default=argparse.SUPPRESS, type=integer, metavar='EMBED_ID', help='same as EMBED_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_smart_link_property, flags={'embed_id': '--embed-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_smart_link_property_by_id'})
    c = g_content_properties_commands.add_parser('list-folder', parents=[common], help='Get content properties for folder', description='Retrieves Content Properties tied to a specified folder.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the folder.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-folder ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder for which content properties should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_folder, flags={'id': '--id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_content_properties'})
    c = g_content_properties_commands.add_parser('create-folder-property', parents=[common], help='Create content property for folder', description='Creates a new content property for a folder.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the folder.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-folder-property ID --key KEY', 'codapact-confluence content-properties create-folder-property ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder to create a property for.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_folder_property, flags={'id': '--id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_folder_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-folder-by-id', parents=[common], help='Get content property for folder by id', description='Retrieves a specific Content Property by ID that is attached to a specified\nfolder.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the folder.', usage='%(prog)s FOLDER_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-folder-by-id FOLDER_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_folder_id', metavar='FOLDER_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property being requested.')
    c.add_argument('--folder-id', dest='p_folder_id', default=argparse.SUPPRESS, type=integer, metavar='FOLDER_ID', help='same as FOLDER_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_folder_by_id, flags={'folder_id': '--folder-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-folder-property', parents=[common], help='Update content property for folder by id', description='Update a content property for a folder by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the folder.', usage='%(prog)s FOLDER_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-folder-property FOLDER_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-folder-property FOLDER_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_folder_id', metavar='FOLDER_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--folder-id', dest='p_folder_id', default=argparse.SUPPRESS, type=integer, metavar='FOLDER_ID', help='same as FOLDER_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-folder-property')
    c.set_defaults(handler=_run_content_properties_update_folder_property, flags={'folder_id': '--folder-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_folder_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-folder-property', parents=[common], help='Delete content property for folder by id', description='Deletes a content property for a folder by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the folder.', usage='%(prog)s FOLDER_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-folder-property FOLDER_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-folder-property FOLDER_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_folder_id', metavar='FOLDER_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--folder-id', dest='p_folder_id', default=argparse.SUPPRESS, type=integer, metavar='FOLDER_ID', help='same as FOLDER_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_folder_property, flags={'folder_id': '--folder-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_folder_property_by_id'})
    c = g_content_properties_commands.add_parser('list-comment', parents=[common], help='Get content properties for comment', description='Retrieves Content Properties attached to a specified comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the comment.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties list-comment COMMENT_ID']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment for which content properties should be returned.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Filters the response to return a specific content property with matching key (case sensitive).')
    c.add_argument('--sort', dest='p_sort', choices=['key', '-key'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of attachments per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_content_properties_list_comment, flags={'comment_id': '--comment-id', 'key': '--key', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_comment_content_properties'})
    c = g_content_properties_commands.add_parser('create-comment-property', parents=[common], help='Create content property for comment', description='Creates a new content property for a comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to update the comment.', usage='%(prog)s COMMENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties create-comment-property COMMENT_ID --key KEY', 'codapact-confluence content-properties create-comment-property COMMENT_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment to create a property for.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.set_defaults(handler=_run_content_properties_create_comment_property, flags={'comment_id': '--comment-id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_comment_property', 'requires_one_of': [['--key', '--value']]})
    c = g_content_properties_commands.add_parser('get-comment-by-id', parents=[common], help='Get content property for comment by id', description='Retrieves a specific Content Property by ID that is attached to a specified\ncomment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the comment.', usage='%(prog)s COMMENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties get-comment-by-id COMMENT_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment for which content properties should be returned.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the content property being requested.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_content_properties_get_comment_by_id, flags={'comment_id': '--comment-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_comment_content_properties_by_id'})
    c = g_content_properties_commands.add_parser('update-comment-property', parents=[common], help='Update content property for comment by id', description='Update a content property for a comment by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the comment.', usage='%(prog)s COMMENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties update-comment-property COMMENT_ID PROPERTY_ID --key KEY', 'codapact-confluence content-properties update-comment-property COMMENT_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the content property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the content property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe content-properties update-comment-property')
    c.set_defaults(handler=_run_content_properties_update_comment_property, flags={'comment_id': '--comment-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_comment_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_content_properties_commands.add_parser('delete-comment-property', parents=[common], help='Delete content property for comment by id', description='Deletes a content property for a comment by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the comment.', usage='%(prog)s COMMENT_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence content-properties delete-comment-property COMMENT_ID PROPERTY_ID --dry-run', 'codapact-confluence content-properties delete-comment-property COMMENT_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_comment_id', metavar='COMMENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the comment the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--comment-id', dest='p_comment_id', default=argparse.SUPPRESS, type=integer, metavar='COMMENT_ID', help='same as COMMENT_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_content_properties_delete_comment_property, flags={'comment_id': '--comment-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_comment_property_by_id'})
    g_custom_content = commands.add_parser('custom-content', help='create, delete, get, … (8 commands)', description="Run 'codapact-confluence custom-content COMMAND --help' for a command's options and examples.")
    g_custom_content_commands = g_custom_content.add_subparsers(dest="g_custom_content", metavar="COMMAND", required=True)
    c = g_custom_content_commands.add_parser('get-by-type-in-blog-post', parents=[common], help='Get custom content by type in blog post', description='Returns all custom content for a given type within a given blogpost. The\nnumber of results is limited by the `limit` parameter and additional results\n(if available) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content, the container of the custom content\n(blog post), and the corresponding space.', usage='%(prog)s ID --type TYPE [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content get-by-type-in-blog-post ID --type TYPE']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which custom content should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--type', dest='p_type', metavar='TYPE', required=True, help='The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--body-format', dest='p_body_format', choices=['raw', 'storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.set_defaults(handler=_run_custom_content_get_by_type_in_blog_post, flags={'id': '--id', 'type': '--type', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit', 'body_format': '--body-format'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_by_type_in_blog_post'})
    c = g_custom_content_commands.add_parser('get-by-type', parents=[common], help='Get custom content by type', description='Returns all custom content for a given type. The number of results is limited\nby the `limit` parameter and additional results (if available) will be\navailable through the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content, the container of the custom content,\nand the corresponding space (if different from the container).', usage='%(prog)s --type TYPE [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content get-by-type --type TYPE']), formatter_class=RAW)
    c.add_argument('--type', dest='p_type', metavar='TYPE', required=True, help='The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.')
    c.add_argument('--id', dest='p_id', action="append", type=integer, metavar='ID', help='Filter the results based on custom content ids. Multiple custom content ids can be specified as a comma-separated list.')
    c.add_argument('--space-id', dest='p_space_id', action="append", type=integer, metavar='SPACE_ID', help='Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--body-format', dest='p_body_format', choices=['raw', 'storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.set_defaults(handler=_run_custom_content_get_by_type, flags={'type': '--type', 'id': '--id', 'space_id': '--space-id', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit', 'body_format': '--body-format'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_by_type'})
    c = g_custom_content_commands.add_parser('create', parents=[common], help='Create custom content', description='Creates a new custom content in the given space, page, blogpost or other\ncustom content.\n\nOnly one of `spaceId`, `pageId`, `blogPostId`, or `customContentId` is\nrequired in the request body.\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to create custom content in the space.', usage='%(prog)s --type TYPE --title TITLE --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content create --type TYPE --title TITLE --body @body.json', 'codapact-confluence custom-content create --type TYPE --title TITLE --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('--type', dest='p_type', metavar='TYPE', required=True, help='Type of custom content.')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft'], help='The status of the custom content. Defaults to `current` when status not provided.')
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', help='ID of the containing space.')
    c.add_argument('--page-id', dest='p_page_id', metavar='PAGE_ID', help='ID of the containing page.')
    c.add_argument('--blog-post-id', dest='p_blog_post_id', metavar='BLOG_POST_ID', help='ID of the containing Blog Post.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', metavar='CUSTOM_CONTENT_ID', help='ID of the containing custom content.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', required=True, help='Title of the custom content.')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True)
    c.set_defaults(handler=_run_custom_content_create, flags={'body.type': '--type', 'body.status': '--status', 'body.space_id': '--space-id', 'body.page_id': '--page-id', 'body.blog_post_id': '--blog-post-id', 'body.custom_content_id': '--custom-content-id', 'body.title': '--title', 'body.body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_custom_content'})
    c = g_custom_content_commands.add_parser('get', parents=[common], help='Get custom content by id', description='Returns a specific piece of custom content.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content, the container of the custom content,\nand the corresponding space (if different from the container).', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the custom content to be returned. If you don't know the custom content ID, use Get Custom Content by Type and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['raw', 'storage', 'atlas_doc_format', 'view', 'export_view', 'anonymous_export_view'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.")
    c.add_argument('--include-labels', dest='p_include_labels', action=argparse.BooleanOptionalAction, help='Includes labels associated with this custom content in the response. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this custom content in the response. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this custom content in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-versions', dest='p_include_versions', action=argparse.BooleanOptionalAction, help='Includes versions associated with this custom content in the response. (default: False)')
    c.add_argument('--include-version', dest='p_include_version', action=argparse.BooleanOptionalAction, help='Includes the current version associated with this custom content in the response. (default: True)')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the custom content. (default: False)')
    c.set_defaults(handler=_run_custom_content_get, flags={'id': '--id', 'body_format': '--body-format', 'version': '--arg-version', 'include_labels': '--include-labels', 'include_properties': '--include-properties', 'include_operations': '--include-operations', 'include_versions': '--include-versions', 'include_version': '--include-version', 'include_collaborators': '--include-collaborators'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_by_id'})
    c = g_custom_content_commands.add_parser('update', parents=[common], help='Update custom content', description='Update a custom content by id. At most one of `spaceId`, `pageId`,\n`blogPostId`, or `customContentId` is allowed in the request body. Note that\nif `spaceId` is specified, it must be the same as the `spaceId` used for\ncreating the custom content as moving custom content to a different space is\nnot supported.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blogpost and its corresponding\nspace. Permission to update custom content in the space.', usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content update ID --body @body.json', 'codapact-confluence custom-content update ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the custom content to be updated. If you don't know the custom content ID, use Get Custom Content by Type and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id*, type*, status*, title*, body*, version*, space_id, page_id, blog_post_id, custom_content_id (* required). Schema: codapact-confluence describe custom-content update')
    c.set_defaults(handler=_run_custom_content_update, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_custom_content'})
    c = g_custom_content_commands.add_parser('delete', parents=[common], help='Delete custom content', description='Delete a custom content by id.\n\nDeleting a custom content will either move it to the trash or permanently\ndelete it (purge it), depending on the apiSupport. To permanently delete a\n**trashed** custom content, the endpoint must be called with the following\nparam `purge=true`.\n\n**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-\nconfluences-roles/) required**: Permission to view the content of the page or\nblogpost and its corresponding space. Permission to delete custom content in\nthe space. [`manage/content`](https://developer.atlassian.com/cloud/confluence\n/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission\nfor the space (if attempting to purge).\n\n**Note:** To find the display name for each permission ID, call the [Get\navailable space\npermissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) API.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content delete ID --dry-run', 'codapact-confluence custom-content delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--purge', dest='p_purge', action=argparse.BooleanOptionalAction, help='If attempting to purge the custom content. (default: False)')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_custom_content_delete, flags={'id': '--id', 'purge': '--purge'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_custom_content'})
    c = g_custom_content_commands.add_parser('get-by-type-in-page', parents=[common], help='Get custom content by type in page', description='Returns all custom content for a given type within a given page. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content, the container of the custom content\n(page), and the corresponding space.', usage='%(prog)s ID --type TYPE [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content get-by-type-in-page ID --type TYPE']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which custom content should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--type', dest='p_type', metavar='TYPE', required=True, help='The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--body-format', dest='p_body_format', choices=['raw', 'storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.set_defaults(handler=_run_custom_content_get_by_type_in_page, flags={'id': '--id', 'type': '--type', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit', 'body_format': '--body-format'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_by_type_in_page'})
    c = g_custom_content_commands.add_parser('get-by-type-in-space', parents=[common], help='Get custom content by type in space', description='Returns all custom content for a given type within a given space. The number\nof results is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content and the corresponding space.', usage='%(prog)s ID --type TYPE [options]', epilog=RUNTIME.command_epilog(['codapact-confluence custom-content get-by-type-in-space ID --type TYPE']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which custom content should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--type', dest='p_type', metavar='TYPE', required=True, help='The type of custom content being requested. See: https://developer.atlassian.com/cloud/confluence/custom-content/ for additional details on custom content.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--body-format', dest='p_body_format', choices=['raw', 'storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.set_defaults(handler=_run_custom_content_get_by_type_in_space, flags={'id': '--id', 'type': '--type', 'cursor': '--cursor', 'limit': '--limit', 'body_format': '--body-format'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_by_type_in_space'})
    g_data_policies = commands.add_parser('data-policies', help='get-metadata, list-spaces', description="Run 'codapact-confluence data-policies COMMAND --help' for a command's options and examples.")
    g_data_policies_commands = g_data_policies.add_subparsers(dest="g_data_policies", metavar="COMMAND", required=True)
    c = g_data_policies_commands.add_parser('get-metadata', parents=[common], help='Get data policy metadata for the workspace', description="Returns data policy metadata for the workspace.\n\n**[Permissions](#permissions) required:** Only apps can make this request.\nPermission to access the Confluence site ('Can use' global permission).", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence data-policies get-metadata']), formatter_class=RAW)
    c.set_defaults(handler=_run_data_policies_get_metadata, flags={}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_data_policy_metadata'})
    c = g_data_policies_commands.add_parser('list-spaces', parents=[common], help='Get spaces with data policies', description="Returns all spaces. The results will be sorted by id ascending. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: Only\napps can make this request. Permission to access the Confluence site ('Can\nuse' global permission). Only spaces that the app has permission to view will\nbe returned.", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence data-policies list-spaces']), formatter_class=RAW)
    c.add_argument('--ids', dest='p_ids', action="append", type=integer, metavar='IDS', help='Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.')
    c.add_argument('--keys', dest='p_keys', action="append", metavar='KEYS', help='Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'key', '-key', 'name', '-name'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of spaces per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_data_policies_list_spaces, flags={'ids': '--ids', 'keys': '--keys', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_data_policy_spaces'})
    g_database = commands.add_parser('database', help='create, delete, get, … (7 commands)', description="Run 'codapact-confluence database COMMAND --help' for a command's options and examples.")
    g_database_commands = g_database.add_subparsers(dest="g_database", metavar="COMMAND", required=True)
    c = g_database_commands.add_parser('create', parents=[common], help='Create database', description='Creates a database in the space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the corresponding space. Permission to create a database in\nthe space.', usage='%(prog)s --space-id SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence database create --space-id SPACE_ID', 'codapact-confluence database create --space-id SPACE_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--private', dest='p_private', action=argparse.BooleanOptionalAction, help='The database will be private. Only the user who creates this database will have permission to view and edit one. (default: False)')
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', required=True, help='ID of the space.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Title of the database.')
    c.add_argument('--parent-id', dest='p_parent_id', metavar='PARENT_ID', help='The parent content ID of the database.')
    c.set_defaults(handler=_run_database_create, flags={'private': '--private', 'body.space_id': '--space-id', 'body.title': '--title', 'body.parent_id': '--parent-id'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_database'})
    c = g_database_commands.add_parser('get', parents=[common], help='Get database by id', description='Returns a specific database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence database get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database to be returned')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the database. (default: False)')
    c.add_argument('--include-direct-children', dest='p_include_direct_children', action=argparse.BooleanOptionalAction, help='Includes direct children of the database, as defined in the `ChildrenResponse` object. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this database in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this database in the response. (default: False)')
    c.set_defaults(handler=_run_database_get, flags={'id': '--id', 'include_collaborators': '--include-collaborators', 'include_direct_children': '--include-direct-children', 'include_operations': '--include-operations', 'include_properties': '--include-properties'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_by_id'})
    c = g_database_commands.add_parser('delete', parents=[common], help='Delete database', description='Delete a database by id.\n\nDeleting a database moves the database to the trash, where it can be restored\nlater\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database and its corresponding space. Permission to\ndelete databases in the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence database delete ID --dry-run', 'codapact-confluence database delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_database_delete, flags={'id': '--id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_database'})
    c = g_database_commands.add_parser('list-fields', parents=[common], help='Get fields for database', description='Returns the field definitions (schema) for a database, ordered by the user-\ndefined column order, using cursor-based pagination.\n\n> **Consistency:** Responses may not immediately reflect recent changes.\nClients requiring read-after-write confirmation should poll with bounded\nbackoff.\n\n> **Experimental:** This operation is experimental and may change in\nbackwards-incompatible ways without notice.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence database list-fields ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='The Confluence content ID of the database, represented as an ASCII decimal-digit string.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of results to return. The value must be a positive integer (default: 50)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Opaque, offset-based continuation token obtained from `_links.next` or the')
    c.add_argument('--if-none-match', dest='p_if_none_match', metavar='IF_NONE_MATCH', help='One or more entity tags previously returned for this exact request URL.')
    c.set_defaults(handler=_run_database_list_fields, flags={'id': '--id', 'limit': '--limit', 'cursor': '--cursor', 'if_none_match': '--if-none-match'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_fields'})
    c = g_database_commands.add_parser('list-views', parents=[common], help='Get views for database', description='Returns the views defined on a database using cursor-based pagination. Only\nview IDs, names, and types are returned; view configuration is not exposed.\n\n> **Consistency:** Responses may not immediately reflect recent changes.\nClients requiring read-after-write confirmation should poll with bounded\nbackoff.\n\n> **Experimental:** This operation is experimental and may change in\nbackwards-incompatible ways without notice.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence database list-views ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='The Confluence content ID of the database, represented as an ASCII decimal-digit string.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of results to return. The value must be a positive integer (default: 50)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Opaque, offset-based continuation token obtained from `_links.next` or the')
    c.add_argument('--if-none-match', dest='p_if_none_match', metavar='IF_NONE_MATCH', help='One or more entity tags previously returned for this exact request URL.')
    c.set_defaults(handler=_run_database_list_views, flags={'id': '--id', 'limit': '--limit', 'cursor': '--cursor', 'if_none_match': '--if-none-match'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_views'})
    c = g_database_commands.add_parser('list-entries', parents=[common], help='Get entries for database', description="Returns the entries (rows) of a database, with optional filtering, sorting,\nand cursor-based pagination. Entry values are keyed by field ID; use Get\nfields for database (`GET /databases/{id}/fields`) to map field IDs to names.\n\nFiltering is expressed with bracket-scoped query parameters keyed on field ID.\nThe exact operators vary by field type and are documented on the `filter`\nparameter. Multiple filters are combined with AND. Unsupported operators and\nnon-filterable fields return distinct structured `400` responses.\n\nPagination uses opaque, offset-based continuation tokens and is best effort\nwhile a database is changing. Concurrent inserts, deletes, or changes to a\nsort value can cause duplicate or omitted rows across pages. Restart from the\nfirst page when a consistent export is required.\n\nResults are based on the database, not a particular view. A view's filters,\nsorting, grouping, and field visibility do not affect the response.\n\n> **Consistency:** Responses may not immediately reflect recent changes.\nClients requiring read-after-write confirmation should poll with bounded\nbackoff.\n\n> **Experimental:** This operation is experimental and may change in\nbackwards-incompatible ways without notice.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database and its corresponding space.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence database list-entries ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='The Confluence content ID of the database, represented as an ASCII decimal-digit string.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of results to return. The value must be a positive integer (default: 50)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Opaque, offset-based continuation token obtained from `_links.next` or the')
    c.add_argument('--if-none-match', dest='p_if_none_match', metavar='IF_NONE_MATCH', help='One or more entity tags previously returned for this exact request URL.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a single field ID. Prefix the field ID with')
    c.add_argument('--filter', dest='p_filter', type=json_value, metavar="JSON", help='Filters entries by field value. Bracket-scoped on field ID, for example')
    c.set_defaults(handler=_run_database_list_entries, flags={'id': '--id', 'limit': '--limit', 'cursor': '--cursor', 'if_none_match': '--if-none-match', 'sort': '--sort', 'filter': '--filter'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_entries'})
    c = g_database_commands.add_parser('get-entry', parents=[common], help='Get entry by id', description='Returns a single entry (row) from a database by ID.\n\n> **Consistency:** Responses may not immediately reflect recent changes.\nClients requiring read-after-write confirmation should poll with bounded\nbackoff.\n\n> **Experimental:** This operation is experimental and may change in\nbackwards-incompatible ways without notice.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database and its corresponding space.', usage='%(prog)s ID ENTRY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence database get-entry ID ENTRY_ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='The Confluence content ID of the database, represented as an ASCII decimal-digit string.')
    c.add_argument('p_entry_id', metavar='ENTRY_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the entry to be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--entry-id', dest='p_entry_id', default=argparse.SUPPRESS, metavar='ENTRY_ID', help='same as ENTRY_ID')
    c.add_argument('--if-none-match', dest='p_if_none_match', metavar='IF_NONE_MATCH', help='One or more entity tags previously returned for this exact request URL.')
    c.set_defaults(handler=_run_database_get_entry, flags={'id': '--id', 'entry_id': '--entry-id', 'if_none_match': '--if-none-match'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_entry_by_id'})
    g_descendants = commands.add_parser('descendants', help='list-database, list-folder, list-page, … (5 commands)', description="Run 'codapact-confluence descendants COMMAND --help' for a command's options and examples.")
    g_descendants_commands = g_descendants.add_subparsers(dest="g_descendants", metavar="COMMAND", required=True)
    c = g_descendants_commands.add_parser('list-whiteboard', parents=[common], help='Get descendants of a whiteboard', description="Returns descendants in the content tree for a given whiteboard by ID in top-\nto-bottom order (that is, the highest descendant is the first item in the\nresponse payload). The number of results is limited by the `limit` parameter\nand additional results (if available) will be available by calling this\nendpoint with the cursor in the response payload. There is also a `depth`\nparameter specifying depth of descendants to be fetched.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each descendant. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the whiteboard and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence descendants list-whiteboard ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results. (default: 25)')
    c.add_argument('--depth', dest='p_depth', type=integer, metavar='DEPTH', help='Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants. (default: 2)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.set_defaults(handler=_run_descendants_list_whiteboard, flags={'id': '--id', 'limit': '--limit', 'depth': '--depth', 'cursor': '--cursor'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_descendants'})
    c = g_descendants_commands.add_parser('list-database', parents=[common], help='Get descendants of a database', description="Returns descendants in the content tree for a given database by ID in top-to-\nbottom order (that is, the highest descendant is the first item in the\nresponse payload). The number of results is limited by the `limit` parameter\nand additional results (if available) will be available by calling this\nendpoint with the cursor in the response payload. There is also a `depth`\nparameter specifying depth of descendants to be fetched.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each descendant. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the database and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence descendants list-database ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results. (default: 25)')
    c.add_argument('--depth', dest='p_depth', type=integer, metavar='DEPTH', help='Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants. (default: 2)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.set_defaults(handler=_run_descendants_list_database, flags={'id': '--id', 'limit': '--limit', 'depth': '--depth', 'cursor': '--cursor'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_descendants'})
    c = g_descendants_commands.add_parser('list-smart-link', parents=[common], help='Get descendants of a smart link', description="Returns descendants in the content tree for a given smart link by ID in top-\nto-bottom order (that is, the highest descendant is the first item in the\nresponse payload). The number of results is limited by the `limit` parameter\nand additional results (if available) will be available by calling this\nendpoint with the cursor in the response payload. There is also a `depth`\nparameter specifying depth of descendants to be fetched.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each descendant. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the smart link and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence descendants list-smart-link ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the smart link.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results. (default: 25)')
    c.add_argument('--depth', dest='p_depth', type=integer, metavar='DEPTH', help='Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants. (default: 2)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.set_defaults(handler=_run_descendants_list_smart_link, flags={'id': '--id', 'limit': '--limit', 'depth': '--depth', 'cursor': '--cursor'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_smart_link_descendants'})
    c = g_descendants_commands.add_parser('list-folder', parents=[common], help='Get descendants of folder', description="Returns descendants in the content tree for a given folder by ID in top-to-\nbottom order (that is, the highest descendant is the first item in the\nresponse payload). The number of results is limited by the `limit` parameter\nand additional results (if available) will be available by calling this\nendpoint with the cursor in the response payload. There is also a `depth`\nparameter specifying depth of descendants to be fetched.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each descendant. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence descendants list-folder ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results. (default: 25)')
    c.add_argument('--depth', dest='p_depth', type=integer, metavar='DEPTH', help='Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants. (default: 2)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.set_defaults(handler=_run_descendants_list_folder, flags={'id': '--id', 'limit': '--limit', 'depth': '--depth', 'cursor': '--cursor'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_descendants'})
    c = g_descendants_commands.add_parser('list-page', parents=[common], help='Get descendants of page', description="Returns descendants in the content tree for a given page by ID in top-to-\nbottom order (that is, the highest descendant is the first item in the\nresponse payload). The number of results is limited by the `limit` parameter\nand additional results (if available) will be available by calling this\nendpoint with the cursor in the response payload. There is also a `depth`\nparameter specifying depth of descendants to be fetched.\n\nThe following types of content will be returned: - Database - Embed - Folder -\nPage - Whiteboard\n\nThis endpoint returns minimal information about each descendant. To fetch more\ndetails, use a related endpoint based on the content type, such as:\n\n- [Get database by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\ndatabase/#api-databases-id-get) - [Get embed by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-\nlink/#api-embeds-id-get) - [Get folder by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nfolder/#api-folders-id-get) - [Get page by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\npage/#api-pages-id-get) - [Get whiteboard by\nid](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-\nwhiteboard/#api-whiteboards-id-get).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).\nPermission to view the page and its corresponding space", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence descendants list-page ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of items per result to return. If more results exist, call the endpoint with the cursor to fetch the next set of results. (default: 25)')
    c.add_argument('--depth', dest='p_depth', type=integer, metavar='DEPTH', help='Maximum depth of descendants to return. If more results are required, use the endpoint corresponding to the content type of the deepest descendant to fetch more descendants. (default: 2)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.set_defaults(handler=_run_descendants_list_page, flags={'id': '--id', 'limit': '--limit', 'depth': '--depth', 'cursor': '--cursor'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_descendants'})
    g_folder = commands.add_parser('folder', help='create, delete, get', description="Run 'codapact-confluence folder COMMAND --help' for a command's options and examples.")
    g_folder_commands = g_folder.add_subparsers(dest="g_folder", metavar="COMMAND", required=True)
    c = g_folder_commands.add_parser('create', parents=[common], help='Create folder', description='Creates a folder in the space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the corresponding space. Permission to create a folder in\nthe space.', usage='%(prog)s --space-id SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence folder create --space-id SPACE_ID', 'codapact-confluence folder create --space-id SPACE_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', required=True, help='ID of the space.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Title of the folder.')
    c.add_argument('--parent-id', dest='p_parent_id', metavar='PARENT_ID', help='The parent content ID of the folder.')
    c.set_defaults(handler=_run_folder_create, flags={'body.space_id': '--space-id', 'body.title': '--title', 'body.parent_id': '--parent-id'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_folder'})
    c = g_folder_commands.add_parser('get', parents=[common], help='Get folder by id', description='Returns a specific folder.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the folder and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence folder get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder to be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the folder. (default: False)')
    c.add_argument('--include-direct-children', dest='p_include_direct_children', action=argparse.BooleanOptionalAction, help='Includes direct children of the folder, as defined in the `ChildrenResponse` object. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this folder in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this folder in the response. (default: False)')
    c.set_defaults(handler=_run_folder_get, flags={'id': '--id', 'include_collaborators': '--include-collaborators', 'include_direct_children': '--include-direct-children', 'include_operations': '--include-operations', 'include_properties': '--include-properties'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_by_id'})
    c = g_folder_commands.add_parser('delete', parents=[common], help='Delete folder', description='Delete a folder by id.\n\nDeleting a folder moves the folder to the trash, where it can be restored\nlater\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the folder and its corresponding space. Permission to\ndelete folders in the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence folder delete ID --dry-run', 'codapact-confluence folder delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_folder_delete, flags={'id': '--id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_folder'})
    g_label = commands.add_parser('label', help='list-attachment-labels, list-blog-post-labels, list-custom-content-labels, … (7 commands)', description="Run 'codapact-confluence label COMMAND --help' for a command's options and examples.")
    g_label_commands = g_label.add_subparsers(dest="g_label", metavar="COMMAND", required=True)
    c = g_label_commands.add_parser('list-attachment-labels', parents=[common], help='Get labels for attachment', description='Returns the labels of specific attachment. The number of results is limited by\nthe `limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the parent content of the attachment and its corresponding\nspace. Only labels that the user has permission to view will be returned.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence label list-attachment-labels ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the attachment for which labels should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--prefix', dest='p_prefix', choices=['my', 'team', 'global', 'system'], help='Filter the results to labels based on their prefix.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_label_list_attachment_labels, flags={'id': '--id', 'prefix': '--prefix', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_labels'})
    c = g_label_commands.add_parser('list-blog-post-labels', parents=[common], help='Get labels for blog post', description='Returns the labels of specific blog post. The number of results is limited by\nthe `limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the blog post and its corresponding space.\nOnly labels that the user has permission to view will be returned.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence label list-blog-post-labels ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which labels should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--prefix', dest='p_prefix', choices=['my', 'team', 'global', 'system'], help='Filter the results to labels based on their prefix.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_label_list_blog_post_labels, flags={'id': '--id', 'prefix': '--prefix', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_labels'})
    c = g_label_commands.add_parser('list-custom-content-labels', parents=[common], help='Get labels for custom content', description='Returns the labels for a specific piece of custom content. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content and its corresponding space. Only labels\nthat the user has permission to view will be returned.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence label list-custom-content-labels ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content for which labels should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--prefix', dest='p_prefix', choices=['my', 'team', 'global', 'system'], help='Filter the results to labels based on their prefix.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_label_list_custom_content_labels, flags={'id': '--id', 'prefix': '--prefix', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_labels'})
    c = g_label_commands.add_parser('list-labels', parents=[common], help='Get labels', description="Returns all labels. The number of results is limited by the `limit` parameter\nand additional results (if available) will be available through the `next` URL\npresent in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\nlabels that the user has permission to view will be returned.", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence label list-labels']), formatter_class=RAW)
    c.add_argument('--label-id', dest='p_label_id', action="append", type=integer, metavar='LABEL_ID', help='Filters on label ID. Multiple IDs can be specified as a comma-separated list.')
    c.add_argument('--prefix', dest='p_prefix', action="append", metavar='PREFIX', help='Filters on label prefix. Multiple IDs can be specified as a comma-separated list.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_label_list_labels, flags={'label_id': '--label-id', 'prefix': '--prefix', 'cursor': '--cursor', 'sort': '--sort', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_labels'})
    c = g_label_commands.add_parser('list-page-labels', parents=[common], help='Get labels for page', description='Returns the labels of specific page. The number of results is limited by the\n`limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space. Only\nlabels that the user has permission to view will be returned.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence label list-page-labels ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which labels should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--prefix', dest='p_prefix', choices=['my', 'team', 'global', 'system'], help='Filter the results to labels based on their prefix.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_label_list_page_labels, flags={'id': '--id', 'prefix': '--prefix', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_labels'})
    c = g_label_commands.add_parser('list-space-labels', parents=[common], help='Get labels for space', description='Returns the labels of specific space. The number of results is limited by the\n`limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the space. Only labels that the user has permission to view\nwill be returned.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence label list-space-labels ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which labels should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--prefix', dest='p_prefix', choices=['my', 'team'], help='Filter the results to labels based on their prefix.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_label_list_space_labels, flags={'id': '--id', 'prefix': '--prefix', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_labels'})
    c = g_label_commands.add_parser('list-space-content-labels', parents=[common], help='Get labels for space content', description='Returns the labels of space content (pages, blogposts etc). The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the space. Only labels that the user has permission to view\nwill be returned.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence label list-space-content-labels ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which labels should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--prefix', dest='p_prefix', choices=['my', 'team'], help='Filter the results to labels based on their prefix.')
    c.add_argument('--sort', dest='p_sort', metavar='SORT', help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of labels per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_label_list_space_content_labels, flags={'id': '--id', 'prefix': '--prefix', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_content_labels'})
    g_like = commands.add_parser('like', help='get-blog-post-count, get-footer-count, get-inline-count, … (8 commands)', description="Run 'codapact-confluence like COMMAND --help' for a command's options and examples.")
    g_like_commands = g_like.add_subparsers(dest="g_like", metavar="COMMAND", required=True)
    c = g_like_commands.add_parser('get-blog-post-count', parents=[common], help='Get like count for blog post', description='Returns the count of likes of specific blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the blog post and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like get-blog-post-count ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which like count should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_like_get_blog_post_count, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_like_count'})
    c = g_like_commands.add_parser('list-blog-post-users', parents=[common], help='Get account IDs of likes for blog post', description='Returns the account IDs of likes of specific blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the blog post and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like list-blog-post-users ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which account IDs should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_like_list_blog_post_users, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_like_users'})
    c = g_like_commands.add_parser('get-page-count', parents=[common], help='Get like count for page', description='Returns the count of likes of specific page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like get-page-count ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which like count should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_like_get_page_count, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_like_count'})
    c = g_like_commands.add_parser('list-page-users', parents=[common], help='Get account IDs of likes for page', description='Returns the account IDs of likes of specific page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like list-page-users ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which like count should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_like_list_page_users, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_like_users'})
    c = g_like_commands.add_parser('get-footer-count', parents=[common], help='Get like count for footer comment', description='Returns the count of likes of specific footer comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page/blogpost and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like get-footer-count ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the footer comment for which like count should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_like_get_footer_count, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_like_count'})
    c = g_like_commands.add_parser('list-footer-users', parents=[common], help='Get account IDs of likes for footer comment', description='Returns the account IDs of likes of specific footer comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page/blogpost and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like list-footer-users ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the footer comment for which like count should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_like_list_footer_users, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_like_users'})
    c = g_like_commands.add_parser('get-inline-count', parents=[common], help='Get like count for inline comment', description='Returns the count of likes of specific inline comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page/blogpost and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like get-inline-count ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the inline comment for which like count should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_like_get_inline_count, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_like_count'})
    c = g_like_commands.add_parser('list-inline-users', parents=[common], help='Get account IDs of likes for inline comment', description='Returns the account IDs of likes of specific inline comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page/blogpost and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence like list-inline-users ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the inline comment for which like count should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of account IDs per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_like_list_inline_users, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_like_users'})
    g_operation = commands.add_parser('operation', help='list-attachment-operations, list-blog-post-operations, list-custom-content-operations, … (11 commands)', description="Run 'codapact-confluence operation COMMAND --help' for a command's options and examples.")
    g_operation_commands = g_operation.add_subparsers(dest="g_operation", metavar="COMMAND", required=True)
    c = g_operation_commands.add_parser('list-attachment-operations', parents=[common], help='Get permitted operations for attachment', description='Returns the permitted operations on specific attachment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the parent content of the attachment and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-attachment-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_attachment_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_operations'})
    c = g_operation_commands.add_parser('list-blog-post-operations', parents=[common], help='Get permitted operations for blog post', description='Returns the permitted operations on specific blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the parent content of the blog post and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-blog-post-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_blog_post_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_operations'})
    c = g_operation_commands.add_parser('list-custom-content-operations', parents=[common], help='Get permitted operations for custom content', description='Returns the permitted operations on specific custom content.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the parent content of the custom content and its\ncorresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-custom-content-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_custom_content_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_operations'})
    c = g_operation_commands.add_parser('list-page-operations', parents=[common], help='Get permitted operations for page', description='Returns the permitted operations on specific page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the parent content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-page-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_page_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_operations'})
    c = g_operation_commands.add_parser('list-whiteboard-operations', parents=[common], help='Get permitted operations for a whiteboard', description='Returns the permitted operations on specific whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the whiteboard and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-whiteboard-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_whiteboard_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_operations'})
    c = g_operation_commands.add_parser('list-database-operations', parents=[common], help='Get permitted operations for a database', description='Returns the permitted operations on specific database.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the database and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-database-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the database for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_database_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_database_operations'})
    c = g_operation_commands.add_parser('list-smart-link-operations', parents=[common], help='Get permitted operations for a Smart Link in the content tree', description='Returns the permitted operations on specific Smart Link in the content tree.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the Smart Link in the content tree and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-smart-link-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_smart_link_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_smart_link_operations'})
    c = g_operation_commands.add_parser('list-folder-operations', parents=[common], help='Get permitted operations for a folder', description='Returns the permitted operations on specific folder.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the folder and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-folder-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the folder for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_folder_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_folder_operations'})
    c = g_operation_commands.add_parser('list-space-operations', parents=[common], help='Get permitted operations for space', description='Returns the permitted operations on specific space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-space-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_space_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_operations'})
    c = g_operation_commands.add_parser('list-footer-comment-operations', parents=[common], help='Get permitted operations for footer comment', description='Returns the permitted operations on specific footer comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the parent content of the footer comment and its\ncorresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-footer-comment-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the footer comment for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_footer_comment_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_comment_operations'})
    c = g_operation_commands.add_parser('list-inline-comment-operations', parents=[common], help='Get permitted operations for inline comment', description='Returns the permitted operations on specific inline comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the parent content of the inline comment and its\ncorresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence operation list-inline-comment-operations ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the inline comment for which operations should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_operation_list_inline_comment_operations, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_comment_operations'})
    g_page = commands.add_parser('page', help='create, delete, get, … (8 commands)', description="Run 'codapact-confluence page COMMAND --help' for a command's options and examples.")
    g_page_commands = g_page.add_subparsers(dest="g_page", metavar="COMMAND", required=True)
    c = g_page_commands.add_parser('list-label-pages', parents=[common], help='Get pages for label', description='Returns the pages of specified label. The number of results is limited by the\n`limit` parameter and additional results (if available) will be available\nthrough the `next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page list-label-pages ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the label for which pages should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--space-id', dest='p_space_id', action="append", type=integer, metavar='SPACE_ID', help='Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title'], help='Used to sort the result by a particular field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_page_list_label_pages, flags={'id': '--id', 'space_id': '--space-id', 'body_format': '--body-format', 'sort': '--sort', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_label_pages'})
    c = g_page_commands.add_parser('list-pages', parents=[common], help='Get pages', description="Returns all pages. The number of results is limited by the `limit` parameter\nand additional results (if available) will be available through the `next` URL\npresent in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\npages that the user has permission to view will be returned.", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page list-pages']), formatter_class=RAW)
    c.add_argument('--id', dest='p_id', action="append", type=integer, metavar='ID', help='Filter the results based on page ids. Multiple page ids can be specified as a comma-separated list.')
    c.add_argument('--space-id', dest='p_space_id', action="append", type=integer, metavar='SPACE_ID', help='Filter the results based on space ids. Multiple space ids can be specified as a comma-separated list.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title'], help='Used to sort the result by a particular field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'deleted', 'trashed'], help='Filter the results to pages based on their status. By default, `current` and `archived` are used.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Filter the results to pages based on their title.')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--subtype', dest='p_subtype', choices=['live', 'page'], help='Filter the results to pages based on their subtype.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_page_list_pages, flags={'id': '--id', 'space_id': '--space-id', 'sort': '--sort', 'status': '--status', 'title': '--title', 'body_format': '--body-format', 'subtype': '--subtype', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_pages'})
    c = g_page_commands.add_parser('create', parents=[common], help='Create page', description='Creates a page in the space.\n\nPages are created as published by default unless specified as a draft in the\nstatus field. If creating a published page, the title must be specified.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the corresponding space. Permission to create a page in the\nspace.', usage='%(prog)s --space-id SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page create --space-id SPACE_ID', 'codapact-confluence page create --space-id SPACE_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--embedded', dest='p_embedded', action=argparse.BooleanOptionalAction, help='Tag the content as embedded and content will be created in NCS. (default: False)')
    c.add_argument('--private', dest='p_private', action=argparse.BooleanOptionalAction, help='The page will be private. Only the user who creates this page will have permission to view and edit one. (default: False)')
    c.add_argument('--root-level', dest='p_root_level', action=argparse.BooleanOptionalAction, help='The page will be created at the root level of the space (outside the space homepage tree). If true, then a  (default: False)')
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', required=True, help='ID of the space.')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft'], help='The status of the page, published or draft.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Title of the page, required if page status is not draft.')
    c.add_argument('--parent-id', dest='p_parent_id', metavar='PARENT_ID', help='The parent content ID of the page. If the `root-level` query parameter is set to false and a value is ')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON")
    c.add_argument('--subtype', dest='p_subtype', choices=['live'], help='The subtype of the page. Provide the subtype live to create a live doc or no subtype to create a page.')
    c.set_defaults(handler=_run_page_create, flags={'embedded': '--embedded', 'private': '--private', 'root_level': '--root-level', 'body.space_id': '--space-id', 'body.status': '--status', 'body.title': '--title', 'body.parent_id': '--parent-id', 'body.body': '--body', 'body.subtype': '--subtype'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_page'})
    c = g_page_commands.add_parser('get', parents=[common], help='Get page by id', description='Returns a specific page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the page to be returned. If you don't know the page ID, use Get pages and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format', 'view', 'export_view', 'anonymous_export_view', 'styled_view', 'editor'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--get-draft', dest='p_get_draft', action=argparse.BooleanOptionalAction, help='Retrieve the draft version of this page. (default: False)')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'trashed', 'deleted', 'historical', 'draft'], help='Filter the page being retrieved by its status.')
    c.add_argument('--arg-version', dest='p_arg_version', type=integer, metavar='ARG_VERSION', help="Allows you to retrieve a previously published version. Specify the previous version's number to retrieve its details.")
    c.add_argument('--include-labels', dest='p_include_labels', action=argparse.BooleanOptionalAction, help='Includes labels associated with this page in the response. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this page in the response. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this page in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-likes', dest='p_include_likes', action=argparse.BooleanOptionalAction, help='Includes likes associated with this page in the response. (default: False)')
    c.add_argument('--include-versions', dest='p_include_versions', action=argparse.BooleanOptionalAction, help='Includes versions associated with this page in the response. (default: False)')
    c.add_argument('--include-version', dest='p_include_version', action=argparse.BooleanOptionalAction, help='Includes the current version associated with this page in the response. (default: True)')
    c.add_argument('--include-favorited-by-current-user-status', dest='p_include_favorited_by_current_user_status', action=argparse.BooleanOptionalAction, help='Includes whether this page has been favorited by the current user. (default: False)')
    c.add_argument('--include-webresources', dest='p_include_webresources', action=argparse.BooleanOptionalAction, help='Includes web resources that can be used to render page content on a client. (default: False)')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the page. (default: False)')
    c.add_argument('--include-direct-children', dest='p_include_direct_children', action=argparse.BooleanOptionalAction, help='Includes direct children of the page, as defined in the `ChildrenResponse` object. (default: False)')
    c.set_defaults(handler=_run_page_get, flags={'id': '--id', 'body_format': '--body-format', 'get_draft': '--get-draft', 'status': '--status', 'version': '--arg-version', 'include_labels': '--include-labels', 'include_properties': '--include-properties', 'include_operations': '--include-operations', 'include_likes': '--include-likes', 'include_versions': '--include-versions', 'include_version': '--include-version', 'include_favorited_by_current_user_status': '--include-favorited-by-current-user-status', 'include_webresources': '--include-webresources', 'include_collaborators': '--include-collaborators', 'include_direct_children': '--include-direct-children'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_by_id'})
    c = g_page_commands.add_parser('update', parents=[common], help='Update page', description='Update a page by id.\n\nWhen the "current" version is updated, the provided body content is considered\nas the latest version. This latest body content will be attempted to be merged\ninto the draft version through a content reconciliation algorithm. If two\nversions are significantly diverged, the latest provided content may entirely\noverride what was previously in the draft.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page and its corresponding space. Permission to update\npages in the space.', usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page update ID --body @body.json', 'codapact-confluence page update ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with id*, status*, title*, body*, version*, space_id, parent_id, owner_id (* required). Schema: codapact-confluence describe page update')
    c.set_defaults(handler=_run_page_update, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_page'})
    c = g_page_commands.add_parser('delete', parents=[common], help='Delete page', description='Delete a page by id.\n\nBy default this will delete pages that are non-drafts. To delete a page that\nis a draft, the endpoint must be called on a draft with the following param\n`draft=true`. Discarded drafts are not sent to the trash and are permanently\ndeleted.\n\nDeleting a page moves the page to the trash, where it can be restored later.\nTo permanently delete a page (or "purge" it), the endpoint must be called on a\n**trashed** page with the following param `purge=true`.\n\n**[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-\nconfluences-roles/) required**: Permission to view the page and its\ncorresponding space. Permission to delete pages in the space. [`manage/content\n`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-\npermissions/#api-space-permissions-get) permission for the space (if\nattempting to purge).\n\n**Note:** To find the display name for each permission ID, call the [Get\navailable space\npermissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-\ngroup-space-permissions/#api-space-permissions-get) API.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page delete ID --dry-run', 'codapact-confluence page delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--purge', dest='p_purge', action=argparse.BooleanOptionalAction, help='If attempting to purge the page. (default: False)')
    c.add_argument('--draft', dest='p_draft', action=argparse.BooleanOptionalAction, help='If attempting to delete a page that is a draft. (default: False)')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_page_delete, flags={'id': '--id', 'purge': '--purge', 'draft': '--draft'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_page'})
    c = g_page_commands.add_parser('update-title', parents=[common], help='Update page title', description='Updates the title of a specified page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page and its corresponding space. Permission to update\npages in the space.', usage='%(prog)s ID --status {current,draft} --title TITLE [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page update-title ID --status current --title TITLE', 'codapact-confluence page update-title ID --status current --title TITLE --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the page to be updated. If you don't know the page ID, use Get Pages and filter the results")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--status', dest='p_status', choices=['current', 'draft'], required=True, help='The status of the page, current or draft.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', required=True, help='The updated title for the page')
    c.set_defaults(handler=_run_page_update_title, flags={'id': '--id', 'body.status': '--status', 'body.title': '--title'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_page_title'})
    c = g_page_commands.add_parser('get-pages-in-space', parents=[common], help='Get pages in space', description="Returns all pages in a space. The number of results is limited by the `limit`\nparameter and additional results (if available) will be available through the\n`next` URL present in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission) and\n'View' permission for the space. Only pages that the user has permission to\nview will be returned.", usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence page get-pages-in-space ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which pages should be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--depth', dest='p_depth', choices=['all', 'root'], help='Filter the results to pages at the root level of the space or to all pages in the space. (default: all)')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title'], help='Used to sort the result by a particular field.')
    c.add_argument('--status', dest='p_status', action="append", choices=['current', 'archived', 'deleted', 'trashed'], help='Filter the results to pages based on their status. By default, `current` and `archived` are used.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Filter the results to pages based on their title.')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_page_get_pages_in_space, flags={'id': '--id', 'depth': '--depth', 'sort': '--sort', 'status': '--status', 'title': '--title', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_pages_in_space'})
    g_redactions = commands.add_parser('redactions', help='post-redact-blog, post-redact-page', description="Run 'codapact-confluence redactions COMMAND --help' for a command's options and examples.")
    g_redactions_commands = g_redactions.add_subparsers(dest="g_redactions", metavar="COMMAND", required=True)
    c = g_redactions_commands.add_parser('post-redact-page', parents=[common], help='Redact Content in a Confluence Page', description='Redacts sensitive content in a Confluence page by replacing specified text\nranges with redaction markers. Each redaction in the response includes a\nunique UUID for restoration (except code block redactions). The response\nmetadata items maintain the same order as the input redaction pointers, and\ncompletely overlapping redactions are merged into a single redaction with one\nUUID.\n\n**Note**: This endpoint requires **Atlassian Guard Premium**.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence redactions post-redact-page ID', 'codapact-confluence redactions post-redact-page ID --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page to redact content from.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--created-at', dest='p_created_at', metavar='DATETIME', help='Timestamp when the content was last updated.')
    c.add_argument('--clean-history', dest='p_clean_history', action=argparse.BooleanOptionalAction, help='Whether to clean up previous versions containing the redaction. When true, historical versions of the content that contain the redacted text will be squashed.')
    c.add_argument('--version-number', dest='p_version_number', type=integer, metavar='VERSION_NUMBER', help='Optional version number of the content to redact. When specified, the redaction will target ')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", help='JSON object with redactions. Schema: codapact-confluence describe redactions post-redact-page')
    c.add_argument('--title', dest='p_title', type=json_value, metavar="JSON", help='JSON object with redactions. Schema: codapact-confluence describe redactions post-redact-page')
    c.set_defaults(handler=_run_redactions_post_redact_page, flags={'id': '--id', 'body.created_at': '--created-at', 'body.clean_history': '--clean-history', 'body.version_number': '--version-number', 'body.body': '--body', 'body.title': '--title'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'post_redact_page'})
    c = g_redactions_commands.add_parser('post-redact-blog', parents=[common], help='Redact Content in a Confluence Blog Post', description='Redacts sensitive content in a Confluence blog post by replacing specified\ntext ranges with redaction markers. Each redaction in the response includes a\nunique UUID for restoration (except code block redactions). The response\nmetadata items maintain the same order as the input redaction pointers, and\ncompletely overlapping redactions are merged into a single redaction with one\nUUID.\n\n**Note**: This endpoint requires **Atlassian Guard Premium**.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence redactions post-redact-blog ID', 'codapact-confluence redactions post-redact-blog ID --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post to redact content from.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--created-at', dest='p_created_at', metavar='DATETIME', help='Timestamp when the content was last updated.')
    c.add_argument('--clean-history', dest='p_clean_history', action=argparse.BooleanOptionalAction, help='Whether to clean up previous versions containing the redaction. When true, historical versions of the content that contain the redacted text will be squashed.')
    c.add_argument('--version-number', dest='p_version_number', type=integer, metavar='VERSION_NUMBER', help='Optional version number of the content to redact. When specified, the redaction will target ')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", help='JSON object with redactions. Schema: codapact-confluence describe redactions post-redact-blog')
    c.add_argument('--title', dest='p_title', type=json_value, metavar="JSON", help='JSON object with redactions. Schema: codapact-confluence describe redactions post-redact-blog')
    c.set_defaults(handler=_run_redactions_post_redact_blog, flags={'id': '--id', 'body.created_at': '--created-at', 'body.clean_history': '--clean-history', 'body.version_number': '--version-number', 'body.body': '--body', 'body.title': '--title'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'post_redact_blog'})
    g_smart_link = commands.add_parser('smart-link', help='create, delete, get', description="Run 'codapact-confluence smart-link COMMAND --help' for a command's options and examples.")
    g_smart_link_commands = g_smart_link.add_subparsers(dest="g_smart_link", metavar="COMMAND", required=True)
    c = g_smart_link_commands.add_parser('create', parents=[common], help='Create Smart Link in the content tree', description='Creates a Smart Link in the content tree in the space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the corresponding space. Permission to create a Smart Link\nin the content tree in the space.', usage='%(prog)s --space-id SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence smart-link create --space-id SPACE_ID', 'codapact-confluence smart-link create --space-id SPACE_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', required=True, help='ID of the space.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Title of the Smart Link in the content tree.')
    c.add_argument('--parent-id', dest='p_parent_id', metavar='PARENT_ID', help='The parent content ID of the Smart Link in the content tree.')
    c.add_argument('--embed-url', dest='p_embed_url', metavar='EMBED_URL', help='The URL that the Smart Link in the content tree should be populated with.')
    c.set_defaults(handler=_run_smart_link_create, flags={'body.space_id': '--space-id', 'body.title': '--title', 'body.parent_id': '--parent-id', 'body.embed_url': '--embed-url'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_smart_link'})
    c = g_smart_link_commands.add_parser('get', parents=[common], help='Get Smart Link in the content tree by id', description='Returns a specific Smart Link in the content tree.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the Smart Link in the content tree and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence smart-link get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree to be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the Smart Link. (default: False)')
    c.add_argument('--include-direct-children', dest='p_include_direct_children', action=argparse.BooleanOptionalAction, help='Includes direct children of the Smart Link, as defined in the `ChildrenResponse` object. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this Smart Link in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this Smart Link in the response. (default: False)')
    c.set_defaults(handler=_run_smart_link_get, flags={'id': '--id', 'include_collaborators': '--include-collaborators', 'include_direct_children': '--include-direct-children', 'include_operations': '--include-operations', 'include_properties': '--include-properties'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_smart_link_by_id'})
    c = g_smart_link_commands.add_parser('delete', parents=[common], help='Delete Smart Link in the content tree', description='Delete a Smart Link in the content tree by id.\n\nDeleting a Smart Link in the content tree moves the Smart Link to the trash,\nwhere it can be restored later\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the Smart Link in the content tree and its corresponding\nspace. Permission to delete Smart Links in the content tree in the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence smart-link delete ID --dry-run', 'codapact-confluence smart-link delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the Smart Link in the content tree to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_smart_link_delete, flags={'id': '--id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_smart_link'})
    g_space = commands.add_parser('space', help='create, get, list-spaces', description="Run 'codapact-confluence space COMMAND --help' for a command's options and examples.")
    g_space_commands = g_space.add_subparsers(dest="g_space", metavar="COMMAND", required=True)
    c = g_space_commands.add_parser('list-spaces', parents=[common], help='Get spaces', description="Returns all spaces. The results will be sorted by id ascending. The number of\nresults is limited by the `limit` parameter and additional results (if\navailable) will be available through the `next` URL present in the `Link`\nresponse header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\nspaces that the user has permission to view will be returned.", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space list-spaces']), formatter_class=RAW)
    c.add_argument('--ids', dest='p_ids', action="append", type=integer, metavar='IDS', help='Filter the results to spaces based on their IDs. Multiple IDs can be specified as a comma-separated list.')
    c.add_argument('--keys', dest='p_keys', action="append", metavar='KEYS', help='Filter the results to spaces based on their keys. Multiple keys can be specified as a comma-separated list.')
    c.add_argument('--type', dest='p_type', choices=['global', 'collaboration', 'knowledge_base', 'personal', 'system', 'onboarding', 'xflow_sample_space'], help='Filter the results to spaces based on their type.')
    c.add_argument('--status', dest='p_status', choices=['current', 'archived', 'trashed'], help='Filter the results to spaces based on their status.')
    c.add_argument('--labels', dest='p_labels', action="append", metavar='LABELS', help='Filter the results to spaces based on their labels. Multiple labels can be specified as a comma-separated list.')
    c.add_argument('--favorited-by', dest='p_favorited_by', metavar='FAVORITED_BY', help='Filter the results to spaces favorited by the user with the specified account ID.')
    c.add_argument('--not-favorited-by', dest='p_not_favorited_by', metavar='NOT_FAVORITED_BY', help='Filter the results to spaces NOT favorited by the user with the specified account ID.')
    c.add_argument('--sort', dest='p_sort', choices=['id', '-id', 'key', '-key', 'name', '-name'], help='Used to sort the result by a particular field.')
    c.add_argument('--description-format', dest='p_description_format', choices=['plain', 'view'], help='The content format type to be returned in the `description` field of the response. If available, the representation will be available under a response field of the same name under the `description` field.')
    c.add_argument('--include-icon', dest='p_include_icon', action=argparse.BooleanOptionalAction, help='If the icon for the space should be fetched or not. (default: False)')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of spaces per result to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_space_list_spaces, flags={'ids': '--ids', 'keys': '--keys', 'type': '--type', 'status': '--status', 'labels': '--labels', 'favorited_by': '--favorited-by', 'not_favorited_by': '--not-favorited-by', 'sort': '--sort', 'description_format': '--description-format', 'include_icon': '--include-icon', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_spaces'})
    c = g_space_commands.add_parser('create', parents=[common], help='Create space', description='Creates a Space as specified in the payload.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to create spaces.', usage='%(prog)s --name NAME [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space create --name NAME', 'codapact-confluence space create --name NAME --dry-run']), formatter_class=RAW)
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True, help='The name of the space to be created.')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='The key for the new space. See [Space Keys](https://support.atlassian.com/confluence-cloud/docs/create-a-space/). If the key property is not provided, the alias property is required to be used instead.')
    c.add_argument('--alias', dest='p_alias', metavar='ALIAS', help='This field will be used as the new identifier for the space in confluence page URLs. If the alias property is not provided, the key property is required to be used instead. Maximum 255 alphanumeric characters in length.')
    c.add_argument('--description', dest='p_description', type=json_value, metavar="JSON", help="The description of the new/updated space. Note, only the 'plain' representation is currently supported. JSON object with value, representation. Schema: codapact-confluence describe space create")
    c.add_argument('--role-assignments', dest='p_role_assignments', type=json_value, metavar="JSON", help='JSON array of objects with principal, role_id. Schema: codapact-confluence describe space create')
    c.add_argument('--copy-space-access-configuration', dest='p_copy_space_access_configuration', type=integer, metavar='COPY_SPACE_ACCESS_CONFIGURATION', help='The id of the space to copy the space access configuration from.')
    c.add_argument('--create-private-space', dest='p_create_private_space', action=argparse.BooleanOptionalAction, help='Whether to create the space as private.')
    c.add_argument('--template-key', dest='p_template_key', metavar='TEMPLATE_KEY', help='The key of the template to use.')
    c.set_defaults(handler=_run_space_create, flags={'body.name': '--name', 'body.key': '--key', 'body.alias': '--alias', 'body.description': '--description', 'body.role_assignments': '--role-assignments', 'body.copy_space_access_configuration': '--copy-space-access-configuration', 'body.create_private_space': '--create-private-space', 'body.template_key': '--template-key'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_space'})
    c = g_space_commands.add_parser('get', parents=[common], help='Get space by id', description='Returns a specific space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space to be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--description-format', dest='p_description_format', choices=['plain', 'view'], help='The content format type to be returned in the `description` field of the response. If available, the representation will be available under a response field of the same name under the `description` field.')
    c.add_argument('--include-icon', dest='p_include_icon', action=argparse.BooleanOptionalAction, help='If the icon for the space should be fetched or not. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this space in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes space properties associated with this space in the response. (default: False)')
    c.add_argument('--include-permissions', dest='p_include_permissions', action=argparse.BooleanOptionalAction, help='Includes space permissions associated with this space in the response. (default: False)')
    c.add_argument('--include-role-assignments', dest='p_include_role_assignments', action=argparse.BooleanOptionalAction, help='Includes role assignments associated with this space in the response. This parameter is only accepted for EAP sites. (default: False)')
    c.add_argument('--include-labels', dest='p_include_labels', action=argparse.BooleanOptionalAction, help='Includes labels associated with this space in the response. (default: False)')
    c.set_defaults(handler=_run_space_get, flags={'id': '--id', 'description_format': '--description-format', 'include_icon': '--include-icon', 'include_operations': '--include-operations', 'include_properties': '--include-properties', 'include_permissions': '--include-permissions', 'include_role_assignments': '--include-role-assignments', 'include_labels': '--include-labels'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_by_id'})
    g_space_permission_transition = commands.add_parser('space-permission-transition', help='bulk-assign-space-permission-roles, bulk-remove-space-permission-access, generate-space-permission-combinations, … (5 commands)', description="Run 'codapact-confluence space-permission-transition COMMAND --help' for a command's options and examples.")
    g_space_permission_transition_commands = g_space_permission_transition.add_subparsers(dest="g_space_permission_transition", metavar="COMMAND", required=True)
    c = g_space_permission_transition_commands.add_parser('list-space-permission-combinations', parents=[common], help='List unassigned space permission combinations', description='Lists the unique unassigned space permission combinations currently present on\nthe tenant. Combinations that already map to a space role are filtered out\nserver-side. Each row carries the decoded set of space permissions and the\nprincipal types that currently hold the combination — these inform which\n`principalType` values are valid to include in the matching bulk role-\nassignments request.\n\nResults are always sorted by `principalCount` descending. Sort field and sort\norder are not configurable; page size is controlled by the `limit` query\nparameter (default 25, min 1, max 250). Use the `cursor` field to page through\nadditional results. The `generatedAt` field reflects the last audit run that\npopulated the combinations table — call the generate-combinations endpoint to\nrefresh stale data.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be a Confluence administrator.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-permission-transition list-space-permission-combinations']), formatter_class=RAW)
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Opaque cursor returned from a previous page in the `cursor` field of the response. Omit for the first page.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='The maximum number of combinations to return per page. Requests outside the supported range return `400`. (default: 25)')
    c.set_defaults(handler=_run_space_permission_transition_list_space_permission_combinations, flags={'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'list_space_permission_combinations'})
    c = g_space_permission_transition_commands.add_parser('generate-space-permission-combinations', parents=[common], help='Generate space permission combinations', description='Submits a task to refresh the space permission combinations in the database,\nwhich identifies all unique permission combinations across the site. This\nprovides permission combination IDs that can be used with the assign-roles and\nremove-access endpoints.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be a Confluence administrator.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-permission-transition generate-space-permission-combinations', 'codapact-confluence space-permission-transition generate-space-permission-combinations --dry-run']), formatter_class=RAW)
    c.set_defaults(handler=_run_space_permission_transition_generate_space_permission_combinations, flags={}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'generate_space_permission_combinations'})
    c = g_space_permission_transition_commands.add_parser('bulk-assign-space-permission-roles', parents=[common], help='Bulk assign space permission roles', description='Bulk assigns roles for one or more permission combination IDs obtained from\nthe space permission combinations. Supports targeting all spaces, specific\nspaces, or excluding specific spaces.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be a Confluence administrator.', usage='%(prog)s --assignments @assignments.json --space-selection @space-selection.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-permission-transition bulk-assign-space-permission-roles --assignments @assignments.json --space-selection @space-selection.json', 'codapact-confluence space-permission-transition bulk-assign-space-permission-roles --assignments @assignments.json --space-selection @space-selection.json --dry-run']), formatter_class=RAW)
    c.add_argument('--assignments', dest='p_assignments', type=json_value, metavar="JSON", required=True, help='List of role assignments to apply. JSON array of objects with permission_combination_id*, principal_type_assignments* (* required). Schema: codapact-confluence describe space-permission-transition bulk-assign-space-permission-roles')
    c.add_argument('--space-selection', dest='p_space_selection', type=json_value, metavar="JSON", required=True, help='JSON object with space_type*, selected_spaces (* required). Schema: codapact-confluence describe space-permission-transition bulk-assign-space-permission-roles')
    c.set_defaults(handler=_run_space_permission_transition_bulk_assign_space_permission_roles, flags={'body.assignments': '--assignments', 'body.space_selection': '--space-selection'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'bulk_assign_space_permission_roles'})
    c = g_space_permission_transition_commands.add_parser('bulk-remove-space-permission-access', parents=[common], help='Bulk remove space permission access', description='Bulk removes access for one or more permission combination IDs obtained from\nthe space permission combinations. This removes all space permissions for the\nspecified combinations across the targeted spaces.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be a Confluence administrator.', usage='%(prog)s --permission-combination-ids PERMISSION_COMBINATION_IDS --space-selection @space-selection.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-permission-transition bulk-remove-space-permission-access --permission-combination-ids PERMISSION_COMBINATION_IDS --space-selection @space-selection.json', 'codapact-confluence space-permission-transition bulk-remove-space-permission-access --permission-combination-ids PERMISSION_COMBINATION_IDS --space-selection @space-selection.json --dry-run']), formatter_class=RAW)
    c.add_argument('--permission-combination-ids', dest='p_permission_combination_ids', action="append", metavar='PERMISSION_COMBINATION_IDS', required=True, help='List of permission combination IDs to remove access for.')
    c.add_argument('--space-selection', dest='p_space_selection', type=json_value, metavar="JSON", required=True, help='JSON object with space_type*, selected_spaces (* required). Schema: codapact-confluence describe space-permission-transition bulk-remove-space-permission-access')
    c.set_defaults(handler=_run_space_permission_transition_bulk_remove_space_permission_access, flags={'body.permission_combination_ids': '--permission-combination-ids', 'body.space_selection': '--space-selection'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'bulk_remove_space_permission_access'})
    c = g_space_permission_transition_commands.add_parser('get-task-status', parents=[common], help='Get space permission transition task status', description='Retrieves the status of an async space permission transition task. Use the\ntaskId returned from the generate-combinations, assign-roles, or remove-access\nendpoints to poll for progress and completion.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be a Confluence administrator.', usage='%(prog)s TASK_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-permission-transition get-task-status TASK_ID']), formatter_class=RAW)
    c.add_argument('p_task_id', metavar='TASK_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the async task, as returned by the generate-combinations, assign-roles, or remove-access endpoints.')
    c.add_argument('--task-id', dest='p_task_id', default=argparse.SUPPRESS, metavar='TASK_ID', help='same as TASK_ID')
    c.set_defaults(handler=_run_space_permission_transition_get_task_status, flags={'task_id': '--task-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_permission_transition_task_status'})
    g_space_permissions = commands.add_parser('space-permissions', help='list, list-assignments', description="Run 'codapact-confluence space-permissions COMMAND --help' for a command's options and examples.")
    g_space_permissions_commands = g_space_permissions.add_subparsers(dest="g_space_permissions", metavar="COMMAND", required=True)
    c = g_space_permissions_commands.add_parser('list-assignments', parents=[common], help='Get space permissions assignments', description='Returns space permission assignments for a specific space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-permissions list-assignments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space to be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of assignments to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_space_permissions_list_assignments, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_permissions_assignments'})
    c = g_space_permissions_commands.add_parser('list', parents=[common], help='Get available space permissions', description='Retrieves the available space permissions.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-permissions list']), formatter_class=RAW)
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of space permissions to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_space_permissions_list, flags={'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_available_space_permissions'})
    g_space_properties = commands.add_parser('space-properties', help='create, delete, get, … (5 commands)', description="Run 'codapact-confluence space-properties COMMAND --help' for a command's options and examples.")
    g_space_properties_commands = g_space_properties.add_subparsers(dest="g_space_properties", metavar="COMMAND", required=True)
    c = g_space_properties_commands.add_parser('list', parents=[common], help='Get space properties in space', description="Returns all properties for the given space. Space properties are a key-value\nstorage associated with a space. The limit parameter specifies the maximum\nnumber of results returned in a single response. Use the `link` response\nheader to paginate through additional results.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission) and\n'View' permission for the space.", usage='%(prog)s SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-properties list SPACE_ID']), formatter_class=RAW)
    c.add_argument('p_space_id', metavar='SPACE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which space properties should be returned.')
    c.add_argument('--space-id', dest='p_space_id', default=argparse.SUPPRESS, type=integer, metavar='SPACE_ID', help='same as SPACE_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='The key of the space property to retrieve. This should be used when a user knows the key of their property, but needs to retrieve the id for use in other methods.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of pages per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_space_properties_list, flags={'space_id': '--space-id', 'key': '--key', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_properties'})
    c = g_space_properties_commands.add_parser('create', parents=[common], help='Create space property in space', description="Creates a new space property.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission) and\n'Admin' permission for the space.", usage='%(prog)s SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-properties create SPACE_ID --key KEY', 'codapact-confluence space-properties create SPACE_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_space_id', metavar='SPACE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which space properties should be returned.')
    c.add_argument('--space-id', dest='p_space_id', default=argparse.SUPPRESS, type=integer, metavar='SPACE_ID', help='same as SPACE_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the space property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the space property.')
    c.set_defaults(handler=_run_space_properties_create, flags={'space_id': '--space-id', 'body.key': '--key', 'body.value': '--value'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_space_property', 'requires_one_of': [['--key', '--value']]})
    c = g_space_properties_commands.add_parser('get', parents=[common], help='Get space property by id', description="Retrieve a space property by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission) and\n'View' permission for the space.", usage='%(prog)s SPACE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-properties get SPACE_ID PROPERTY_ID']), formatter_class=RAW)
    c.add_argument('p_space_id', metavar='SPACE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be retrieved.')
    c.add_argument('--space-id', dest='p_space_id', default=argparse.SUPPRESS, type=integer, metavar='SPACE_ID', help='same as SPACE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.set_defaults(handler=_run_space_properties_get, flags={'space_id': '--space-id', 'property_id': '--property-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_property_by_id'})
    c = g_space_properties_commands.add_parser('update', parents=[common], help='Update space property by id', description="Update a space property by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission) and\n'Admin' permission for the space.", usage='%(prog)s SPACE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-properties update SPACE_ID PROPERTY_ID --key KEY', 'codapact-confluence space-properties update SPACE_ID PROPERTY_ID --key KEY --dry-run']), formatter_class=RAW)
    c.add_argument('p_space_id', metavar='SPACE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be updated.')
    c.add_argument('--space-id', dest='p_space_id', default=argparse.SUPPRESS, type=integer, metavar='SPACE_ID', help='same as SPACE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    c.add_argument('--key', dest='p_key', metavar='KEY', help='Key of the space property')
    c.add_argument('--value', dest='p_value', type=json_value, metavar="JSON", help='Value of the space property.')
    c.add_argument('--arg-version', dest='p_arg_version', type=json_value, metavar="JSON", help='New version number and associated message JSON object with number, message. Schema: codapact-confluence describe space-properties update')
    c.set_defaults(handler=_run_space_properties_update, flags={'space_id': '--space-id', 'property_id': '--property-id', 'body.key': '--key', 'body.value': '--value', 'body.version': '--arg-version'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_space_property_by_id', 'requires_one_of': [['--key', '--value', '--arg-version']]})
    c = g_space_properties_commands.add_parser('delete', parents=[common], help='Delete space property by id', description="Deletes a space property by its id.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission) and\n'Admin' permission for the space.", usage='%(prog)s SPACE_ID PROPERTY_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-properties delete SPACE_ID PROPERTY_ID --dry-run', 'codapact-confluence space-properties delete SPACE_ID PROPERTY_ID --yes']), formatter_class=RAW)
    c.add_argument('p_space_id', metavar='SPACE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space the property belongs to.')
    c.add_argument('p_property_id', metavar='PROPERTY_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the property to be deleted.')
    c.add_argument('--space-id', dest='p_space_id', default=argparse.SUPPRESS, type=integer, metavar='SPACE_ID', help='same as SPACE_ID')
    c.add_argument('--property-id', dest='p_property_id', default=argparse.SUPPRESS, type=integer, metavar='PROPERTY_ID', help='same as PROPERTY_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_space_properties_delete, flags={'space_id': '--space-id', 'property_id': '--property-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_space_property_by_id'})
    g_space_roles = commands.add_parser('space-roles', help='create, delete, get, … (8 commands)', description="Run 'codapact-confluence space-roles COMMAND --help' for a command's options and examples.")
    g_space_roles_commands = g_space_roles.add_subparsers(dest="g_space_roles", metavar="COMMAND", required=True)
    c = g_space_roles_commands.add_parser('list', parents=[common], help='Get available space roles', description="Retrieves the available space roles.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site; if requesting a certain space's\nroles, permission to view the space.", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles list']), formatter_class=RAW)
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', help='The space ID for which to filter available space roles; if empty, return all available space roles for the tenant.')
    c.add_argument('--role-type', dest='p_role_type', metavar='ROLE_TYPE', help='The space role type to filter results by.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='The principal ID to filter results by. If specified, a principal-type must also be specified. Paired with a `principal-type` of `ACCESS_CLASS`, valid values include [`anonymous-users`, `jsm-project-admins`, `authenticated-users`, `all-licensed-users`, `all-product-admins`]')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['USER', 'GROUP', 'ACCESS_CLASS'], help='The principal type to filter results by. If specified, a principal-id must also be specified.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of space roles to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_space_roles_list, flags={'space_id': '--space-id', 'role_type': '--role-type', 'principal_id': '--principal-id', 'principal_type': '--principal-type', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_available_space_roles'})
    c = g_space_roles_commands.add_parser('create', parents=[common], help='Create a space role', description='Create a space role.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be an organization or site admin. Connect and Forge app users are not\nauthorized to access this resource.', usage='%(prog)s --name NAME --description DESCRIPTION --space-permissions SPACE_PERMISSIONS [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles create --name NAME --description DESCRIPTION --space-permissions SPACE_PERMISSIONS', 'codapact-confluence space-roles create --name NAME --description DESCRIPTION --space-permissions SPACE_PERMISSIONS --dry-run']), formatter_class=RAW)
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True, help='Name of the space role')
    c.add_argument('--description', dest='p_description', metavar='DESCRIPTION', required=True, help='Description for the space role')
    c.add_argument('--space-permissions', dest='p_space_permissions', action="append", metavar='SPACE_PERMISSIONS', required=True, help='The ids of the space permissions associated with the space role. Sample value "read/space"; retrieve ids from responses returned by [GET /space-permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) endpoint')
    c.set_defaults(handler=_run_space_roles_create, flags={'body.name': '--name', 'body.description': '--description', 'body.space_permissions': '--space-permissions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_space_role'})
    c = g_space_roles_commands.add_parser('get', parents=[common], help='Get space role by ID', description='Retrieves the space role by ID.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space role to retrieve.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.set_defaults(handler=_run_space_roles_get, flags={'id': '--id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_roles_by_id'})
    c = g_space_roles_commands.add_parser('update', parents=[common], help='Update a space role', description='Update a space role.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be an organization or site admin. Connect and Forge app users are not\nauthorized to access this resource.', usage='%(prog)s ID --name NAME --description DESCRIPTION --space-permissions SPACE_PERMISSIONS [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles update ID --name NAME --description DESCRIPTION --space-permissions SPACE_PERMISSIONS', 'codapact-confluence space-roles update ID --name NAME --description DESCRIPTION --space-permissions SPACE_PERMISSIONS --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='Id of the space role')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True, help='Name of the space role')
    c.add_argument('--description', dest='p_description', metavar='DESCRIPTION', required=True, help='Description for the space role')
    c.add_argument('--space-permissions', dest='p_space_permissions', action="append", metavar='SPACE_PERMISSIONS', required=True, help='The ids of the space permissions associated with the space role. Sample value "read/space"; retrieve ids from responses returned by [GET /space-permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) endpoint')
    c.add_argument('--anonymous-reassignment-role-id', dest='p_anonymous_reassignment_role_id', metavar='ANONYMOUS_REASSIGNMENT_ROLE_ID', help='If space anonymous access is assigned to the role being modified, the Id of a role to migrate those assignments to can be specified. Anonymous access role assignments left unchanged if unspecified.')
    c.add_argument('--guest-reassignment-role-id', dest='p_guest_reassignment_role_id', metavar='GUEST_REASSIGNMENT_ROLE_ID', help='If guests are assigned to the role being modified, the Id of a role to migrate those assignments to can be specified. Guest role assignments left unchanged if unspecified.')
    c.set_defaults(handler=_run_space_roles_update, flags={'id': '--id', 'body.name': '--name', 'body.description': '--description', 'body.space_permissions': '--space-permissions', 'body.anonymous_reassignment_role_id': '--anonymous-reassignment-role-id', 'body.guest_reassignment_role_id': '--guest-reassignment-role-id'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_space_role'})
    c = g_space_roles_commands.add_parser('delete', parents=[common], help='Delete a space role', description='Delete a space role\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**: User\nmust be an organization or site admin. Connect and Forge app users are not\nauthorized to access this resource.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles delete ID --dry-run', 'codapact-confluence space-roles delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help='Id of the space role')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_space_roles_delete, flags={'id': '--id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_space_role'})
    c = g_space_roles_commands.add_parser('get-mode', parents=[common], help='Get space role mode', description="Retrieves the space role mode.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles get-mode']), formatter_class=RAW)
    c.set_defaults(handler=_run_space_roles_get_mode, flags={}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_role_mode'})
    c = g_space_roles_commands.add_parser('list-assignments', parents=[common], help='Get space role assignments', description='Retrieves the space role assignments.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles list-assignments ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which to retrieve assignments.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--role-id', dest='p_role_id', metavar='ROLE_ID', help='Filters the returned role assignments to the provided role ID.')
    c.add_argument('--role-type', dest='p_role_type', metavar='ROLE_TYPE', help='Filters the returned role assignments to the provided role type.')
    c.add_argument('--principal-id', dest='p_principal_id', metavar='PRINCIPAL_ID', help='Filters the returned role assignments to the provided principal id. If specified, a principal-type must also be specified. Paired with a `principal-type` of `ACCESS_CLASS`, valid values include [`anonymous-users`, `jsm-project-admins`, `authenticated-users`, `all-licensed-users`, `all-product-admins`]')
    c.add_argument('--principal-type', dest='p_principal_type', choices=['USER', 'GROUP', 'ACCESS_CLASS'], help='Filters the returned role assignments to the provided principal type. If specified, a principal-id must also be specified.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of space roles to return. If more results exist, use the `Link` response header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_space_roles_list_assignments, flags={'id': '--id', 'role_id': '--role-id', 'role_type': '--role-type', 'principal_id': '--principal-id', 'principal_type': '--principal-type', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_space_role_assignments'})
    c = g_space_roles_commands.add_parser('set-assignments', parents=[common], help='Set space role assignments', description='Sets space role assignments as specified in the payload. For each entry, if\n`roleId` is provided the principal is assigned to that role. If `roleId` is\nomitted, the role assignment for that principal is removed, if it exists.\n\nAvailable on tenants with [Role-Based Access\nControl](https://support.atlassian.com/confluence-cloud/docs/manage-user-\nroles/).\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to manage roles in the space.', usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence space-roles set-assignments ID --body @body.json', 'codapact-confluence space-roles set-assignments ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the space for which to retrieve assignments.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON array of objects with principal*, role_id (* required). Schema: codapact-confluence describe space-roles set-assignments')
    c.set_defaults(handler=_run_space_roles_set_assignments, flags={'id': '--id', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'set_space_role_assignments'})
    g_task = commands.add_parser('task', help='get, list-tasks, update', description="Run 'codapact-confluence task COMMAND --help' for a command's options and examples.")
    g_task_commands = g_task.add_subparsers(dest="g_task", metavar="COMMAND", required=True)
    c = g_task_commands.add_parser('list-tasks', parents=[common], help='Get tasks', description="Returns all tasks. The number of results is limited by the `limit` parameter\nand additional results (if available) will be available through the `next` URL\npresent in the `Link` response header.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). Only\ntasks that the user has permission to view will be returned.", usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['codapact-confluence task list-tasks']), formatter_class=RAW)
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--include-blank-tasks', dest='p_include_blank_tasks', action=argparse.BooleanOptionalAction, help='Specifies whether to include blank tasks in the response. Defaults to `true`.')
    c.add_argument('--status', dest='p_status', choices=['complete', 'incomplete'], help='Filters on the status of the task.')
    c.add_argument('--task-id', dest='p_task_id', action="append", type=integer, metavar='TASK_ID', help='Filters on task ID. Multiple IDs can be specified.')
    c.add_argument('--space-id', dest='p_space_id', action="append", type=integer, metavar='SPACE_ID', help='Filters on the space ID of the task. Multiple IDs can be specified.')
    c.add_argument('--page-id', dest='p_page_id', action="append", type=integer, metavar='PAGE_ID', help='Filters on the page ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.')
    c.add_argument('--blogpost-id', dest='p_blogpost_id', action="append", type=integer, metavar='BLOGPOST_ID', help='Filters on the blog post ID of the task. Multiple IDs can be specified. Note - page and blog post filters can be used in conjunction.')
    c.add_argument('--created-by', dest='p_created_by', action="append", metavar='CREATED_BY', help='Filters on the Account ID of the user who created this task. Multiple IDs can be specified.')
    c.add_argument('--assigned-to', dest='p_assigned_to', action="append", metavar='ASSIGNED_TO', help='Filters on the Account ID of the user to whom this task is assigned. Multiple IDs can be specified.')
    c.add_argument('--completed-by', dest='p_completed_by', action="append", metavar='COMPLETED_BY', help='Filters on the Account ID of the user who completed this task. Multiple IDs can be specified.')
    c.add_argument('--created-at-from', dest='p_created_at_from', type=integer, metavar='CREATED_AT_FROM', help='Filters on start of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.')
    c.add_argument('--created-at-to', dest='p_created_at_to', type=integer, metavar='CREATED_AT_TO', help='Filters on end of date-time range of task based on creation date (inclusive). Input is epoch time in milliseconds.')
    c.add_argument('--due-at-from', dest='p_due_at_from', type=integer, metavar='DUE_AT_FROM', help='Filters on start of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.')
    c.add_argument('--due-at-to', dest='p_due_at_to', type=integer, metavar='DUE_AT_TO', help='Filters on end of date-time range of task based on due date (inclusive). Input is epoch time in milliseconds.')
    c.add_argument('--completed-at-from', dest='p_completed_at_from', type=integer, metavar='COMPLETED_AT_FROM', help='Filters on start of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.')
    c.add_argument('--completed-at-to', dest='p_completed_at_to', type=integer, metavar='COMPLETED_AT_TO', help='Filters on end of date-time range of task based on completion date (inclusive). Input is epoch time in milliseconds.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of tasks per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.set_defaults(handler=_run_task_list_tasks, flags={'body_format': '--body-format', 'include_blank_tasks': '--include-blank-tasks', 'status': '--status', 'task_id': '--task-id', 'space_id': '--space-id', 'page_id': '--page-id', 'blogpost_id': '--blogpost-id', 'created_by': '--created-by', 'assigned_to': '--assigned-to', 'completed_by': '--completed-by', 'created_at_from': '--created-at-from', 'created_at_to': '--created-at-to', 'due_at_from': '--due-at-from', 'due_at_to': '--due-at-to', 'completed_at_from': '--completed-at-from', 'completed_at_to': '--completed-at-to', 'cursor': '--cursor', 'limit': '--limit'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_tasks'})
    c = g_task_commands.add_parser('get', parents=[common], help='Get task by id', description='Returns a specific task.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the containing page or blog post and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence task get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the task to be returned. If you don't know the task ID, use Get tasks and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.set_defaults(handler=_run_task_get, flags={'id': '--id', 'body_format': '--body-format'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_task_by_id'})
    c = g_task_commands.add_parser('update', parents=[common], help='Update task', description='Update a task by id. This endpoint currently only supports updating task\nstatus.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to edit the containing page or blog post and view its corresponding\nspace.', usage='%(prog)s ID --body @body.json [options]', epilog=RUNTIME.command_epilog(['codapact-confluence task update ID --body @body.json', 'codapact-confluence task update ID --body @body.json --dry-run']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the task to be updated. If you don't know the task ID, use Get tasks and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--body', dest='p_body', type=json_value, metavar="JSON", required=True, help='JSON object with status*, id, local_id, space_id, page_id, blog_post_id, created_by, assigned_to, completed_by, created_at, updated_at, due_at, ... (* required). Schema: codapact-confluence describe task update')
    c.set_defaults(handler=_run_task_update, flags={'id': '--id', 'body_format': '--body-format', 'body': '--body'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_task'})
    g_user = commands.add_parser('user', help='check-access-by-email, create-bulk-lookup, invite-by-email', description="Run 'codapact-confluence user COMMAND --help' for a command's options and examples.")
    g_user_commands = g_user.add_subparsers(dest="g_user", metavar="COMMAND", required=True)
    c = g_user_commands.add_parser('create-bulk-lookup', parents=[common], help='Create bulk user lookup using ids', description="Returns user details for the ids provided in the request body.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission). The\nuser must be able to view user profiles in the Confluence site.", usage='%(prog)s --account-ids ACCOUNT_IDS [options]', epilog=RUNTIME.command_epilog(['codapact-confluence user create-bulk-lookup --account-ids ACCOUNT_IDS', 'codapact-confluence user create-bulk-lookup --account-ids ACCOUNT_IDS --dry-run']), formatter_class=RAW)
    c.add_argument('--account-ids', dest='p_account_ids', action="append", metavar='ACCOUNT_IDS', required=True, help='List of accountIds to retrieve user info for.')
    c.set_defaults(handler=_run_user_create_bulk_lookup, flags={'body.account_ids': '--account-ids'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_bulk_user_lookup'})
    c = g_user_commands.add_parser('check-access-by-email', parents=[common], help='Check site access for a list of emails', description="Returns the list of emails from the input list that do not have access to\nsite.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).", usage='%(prog)s --emails EMAILS [options]', epilog=RUNTIME.command_epilog(['codapact-confluence user check-access-by-email --emails EMAILS', 'codapact-confluence user check-access-by-email --emails EMAILS --dry-run']), formatter_class=RAW)
    c.add_argument('--emails', dest='p_emails', action="append", metavar='EMAILS', required=True, help='List of emails to check access to site.')
    c.set_defaults(handler=_run_user_check_access_by_email, flags={'body.emails': '--emails'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'check_access_by_email'})
    c = g_user_commands.add_parser('invite-by-email', parents=[common], help='Invite a list of emails to the site', description="Invite a list of emails to the site.\n\nIgnores all invalid emails and no action is taken for the emails that already\nhave access to the site.\n\n<b>NOTE:</b> This API is asynchronous and may take some time to complete.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to access the Confluence site ('Can use' global permission).", usage='%(prog)s --emails EMAILS [options]', epilog=RUNTIME.command_epilog(['codapact-confluence user invite-by-email --emails EMAILS', 'codapact-confluence user invite-by-email --emails EMAILS --dry-run']), formatter_class=RAW)
    c.add_argument('--emails', dest='p_emails', action="append", metavar='EMAILS', required=True, help='List of emails to check access to site.')
    c.set_defaults(handler=_run_user_invite_by_email, flags={'body.emails': '--emails'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'invite_by_email'})
    g_version = commands.add_parser('version', help='list-attachment-details, list-attachment-versions, list-blog-post-details, … (12 commands)', description="Run 'codapact-confluence version COMMAND --help' for a command's options and examples.")
    g_version_commands = g_version.add_subparsers(dest="g_version", metavar="COMMAND", required=True)
    c = g_version_commands.add_parser('list-attachment-versions', parents=[common], help='Get attachment versions', description='Returns the versions of specific attachment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-attachment-versions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, help="The ID of the attachment to be queried for its versions. If you don't know the attachment ID, use Get attachments and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, metavar='ID', help='same as ID')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_version_list_attachment_versions, flags={'id': '--id', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_versions'})
    c = g_version_commands.add_parser('list-attachment-details', parents=[common], help='Get version details for attachment version', description='Retrieves version details for the specified attachment and version number.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the attachment.', usage='%(prog)s ATTACHMENT_ID VERSION_NUMBER [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-attachment-details ATTACHMENT_ID VERSION_NUMBER']), formatter_class=RAW)
    c.add_argument('p_attachment_id', metavar='ATTACHMENT_ID', nargs='?', default=argparse.SUPPRESS, help='The ID of the attachment for which version details should be returned.')
    c.add_argument('p_version_number', metavar='VERSION_NUMBER', nargs='?', default=argparse.SUPPRESS, type=integer, help='The version number of the attachment to be returned.')
    c.add_argument('--attachment-id', dest='p_attachment_id', default=argparse.SUPPRESS, metavar='ATTACHMENT_ID', help='same as ATTACHMENT_ID')
    c.add_argument('--version-number', dest='p_version_number', default=argparse.SUPPRESS, type=integer, metavar='VERSION_NUMBER', help='same as VERSION_NUMBER')
    c.set_defaults(handler=_run_version_list_attachment_details, flags={'attachment_id': '--attachment-id', 'version_number': '--version-number'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_attachment_version_details'})
    c = g_version_commands.add_parser('list-blog-post-versions', parents=[common], help='Get blog post versions', description='Returns the versions of specific blog post.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-blog-post-versions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the blog post to be queried for its versions. If you don't know the blog post ID, use Get blog posts and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_version_list_blog_post_versions, flags={'id': '--id', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_versions'})
    c = g_version_commands.add_parser('list-blog-post-details', parents=[common], help='Get version details for blog post version', description='Retrieves version details for the specified blog post and version number.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the blog post.', usage='%(prog)s BLOGPOST_ID VERSION_NUMBER [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-blog-post-details BLOGPOST_ID VERSION_NUMBER']), formatter_class=RAW)
    c.add_argument('p_blogpost_id', metavar='BLOGPOST_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the blog post for which version details should be returned.')
    c.add_argument('p_version_number', metavar='VERSION_NUMBER', nargs='?', default=argparse.SUPPRESS, type=integer, help='The version number of the blog post to be returned.')
    c.add_argument('--blogpost-id', dest='p_blogpost_id', default=argparse.SUPPRESS, type=integer, metavar='BLOGPOST_ID', help='same as BLOGPOST_ID')
    c.add_argument('--version-number', dest='p_version_number', default=argparse.SUPPRESS, type=integer, metavar='VERSION_NUMBER', help='same as VERSION_NUMBER')
    c.set_defaults(handler=_run_version_list_blog_post_details, flags={'blogpost_id': '--blogpost-id', 'version_number': '--version-number'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_blog_post_version_details'})
    c = g_version_commands.add_parser('list-page-versions', parents=[common], help='Get page versions', description='Returns the versions of specific page.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-page-versions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the page to be queried for its versions. If you don't know the page ID, use Get pages and filter the results.")
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_version_list_page_versions, flags={'id': '--id', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_versions'})
    c = g_version_commands.add_parser('list-page-details', parents=[common], help='Get version details for page version', description='Retrieves version details for the specified page and version number.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page.', usage='%(prog)s PAGE_ID VERSION_NUMBER [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-page-details PAGE_ID VERSION_NUMBER']), formatter_class=RAW)
    c.add_argument('p_page_id', metavar='PAGE_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the page for which version details should be returned.')
    c.add_argument('p_version_number', metavar='VERSION_NUMBER', nargs='?', default=argparse.SUPPRESS, type=integer, help='The version number of the page to be returned.')
    c.add_argument('--page-id', dest='p_page_id', default=argparse.SUPPRESS, type=integer, metavar='PAGE_ID', help='same as PAGE_ID')
    c.add_argument('--version-number', dest='p_version_number', default=argparse.SUPPRESS, type=integer, metavar='VERSION_NUMBER', help='same as VERSION_NUMBER')
    c.set_defaults(handler=_run_version_list_page_details, flags={'page_id': '--page-id', 'version_number': '--version-number'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_page_version_details'})
    c = g_version_commands.add_parser('list-custom-content-versions', parents=[common], help='Get custom content versions', description='Returns the versions of specific custom content.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the custom content and its corresponding page and space.', usage='%(prog)s CUSTOM_CONTENT_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-custom-content-versions CUSTOM_CONTENT_ID']), formatter_class=RAW)
    c.add_argument('p_custom_content_id', metavar='CUSTOM_CONTENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help="The ID of the custom content to be queried for its versions. If you don't know the custom content ID, use Get custom-content by type and filter the results.")
    c.add_argument('--custom-content-id', dest='p_custom_content_id', default=argparse.SUPPRESS, type=integer, metavar='CUSTOM_CONTENT_ID', help='same as CUSTOM_CONTENT_ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['raw', 'storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_version_list_custom_content_versions, flags={'custom_content_id': '--custom-content-id', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_versions'})
    c = g_version_commands.add_parser('list-custom-content-details', parents=[common], help='Get version details for custom content version', description='Retrieves version details for the specified custom content and version number.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the page.', usage='%(prog)s CUSTOM_CONTENT_ID VERSION_NUMBER [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-custom-content-details CUSTOM_CONTENT_ID VERSION_NUMBER']), formatter_class=RAW)
    c.add_argument('p_custom_content_id', metavar='CUSTOM_CONTENT_ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the custom content for which version details should be returned.')
    c.add_argument('p_version_number', metavar='VERSION_NUMBER', nargs='?', default=argparse.SUPPRESS, type=integer, help='The version number of the custom content to be returned.')
    c.add_argument('--custom-content-id', dest='p_custom_content_id', default=argparse.SUPPRESS, type=integer, metavar='CUSTOM_CONTENT_ID', help='same as CUSTOM_CONTENT_ID')
    c.add_argument('--version-number', dest='p_version_number', default=argparse.SUPPRESS, type=integer, metavar='VERSION_NUMBER', help='same as VERSION_NUMBER')
    c.set_defaults(handler=_run_version_list_custom_content_details, flags={'custom_content_id': '--custom-content-id', 'version_number': '--version-number'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_custom_content_version_details'})
    c = g_version_commands.add_parser('list-footer-comment-versions', parents=[common], help='Get footer comment versions', description='Retrieves the versions of the specified footer comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blog post and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-footer-comment-versions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the footer comment for which versions should be returned')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_version_list_footer_comment_versions, flags={'id': '--id', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_comment_versions'})
    c = g_version_commands.add_parser('list-footer-comment-details', parents=[common], help='Get version details for footer comment version', description='Retrieves version details for the specified footer comment version.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blog post and its corresponding\nspace.', usage='%(prog)s ID VERSION_NUMBER [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-footer-comment-details ID VERSION_NUMBER']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the footer comment for which version details should be returned.')
    c.add_argument('p_version_number', metavar='VERSION_NUMBER', nargs='?', default=argparse.SUPPRESS, type=integer, help='The version number of the footer comment to be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--version-number', dest='p_version_number', default=argparse.SUPPRESS, type=integer, metavar='VERSION_NUMBER', help='same as VERSION_NUMBER')
    c.set_defaults(handler=_run_version_list_footer_comment_details, flags={'id': '--id', 'version_number': '--version-number'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_footer_comment_version_details'})
    c = g_version_commands.add_parser('list-inline-comment-versions', parents=[common], help='Get inline comment versions', description='Retrieves the versions of the specified inline comment.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blog post and its corresponding\nspace.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-inline-comment-versions ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the inline comment for which versions should be returned')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--body-format', dest='p_body_format', choices=['storage', 'atlas_doc_format'], help='The content format types to be returned in the `body` field of the response. If available, the representation will be available under a response field of the same name under the `body` field.')
    c.add_argument('--cursor', dest='p_cursor', metavar='CURSOR', help='Used for pagination, this opaque cursor will be returned in the `next` URL in the `Link` response header. Use the relative URL in the `Link` header to retrieve the `next` set of results.')
    c.add_argument('--limit', dest='p_limit', type=integer, metavar='LIMIT', help='Maximum number of versions per result to return. If more results exist, use the `Link` header to retrieve a relative URL that will return the next set of results. (default: 25)')
    c.add_argument('--sort', dest='p_sort', choices=['modified-date', '-modified-date'], help='Used to sort the result by a particular field.')
    c.set_defaults(handler=_run_version_list_inline_comment_versions, flags={'id': '--id', 'body_format': '--body-format', 'cursor': '--cursor', 'limit': '--limit', 'sort': '--sort'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_comment_versions'})
    c = g_version_commands.add_parser('list-inline-comment-details', parents=[common], help='Get version details for inline comment version', description='Retrieves version details for the specified inline comment version.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the content of the page or blog post and its corresponding\nspace.', usage='%(prog)s ID VERSION_NUMBER [options]', epilog=RUNTIME.command_epilog(['codapact-confluence version list-inline-comment-details ID VERSION_NUMBER']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the inline comment for which version details should be returned.')
    c.add_argument('p_version_number', metavar='VERSION_NUMBER', nargs='?', default=argparse.SUPPRESS, type=integer, help='The version number of the inline comment to be returned.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--version-number', dest='p_version_number', default=argparse.SUPPRESS, type=integer, metavar='VERSION_NUMBER', help='same as VERSION_NUMBER')
    c.set_defaults(handler=_run_version_list_inline_comment_details, flags={'id': '--id', 'version_number': '--version-number'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_inline_comment_version_details'})
    g_whiteboard = commands.add_parser('whiteboard', help='create, delete, get', description="Run 'codapact-confluence whiteboard COMMAND --help' for a command's options and examples.")
    g_whiteboard_commands = g_whiteboard.add_subparsers(dest="g_whiteboard", metavar="COMMAND", required=True)
    c = g_whiteboard_commands.add_parser('create', parents=[common], help='Create whiteboard', description='Creates a whiteboard in the space.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the corresponding space. Permission to create a whiteboard\nin the space.', usage='%(prog)s --space-id SPACE_ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence whiteboard create --space-id SPACE_ID', 'codapact-confluence whiteboard create --space-id SPACE_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--private', dest='p_private', action=argparse.BooleanOptionalAction, help='The whiteboard will be private. Only the user who creates this whiteboard will have permission to view and edit one. (default: False)')
    c.add_argument('--space-id', dest='p_space_id', metavar='SPACE_ID', required=True, help='ID of the space.')
    c.add_argument('--title', dest='p_title', metavar='TITLE', help='Title of the whiteboard.')
    c.add_argument('--parent-id', dest='p_parent_id', metavar='PARENT_ID', help='The parent content ID of the whiteboard.')
    c.add_argument('--template-key', dest='p_template_key', choices=['2x2-prioritization', '4ls-retro', 'annual-calendar', 'brainwriting', 'concept-map', 'crazy-8s', 'daily-sync', 'disruptive-brainstorm', 'dot-voting', 'elevator-pitch', 'flow-chart', 'gap-analysis', 'ice-breakers', 'incident-postmortem', 'journey-mapping-kit', 'kanban-board', 'lean-coffee', 'network-of-teams', 'org-chart', 'pi-planning', 'prioritization', 'prioritization-experiment', 'product-roadmap', 'product-vision-board', 'rice', 'sailboat-retro', 'service-blueprint', 'simple-retrospective', 'sprint-planning', 'sticky-note-pack', 'swimlanes', 'team-formation-guide', 'timeline', 'timeline-workflow', 'user-story-map', 'workflow', 'vision-board', 'venn-diagram', 'storyboard', 'action-plan', 'root-cause-analysis', 'executive-summary', 'stakeholder-mapping', 'annual-calendar-2025-2026', 'health-monitor', 'okr-planning', 'swot-analysis', 'poker-planning', 'fishbone-diagram', 'risk-assessment', 'bounded-context', 'hopes-and-fears', 'swimlane-vertical'], help='Providing a template key will add that template to the new whiteboard.')
    c.add_argument('--locale', dest='p_locale', choices=['de-DE', 'cs-CZ', 'ko-KR', 'fr-FR', 'it-IT', 'ja-JP', 'nl-NL', 'nb-NO', 'da-DK', 'sv-SE', 'fi-FI', 'ru-RU', 'pl-PL', 'tr-TR', 'hu-HU', 'en-GB', 'en-US', 'pt-BR', 'zh-CN', 'zh-TW', 'es-ES'], help="If templateKey is provided, locale will decide which language the template will be created with. If locale is omitted, the user's locale will be used.")
    c.set_defaults(handler=_run_whiteboard_create, flags={'private': '--private', 'body.space_id': '--space-id', 'body.title': '--title', 'body.parent_id': '--parent-id', 'body.template_key': '--template-key', 'body.locale': '--locale'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_whiteboard'})
    c = g_whiteboard_commands.add_parser('get', parents=[common], help='Get whiteboard by id', description='Returns a specific whiteboard.\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the whiteboard and its corresponding space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence whiteboard get ID']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard to be returned')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    c.add_argument('--include-collaborators', dest='p_include_collaborators', action=argparse.BooleanOptionalAction, help='Includes collaborators on the whiteboard. (default: False)')
    c.add_argument('--include-direct-children', dest='p_include_direct_children', action=argparse.BooleanOptionalAction, help='Includes direct children of the whiteboard, as defined in the `ChildrenResponse` object. (default: False)')
    c.add_argument('--include-operations', dest='p_include_operations', action=argparse.BooleanOptionalAction, help='Includes operations associated with this whiteboard in the response, as defined in the `Operation` object. (default: False)')
    c.add_argument('--include-properties', dest='p_include_properties', action=argparse.BooleanOptionalAction, help='Includes content properties associated with this whiteboard in the response. (default: False)')
    c.set_defaults(handler=_run_whiteboard_get, flags={'id': '--id', 'include_collaborators': '--include-collaborators', 'include_direct_children': '--include-direct-children', 'include_operations': '--include-operations', 'include_properties': '--include-properties'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_whiteboard_by_id'})
    c = g_whiteboard_commands.add_parser('delete', parents=[common], help='Delete whiteboard', description='Delete a whiteboard by id.\n\nDeleting a whiteboard moves the whiteboard to the trash, where it can be\nrestored later\n\n**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:\nPermission to view the whiteboard and its corresponding space. Permission to\ndelete whiteboards in the space.', usage='%(prog)s ID [options]', epilog=RUNTIME.command_epilog(['codapact-confluence whiteboard delete ID --dry-run', 'codapact-confluence whiteboard delete ID --yes']), formatter_class=RAW)
    c.add_argument('p_id', metavar='ID', nargs='?', default=argparse.SUPPRESS, type=integer, help='The ID of the whiteboard to be deleted.')
    c.add_argument('--id', dest='p_id', default=argparse.SUPPRESS, type=integer, metavar='ID', help='same as ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_whiteboard_delete, flags={'id': '--id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_whiteboard'})
    RUNTIME.add_builtins(commands)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Parse arguments, run one command, and return the exit code."""
    return RUNTIME.main(
        build_parser, lambda options: Client(**options), _api_model, argv
    )
