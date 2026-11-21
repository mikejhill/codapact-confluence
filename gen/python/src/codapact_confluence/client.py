"""Client generated from the library surface. Do not edit."""

# ruff: noqa: E501
from __future__ import annotations

import builtins
from collections.abc import Mapping, Sequence
from functools import cache
from importlib.resources import files
from typing import Any, cast

from codapact.runtime import (
    AuthProvider,
    Middleware,
    RuntimeClient,
    Transport,
    load_model,
)
from codapact.runtime.arguments import UNSET, Unset, call_args

from . import types as _t

PROTOCOLS: dict[str, Any] = {}
"""Custom protocol handlers (``module:attribute``) this client registers by default."""


@cache
def _model() -> Any:
    return load_model(files(__package__).joinpath("_model.json"))


class _AdminKeyResource:
    """Operations under ``admin_key``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self) -> _t.AdminKeyResponse:
        """
        Get Admin Key

        Returns information about the admin key if one is currently enabled for the calling user within the site.

        **[Permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/#Centralized-user-management-content) required**:
        User must be an organization or site admin.
        """
        return cast('_t.AdminKeyResponse', self._runtime.call('get_admin_key', call_args({})))

    def enable(self, *, duration_in_minutes: int | Unset = UNSET) -> _t.AdminKeyResponse:
        """
        Enable Admin Key

        Enables admin key access for the calling user within the site. If an admin key already exists for the user, a new one will be issued with an updated expiration time.

        **Note:** The `durationInMinutes` field within the request body is optional. If the request body is empty or if the `durationInMinutes` is set to 0 minutes, a new admin key will be issued to the calling user with a default duration of 10 minutes.

        **[Permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/#Centralized-user-management-content) required**:
        User must be an organization or site admin.
        """
        return cast('_t.AdminKeyResponse', self._runtime.call('enable_admin_key', call_args({}, {'body': {'duration_in_minutes': duration_in_minutes}})))

    def disable(self) -> None:
        """
        Disable Admin Key

        Disables admin key access for the calling user within the site.

        **[Permissions](https://support.atlassian.com/user-management/docs/give-users-admin-permissions/#Centralized-user-management-content) required**:
        User must be an organization or site admin.
        """
        self._runtime.call('disable_admin_key', call_args({}))

class _AncestorsResource:
    """Operations under ``ancestors``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_whiteboard(self, *, id: int, limit: int | Unset = UNSET) -> _t.GetWhiteboardAncestorsResponse:
        """
        Get all ancestors of whiteboard

        Returns all ancestors for a given whiteboard by ID in top-to-bottom order (that is, the highest ancestor is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the ID of first ancestor in the response payload.

        This endpoint returns minimal information about each ancestor. To fetch more details, use a related endpoint, such
        as [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the whiteboard and its corresponding space
        """
        return cast('_t.GetWhiteboardAncestorsResponse', self._runtime.call('get_whiteboard_ancestors', call_args({'id': id, 'limit': limit})))

    def list_database(self, *, id: int, limit: int | Unset = UNSET) -> _t.GetDatabaseAncestorsResponse:
        """
        Get all ancestors of database

        Returns all ancestors for a given database by ID in top-to-bottom order (that is, the highest ancestor is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the ID of first ancestor in the response payload.

        This endpoint returns minimal information about each ancestor. To fetch more details, use a related endpoint, such
        as [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the database and its corresponding space
        """
        return cast('_t.GetDatabaseAncestorsResponse', self._runtime.call('get_database_ancestors', call_args({'id': id, 'limit': limit})))

    def list_smart_link(self, *, id: int, limit: int | Unset = UNSET) -> _t.GetSmartLinkAncestorsResponse:
        """
        Get all ancestors of Smart Link in content tree

        Returns all ancestors for a given Smart Link in the content tree by ID in top-to-bottom order (that is, the highest ancestor is
        the first item in the response payload). The number of results is limited by the `limit` parameter and additional results 
        (if available) will be available by calling this endpoint with the ID of first ancestor in the response payload.

        This endpoint returns minimal information about each ancestor. To fetch more details, use a related endpoint, such
        as [Get Smart Link in the content tree by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the Smart Link in the content tree and its corresponding space
        """
        return cast('_t.GetSmartLinkAncestorsResponse', self._runtime.call('get_smart_link_ancestors', call_args({'id': id, 'limit': limit})))

    def list_folder(self, *, id: int, limit: int | Unset = UNSET) -> _t.GetFolderAncestorsResponse:
        """
        Get all ancestors of folder

        Returns all ancestors for a given folder by ID in top-to-bottom order (that is, the highest ancestor is
        the first item in the response payload). The number of results is limited by the `limit` parameter and additional results 
        (if available) will be available by calling this endpoint with the ID of first ancestor in the response payload.

        This endpoint returns minimal information about each ancestor. To fetch more details, use a related endpoint, such
        as [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-folders-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the folder and its corresponding space
        """
        return cast('_t.GetFolderAncestorsResponse', self._runtime.call('get_folder_ancestors', call_args({'id': id, 'limit': limit})))

    def list_page(self, *, id: int, limit: int | Unset = UNSET) -> _t.GetPageAncestorsResponse:
        """
        Get all ancestors of page

        Returns all ancestors for a given page by ID in top-to-bottom order (that is, the highest ancestor is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the ID of first ancestor in the response payload.

        This endpoint returns minimal information about each ancestor. To fetch more details, use a related endpoint, such
        as [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        """
        return cast('_t.GetPageAncestorsResponse', self._runtime.call('get_page_ancestors', call_args({'id': id, 'limit': limit})))

class _AppPropertiesResource:
    """Operations under ``app_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetForgeAppPropertiesResponse:
        """
        Get Forge app properties.

        Gets Forge app properties. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
        """
        return cast('_t.GetForgeAppPropertiesResponse', self._runtime.call('get_forge_app_properties', call_args({'cursor': cursor, 'limit': limit})))

    def get(self, *, property_key: str) -> _t.GetForgeAppPropertyResponse:
        """
        Get a Forge app property by key.

        Gets a Forge app property by property key. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
        """
        return cast('_t.GetForgeAppPropertyResponse', self._runtime.call('get_forge_app_property', call_args({'property_key': property_key})))

    def put(self, *, property_key: str, body: builtins.dict[str, Any]) -> None:
        """
        Create or update a Forge app property.

        Creates or updates a Forge app property. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
        """
        self._runtime.call('put_forge_app_property', call_args({'property_key': property_key, 'body': body}))

    def delete(self, *, property_key: str) -> None:
        """
        Deletes a Forge app property.

        Deletes a Forge app property. This API can only be accessed using **[asApp()](https://developer.atlassian.com/platform/forge/apis-reference/fetch-api-product.requestconfluence/#method-signature)** requests from Forge.
        """
        self._runtime.call('delete_forge_app_property', call_args({'property_key': property_key}))

class _AttachmentResource:
    """Operations under ``attachment``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_attachments(self, *, sort: _t.AttachmentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, status: builtins.list[_t.GetAttachmentsStatusItem] | Unset = UNSET, media_type: str | Unset = UNSET, filename: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetAttachmentsResponse:
        """
        Get attachments

        Returns all attachments. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the container of the attachment.
        """
        return cast('_t.GetAttachmentsResponse', self._runtime.call('get_attachments', call_args({'sort': sort, 'cursor': cursor, 'status': status, 'media_type': media_type, 'filename': filename, 'limit': limit})))

    def get(self, *, id: str, version: int | Unset = UNSET, include_labels: bool | Unset = UNSET, include_properties: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_versions: bool | Unset = UNSET, include_version: bool | Unset = UNSET, include_collaborators: bool | Unset = UNSET) -> _t.GetAttachmentByIdResponse:
        """
        Get attachment by id

        Returns a specific attachment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment's container.
        """
        return cast('_t.GetAttachmentByIdResponse', self._runtime.call('get_attachment_by_id', call_args({'id': id, 'version': version, 'include_labels': include_labels, 'include_properties': include_properties, 'include_operations': include_operations, 'include_versions': include_versions, 'include_version': include_version, 'include_collaborators': include_collaborators})))

    def delete(self, *, id: int, purge: bool | Unset = UNSET) -> None:
        """
        Delete attachment

        Delete an attachment by id.

        Deleting an attachment moves the attachment to the trash, where it can be restored later. To permanently delete an attachment (or "purge" it),
        the endpoint must be called on a **trashed** attachment with the following param `purge=true`.

        **[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
        Permission to view the container of the attachment.
        Permission to delete attachments in the space.
        [`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

        **Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
        """
        self._runtime.call('delete_attachment', call_args({'id': id, 'purge': purge}))

    def list_blogpost_attachments(self, *, id: int, sort: _t.AttachmentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, status: builtins.list[_t.GetBlogpostAttachmentsStatusItem] | Unset = UNSET, media_type: str | Unset = UNSET, filename: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogpostAttachmentsResponse:
        """
        Get attachments for blog post

        Returns the attachments of specific blog post. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the blog post and its corresponding space.
        """
        return cast('_t.GetBlogpostAttachmentsResponse', self._runtime.call('get_blogpost_attachments', call_args({'id': id, 'sort': sort, 'cursor': cursor, 'status': status, 'media_type': media_type, 'filename': filename, 'limit': limit})))

    def list_custom_content_attachments(self, *, id: int, sort: _t.AttachmentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, status: builtins.list[_t.GetCustomContentAttachmentsStatusItem] | Unset = UNSET, media_type: str | Unset = UNSET, filename: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetCustomContentAttachmentsResponse:
        """
        Get attachments for custom content

        Returns the attachments of specific custom content. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the custom content and its corresponding space.
        """
        return cast('_t.GetCustomContentAttachmentsResponse', self._runtime.call('get_custom_content_attachments', call_args({'id': id, 'sort': sort, 'cursor': cursor, 'status': status, 'media_type': media_type, 'filename': filename, 'limit': limit})))

    def list_label_attachments(self, *, id: int, sort: _t.AttachmentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetLabelAttachmentsResponse:
        """
        Get attachments for label

        Returns the attachments of specified label. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment and its corresponding space.
        """
        return cast('_t.GetLabelAttachmentsResponse', self._runtime.call('get_label_attachments', call_args({'id': id, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_page_attachments(self, *, id: int, sort: _t.AttachmentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, status: builtins.list[_t.GetPageAttachmentsStatusItem] | Unset = UNSET, media_type: str | Unset = UNSET, filename: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPageAttachmentsResponse:
        """
        Get attachments for page

        Returns the attachments of specific page. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetPageAttachmentsResponse', self._runtime.call('get_page_attachments', call_args({'id': id, 'sort': sort, 'cursor': cursor, 'status': status, 'media_type': media_type, 'filename': filename, 'limit': limit})))

    def get_thumbnail(self, *, id: str, version: int | Unset = UNSET, height: int | Unset = UNSET, width: int | Unset = UNSET) -> None:
        """
        Download attachment thumbnail by id

        Redirects the client to a URL that serves an attachment thumbnail's binary data.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment's container.
        """
        self._runtime.call('get_attachment_thumbnail_by_id', call_args({'id': id, 'version': version, 'height': height, 'width': width}))

class _BlogPostResource:
    """Operations under ``blog_post``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_blog_posts(self, *, id: builtins.list[int] | Unset = UNSET, space_id: builtins.list[int] | Unset = UNSET, sort: _t.BlogPostSortOrder | Unset = UNSET, status: builtins.list[_t.GetBlogPostsStatusItem] | Unset = UNSET, title: str | Unset = UNSET, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogPostsResponse:
        """
        Get blog posts

        Returns all blog posts. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only blog posts that the user has permission to view will be returned.
        """
        return cast('_t.GetBlogPostsResponse', self._runtime.call('get_blog_posts', call_args({'id': id, 'space_id': space_id, 'sort': sort, 'status': status, 'title': title, 'body_format': body_format, 'cursor': cursor, 'limit': limit})))

    def create(self, *, space_id: str, private: bool | Unset = UNSET, status: _t.CreateBlogPostBodyStatus | Unset = UNSET, title: str | Unset = UNSET, body: _t.CreateBlogPostBodyBody | Unset = UNSET, created_at: str | Unset = UNSET) -> _t.CreateBlogPostResponse:
        """
        Create blog post

        Creates a new blog post in the space specified by the spaceId.

        By default this will create the blog post as a non-draft, unless the status is specified as draft.
        If creating a non-draft, the title must not be empty.

        Currently only supports the storage representation specified in the body.representation enums below
        """
        return cast('_t.CreateBlogPostResponse', self._runtime.call('create_blog_post', call_args({'private': private}, {'body': {'space_id': space_id, 'status': status, 'title': title, 'body': body, 'created_at': created_at}}, required=frozenset({'body'}))))

    def get(self, *, id: int, body_format: _t.PrimaryBodyRepresentationSingle | Unset = UNSET, get_draft: bool | Unset = UNSET, status: builtins.list[_t.GetBlogPostByIdStatusItem] | Unset = UNSET, version: int | Unset = UNSET, include_labels: bool | Unset = UNSET, include_properties: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_likes: bool | Unset = UNSET, include_versions: bool | Unset = UNSET, include_version: bool | Unset = UNSET, include_favorited_by_current_user_status: bool | Unset = UNSET, include_webresources: bool | Unset = UNSET, include_collaborators: bool | Unset = UNSET) -> _t.GetBlogPostByIdResponse:
        """
        Get blog post by id

        Returns a specific blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post and its corresponding space.
        """
        return cast('_t.GetBlogPostByIdResponse', self._runtime.call('get_blog_post_by_id', call_args({'id': id, 'body_format': body_format, 'get_draft': get_draft, 'status': status, 'version': version, 'include_labels': include_labels, 'include_properties': include_properties, 'include_operations': include_operations, 'include_likes': include_likes, 'include_versions': include_versions, 'include_version': include_version, 'include_favorited_by_current_user_status': include_favorited_by_current_user_status, 'include_webresources': include_webresources, 'include_collaborators': include_collaborators})))

    def update(self, *, id: int, body: _t.UpdateBlogPostBody) -> _t.UpdateBlogPostResponse:
        """
        Update blog post

        Update a blog post by id.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post and its corresponding space. Permission to update blog posts in the space.
        """
        return cast('_t.UpdateBlogPostResponse', self._runtime.call('update_blog_post', call_args({'id': id, 'body': body})))

    def delete(self, *, id: int, purge: bool | Unset = UNSET, draft: bool | Unset = UNSET) -> None:
        """
        Delete blog post

        Delete a blog post by id.

        By default this will delete blog posts that are non-drafts. To delete a blog post that is a draft, the endpoint must be called on a 
        draft with the following param `draft=true`. Discarded drafts are not sent to the trash and are permanently deleted.

        Deleting a blog post that is not a draft moves the blog post to the trash, where it can be restored later.
        To permanently delete a blog post (or "purge" it), the endpoint must be called on a **trashed** blog post with the following param `purge=true`.

        **[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
        Permission to view the blog post and its corresponding space.
        Permission to delete blog posts in the space.
        [`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

        **Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
        """
        self._runtime.call('delete_blog_post', call_args({'id': id, 'purge': purge, 'draft': draft}))

    def list_label_blog_posts(self, *, id: int, space_id: builtins.list[int] | Unset = UNSET, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, sort: _t.BlogPostSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetLabelBlogPostsResponse:
        """
        Get blog posts for label

        Returns the blogposts of specified label. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetLabelBlogPostsResponse', self._runtime.call('get_label_blog_posts', call_args({'id': id, 'space_id': space_id, 'body_format': body_format, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def get_blog_posts_in_space(self, *, id: int, sort: _t.BlogPostSortOrder | Unset = UNSET, status: builtins.list[_t.GetBlogPostsInSpaceStatusItem] | Unset = UNSET, title: str | Unset = UNSET, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogPostsInSpaceResponse:
        """
        Get blog posts in space

        Returns all blog posts in a space. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission) and view the space.
        Only blog posts that the user has permission to view will be returned.
        """
        return cast('_t.GetBlogPostsInSpaceResponse', self._runtime.call('get_blog_posts_in_space', call_args({'id': id, 'sort': sort, 'status': status, 'title': title, 'body_format': body_format, 'cursor': cursor, 'limit': limit})))

class _ChildrenResource:
    """Operations under ``children``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_whiteboard_direct(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: str | Unset = UNSET) -> _t.GetWhiteboardDirectChildrenResponse:
        """
        Get direct children of a whiteboard

        Returns all children for given whiteboard id in the content tree. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each child. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only content that the user has permission to view will be returned.
        """
        return cast('_t.GetWhiteboardDirectChildrenResponse', self._runtime.call('get_whiteboard_direct_children', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def get_database_direct(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: str | Unset = UNSET) -> _t.GetDatabaseDirectChildrenResponse:
        """
        Get direct children of a database

        Returns all children for given database id in the content tree. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each child. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only content that the user has permission to view will be returned.
        """
        return cast('_t.GetDatabaseDirectChildrenResponse', self._runtime.call('get_database_direct_children', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def get_smart_link_direct(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: str | Unset = UNSET) -> _t.GetSmartLinkDirectChildrenResponse:
        """
        Get direct children of a Smart Link

        Returns all children for given smart link id in the content tree. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each child. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only content that the user has permission to view will be returned.
        """
        return cast('_t.GetSmartLinkDirectChildrenResponse', self._runtime.call('get_smart_link_direct_children', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def get_folder_direct(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: str | Unset = UNSET) -> _t.GetFolderDirectChildrenResponse:
        """
        Get direct children of a folder

        Returns all children for given folder id in the content tree. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each child. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only content that the user has permission to view will be returned.
        """
        return cast('_t.GetFolderDirectChildrenResponse', self._runtime.call('get_folder_direct_children', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_child_pages(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: str | Unset = UNSET) -> _t.GetChildPagesResponse:
        """
        Get child pages

        Returns all child pages for given page id. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only pages that the user has permission to view will be returned.

        Deprecated.
        """
        return cast('_t.GetChildPagesResponse', self._runtime.call('get_child_pages', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def get_child_custom_content(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: str | Unset = UNSET) -> _t.GetChildCustomContentResponse:
        """
        Get child custom content

        Returns all child custom content for given custom content id. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only custom content that the user has permission to view will be returned.
        """
        return cast('_t.GetChildCustomContentResponse', self._runtime.call('get_child_custom_content', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def get_page_direct(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: str | Unset = UNSET) -> _t.GetPageDirectChildrenResponse:
        """
        Get direct children of a page

        Returns all children for given page id in the content tree. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each child. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only content that the user has permission to view will be returned.
        """
        return cast('_t.GetPageDirectChildrenResponse', self._runtime.call('get_page_direct_children', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

class _ClassificationLevelResource:
    """Operations under ``classification_level``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_classification_levels(self) -> builtins.list[_t.ClassificationLevel]:
        """
        Get list of classification levels

        Returns a list of [classification levels](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level) 
        available.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission).
        """
        return cast('builtins.list[_t.ClassificationLevel]', self._runtime.call('get_classification_levels', call_args({})))

    def get_space_default(self, *, id: int) -> _t.ClassificationLevel:
        """
        Get space default classification level

        Returns the [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/) 
        for a specific space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the space.
        """
        return cast('_t.ClassificationLevel', self._runtime.call('get_space_default_classification_level', call_args({'id': id})))

    def put_space_default(self, *, id: int, body: _t.PutSpaceDefaultClassificationLevelBody) -> None:
        """
        Update space default classification level

        Update the [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/) 
        for a specific space.

        **[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
        Permission to access the Confluence site ('Can use' global permission) and
        [`manage/space`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space.

        **Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
        """
        self._runtime.call('put_space_default_classification_level', call_args({'id': id, 'body': body}))

    def delete(self, *, id: int) -> None:
        """
        Delete space default classification level

        Returns the [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/) 
        for a specific space.

        **[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
        Permission to access the Confluence site ('Can use' global permission) and
        [`manage/space`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space.

        **Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
        """
        self._runtime.call('delete_space_default_classification_level', call_args({'id': id}))

    def get_page(self, *, id: int, status: _t.GetPageClassificationLevelStatus | Unset = UNSET) -> _t.ClassificationLevel:
        """
        Get page classification level

        Returns the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the page.
        'Permission to edit the page is required if trying to view classification level for a draft.
        """
        return cast('_t.ClassificationLevel', self._runtime.call('get_page_classification_level', call_args({'id': id, 'status': status})))

    def put_page(self, *, id: int, body: _t.PutPageClassificationLevelBody) -> None:
        """
        Update page classification level

        Updates the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to edit the page.
        """
        self._runtime.call('put_page_classification_level', call_args({'id': id, 'body': body}))

    def post_page(self, *, id: int, status: _t.PostPageClassificationLevelBodyStatus) -> None:
        """
        Reset page classification level

        Resets the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific page for the space 
        [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the page.
        """
        self._runtime.call('post_page_classification_level', call_args({'id': id}, {'body': {'status': status}}, required=frozenset({'body'})))

    def get_blog_post(self, *, id: int, status: _t.GetBlogPostClassificationLevelStatus | Unset = UNSET) -> _t.ClassificationLevel:
        """
        Get blog post classification level

        Returns the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the blog post.
        'Permission to edit the blog post is required if trying to view classification level for a draft.
        """
        return cast('_t.ClassificationLevel', self._runtime.call('get_blog_post_classification_level', call_args({'id': id, 'status': status})))

    def put_blog_post(self, *, id: int, body: _t.PutBlogPostClassificationLevelBody) -> None:
        """
        Update blog post classification level

        Updates the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to edit the blog post.
        """
        self._runtime.call('put_blog_post_classification_level', call_args({'id': id, 'body': body}))

    def post_blog_post(self, *, id: int, status: _t.PostBlogPostClassificationLevelBodyStatus) -> None:
        """
        Reset blog post classification level

        Resets the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific blog post for the space  
        [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the blog post.
        """
        self._runtime.call('post_blog_post_classification_level', call_args({'id': id}, {'body': {'status': status}}, required=frozenset({'body'})))

    def get_whiteboard(self, *, id: int) -> _t.ClassificationLevel:
        """
        Get whiteboard classification level

        Returns the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the whiteboard.
        """
        return cast('_t.ClassificationLevel', self._runtime.call('get_whiteboard_classification_level', call_args({'id': id})))

    def put_whiteboard(self, *, id: int, body: _t.PutWhiteboardClassificationLevelBody) -> None:
        """
        Update whiteboard classification level

        Updates the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to edit the whiteboard.
        """
        self._runtime.call('put_whiteboard_classification_level', call_args({'id': id, 'body': body}))

    def post_whiteboard(self, *, id: int, status: _t.PostWhiteboardClassificationLevelBodyStatus) -> None:
        """
        Reset whiteboard classification level

        Resets the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific whiteboard for the space 
        [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the whiteboard.
        """
        self._runtime.call('post_whiteboard_classification_level', call_args({'id': id}, {'body': {'status': status}}, required=frozenset({'body'})))

    def get_database(self, *, id: int) -> _t.ClassificationLevel:
        """
        Get database classification level

        Returns the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the database.
        """
        return cast('_t.ClassificationLevel', self._runtime.call('get_database_classification_level', call_args({'id': id})))

    def put_database(self, *, id: int, body: _t.PutDatabaseClassificationLevelBody) -> None:
        """
        Update database classification level

        Updates the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to edit the database.
        """
        self._runtime.call('put_database_classification_level', call_args({'id': id, 'body': body}))

    def post_database(self, *, id: int, status: _t.PostDatabaseClassificationLevelBodyStatus) -> None:
        """
        Reset database classification level

        Resets the [classification level](https://developer.atlassian.com/cloud/admin/dlp/rest/intro/#Classification%20level)
        for a specific database for the space 
        [default classification level](https://support.atlassian.com/security-and-access-policies/docs/what-is-a-default-classification-level/).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        'Permission to access the Confluence site ('Can use' global permission) and permission to view the database.
        """
        self._runtime.call('post_database_classification_level', call_args({'id': id}, {'body': {'status': status}}, required=frozenset({'body'})))

class _CommentResource:
    """Operations under ``comment``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_attachment_comments(self, *, id: str, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, version: int | Unset = UNSET) -> _t.GetAttachmentCommentsResponse:
        """
        Get attachment comments

        Returns the comments of the specific attachment.
        The number of results is limited by the `limit` parameter and additional results (if available) will be available through
        the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment and its corresponding containers.
        """
        return cast('_t.GetAttachmentCommentsResponse', self._runtime.call('get_attachment_comments', call_args({'id': id, 'body_format': body_format, 'cursor': cursor, 'limit': limit, 'sort': sort, 'version': version})))

    def list_custom_content_comments(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET) -> _t.GetCustomContentCommentsResponse:
        """
        Get custom content comments

        Returns the comments of the specific custom content.
        The number of results is limited by the `limit` parameter and additional results (if available) will be available through
        the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content and its corresponding containers.
        """
        return cast('_t.GetCustomContentCommentsResponse', self._runtime.call('get_custom_content_comments', call_args({'id': id, 'body_format': body_format, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_page_footer_comments(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, status: builtins.list[_t.GetPageFooterCommentsStatusItem] | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPageFooterCommentsResponse:
        """
        Get footer comments for page

        Returns the root footer comments of specific page. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetPageFooterCommentsResponse', self._runtime.call('get_page_footer_comments', call_args({'id': id, 'body_format': body_format, 'status': status, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_page_inline_comments(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, status: builtins.list[_t.GetPageInlineCommentsStatusItem] | Unset = UNSET, resolution_status: builtins.list[_t.GetPageInlineCommentsResolutionStatusItem] | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPageInlineCommentsResponse:
        """
        Get inline comments for page

        Returns the root inline comments of specific page. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetPageInlineCommentsResponse', self._runtime.call('get_page_inline_comments', call_args({'id': id, 'body_format': body_format, 'status': status, 'resolution_status': resolution_status, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_blog_post_footer_comments(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, status: builtins.list[_t.GetBlogPostFooterCommentsStatusItem] | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogPostFooterCommentsResponse:
        """
        Get footer comments for blog post

        Returns the root footer comments of specific blog post. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the blog post and its corresponding space.
        """
        return cast('_t.GetBlogPostFooterCommentsResponse', self._runtime.call('get_blog_post_footer_comments', call_args({'id': id, 'body_format': body_format, 'status': status, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_blog_post_inline_comments(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, status: builtins.list[_t.GetBlogPostInlineCommentsStatusItem] | Unset = UNSET, resolution_status: builtins.list[_t.GetBlogPostInlineCommentsResolutionStatusItem] | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogPostInlineCommentsResponse:
        """
        Get inline comments for blog post

        Returns the root inline comments of specific blog post. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the blog post and its corresponding space.
        """
        return cast('_t.GetBlogPostInlineCommentsResponse', self._runtime.call('get_blog_post_inline_comments', call_args({'id': id, 'body_format': body_format, 'status': status, 'resolution_status': resolution_status, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_footer_comments(self, *, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetFooterCommentsResponse:
        """
        Get footer comments

        Returns all footer comments. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the container and its corresponding space.
        """
        return cast('_t.GetFooterCommentsResponse', self._runtime.call('get_footer_comments', call_args({'body_format': body_format, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_footer(self, *, blog_post_id: str | Unset = UNSET, page_id: str | Unset = UNSET, parent_comment_id: str | Unset = UNSET, attachment_id: str | Unset = UNSET, custom_content_id: str | Unset = UNSET, body: _t.CreateFooterCommentModelBody | Unset = UNSET) -> _t.CreateFooterCommentResponse:
        """
        Create footer comment

        Create a footer comment.

        The footer comment can be made against several locations: 
        - at the top level (specifying pageId or blogPostId in the request body)
        - as a reply (specifying parentCommentId in the request body)
        - against an attachment (note: this is different than the comments added via the attachment properties page on the UI, which are referred to as version comments)
        - against a custom content

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.
        """
        return cast('_t.CreateFooterCommentResponse', self._runtime.call('create_footer_comment', call_args({}, {'body': {'blog_post_id': blog_post_id, 'page_id': page_id, 'parent_comment_id': parent_comment_id, 'attachment_id': attachment_id, 'custom_content_id': custom_content_id, 'body': body}})))

    def get_footer(self, *, comment_id: int, body_format: _t.PrimaryBodyRepresentationSingle | Unset = UNSET, version: int | Unset = UNSET, include_properties: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_likes: bool | Unset = UNSET, include_versions: bool | Unset = UNSET, include_version: bool | Unset = UNSET) -> _t.GetFooterCommentByIdResponse:
        """
        Get footer comment by id

        Retrieves a footer comment by id

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the container and its corresponding space.
        """
        return cast('_t.GetFooterCommentByIdResponse', self._runtime.call('get_footer_comment_by_id', call_args({'comment_id': comment_id, 'body_format': body_format, 'version': version, 'include_properties': include_properties, 'include_operations': include_operations, 'include_likes': include_likes, 'include_versions': include_versions, 'include_version': include_version})))

    def update_footer(self, *, comment_id: int, version: _t.UpdateFooterCommentModelVersion | Unset = UNSET, body: _t.UpdateFooterCommentModelBody | Unset = UNSET, links: _t.UpdateFooterCommentBodyLinks | Unset = UNSET) -> _t.FooterCommentModel:
        """
        Update footer comment

        Update a footer comment. This can be used to update the body text of a comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.
        """
        return cast('_t.FooterCommentModel', self._runtime.call('update_footer_comment', call_args({'comment_id': comment_id}, {'body': {'version': version, 'body': body, 'links': links}})))

    def delete_footer(self, *, comment_id: int) -> None:
        """
        Delete footer comment

        Deletes a footer comment. This is a permanent deletion and cannot be reverted.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to delete comments in the space.
        """
        self._runtime.call('delete_footer_comment', call_args({'comment_id': comment_id}))

    def get_footer_children(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetFooterCommentChildrenResponse:
        """
        Get children footer comments

        Returns the children footer comments of specific comment. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetFooterCommentChildrenResponse', self._runtime.call('get_footer_comment_children', call_args({'id': id, 'body_format': body_format, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_inline_comments(self, *, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetInlineCommentsResponse:
        """
        Get inline comments

        Returns all inline comments. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetInlineCommentsResponse', self._runtime.call('get_inline_comments', call_args({'body_format': body_format, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_inline(self, *, blog_post_id: str | Unset = UNSET, page_id: str | Unset = UNSET, parent_comment_id: str | Unset = UNSET, body: _t.CreateInlineCommentModelBody | Unset = UNSET, inline_comment_properties: _t.CreateInlineCommentModelInlineCommentProperties | Unset = UNSET) -> _t.CreateInlineCommentResponse:
        """
        Create inline comment

        Create an inline comment. This can be at the top level (specifying pageId or blogPostId in the request body)
        or as a reply (specifying parentCommentId in the request body). Note the inlineCommentProperties object in the
        request body is used to select the text the inline comment should be tied to. This is what determines the text 
        highlighting when viewing a page in Confluence.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.
        """
        return cast('_t.CreateInlineCommentResponse', self._runtime.call('create_inline_comment', call_args({}, {'body': {'blog_post_id': blog_post_id, 'page_id': page_id, 'parent_comment_id': parent_comment_id, 'body': body, 'inline_comment_properties': inline_comment_properties}})))

    def get_inline(self, *, comment_id: int, body_format: _t.PrimaryBodyRepresentationSingle | Unset = UNSET, version: int | Unset = UNSET, include_properties: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_likes: bool | Unset = UNSET, include_versions: bool | Unset = UNSET, include_version: bool | Unset = UNSET) -> _t.GetInlineCommentByIdResponse:
        """
        Get inline comment by id

        Retrieves an inline comment by id

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space.
        """
        return cast('_t.GetInlineCommentByIdResponse', self._runtime.call('get_inline_comment_by_id', call_args({'comment_id': comment_id, 'body_format': body_format, 'version': version, 'include_properties': include_properties, 'include_operations': include_operations, 'include_likes': include_likes, 'include_versions': include_versions, 'include_version': include_version})))

    def update_inline(self, *, comment_id: int, version: _t.UpdateInlineCommentModelVersion | Unset = UNSET, body: _t.UpdateInlineCommentModelBody | Unset = UNSET, resolved: bool | Unset = UNSET) -> _t.UpdateInlineCommentResponse:
        """
        Update inline comment

        Update an inline comment. This can be used to update the body text of a comment and/or to resolve the comment

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to create comments in the space.
        """
        return cast('_t.UpdateInlineCommentResponse', self._runtime.call('update_inline_comment', call_args({'comment_id': comment_id}, {'body': {'version': version, 'body': body, 'resolved': resolved}})))

    def delete_inline(self, *, comment_id: int) -> None:
        """
        Delete inline comment

        Deletes an inline comment. This is a permanent deletion and cannot be reverted.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to delete comments in the space.
        """
        self._runtime.call('delete_inline_comment', call_args({'comment_id': comment_id}))

    def get_inline_children(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, sort: _t.CommentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetInlineCommentChildrenResponse:
        """
        Get children inline comments

        Returns the children inline comments of specific comment. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetInlineCommentChildrenResponse', self._runtime.call('get_inline_comment_children', call_args({'id': id, 'body_format': body_format, 'sort': sort, 'cursor': cursor, 'limit': limit})))

class _ContentResource:
    """Operations under ``content``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def convert_ids_to_content_types(self, *, content_ids: builtins.list[_t.ConvertContentIdsToContentTypesBodyContentIdsItem]) -> _t.ContentIdToContentTypeResponse:
        """
        Convert content ids to content types

        Converts a list of content ids into their associated content types. This is useful for users migrating from v1 to v2
        who may have stored just content ids without their associated type. This will return types as they should be used in v2.
        Notably, this will return `inline-comment` for inline comments and `footer-comment` for footer comments, which is distinct from them
        both being represented by `comment` in v1.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the requested content. Any content that the user does not have permission to view or does not exist will map to `null` in the response.
        """
        return cast('_t.ContentIdToContentTypeResponse', self._runtime.call('convert_content_ids_to_content_types', call_args({}, {'body': {'content_ids': content_ids}}, required=frozenset({'body'}))))

class _ContentPermissionsResource:
    """Operations under ``content_permissions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_page_restriction_state(self, *, id: int) -> _t.RestrictionStateResponse:
        """
        Get page restriction state

        Returns the restriction state of a page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('get_page_restriction_state', call_args({'id': id})))

    def set_page_restriction_state(self, *, id: int, state: _t.ContentRestrictionState, allow_self_lockout: bool | Unset = UNSET) -> _t.RestrictionStateResponse:
        """
        Set page restriction state

        Sets the restriction state of a page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the page or administer the space.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('set_page_restriction_state', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'state': state}}, required=frozenset({'body'}))))

    def get_blog_post_restriction_state(self, *, id: int) -> _t.RestrictionStateResponse:
        """
        Get blog post restriction state

        Returns the restriction state of a blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('get_blog_post_restriction_state', call_args({'id': id})))

    def set_blog_post_restriction_state(self, *, id: int, state: _t.ContentRestrictionState, allow_self_lockout: bool | Unset = UNSET) -> _t.RestrictionStateResponse:
        """
        Set blog post restriction state

        Sets the restriction state of a blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the blog post or administer the space.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('set_blog_post_restriction_state', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'state': state}}, required=frozenset({'body'}))))

    def get_database_restriction_state(self, *, id: int) -> _t.RestrictionStateResponse:
        """
        Get database restriction state

        Returns the restriction state of a database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('get_database_restriction_state', call_args({'id': id})))

    def set_database_restriction_state(self, *, id: int, state: _t.ContentRestrictionState, allow_self_lockout: bool | Unset = UNSET) -> _t.RestrictionStateResponse:
        """
        Set database restriction state

        Sets the restriction state of a database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the database or administer the space.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('set_database_restriction_state', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'state': state}}, required=frozenset({'body'}))))

    def get_whiteboard_restriction_state(self, *, id: int) -> _t.RestrictionStateResponse:
        """
        Get whiteboard restriction state

        Returns the restriction state of a whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the whiteboard.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('get_whiteboard_restriction_state', call_args({'id': id})))

    def set_whiteboard_restriction_state(self, *, id: int, state: _t.ContentRestrictionState, allow_self_lockout: bool | Unset = UNSET) -> _t.RestrictionStateResponse:
        """
        Set whiteboard restriction state

        Sets the restriction state of a whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the whiteboard or administer the space.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('set_whiteboard_restriction_state', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'state': state}}, required=frozenset({'body'}))))

    def get_folder_restriction_state(self, *, id: int) -> _t.RestrictionStateResponse:
        """
        Get folder restriction state

        Returns the restriction state of a folder.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the folder.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('get_folder_restriction_state', call_args({'id': id})))

    def set_folder_restriction_state(self, *, id: int, state: _t.ContentRestrictionState, allow_self_lockout: bool | Unset = UNSET) -> _t.RestrictionStateResponse:
        """
        Set folder restriction state

        Sets the restriction state of a folder.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the folder or administer the space.
        """
        return cast('_t.RestrictionStateResponse', self._runtime.call('set_folder_restriction_state', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'state': state}}, required=frozenset({'body'}))))

    def list_page_permissions(self, *, id: int, operation: _t.GetPagePermissionsOperation | Unset = UNSET, principal_type: _t.GetPagePermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPagePermissionsResponse:
        """
        Get page permissions

        Returns the direct content permissions on a page with optional filtering by operation, principal-type, and principal-id.
        Results are cursor-paginated (max 250 per page).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page.
        """
        return cast('_t.GetPagePermissionsResponse', self._runtime.call('get_page_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'cursor': cursor, 'limit': limit})))

    def set_page_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Set page permissions

        Replaces all direct content permissions on a page with the provided set. Any permissions not included in the request body are removed.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the page or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('set_page_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def add_page_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Add page permissions

        Adds or replaces direct content permissions for the specified principals on a page. Permissions for other principals are preserved; use `PUT` to replace all permissions at once.

        A principal can hold only one `read` or `update` permission. Adding `read` for a principal that currently has `update` downgrades that principal to `read`; adding `update` upgrades them. If the same request contains both operations for a principal, `update` takes precedence.

        Reasserting a principal's existing permission is idempotent and returns a successful response without creating a duplicate entry.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the page or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('add_page_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def delete_page_permissions(self, *, id: int, operation: _t.DeletePagePermissionsOperation | Unset = UNSET, principal_type: _t.DeletePagePermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, allow_self_lockout: bool | Unset = UNSET) -> None:
        """
        Delete page permissions

        Deletes direct content permissions from a page. Filters narrow the deletion scope; omitting all filters deletes all direct permissions.

        The following filter combinations are supported:
        - No filters: deletes all direct permissions.
        - `principal-type` + `principal-id`: deletes the principal's direct `read` or `update` permission.
        - `operation` + `principal-type` + `principal-id`: deletes the permission only when its operation matches.

        Providing `operation` without `principal-type`/`principal-id`, or providing only one of `principal-type`/`principal-id`, returns a 400 error.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the page or administer the space.
        """
        self._runtime.call('delete_page_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'allow_self_lockout': allow_self_lockout}))

    def list_blog_post_permissions(self, *, id: int, operation: _t.GetBlogPostPermissionsOperation | Unset = UNSET, principal_type: _t.GetBlogPostPermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogPostPermissionsResponse:
        """
        Get blog post permissions

        Returns the direct content permissions on a blog post with optional filtering by operation, principal-type, and principal-id.
        Results are cursor-paginated (max 250 per page).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post.
        """
        return cast('_t.GetBlogPostPermissionsResponse', self._runtime.call('get_blog_post_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'cursor': cursor, 'limit': limit})))

    def set_blog_post_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Set blog post permissions

        Replaces all direct content permissions on a blog post with the provided set. Any permissions not included in the request body are removed.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the blog post or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('set_blog_post_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def add_blog_post_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Add blog post permissions

        Adds or replaces direct content permissions for the specified principals on a blog post. Permissions for other principals are preserved; use `PUT` to replace all permissions at once.

        A principal can hold only one `read` or `update` permission. Adding `read` for a principal that currently has `update` downgrades that principal to `read`; adding `update` upgrades them. If the same request contains both operations for a principal, `update` takes precedence.

        Reasserting a principal's existing permission is idempotent and returns a successful response without creating a duplicate entry.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the blog post or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('add_blog_post_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def delete_blog_post_permissions(self, *, id: int, operation: _t.DeleteBlogPostPermissionsOperation | Unset = UNSET, principal_type: _t.DeleteBlogPostPermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, allow_self_lockout: bool | Unset = UNSET) -> None:
        """
        Delete blog post permissions

        Deletes direct content permissions from a blog post. See `DELETE /pages/{id}/permissions` for filter semantics.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the blog post or administer the space.
        """
        self._runtime.call('delete_blog_post_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'allow_self_lockout': allow_self_lockout}))

    def list_database_permissions(self, *, id: int, operation: _t.GetDatabasePermissionsOperation | Unset = UNSET, principal_type: _t.GetDatabasePermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetDatabasePermissionsResponse:
        """
        Get database permissions

        Returns the direct content permissions on a database with optional filtering.
        Results are cursor-paginated (max 250 per page).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database.
        """
        return cast('_t.GetDatabasePermissionsResponse', self._runtime.call('get_database_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'cursor': cursor, 'limit': limit})))

    def set_database_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Set database permissions

        Replaces all direct content permissions on a database with the provided set.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the database or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('set_database_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def add_database_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Add database permissions

        Adds or replaces direct content permissions for the specified principals on a database. Permissions for other principals are preserved; use `PUT` to replace all permissions at once.

        A principal can hold only one `read` or `update` permission. Adding `read` for a principal that currently has `update` downgrades that principal to `read`; adding `update` upgrades them. If the same request contains both operations for a principal, `update` takes precedence.

        Reasserting a principal's existing permission is idempotent and returns a successful response without creating a duplicate entry.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the database or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('add_database_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def delete_database_permissions(self, *, id: int, operation: _t.DeleteDatabasePermissionsOperation | Unset = UNSET, principal_type: _t.DeleteDatabasePermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, allow_self_lockout: bool | Unset = UNSET) -> None:
        """
        Delete database permissions

        Deletes direct content permissions from a database. See `DELETE /pages/{id}/permissions` for filter semantics.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the database or administer the space.
        """
        self._runtime.call('delete_database_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'allow_self_lockout': allow_self_lockout}))

    def list_whiteboard_permissions(self, *, id: int, operation: _t.GetWhiteboardPermissionsOperation | Unset = UNSET, principal_type: _t.GetWhiteboardPermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetWhiteboardPermissionsResponse:
        """
        Get whiteboard permissions

        Returns the direct content permissions on a whiteboard with optional filtering.
        Results are cursor-paginated (max 250 per page).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the whiteboard.
        """
        return cast('_t.GetWhiteboardPermissionsResponse', self._runtime.call('get_whiteboard_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'cursor': cursor, 'limit': limit})))

    def set_whiteboard_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Set whiteboard permissions

        Replaces all direct content permissions on a whiteboard with the provided set.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the whiteboard or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('set_whiteboard_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def add_whiteboard_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Add whiteboard permissions

        Adds or replaces direct content permissions for the specified principals on a whiteboard. Permissions for other principals are preserved; use `PUT` to replace all permissions at once.

        A principal can hold only one `read` or `update` permission. Adding `read` for a principal that currently has `update` downgrades that principal to `read`; adding `update` upgrades them. If the same request contains both operations for a principal, `update` takes precedence.

        Reasserting a principal's existing permission is idempotent and returns a successful response without creating a duplicate entry.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the whiteboard or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('add_whiteboard_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def delete_whiteboard_permissions(self, *, id: int, operation: _t.DeleteWhiteboardPermissionsOperation | Unset = UNSET, principal_type: _t.DeleteWhiteboardPermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, allow_self_lockout: bool | Unset = UNSET) -> None:
        """
        Delete whiteboard permissions

        Deletes direct content permissions from a whiteboard. See `DELETE /pages/{id}/permissions` for filter semantics.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the whiteboard or administer the space.
        """
        self._runtime.call('delete_whiteboard_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'allow_self_lockout': allow_self_lockout}))

    def list_folder_permissions(self, *, id: int, operation: _t.GetFolderPermissionsOperation | Unset = UNSET, principal_type: _t.GetFolderPermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetFolderPermissionsResponse:
        """
        Get folder permissions

        Returns the direct content permissions on a folder with optional filtering.
        Results are cursor-paginated (max 250 per page).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the folder.
        """
        return cast('_t.GetFolderPermissionsResponse', self._runtime.call('get_folder_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'cursor': cursor, 'limit': limit})))

    def set_folder_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Set folder permissions

        Replaces all direct content permissions on a folder with the provided set.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the folder or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('set_folder_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def add_folder_permissions(self, *, id: int, permissions: builtins.list[_t.OperationPermissionsInput], allow_self_lockout: bool | Unset = UNSET) -> _t.ContentPermissionsResponse:
        """
        Add folder permissions

        Adds or replaces direct content permissions for the specified principals on a folder. Permissions for other principals are preserved; use `PUT` to replace all permissions at once.

        A principal can hold only one `read` or `update` permission. Adding `read` for a principal that currently has `update` downgrades that principal to `read`; adding `update` upgrades them. If the same request contains both operations for a principal, `update` takes precedence.

        Reasserting a principal's existing permission is idempotent and returns a successful response without creating a duplicate entry.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the folder or administer the space.
        """
        return cast('_t.ContentPermissionsResponse', self._runtime.call('add_folder_permissions', call_args({'id': id, 'allow_self_lockout': allow_self_lockout}, {'body': {'permissions': permissions}}, required=frozenset({'body'}))))

    def delete_folder_permissions(self, *, id: int, operation: _t.DeleteFolderPermissionsOperation | Unset = UNSET, principal_type: _t.DeleteFolderPermissionsPrincipalType | Unset = UNSET, principal_id: str | Unset = UNSET, allow_self_lockout: bool | Unset = UNSET) -> None:
        """
        Delete folder permissions

        Deletes direct content permissions from a folder. See `DELETE /pages/{id}/permissions` for filter semantics.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the folder or administer the space.
        """
        self._runtime.call('delete_folder_permissions', call_args({'id': id, 'operation': operation, 'principal_type': principal_type, 'principal_id': principal_id, 'allow_self_lockout': allow_self_lockout}))

class _ContentPropertiesResource:
    """Operations under ``content_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_attachment(self, *, attachment_id: str, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetAttachmentContentPropertiesResponse:
        """
        Get content properties for attachment

        Retrieves all Content Properties tied to a specified attachment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment.
        """
        return cast('_t.GetAttachmentContentPropertiesResponse', self._runtime.call('get_attachment_content_properties', call_args({'attachment_id': attachment_id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_attachment_property(self, *, attachment_id: str, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for attachment

        Creates a new content property for an attachment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the attachment.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_attachment_property', call_args({'attachment_id': attachment_id}, {'body': {'key': key, 'value': value}})))

    def get_attachment_by_id(self, *, attachment_id: str, property_id: int) -> _t.ContentProperty:
        """
        Get content property for attachment by id

        Retrieves a specific Content Property by ID that is attached to a specified attachment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_attachment_content_properties_by_id', call_args({'attachment_id': attachment_id, 'property_id': property_id})))

    def update_attachment_property(self, *, attachment_id: str, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for attachment by id

        Update a content property for attachment by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the attachment.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_attachment_property_by_id', call_args({'attachment_id': attachment_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_attachment_property(self, *, attachment_id: str, property_id: int) -> None:
        """
        Delete content property for attachment by id

        Deletes a content property for an attachment by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to attachment the page.
        """
        self._runtime.call('delete_attachment_property_by_id', call_args({'attachment_id': attachment_id, 'property_id': property_id}))

    def list_blogpost(self, *, blogpost_id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogpostContentPropertiesResponse:
        """
        Get content properties for blog post

        Retrieves all Content Properties tied to a specified blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post.
        """
        return cast('_t.GetBlogpostContentPropertiesResponse', self._runtime.call('get_blogpost_content_properties', call_args({'blogpost_id': blogpost_id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_blogpost_property(self, *, blogpost_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for blog post

        Creates a new property for a blogpost.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the blog post.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_blogpost_property', call_args({'blogpost_id': blogpost_id}, {'body': {'key': key, 'value': value}})))

    def get_blogpost_by_id(self, *, blogpost_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for blog post by id

        Retrieves a specific Content Property by ID that is attached to a specified blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_blogpost_content_properties_by_id', call_args({'blogpost_id': blogpost_id, 'property_id': property_id})))

    def update_blogpost_property(self, *, blogpost_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for blog post by id

        Update a content property for blog post by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the blog post.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_blogpost_property_by_id', call_args({'blogpost_id': blogpost_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_blogpost_property(self, *, blogpost_id: int, property_id: int) -> None:
        """
        Delete content property for blogpost by id

        Deletes a content property for a blogpost by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the blog post.
        """
        self._runtime.call('delete_blogpost_property_by_id', call_args({'blogpost_id': blogpost_id, 'property_id': property_id}))

    def list_custom_content(self, *, custom_content_id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetCustomContentContentPropertiesResponse:
        """
        Get content properties for custom content

        Retrieves Content Properties tied to a specified custom content.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content.
        """
        return cast('_t.GetCustomContentContentPropertiesResponse', self._runtime.call('get_custom_content_content_properties', call_args({'custom_content_id': custom_content_id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create(self, *, custom_content_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for custom content

        Creates a new content property for a piece of custom content.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the custom content.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_custom_content_property', call_args({'custom_content_id': custom_content_id}, {'body': {'key': key, 'value': value}})))

    def get_custom_content_by_id(self, *, custom_content_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for custom content by id

        Retrieves a specific Content Property by ID that is attached to a specified custom content.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_custom_content_content_properties_by_id', call_args({'custom_content_id': custom_content_id, 'property_id': property_id})))

    def update(self, *, custom_content_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for custom content by id

        Update a content property for a piece of custom content by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the custom content.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_custom_content_property_by_id', call_args({'custom_content_id': custom_content_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete(self, *, custom_content_id: int, property_id: int) -> None:
        """
        Delete content property for custom content by id

        Deletes a content property for a piece of custom content by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the custom content.
        """
        self._runtime.call('delete_custom_content_property_by_id', call_args({'custom_content_id': custom_content_id, 'property_id': property_id}))

    def list_page(self, *, page_id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPageContentPropertiesResponse:
        """
        Get content properties for page

        Retrieves Content Properties tied to a specified page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page.
        """
        return cast('_t.GetPageContentPropertiesResponse', self._runtime.call('get_page_content_properties', call_args({'page_id': page_id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_page_property(self, *, page_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for page

        Creates a new content property for a page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the page.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_page_property', call_args({'page_id': page_id}, {'body': {'key': key, 'value': value}})))

    def get_page_by_id(self, *, page_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for page by id

        Retrieves a specific Content Property by ID that is attached to a specified page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_page_content_properties_by_id', call_args({'page_id': page_id, 'property_id': property_id})))

    def update_page_property(self, *, page_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for page by id

        Update a content property for a page by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the page.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_page_property_by_id', call_args({'page_id': page_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_page_property(self, *, page_id: int, property_id: int) -> None:
        """
        Delete content property for page by id

        Deletes a content property for a page by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the page.
        """
        self._runtime.call('delete_page_property_by_id', call_args({'page_id': page_id, 'property_id': property_id}))

    def list_whiteboard(self, *, id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetWhiteboardContentPropertiesResponse:
        """
        Get content properties for whiteboard

        Retrieves Content Properties tied to a specified whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the whiteboard.
        """
        return cast('_t.GetWhiteboardContentPropertiesResponse', self._runtime.call('get_whiteboard_content_properties', call_args({'id': id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_whiteboard_property(self, *, id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for whiteboard

        Creates a new content property for a whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the whiteboard.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_whiteboard_property', call_args({'id': id}, {'body': {'key': key, 'value': value}})))

    def get_whiteboard_by_id(self, *, whiteboard_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for whiteboard by id

        Retrieves a specific Content Property by ID that is attached to a specified whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the whiteboard.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_whiteboard_content_properties_by_id', call_args({'whiteboard_id': whiteboard_id, 'property_id': property_id})))

    def update_whiteboard_property(self, *, whiteboard_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for whiteboard by id

        Update a content property for a whiteboard by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the whiteboard.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_whiteboard_property_by_id', call_args({'whiteboard_id': whiteboard_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_whiteboard_property(self, *, whiteboard_id: int, property_id: int) -> None:
        """
        Delete content property for whiteboard by id

        Deletes a content property for a whiteboard by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the whiteboard.
        """
        self._runtime.call('delete_whiteboard_property_by_id', call_args({'whiteboard_id': whiteboard_id, 'property_id': property_id}))

    def list_database(self, *, id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetDatabaseContentPropertiesResponse:
        """
        Get content properties for database

        Retrieves Content Properties tied to a specified database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database.
        """
        return cast('_t.GetDatabaseContentPropertiesResponse', self._runtime.call('get_database_content_properties', call_args({'id': id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_database_property(self, *, id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for database

        Creates a new content property for a database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the database.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_database_property', call_args({'id': id}, {'body': {'key': key, 'value': value}})))

    def get_database_by_id(self, *, database_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for database by id

        Retrieves a specific Content Property by ID that is attached to a specified database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_database_content_properties_by_id', call_args({'database_id': database_id, 'property_id': property_id})))

    def update_database_property(self, *, database_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for database by id

        Update a content property for a database by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the database.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_database_property_by_id', call_args({'database_id': database_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_database_property(self, *, database_id: int, property_id: int) -> None:
        """
        Delete content property for database by id

        Deletes a content property for a database by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the database.
        """
        self._runtime.call('delete_database_property_by_id', call_args({'database_id': database_id, 'property_id': property_id}))

    def list_smart_link(self, *, id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetSmartLinkContentPropertiesResponse:
        """
        Get content properties for Smart Link in the content tree

        Retrieves Content Properties tied to a specified Smart Link in the content tree.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the Smart Link in the content tree.
        """
        return cast('_t.GetSmartLinkContentPropertiesResponse', self._runtime.call('get_smart_link_content_properties', call_args({'id': id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_smart_link_property(self, *, id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for Smart Link in the content tree

        Creates a new content property for a Smart Link in the content tree.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the Smart Link in the content tree.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_smart_link_property', call_args({'id': id}, {'body': {'key': key, 'value': value}})))

    def get_smart_link_by_id(self, *, embed_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for Smart Link in the content tree by id

        Retrieves a specific Content Property by ID that is attached to a specified Smart Link in the content tree.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the Smart Link in the content tree.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_smart_link_content_properties_by_id', call_args({'embed_id': embed_id, 'property_id': property_id})))

    def update_smart_link_property(self, *, embed_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for Smart Link in the content tree by id

        Update a content property for a Smart Link in the content tree by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the Smart Link in the content tree.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_smart_link_property_by_id', call_args({'embed_id': embed_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_smart_link_property(self, *, embed_id: int, property_id: int) -> None:
        """
        Delete content property for Smart Link in the content tree by id

        Deletes a content property for a Smart Link in the content tree by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the Smart Link in the content tree.
        """
        self._runtime.call('delete_smart_link_property_by_id', call_args({'embed_id': embed_id, 'property_id': property_id}))

    def list_folder(self, *, id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetFolderContentPropertiesResponse:
        """
        Get content properties for folder

        Retrieves Content Properties tied to a specified folder.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the folder.
        """
        return cast('_t.GetFolderContentPropertiesResponse', self._runtime.call('get_folder_content_properties', call_args({'id': id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_folder_property(self, *, id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for folder

        Creates a new content property for a folder.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the folder.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_folder_property', call_args({'id': id}, {'body': {'key': key, 'value': value}})))

    def get_folder_by_id(self, *, folder_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for folder by id

        Retrieves a specific Content Property by ID that is attached to a specified folder.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the folder.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_folder_content_properties_by_id', call_args({'folder_id': folder_id, 'property_id': property_id})))

    def update_folder_property(self, *, folder_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for folder by id

        Update a content property for a folder by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the folder.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_folder_property_by_id', call_args({'folder_id': folder_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_folder_property(self, *, folder_id: int, property_id: int) -> None:
        """
        Delete content property for folder by id

        Deletes a content property for a folder by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the folder.
        """
        self._runtime.call('delete_folder_property_by_id', call_args({'folder_id': folder_id, 'property_id': property_id}))

    def list_comment(self, *, comment_id: int, key: str | Unset = UNSET, sort: _t.ContentPropertySortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetCommentContentPropertiesResponse:
        """
        Get content properties for comment

        Retrieves Content Properties attached to a specified comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the comment.
        """
        return cast('_t.GetCommentContentPropertiesResponse', self._runtime.call('get_comment_content_properties', call_args({'comment_id': comment_id, 'key': key, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def create_comment_property(self, *, comment_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.ContentProperty:
        """
        Create content property for comment

        Creates a new content property for a comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to update the comment.
        """
        return cast('_t.ContentProperty', self._runtime.call('create_comment_property', call_args({'comment_id': comment_id}, {'body': {'key': key, 'value': value}})))

    def get_comment_by_id(self, *, comment_id: int, property_id: int) -> _t.ContentProperty:
        """
        Get content property for comment by id

        Retrieves a specific Content Property by ID that is attached to a specified comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the comment.
        """
        return cast('_t.ContentProperty', self._runtime.call('get_comment_content_properties_by_id', call_args({'comment_id': comment_id, 'property_id': property_id})))

    def update_comment_property(self, *, comment_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.ContentPropertyUpdateRequestVersion | Unset = UNSET) -> _t.ContentProperty:
        """
        Update content property for comment by id

        Update a content property for a comment by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the comment.
        """
        return cast('_t.ContentProperty', self._runtime.call('update_comment_property_by_id', call_args({'comment_id': comment_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete_comment_property(self, *, comment_id: int, property_id: int) -> None:
        """
        Delete content property for comment by id

        Deletes a content property for a comment by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the comment.
        """
        self._runtime.call('delete_comment_property_by_id', call_args({'comment_id': comment_id, 'property_id': property_id}))

class _CustomContentResource:
    """Operations under ``custom_content``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_by_type_in_blog_post(self, *, id: int, type_: str, sort: _t.CustomContentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, body_format: _t.CustomContentBodyRepresentation | Unset = UNSET) -> _t.GetCustomContentByTypeInBlogPostResponse:
        """
        Get custom content by type in blog post

        Returns all custom content for a given type within a given blogpost. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content, the container of the custom content (blog post), and the corresponding space.
        """
        return cast('_t.GetCustomContentByTypeInBlogPostResponse', self._runtime.call('get_custom_content_by_type_in_blog_post', call_args({'id': id, 'type': type_, 'sort': sort, 'cursor': cursor, 'limit': limit, 'body_format': body_format})))

    def get_by_type(self, *, type_: str, id: builtins.list[int] | Unset = UNSET, space_id: builtins.list[int] | Unset = UNSET, sort: _t.CustomContentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, body_format: _t.CustomContentBodyRepresentation | Unset = UNSET) -> _t.GetCustomContentByTypeResponse:
        """
        Get custom content by type

        Returns all custom content for a given type. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content, the container of the custom content, and the corresponding space (if different from the container).
        """
        return cast('_t.GetCustomContentByTypeResponse', self._runtime.call('get_custom_content_by_type', call_args({'type': type_, 'id': id, 'space_id': space_id, 'sort': sort, 'cursor': cursor, 'limit': limit, 'body_format': body_format})))

    def create(self, *, type_: str, title: str, body: _t.CreateCustomContentBodyBody, status: _t.CreateCustomContentBodyStatus | Unset = UNSET, space_id: str | Unset = UNSET, page_id: str | Unset = UNSET, blog_post_id: str | Unset = UNSET, custom_content_id: str | Unset = UNSET) -> _t.CreateCustomContentResponse:
        """
        Create custom content

        Creates a new custom content in the given space, page, blogpost or other custom content.

        Only one of `spaceId`, `pageId`, `blogPostId`, or `customContentId` is required in the request body.
        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to create custom content in the space.
        """
        return cast('_t.CreateCustomContentResponse', self._runtime.call('create_custom_content', call_args({}, {'body': {'type': type_, 'status': status, 'space_id': space_id, 'page_id': page_id, 'blog_post_id': blog_post_id, 'custom_content_id': custom_content_id, 'title': title, 'body': body}}, required=frozenset({'body'}))))

    def get(self, *, id: int, body_format: _t.CustomContentBodyRepresentationSingle | Unset = UNSET, version: int | Unset = UNSET, include_labels: bool | Unset = UNSET, include_properties: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_versions: bool | Unset = UNSET, include_version: bool | Unset = UNSET, include_collaborators: bool | Unset = UNSET) -> _t.GetCustomContentByIdResponse:
        """
        Get custom content by id

        Returns a specific piece of custom content. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content, the container of the custom content, and the corresponding space (if different from the container).
        """
        return cast('_t.GetCustomContentByIdResponse', self._runtime.call('get_custom_content_by_id', call_args({'id': id, 'body_format': body_format, 'version': version, 'include_labels': include_labels, 'include_properties': include_properties, 'include_operations': include_operations, 'include_versions': include_versions, 'include_version': include_version, 'include_collaborators': include_collaborators})))

    def update(self, *, id: int, body: _t.UpdateCustomContentBody) -> _t.UpdateCustomContentResponse:
        """
        Update custom content

        Update a custom content by id.
        At most one of `spaceId`, `pageId`, `blogPostId`, or `customContentId` is allowed in the request body.
        Note that if `spaceId` is specified, it must be the same as the `spaceId` used for creating the custom content
        as moving custom content to a different space is not supported.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blogpost and its corresponding space. Permission to update custom content in the space.
        """
        return cast('_t.UpdateCustomContentResponse', self._runtime.call('update_custom_content', call_args({'id': id, 'body': body})))

    def delete(self, *, id: int, purge: bool | Unset = UNSET) -> None:
        """
        Delete custom content

        Delete a custom content by id.

        Deleting a custom content will either move it to the trash or permanently delete it (purge it), depending on the apiSupport.
        To permanently delete a **trashed** custom content, the endpoint must be called with the following param `purge=true`.

        **[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
        Permission to view the content of the page or blogpost and its corresponding space.
        Permission to delete custom content in the space.
        [`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

        **Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
        """
        self._runtime.call('delete_custom_content', call_args({'id': id, 'purge': purge}))

    def get_by_type_in_page(self, *, id: int, type_: str, sort: _t.CustomContentSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, body_format: _t.CustomContentBodyRepresentation | Unset = UNSET) -> _t.GetCustomContentByTypeInPageResponse:
        """
        Get custom content by type in page

        Returns all custom content for a given type within a given page. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content, the container of the custom content (page), and the corresponding space.
        """
        return cast('_t.GetCustomContentByTypeInPageResponse', self._runtime.call('get_custom_content_by_type_in_page', call_args({'id': id, 'type': type_, 'sort': sort, 'cursor': cursor, 'limit': limit, 'body_format': body_format})))

    def get_by_type_in_space(self, *, id: int, type_: str, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, body_format: _t.CustomContentBodyRepresentation | Unset = UNSET) -> _t.GetCustomContentByTypeInSpaceResponse:
        """
        Get custom content by type in space

        Returns all custom content for a given type within a given space. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content and the corresponding space.
        """
        return cast('_t.GetCustomContentByTypeInSpaceResponse', self._runtime.call('get_custom_content_by_type_in_space', call_args({'id': id, 'type': type_, 'cursor': cursor, 'limit': limit, 'body_format': body_format})))

class _DataPoliciesResource:
    """Operations under ``data_policies``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_metadata(self) -> _t.DataPolicyMetadata:
        """
        Get data policy metadata for the workspace

        Returns data policy metadata for the workspace.

        **[Permissions](#permissions) required:**
        Only apps can make this request.
        Permission to access the Confluence site ('Can use' global permission).
        """
        return cast('_t.DataPolicyMetadata', self._runtime.call('get_data_policy_metadata', call_args({})))

    def list_spaces(self, *, ids: builtins.list[int] | Unset = UNSET, keys: builtins.list[str] | Unset = UNSET, sort: _t.SpaceSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetDataPolicySpacesResponse:
        """
        Get spaces with data policies

        Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the `limit` parameter and
        additional results (if available) will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Only apps can make this request.
        Permission to access the Confluence site ('Can use' global permission).
        Only spaces that the app has permission to view will be returned.
        """
        return cast('_t.GetDataPolicySpacesResponse', self._runtime.call('get_data_policy_spaces', call_args({'ids': ids, 'keys': keys, 'sort': sort, 'cursor': cursor, 'limit': limit})))

class _DatabaseResource:
    """Operations under ``database``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create(self, *, space_id: str, private: bool | Unset = UNSET, title: str | Unset = UNSET, parent_id: str | Unset = UNSET) -> _t.CreateDatabaseResponse:
        """
        Create database

        Creates a database in the space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the corresponding space. Permission to create a database in the space.
        """
        return cast('_t.CreateDatabaseResponse', self._runtime.call('create_database', call_args({'private': private}, {'body': {'space_id': space_id, 'title': title, 'parent_id': parent_id}}, required=frozenset({'body'}))))

    def get(self, *, id: int, include_collaborators: bool | Unset = UNSET, include_direct_children: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_properties: bool | Unset = UNSET) -> _t.GetDatabaseByIdResponse:
        """
        Get database by id

        Returns a specific database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database and its corresponding space.
        """
        return cast('_t.GetDatabaseByIdResponse', self._runtime.call('get_database_by_id', call_args({'id': id, 'include_collaborators': include_collaborators, 'include_direct_children': include_direct_children, 'include_operations': include_operations, 'include_properties': include_properties})))

    def delete(self, *, id: int) -> None:
        """
        Delete database

        Delete a database by id.

        Deleting a database moves the database to the trash, where it can be restored later

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database and its corresponding space.
        Permission to delete databases in the space.
        """
        self._runtime.call('delete_database', call_args({'id': id}))

    def list_fields(self, *, id: str, limit: int | Unset = UNSET, cursor: str | Unset = UNSET, if_none_match: str | Unset = UNSET) -> _t.DatabaseFieldListResponse:
        """
        Get fields for database

        Returns the field definitions (schema) for a database, ordered by the
        user-defined column order, using cursor-based pagination.

        > **Consistency:** Responses may not immediately reflect recent changes.
        Clients requiring read-after-write confirmation should poll with bounded backoff.

        > **Experimental:** This operation is experimental and may change in backwards-incompatible ways without notice.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database and its corresponding space.
        """
        return cast('_t.DatabaseFieldListResponse', self._runtime.call('get_database_fields', call_args({'id': id, 'limit': limit, 'cursor': cursor, 'if_none_match': if_none_match})))

    def list_views(self, *, id: str, limit: int | Unset = UNSET, cursor: str | Unset = UNSET, if_none_match: str | Unset = UNSET) -> _t.DatabaseViewListResponse:
        """
        Get views for database

        Returns the views defined on a database using cursor-based pagination.
        Only view IDs, names, and types are returned; view configuration is not exposed.

        > **Consistency:** Responses may not immediately reflect recent changes.
        Clients requiring read-after-write confirmation should poll with bounded backoff.

        > **Experimental:** This operation is experimental and may change in backwards-incompatible ways without notice.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database and its corresponding space.
        """
        return cast('_t.DatabaseViewListResponse', self._runtime.call('get_database_views', call_args({'id': id, 'limit': limit, 'cursor': cursor, 'if_none_match': if_none_match})))

    def list_entries(self, *, id: str, limit: int | Unset = UNSET, cursor: str | Unset = UNSET, if_none_match: str | Unset = UNSET, sort: str | Unset = UNSET, filter: builtins.dict[str, Any] | Unset = UNSET) -> _t.DatabaseEntryListResponse:
        """
        Get entries for database

        Returns the entries (rows) of a database, with optional filtering, sorting,
        and cursor-based pagination. Entry values are keyed by field ID; use
        Get fields for database (`GET /databases/{id}/fields`) to map field IDs to
        names.

        Filtering is expressed with bracket-scoped query parameters keyed on field
        ID. The exact operators vary by field type and are documented on the
        `filter` parameter. Multiple filters are combined with AND. Unsupported
        operators and non-filterable fields return distinct structured `400`
        responses.

        Pagination uses opaque, offset-based continuation tokens and is best effort
        while a database is changing. Concurrent inserts, deletes, or changes to a
        sort value can cause duplicate or omitted rows across pages. Restart from
        the first page when a consistent export is required.

        Results are based on the database, not a particular view. A view's filters,
        sorting, grouping, and field visibility do not affect the response.

        > **Consistency:** Responses may not immediately reflect recent changes.
        Clients requiring read-after-write confirmation should poll with bounded backoff.

        > **Experimental:** This operation is experimental and may change in backwards-incompatible ways without notice.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database and its corresponding space.
        """
        return cast('_t.DatabaseEntryListResponse', self._runtime.call('get_database_entries', call_args({'id': id, 'limit': limit, 'cursor': cursor, 'if_none_match': if_none_match, 'sort': sort, 'filter': filter})))

    def get_entry(self, *, id: str, entry_id: str, if_none_match: str | Unset = UNSET) -> _t.DatabaseEntrySingleResponse:
        """
        Get entry by id

        Returns a single entry (row) from a database by ID.

        > **Consistency:** Responses may not immediately reflect recent changes.
        Clients requiring read-after-write confirmation should poll with bounded backoff.

        > **Experimental:** This operation is experimental and may change in backwards-incompatible ways without notice.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database and its corresponding space.
        """
        return cast('_t.DatabaseEntrySingleResponse', self._runtime.call('get_database_entry_by_id', call_args({'id': id, 'entry_id': entry_id, 'if_none_match': if_none_match})))

class _DescendantsResource:
    """Operations under ``descendants``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_whiteboard(self, *, id: int, limit: int | Unset = UNSET, depth: int | Unset = UNSET, cursor: str | Unset = UNSET) -> _t.GetWhiteboardDescendantsResponse:
        """
        Get descendants of a whiteboard

        Returns descendants in the content tree for a given whiteboard by ID in top-to-bottom order (that is, the highest descendant is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the cursor in the response payload. There is also a `depth` parameter specifying depth
        of descendants to be fetched.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each descendant. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the whiteboard and its corresponding space
        """
        return cast('_t.GetWhiteboardDescendantsResponse', self._runtime.call('get_whiteboard_descendants', call_args({'id': id, 'limit': limit, 'depth': depth, 'cursor': cursor})))

    def list_database(self, *, id: int, limit: int | Unset = UNSET, depth: int | Unset = UNSET, cursor: str | Unset = UNSET) -> _t.GetDatabaseDescendantsResponse:
        """
        Get descendants of a database

        Returns descendants in the content tree for a given database by ID in top-to-bottom order (that is, the highest descendant is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the cursor in the response payload. There is also a `depth` parameter specifying depth
        of descendants to be fetched.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each descendant. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the database and its corresponding space
        """
        return cast('_t.GetDatabaseDescendantsResponse', self._runtime.call('get_database_descendants', call_args({'id': id, 'limit': limit, 'depth': depth, 'cursor': cursor})))

    def list_smart_link(self, *, id: int, limit: int | Unset = UNSET, depth: int | Unset = UNSET, cursor: str | Unset = UNSET) -> _t.GetSmartLinkDescendantsResponse:
        """
        Get descendants of a smart link

        Returns descendants in the content tree for a given smart link by ID in top-to-bottom order (that is, the highest descendant is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the cursor in the response payload. There is also a `depth` parameter specifying depth
        of descendants to be fetched.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard


        This endpoint returns minimal information about each descendant. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the smart link and its corresponding space
        """
        return cast('_t.GetSmartLinkDescendantsResponse', self._runtime.call('get_smart_link_descendants', call_args({'id': id, 'limit': limit, 'depth': depth, 'cursor': cursor})))

    def list_folder(self, *, id: int, limit: int | Unset = UNSET, depth: int | Unset = UNSET, cursor: str | Unset = UNSET) -> _t.GetFolderDescendantsResponse:
        """
        Get descendants of folder

        Returns descendants in the content tree for a given folder by ID in top-to-bottom order (that is, the highest descendant is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the cursor in the response payload. There is also a `depth` parameter specifying depth
        of descendants to be fetched.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each descendant. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the  and its corresponding space
        """
        return cast('_t.GetFolderDescendantsResponse', self._runtime.call('get_folder_descendants', call_args({'id': id, 'limit': limit, 'depth': depth, 'cursor': cursor})))

    def list_page(self, *, id: int, limit: int | Unset = UNSET, depth: int | Unset = UNSET, cursor: str | Unset = UNSET) -> _t.GetPageDescendantsResponse:
        """
        Get descendants of page

        Returns descendants in the content tree for a given page by ID in top-to-bottom order (that is, the highest descendant is the first
        item in the response payload). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available by calling this endpoint with the cursor in the response payload. There is also a `depth` parameter specifying depth
        of descendants to be fetched.

        The following types of content will be returned:
        - Database
        - Embed
        - Folder
        - Page
        - Whiteboard

        This endpoint returns minimal information about each descendant. To fetch more details, use a related endpoint based on the content type, such
        as:

        - [Get database by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-database/#api-databases-id-get)
        - [Get embed by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-smart-link/#api-embeds-id-get)
        - [Get folder by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-folder/#api-folders-id-get)
        - [Get page by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/#api-pages-id-get)
        - [Get whiteboard by id](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-whiteboard/#api-whiteboards-id-get).

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Permission to view the page and its corresponding space
        """
        return cast('_t.GetPageDescendantsResponse', self._runtime.call('get_page_descendants', call_args({'id': id, 'limit': limit, 'depth': depth, 'cursor': cursor})))

class _FolderResource:
    """Operations under ``folder``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create(self, *, space_id: str, title: str | Unset = UNSET, parent_id: str | Unset = UNSET) -> _t.CreateFolderResponse:
        """
        Create folder

        Creates a folder in the space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the corresponding space. Permission to create a folder in the space.
        """
        return cast('_t.CreateFolderResponse', self._runtime.call('create_folder', call_args({}, {'body': {'space_id': space_id, 'title': title, 'parent_id': parent_id}}, required=frozenset({'body'}))))

    def get(self, *, id: int, include_collaborators: bool | Unset = UNSET, include_direct_children: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_properties: bool | Unset = UNSET) -> _t.GetFolderByIdResponse:
        """
        Get folder by id

        Returns a specific folder.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the folder and its corresponding space.
        """
        return cast('_t.GetFolderByIdResponse', self._runtime.call('get_folder_by_id', call_args({'id': id, 'include_collaborators': include_collaborators, 'include_direct_children': include_direct_children, 'include_operations': include_operations, 'include_properties': include_properties})))

    def delete(self, *, id: int) -> None:
        """
        Delete folder

        Delete a folder by id.

        Deleting a folder moves the folder to the trash, where it can be restored later

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the folder and its corresponding space.
        Permission to delete folders in the space.
        """
        self._runtime.call('delete_folder', call_args({'id': id}))

class _LabelResource:
    """Operations under ``label``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_attachment_labels(self, *, id: int, prefix: _t.GetAttachmentLabelsPrefix | Unset = UNSET, sort: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetAttachmentLabelsResponse:
        """
        Get labels for attachment

        Returns the labels of specific attachment. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the parent content of the attachment and its corresponding space.
        Only labels that the user has permission to view will be returned.
        """
        return cast('_t.GetAttachmentLabelsResponse', self._runtime.call('get_attachment_labels', call_args({'id': id, 'prefix': prefix, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_blog_post_labels(self, *, id: int, prefix: _t.GetBlogPostLabelsPrefix | Unset = UNSET, sort: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogPostLabelsResponse:
        """
        Get labels for blog post

        Returns the labels of specific blog post. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the blog post and its corresponding space.
        Only labels that the user has permission to view will be returned.
        """
        return cast('_t.GetBlogPostLabelsResponse', self._runtime.call('get_blog_post_labels', call_args({'id': id, 'prefix': prefix, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_custom_content_labels(self, *, id: int, prefix: _t.GetCustomContentLabelsPrefix | Unset = UNSET, sort: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetCustomContentLabelsResponse:
        """
        Get labels for custom content

        Returns the labels for a specific piece of custom content. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content and its corresponding space.
        Only labels that the user has permission to view will be returned.
        """
        return cast('_t.GetCustomContentLabelsResponse', self._runtime.call('get_custom_content_labels', call_args({'id': id, 'prefix': prefix, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_labels(self, *, label_id: builtins.list[int] | Unset = UNSET, prefix: builtins.list[str] | Unset = UNSET, cursor: str | Unset = UNSET, sort: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetLabelsResponse:
        """
        Get labels

        Returns all labels. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only labels that the user has permission to view will be returned.
        """
        return cast('_t.GetLabelsResponse', self._runtime.call('get_labels', call_args({'label_id': label_id, 'prefix': prefix, 'cursor': cursor, 'sort': sort, 'limit': limit})))

    def list_page_labels(self, *, id: int, prefix: _t.GetPageLabelsPrefix | Unset = UNSET, sort: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPageLabelsResponse:
        """
        Get labels for page

        Returns the labels of specific page. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        Only labels that the user has permission to view will be returned.
        """
        return cast('_t.GetPageLabelsResponse', self._runtime.call('get_page_labels', call_args({'id': id, 'prefix': prefix, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_space_labels(self, *, id: int, prefix: _t.GetSpaceLabelsPrefix | Unset = UNSET, sort: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetSpaceLabelsResponse:
        """
        Get labels for space

        Returns the labels of specific space. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the space.
        Only labels that the user has permission to view will be returned.
        """
        return cast('_t.GetSpaceLabelsResponse', self._runtime.call('get_space_labels', call_args({'id': id, 'prefix': prefix, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_space_content_labels(self, *, id: int, prefix: _t.GetSpaceContentLabelsPrefix | Unset = UNSET, sort: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetSpaceContentLabelsResponse:
        """
        Get labels for space content

        Returns the labels of space content (pages, blogposts etc). The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the space.
        Only labels that the user has permission to view will be returned.
        """
        return cast('_t.GetSpaceContentLabelsResponse', self._runtime.call('get_space_content_labels', call_args({'id': id, 'prefix': prefix, 'sort': sort, 'cursor': cursor, 'limit': limit})))

class _LikeResource:
    """Operations under ``like``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get_blog_post_count(self, *, id: int) -> _t.GetBlogPostLikeCountResponse:
        """
        Get like count for blog post

        Returns the count of likes of specific blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the blog post and its corresponding space.
        """
        return cast('_t.GetBlogPostLikeCountResponse', self._runtime.call('get_blog_post_like_count', call_args({'id': id})))

    def list_blog_post_users(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetBlogPostLikeUsersResponse:
        """
        Get account IDs of likes for blog post

        Returns the account IDs of likes of specific blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the blog post and its corresponding space.
        """
        return cast('_t.GetBlogPostLikeUsersResponse', self._runtime.call('get_blog_post_like_users', call_args({'id': id, 'cursor': cursor, 'limit': limit})))

    def get_page_count(self, *, id: int) -> _t.GetPageLikeCountResponse:
        """
        Get like count for page

        Returns the count of likes of specific page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetPageLikeCountResponse', self._runtime.call('get_page_like_count', call_args({'id': id})))

    def list_page_users(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPageLikeUsersResponse:
        """
        Get account IDs of likes for page

        Returns the account IDs of likes of specific page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetPageLikeUsersResponse', self._runtime.call('get_page_like_users', call_args({'id': id, 'cursor': cursor, 'limit': limit})))

    def get_footer_count(self, *, id: int) -> _t.GetFooterLikeCountResponse:
        """
        Get like count for footer comment

        Returns the count of likes of specific footer comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page/blogpost and its corresponding space.
        """
        return cast('_t.GetFooterLikeCountResponse', self._runtime.call('get_footer_like_count', call_args({'id': id})))

    def list_footer_users(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetFooterLikeUsersResponse:
        """
        Get account IDs of likes for footer comment

        Returns the account IDs of likes of specific footer comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page/blogpost and its corresponding space.
        """
        return cast('_t.GetFooterLikeUsersResponse', self._runtime.call('get_footer_like_users', call_args({'id': id, 'cursor': cursor, 'limit': limit})))

    def get_inline_count(self, *, id: int) -> _t.GetInlineLikeCountResponse:
        """
        Get like count for inline comment

        Returns the count of likes of specific inline comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page/blogpost and its corresponding space.
        """
        return cast('_t.GetInlineLikeCountResponse', self._runtime.call('get_inline_like_count', call_args({'id': id})))

    def list_inline_users(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetInlineLikeUsersResponse:
        """
        Get account IDs of likes for inline comment

        Returns the account IDs of likes of specific inline comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page/blogpost and its corresponding space.
        """
        return cast('_t.GetInlineLikeUsersResponse', self._runtime.call('get_inline_like_users', call_args({'id': id, 'cursor': cursor, 'limit': limit})))

class _OperationResource:
    """Operations under ``operation``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_attachment_operations(self, *, id: str) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for attachment

        Returns the permitted operations on specific attachment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the parent content of the attachment and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_attachment_operations', call_args({'id': id})))

    def list_blog_post_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for blog post

        Returns the permitted operations on specific blog post.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the parent content of the blog post and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_blog_post_operations', call_args({'id': id})))

    def list_custom_content_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for custom content

        Returns the permitted operations on specific custom content.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the parent content of the custom content and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_custom_content_operations', call_args({'id': id})))

    def list_page_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for page

        Returns the permitted operations on specific page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the parent content of the page and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_page_operations', call_args({'id': id})))

    def list_whiteboard_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for a whiteboard

        Returns the permitted operations on specific whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the whiteboard and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_whiteboard_operations', call_args({'id': id})))

    def list_database_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for a database

        Returns the permitted operations on specific database.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the database and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_database_operations', call_args({'id': id})))

    def list_smart_link_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for a Smart Link in the content tree

        Returns the permitted operations on specific Smart Link in the content tree.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the Smart Link in the content tree and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_smart_link_operations', call_args({'id': id})))

    def list_folder_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for a folder

        Returns the permitted operations on specific folder.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the folder and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_folder_operations', call_args({'id': id})))

    def list_space_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for space

        Returns the permitted operations on specific space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_space_operations', call_args({'id': id})))

    def list_footer_comment_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for footer comment

        Returns the permitted operations on specific footer comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the parent content of the footer comment and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_footer_comment_operations', call_args({'id': id})))

    def list_inline_comment_operations(self, *, id: int) -> _t.PermittedOperationsResponse:
        """
        Get permitted operations for inline comment

        Returns the permitted operations on specific inline comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the parent content of the inline comment and its corresponding space.
        """
        return cast('_t.PermittedOperationsResponse', self._runtime.call('get_inline_comment_operations', call_args({'id': id})))

class _PageResource:
    """Operations under ``page``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_label_pages(self, *, id: int, space_id: builtins.list[int] | Unset = UNSET, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, sort: _t.PageSortOrder | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetLabelPagesResponse:
        """
        Get pages for label

        Returns the pages of specified label. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page and its corresponding space.
        """
        return cast('_t.GetLabelPagesResponse', self._runtime.call('get_label_pages', call_args({'id': id, 'space_id': space_id, 'body_format': body_format, 'sort': sort, 'cursor': cursor, 'limit': limit})))

    def list_pages(self, *, id: builtins.list[int] | Unset = UNSET, space_id: builtins.list[int] | Unset = UNSET, sort: _t.PageSortOrder | Unset = UNSET, status: builtins.list[_t.GetPagesStatusItem] | Unset = UNSET, title: str | Unset = UNSET, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, subtype: _t.GetPagesSubtype | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPagesResponse:
        """
        Get pages

        Returns all pages. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only pages that the user has permission to view will be returned.
        """
        return cast('_t.GetPagesResponse', self._runtime.call('get_pages', call_args({'id': id, 'space_id': space_id, 'sort': sort, 'status': status, 'title': title, 'body_format': body_format, 'subtype': subtype, 'cursor': cursor, 'limit': limit})))

    def create(self, *, space_id: str, embedded: bool | Unset = UNSET, private: bool | Unset = UNSET, root_level: bool | Unset = UNSET, status: _t.CreatePageBodyStatus | Unset = UNSET, title: str | Unset = UNSET, parent_id: str | Unset = UNSET, body: _t.CreatePageBodyBody | Unset = UNSET, subtype: _t.CreatePageBodySubtype | Unset = UNSET) -> _t.CreatePageResponse:
        """
        Create page

        Creates a page in the space.

        Pages are created as published by default unless specified as a draft in the status field. If creating a published page, the title must be specified.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the corresponding space. Permission to create a page in the space.
        """
        return cast('_t.CreatePageResponse', self._runtime.call('create_page', call_args({'embedded': embedded, 'private': private, 'root_level': root_level}, {'body': {'space_id': space_id, 'status': status, 'title': title, 'parent_id': parent_id, 'body': body, 'subtype': subtype}}, required=frozenset({'body'}))))

    def get(self, *, id: int, body_format: _t.PrimaryBodyRepresentationSingle | Unset = UNSET, get_draft: bool | Unset = UNSET, status: builtins.list[_t.GetPageByIdStatusItem] | Unset = UNSET, version: int | Unset = UNSET, include_labels: bool | Unset = UNSET, include_properties: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_likes: bool | Unset = UNSET, include_versions: bool | Unset = UNSET, include_version: bool | Unset = UNSET, include_favorited_by_current_user_status: bool | Unset = UNSET, include_webresources: bool | Unset = UNSET, include_collaborators: bool | Unset = UNSET, include_direct_children: bool | Unset = UNSET) -> _t.GetPageByIdResponse:
        """
        Get page by id

        Returns a specific page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page and its corresponding space.
        """
        return cast('_t.GetPageByIdResponse', self._runtime.call('get_page_by_id', call_args({'id': id, 'body_format': body_format, 'get_draft': get_draft, 'status': status, 'version': version, 'include_labels': include_labels, 'include_properties': include_properties, 'include_operations': include_operations, 'include_likes': include_likes, 'include_versions': include_versions, 'include_version': include_version, 'include_favorited_by_current_user_status': include_favorited_by_current_user_status, 'include_webresources': include_webresources, 'include_collaborators': include_collaborators, 'include_direct_children': include_direct_children})))

    def update(self, *, id: int, body: _t.UpdatePageBody) -> _t.UpdatePageResponse:
        """
        Update page

        Update a page by id.

        When the "current" version is updated, the provided body content is considered as the latest version. This latest body content
        will be attempted to be merged into the draft version through a content reconciliation algorithm. If two versions are significantly diverged, 
        the latest provided content may entirely override what was previously in the draft. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page and its corresponding space. Permission to update pages in the space.
        """
        return cast('_t.UpdatePageResponse', self._runtime.call('update_page', call_args({'id': id, 'body': body})))

    def delete(self, *, id: int, purge: bool | Unset = UNSET, draft: bool | Unset = UNSET) -> None:
        """
        Delete page

        Delete a page by id.

        By default this will delete pages that are non-drafts. To delete a page that is a draft, the endpoint must be called on a 
        draft with the following param `draft=true`. Discarded drafts are not sent to the trash and are permanently deleted.

        Deleting a page moves the page to the trash, where it can be restored later. To permanently delete a page (or "purge" it),
        the endpoint must be called on a **trashed** page with the following param `purge=true`.

        **[Permissions](https://support.atlassian.com/confluence-cloud/docs/what-are-confluences-roles/) required**:
        Permission to view the page and its corresponding space.
        Permission to delete pages in the space.
        [`manage/content`](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) permission for the space (if attempting to purge).

        **Note:** To find the display name for each permission ID, call the [Get available space permissions](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-space-permissions/#api-space-permissions-get) API.
        """
        self._runtime.call('delete_page', call_args({'id': id, 'purge': purge, 'draft': draft}))

    def update_title(self, *, id: int, status: _t.UpdatePageTitleBodyStatus, title: str) -> _t.UpdatePageTitleResponse:
        """
        Update page title

        Updates the title of a specified page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page and its corresponding space. Permission to update pages in the space.
        """
        return cast('_t.UpdatePageTitleResponse', self._runtime.call('update_page_title', call_args({'id': id}, {'body': {'status': status, 'title': title}}, required=frozenset({'body'}))))

    def get_pages_in_space(self, *, id: int, depth: _t.GetPagesInSpaceDepth | Unset = UNSET, sort: _t.PageSortOrder | Unset = UNSET, status: builtins.list[_t.GetPagesInSpaceStatusItem] | Unset = UNSET, title: str | Unset = UNSET, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetPagesInSpaceResponse:
        """
        Get pages in space

        Returns all pages in a space. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission) and 'View' permission for the space.
        Only pages that the user has permission to view will be returned.
        """
        return cast('_t.GetPagesInSpaceResponse', self._runtime.call('get_pages_in_space', call_args({'id': id, 'depth': depth, 'sort': sort, 'status': status, 'title': title, 'body_format': body_format, 'cursor': cursor, 'limit': limit})))

class _RedactionsResource:
    """Operations under ``redactions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def post_redact_page(self, *, id: int, created_at: str | Unset = UNSET, clean_history: bool | None | Unset = UNSET, version_number: int | None | Unset = UNSET, body: _t.PostRedactPageBodyBody | Unset = UNSET, title: _t.PostRedactPageBodyTitle | Unset = UNSET) -> _t.RedactionResponse:
        """
        Redact Content in a Confluence Page

        Redacts sensitive content in a Confluence page by replacing specified text ranges with redaction markers. 
        Each redaction in the response includes a unique UUID for restoration (except code block redactions). 
        The response metadata items maintain the same order as the input redaction pointers, and completely 
        overlapping redactions are merged into a single redaction with one UUID.

        **Note**: This endpoint requires **Atlassian Guard Premium**.
        """
        return cast('_t.RedactionResponse', self._runtime.call('post_redact_page', call_args({'id': id}, {'body': {'created_at': created_at, 'clean_history': clean_history, 'version_number': version_number, 'body': body, 'title': title}})))

    def post_redact_blog(self, *, id: int, created_at: str | Unset = UNSET, clean_history: bool | None | Unset = UNSET, version_number: int | None | Unset = UNSET, body: _t.PostRedactBlogBodyBody | Unset = UNSET, title: _t.PostRedactBlogBodyTitle | Unset = UNSET) -> _t.RedactionResponse:
        """
        Redact Content in a Confluence Blog Post

        Redacts sensitive content in a Confluence blog post by replacing specified text ranges with redaction markers. 
        Each redaction in the response includes a unique UUID for restoration (except code block redactions). 
        The response metadata items maintain the same order as the input redaction pointers, and completely 
        overlapping redactions are merged into a single redaction with one UUID.

        **Note**: This endpoint requires **Atlassian Guard Premium**.
        """
        return cast('_t.RedactionResponse', self._runtime.call('post_redact_blog', call_args({'id': id}, {'body': {'created_at': created_at, 'clean_history': clean_history, 'version_number': version_number, 'body': body, 'title': title}})))

class _SmartLinkResource:
    """Operations under ``smart_link``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create(self, *, space_id: str, title: str | Unset = UNSET, parent_id: str | Unset = UNSET, embed_url: str | Unset = UNSET) -> _t.CreateSmartLinkResponse:
        """
        Create Smart Link in the content tree

        Creates a Smart Link in the content tree in the space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the corresponding space. Permission to create a Smart Link in the content tree in the space.
        """
        return cast('_t.CreateSmartLinkResponse', self._runtime.call('create_smart_link', call_args({}, {'body': {'space_id': space_id, 'title': title, 'parent_id': parent_id, 'embed_url': embed_url}}, required=frozenset({'body'}))))

    def get(self, *, id: int, include_collaborators: bool | Unset = UNSET, include_direct_children: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_properties: bool | Unset = UNSET) -> _t.GetSmartLinkByIdResponse:
        """
        Get Smart Link in the content tree by id

        Returns a specific Smart Link in the content tree.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the Smart Link in the content tree and its corresponding space.
        """
        return cast('_t.GetSmartLinkByIdResponse', self._runtime.call('get_smart_link_by_id', call_args({'id': id, 'include_collaborators': include_collaborators, 'include_direct_children': include_direct_children, 'include_operations': include_operations, 'include_properties': include_properties})))

    def delete(self, *, id: int) -> None:
        """
        Delete Smart Link in the content tree

        Delete a Smart Link in the content tree by id.

        Deleting a Smart Link in the content tree moves the Smart Link to the trash, where it can be restored later

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the Smart Link in the content tree and its corresponding space.
        Permission to delete Smart Links in the content tree in the space.
        """
        self._runtime.call('delete_smart_link', call_args({'id': id}))

class _SpaceResource:
    """Operations under ``space``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_spaces(self, *, ids: builtins.list[int] | Unset = UNSET, keys: builtins.list[str] | Unset = UNSET, type_: _t.GetSpacesType | Unset = UNSET, status: _t.GetSpacesStatus | Unset = UNSET, labels: builtins.list[str] | Unset = UNSET, favorited_by: str | Unset = UNSET, not_favorited_by: str | Unset = UNSET, sort: _t.SpaceSortOrder | Unset = UNSET, description_format: _t.SpaceDescriptionBodyRepresentation | Unset = UNSET, include_icon: bool | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetSpacesResponse:
        """
        Get spaces

        Returns all spaces. The results will be sorted by id ascending. The number of results is limited by the `limit` parameter and
        additional results (if available) will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only spaces that the user has permission to view will be returned.
        """
        return cast('_t.GetSpacesResponse', self._runtime.call('get_spaces', call_args({'ids': ids, 'keys': keys, 'type': type_, 'status': status, 'labels': labels, 'favorited_by': favorited_by, 'not_favorited_by': not_favorited_by, 'sort': sort, 'description_format': description_format, 'include_icon': include_icon, 'cursor': cursor, 'limit': limit})))

    def create(self, *, name: str, key: str | Unset = UNSET, alias: str | Unset = UNSET, description: _t.CreateSpaceBodyDescription | Unset = UNSET, role_assignments: builtins.list[_t.CreateSpaceBodyRoleAssignmentsItem] | Unset = UNSET, copy_space_access_configuration: int | Unset = UNSET, create_private_space: bool | Unset = UNSET, template_key: str | Unset = UNSET) -> _t.CreateSpaceResponse:
        """
        Create space

        Creates a Space as specified in the payload.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to create spaces.
        """
        return cast('_t.CreateSpaceResponse', self._runtime.call('create_space', call_args({}, {'body': {'name': name, 'key': key, 'alias': alias, 'description': description, 'role_assignments': role_assignments, 'copy_space_access_configuration': copy_space_access_configuration, 'create_private_space': create_private_space, 'template_key': template_key}}, required=frozenset({'body'}))))

    def get(self, *, id: int, description_format: _t.SpaceDescriptionBodyRepresentation | Unset = UNSET, include_icon: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_properties: bool | Unset = UNSET, include_permissions: bool | Unset = UNSET, include_role_assignments: bool | Unset = UNSET, include_labels: bool | Unset = UNSET) -> _t.GetSpaceByIdResponse:
        """
        Get space by id

        Returns a specific space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the space.
        """
        return cast('_t.GetSpaceByIdResponse', self._runtime.call('get_space_by_id', call_args({'id': id, 'description_format': description_format, 'include_icon': include_icon, 'include_operations': include_operations, 'include_properties': include_properties, 'include_permissions': include_permissions, 'include_role_assignments': include_role_assignments, 'include_labels': include_labels})))

class _SpacePermissionTransitionResource:
    """Operations under ``space_permission_transition``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_space_permission_combinations(self, *, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.ListSpacePermissionCombinationsResponse:
        """
        List unassigned space permission combinations

        Lists the unique unassigned space permission combinations currently present on the tenant.
        Combinations that already map to a space role are filtered out server-side. Each row carries
        the decoded set of space permissions and the principal types that currently hold the
        combination — these inform which `principalType` values are valid to include in the matching
        bulk role-assignments request.

        Results are always sorted by `principalCount` descending. Sort field and sort order are not
        configurable; page size is controlled by the `limit` query parameter (default 25, min 1,
        max 250). Use the `cursor` field to page through additional results. The `generatedAt` field
        reflects the last audit run that populated the combinations table — call the
        generate-combinations endpoint to refresh stale data.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be a Confluence administrator.
        """
        return cast('_t.ListSpacePermissionCombinationsResponse', self._runtime.call('list_space_permission_combinations', call_args({'cursor': cursor, 'limit': limit})))

    def generate_space_permission_combinations(self) -> _t.BulkTransitionTaskResponse:
        """
        Generate space permission combinations

        Submits a task to refresh the space permission combinations in the database, which identifies
        all unique permission combinations across the site. This provides permission combination IDs
        that can be used with the assign-roles and remove-access endpoints.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be a Confluence administrator.
        """
        return cast('_t.BulkTransitionTaskResponse', self._runtime.call('generate_space_permission_combinations', call_args({})))

    def bulk_assign_space_permission_roles(self, *, assignments: builtins.list[_t.BulkTransitionRoleAssignment], space_selection: _t.BulkTransitionSpaceSelection) -> _t.BulkTransitionTaskResponse:
        """
        Bulk assign space permission roles

        Bulk assigns roles for one or more permission combination IDs obtained from the space permission
        combinations. Supports targeting all spaces, specific spaces, or excluding specific spaces.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be a Confluence administrator.
        """
        return cast('_t.BulkTransitionTaskResponse', self._runtime.call('bulk_assign_space_permission_roles', call_args({}, {'body': {'assignments': assignments, 'space_selection': space_selection}}, required=frozenset({'body'}))))

    def bulk_remove_space_permission_access(self, *, permission_combination_ids: builtins.list[str], space_selection: _t.BulkTransitionSpaceSelection) -> _t.BulkTransitionTaskResponse:
        """
        Bulk remove space permission access

        Bulk removes access for one or more permission combination IDs obtained from the space permission
        combinations. This removes all space permissions for the specified combinations across
        the targeted spaces.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be a Confluence administrator.
        """
        return cast('_t.BulkTransitionTaskResponse', self._runtime.call('bulk_remove_space_permission_access', call_args({}, {'body': {'permission_combination_ids': permission_combination_ids, 'space_selection': space_selection}}, required=frozenset({'body'}))))

    def get_task_status(self, *, task_id: str) -> _t.BulkTransitionTaskStatusResponse:
        """
        Get space permission transition task status

        Retrieves the status of an async space permission transition task. Use the taskId returned
        from the generate-combinations, assign-roles, or remove-access endpoints to poll for
        progress and completion.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be a Confluence administrator.
        """
        return cast('_t.BulkTransitionTaskStatusResponse', self._runtime.call('get_space_permission_transition_task_status', call_args({'task_id': task_id})))

class _SpacePermissionsResource:
    """Operations under ``space_permissions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_assignments(self, *, id: int, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetSpacePermissionsAssignmentsResponse:
        """
        Get space permissions assignments

        Returns space permission assignments for a specific space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the space.
        """
        return cast('_t.GetSpacePermissionsAssignmentsResponse', self._runtime.call('get_space_permissions_assignments', call_args({'id': id, 'cursor': cursor, 'limit': limit})))

    def list(self, *, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetAvailableSpacePermissionsResponse:
        """
        Get available space permissions

        Retrieves the available space permissions.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site.
        """
        return cast('_t.GetAvailableSpacePermissionsResponse', self._runtime.call('get_available_space_permissions', call_args({'cursor': cursor, 'limit': limit})))

class _SpacePropertiesResource:
    """Operations under ``space_properties``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, space_id: int, key: str | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetSpacePropertiesResponse:
        """
        Get space properties in space

        Returns all properties for the given space. Space properties are a key-value storage associated with a space.
        The limit parameter specifies the maximum number of results returned in a single response. Use the `link` response header
        to paginate through additional results.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission) and 'View' permission for the space.
        """
        return cast('_t.GetSpacePropertiesResponse', self._runtime.call('get_space_properties', call_args({'space_id': space_id, 'key': key, 'cursor': cursor, 'limit': limit})))

    def create(self, *, space_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET) -> _t.SpaceProperty:
        """
        Create space property in space

        Creates a new space property.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space.
        """
        return cast('_t.SpaceProperty', self._runtime.call('create_space_property', call_args({'space_id': space_id}, {'body': {'key': key, 'value': value}})))

    def get(self, *, space_id: int, property_id: int) -> _t.SpaceProperty:
        """
        Get space property by id

        Retrieve a space property by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission) and 'View' permission for the space.
        """
        return cast('_t.SpaceProperty', self._runtime.call('get_space_property_by_id', call_args({'space_id': space_id, 'property_id': property_id})))

    def update(self, *, space_id: int, property_id: int, key: str | Unset = UNSET, value: Any | Unset = UNSET, version: _t.SpacePropertyUpdateRequestVersion | Unset = UNSET) -> _t.SpaceProperty:
        """
        Update space property by id

        Update a space property by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space.
        """
        return cast('_t.SpaceProperty', self._runtime.call('update_space_property_by_id', call_args({'space_id': space_id, 'property_id': property_id}, {'body': {'key': key, 'value': value, 'version': version}})))

    def delete(self, *, space_id: int, property_id: int) -> None:
        """
        Delete space property by id

        Deletes a space property by its id. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission) and 'Admin' permission for the space.
        """
        self._runtime.call('delete_space_property_by_id', call_args({'space_id': space_id, 'property_id': property_id}))

class _SpaceRolesResource:
    """Operations under ``space_roles``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, space_id: str | Unset = UNSET, role_type: str | Unset = UNSET, principal_id: str | Unset = UNSET, principal_type: _t.PrincipalType | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetAvailableSpaceRolesResponse:
        """
        Get available space roles

        Retrieves the available space roles.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site; if requesting a certain space's roles, permission to view the space.
        """
        return cast('_t.GetAvailableSpaceRolesResponse', self._runtime.call('get_available_space_roles', call_args({'space_id': space_id, 'role_type': role_type, 'principal_id': principal_id, 'principal_type': principal_type, 'cursor': cursor, 'limit': limit})))

    def create(self, *, name: str, description: str, space_permissions: builtins.list[str]) -> _t.SpaceRole:
        """
        Create a space role

        Create a space role.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource.
        """
        return cast('_t.SpaceRole', self._runtime.call('create_space_role', call_args({}, {'body': {'name': name, 'description': description, 'space_permissions': space_permissions}}, required=frozenset({'body'}))))

    def get(self, *, id: int) -> _t.GetSpaceRolesByIdResponse:
        """
        Get space role by ID

        Retrieves the space role by ID.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site.
        """
        return cast('_t.GetSpaceRolesByIdResponse', self._runtime.call('get_space_roles_by_id', call_args({'id': id})))

    def update(self, *, id: str, name: str, description: str, space_permissions: builtins.list[str], anonymous_reassignment_role_id: str | Unset = UNSET, guest_reassignment_role_id: str | Unset = UNSET) -> _t.UpdateSpaceRoleResponse:
        """
        Update a space role

        Update a space role.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource.
        """
        return cast('_t.UpdateSpaceRoleResponse', self._runtime.call('update_space_role', call_args({'id': id}, {'body': {'name': name, 'description': description, 'space_permissions': space_permissions, 'anonymous_reassignment_role_id': anonymous_reassignment_role_id, 'guest_reassignment_role_id': guest_reassignment_role_id}}, required=frozenset({'body'}))))

    def delete(self, *, id: str) -> _t.DeleteSpaceRoleResponse:
        """
        Delete a space role

        Delete a space role

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        User must be an organization or site admin. Connect and Forge app users are not authorized to access this resource.
        """
        return cast('_t.DeleteSpaceRoleResponse', self._runtime.call('delete_space_role', call_args({'id': id})))

    def get_mode(self) -> _t.GetSpaceRoleModeResponse:
        """
        Get space role mode

        Retrieves the space role mode.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        """
        return cast('_t.GetSpaceRoleModeResponse', self._runtime.call('get_space_role_mode', call_args({})))

    def list_assignments(self, *, id: int, role_id: str | Unset = UNSET, role_type: str | Unset = UNSET, principal_id: str | Unset = UNSET, principal_type: _t.PrincipalType | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetSpaceRoleAssignmentsResponse:
        """
        Get space role assignments

        Retrieves the space role assignments.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the space.
        """
        return cast('_t.GetSpaceRoleAssignmentsResponse', self._runtime.call('get_space_role_assignments', call_args({'id': id, 'role_id': role_id, 'role_type': role_type, 'principal_id': principal_id, 'principal_type': principal_type, 'cursor': cursor, 'limit': limit})))

    def set_assignments(self, *, id: int, body: builtins.list[_t.SetSpaceRoleAssignmentsBodyItem]) -> _t.SetSpaceRoleAssignmentsResponse:
        """
        Set space role assignments

        Sets space role assignments as specified in the payload. For each entry, if `roleId` is provided
        the principal is assigned to that role. If `roleId` is omitted, the role assignment for that principal is removed, if it exists.

        Available on tenants with [Role-Based Access Control](https://support.atlassian.com/confluence-cloud/docs/manage-user-roles/). 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to manage roles in the space.
        """
        return cast('_t.SetSpaceRoleAssignmentsResponse', self._runtime.call('set_space_role_assignments', call_args({'id': id, 'body': body})))

class _TaskResource:
    """Operations under ``task``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_tasks(self, *, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, include_blank_tasks: bool | Unset = UNSET, status: _t.GetTasksStatus | Unset = UNSET, task_id: builtins.list[int] | Unset = UNSET, space_id: builtins.list[int] | Unset = UNSET, page_id: builtins.list[int] | Unset = UNSET, blogpost_id: builtins.list[int] | Unset = UNSET, created_by: builtins.list[str] | Unset = UNSET, assigned_to: builtins.list[str] | Unset = UNSET, completed_by: builtins.list[str] | Unset = UNSET, created_at_from: int | Unset = UNSET, created_at_to: int | Unset = UNSET, due_at_from: int | Unset = UNSET, due_at_to: int | Unset = UNSET, completed_at_from: int | Unset = UNSET, completed_at_to: int | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET) -> _t.GetTasksResponse:
        """
        Get tasks

        Returns all tasks. The number of results is limited by the `limit` parameter and additional results (if available)
        will be available through the `next` URL present in the `Link` response header.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        Only tasks that the user has permission to view will be returned.
        """
        return cast('_t.GetTasksResponse', self._runtime.call('get_tasks', call_args({'body_format': body_format, 'include_blank_tasks': include_blank_tasks, 'status': status, 'task_id': task_id, 'space_id': space_id, 'page_id': page_id, 'blogpost_id': blogpost_id, 'created_by': created_by, 'assigned_to': assigned_to, 'completed_by': completed_by, 'created_at_from': created_at_from, 'created_at_to': created_at_to, 'due_at_from': due_at_from, 'due_at_to': due_at_to, 'completed_at_from': completed_at_from, 'completed_at_to': completed_at_to, 'cursor': cursor, 'limit': limit})))

    def get(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET) -> _t.Task:
        """
        Get task by id

        Returns a specific task. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the containing page or blog post and its corresponding space.
        """
        return cast('_t.Task', self._runtime.call('get_task_by_id', call_args({'id': id, 'body_format': body_format})))

    def update(self, *, id: int, body: _t.UpdateTaskBody, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET) -> _t.Task:
        """
        Update task

        Update a task by id. This endpoint currently only supports updating task status.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to edit the containing page or blog post and view its corresponding space.
        """
        return cast('_t.Task', self._runtime.call('update_task', call_args({'id': id, 'body_format': body_format, 'body': body})))

class _UserResource:
    """Operations under ``user``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create_bulk_lookup(self, *, account_ids: builtins.list[str]) -> _t.CreateBulkUserLookupResponse:
        """
        Create bulk user lookup using ids

        Returns user details for the ids provided in the request body.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        The user must be able to view user profiles in the Confluence site.
        """
        return cast('_t.CreateBulkUserLookupResponse', self._runtime.call('create_bulk_user_lookup', call_args({}, {'body': {'account_ids': account_ids}}, required=frozenset({'body'}))))

    def check_access_by_email(self, *, emails: builtins.list[str]) -> _t.CheckAccessByEmailResponse:
        """
        Check site access for a list of emails

        Returns the list of emails from the input list that do not have access to site.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        """
        return cast('_t.CheckAccessByEmailResponse', self._runtime.call('check_access_by_email', call_args({}, {'body': {'emails': emails}}, required=frozenset({'body'}))))

    def invite_by_email(self, *, emails: builtins.list[str]) -> None:
        """
        Invite a list of emails to the site

        Invite a list of emails to the site.

        Ignores all invalid emails and no action is taken for the emails that already have access to the site.

        <b>NOTE:</b> This API is asynchronous and may take some time to complete.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to access the Confluence site ('Can use' global permission).
        """
        self._runtime.call('invite_by_email', call_args({}, {'body': {'emails': emails}}, required=frozenset({'body'})))

class _VersionResource:
    """Operations under ``version``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list_attachment_versions(self, *, id: str, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.VersionSortOrder | Unset = UNSET) -> _t.GetAttachmentVersionsResponse:
        """
        Get attachment versions

        Returns the versions of specific attachment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment and its corresponding space.
        """
        return cast('_t.GetAttachmentVersionsResponse', self._runtime.call('get_attachment_versions', call_args({'id': id, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_attachment_details(self, *, attachment_id: str, version_number: int) -> _t.DetailedVersion:
        """
        Get version details for attachment version

        Retrieves version details for the specified attachment and version number.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the attachment.
        """
        return cast('_t.DetailedVersion', self._runtime.call('get_attachment_version_details', call_args({'attachment_id': attachment_id, 'version_number': version_number})))

    def list_blog_post_versions(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.VersionSortOrder | Unset = UNSET) -> _t.GetBlogPostVersionsResponse:
        """
        Get blog post versions

        Returns the versions of specific blog post. 

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post and its corresponding space.
        """
        return cast('_t.GetBlogPostVersionsResponse', self._runtime.call('get_blog_post_versions', call_args({'id': id, 'body_format': body_format, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_blog_post_details(self, *, blogpost_id: int, version_number: int) -> _t.DetailedVersion:
        """
        Get version details for blog post version

        Retrieves version details for the specified blog post and version number.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the blog post.
        """
        return cast('_t.DetailedVersion', self._runtime.call('get_blog_post_version_details', call_args({'blogpost_id': blogpost_id, 'version_number': version_number})))

    def list_page_versions(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.VersionSortOrder | Unset = UNSET) -> _t.GetPageVersionsResponse:
        """
        Get page versions

        Returns the versions of specific page.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page and its corresponding space.
        """
        return cast('_t.GetPageVersionsResponse', self._runtime.call('get_page_versions', call_args({'id': id, 'body_format': body_format, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_page_details(self, *, page_id: int, version_number: int) -> _t.DetailedVersion:
        """
        Get version details for page version

        Retrieves version details for the specified page and version number.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page.
        """
        return cast('_t.DetailedVersion', self._runtime.call('get_page_version_details', call_args({'page_id': page_id, 'version_number': version_number})))

    def list_custom_content_versions(self, *, custom_content_id: int, body_format: _t.CustomContentBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.VersionSortOrder | Unset = UNSET) -> _t.GetCustomContentVersionsResponse:
        """
        Get custom content versions

        Returns the versions of specific custom content.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the custom content and its corresponding page and space.
        """
        return cast('_t.GetCustomContentVersionsResponse', self._runtime.call('get_custom_content_versions', call_args({'custom_content_id': custom_content_id, 'body_format': body_format, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_custom_content_details(self, *, custom_content_id: int, version_number: int) -> _t.DetailedVersion:
        """
        Get version details for custom content version

        Retrieves version details for the specified custom content and version number.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the page.
        """
        return cast('_t.DetailedVersion', self._runtime.call('get_custom_content_version_details', call_args({'custom_content_id': custom_content_id, 'version_number': version_number})))

    def list_footer_comment_versions(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.VersionSortOrder | Unset = UNSET) -> _t.GetFooterCommentVersionsResponse:
        """
        Get footer comment versions

        Retrieves the versions of the specified footer comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blog post and its corresponding space.
        """
        return cast('_t.GetFooterCommentVersionsResponse', self._runtime.call('get_footer_comment_versions', call_args({'id': id, 'body_format': body_format, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_footer_comment_details(self, *, id: int, version_number: int) -> _t.DetailedVersion:
        """
        Get version details for footer comment version

        Retrieves version details for the specified footer comment version.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blog post and its corresponding space.
        """
        return cast('_t.DetailedVersion', self._runtime.call('get_footer_comment_version_details', call_args({'id': id, 'version_number': version_number})))

    def list_inline_comment_versions(self, *, id: int, body_format: _t.PrimaryBodyRepresentation | Unset = UNSET, cursor: str | Unset = UNSET, limit: int | Unset = UNSET, sort: _t.VersionSortOrder | Unset = UNSET) -> _t.GetInlineCommentVersionsResponse:
        """
        Get inline comment versions

        Retrieves the versions of the specified inline comment.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blog post and its corresponding space.
        """
        return cast('_t.GetInlineCommentVersionsResponse', self._runtime.call('get_inline_comment_versions', call_args({'id': id, 'body_format': body_format, 'cursor': cursor, 'limit': limit, 'sort': sort})))

    def list_inline_comment_details(self, *, id: int, version_number: int) -> _t.DetailedVersion:
        """
        Get version details for inline comment version

        Retrieves version details for the specified inline comment version.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the content of the page or blog post and its corresponding space.
        """
        return cast('_t.DetailedVersion', self._runtime.call('get_inline_comment_version_details', call_args({'id': id, 'version_number': version_number})))

class _WhiteboardResource:
    """Operations under ``whiteboard``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def create(self, *, space_id: str, private: bool | Unset = UNSET, title: str | Unset = UNSET, parent_id: str | Unset = UNSET, template_key: _t.CreateWhiteboardBodyTemplateKey | Unset = UNSET, locale: _t.CreateWhiteboardBodyLocale | Unset = UNSET) -> _t.CreateWhiteboardResponse:
        """
        Create whiteboard

        Creates a whiteboard in the space.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the corresponding space. Permission to create a whiteboard in the space.
        """
        return cast('_t.CreateWhiteboardResponse', self._runtime.call('create_whiteboard', call_args({'private': private}, {'body': {'space_id': space_id, 'title': title, 'parent_id': parent_id, 'template_key': template_key, 'locale': locale}}, required=frozenset({'body'}))))

    def get(self, *, id: int, include_collaborators: bool | Unset = UNSET, include_direct_children: bool | Unset = UNSET, include_operations: bool | Unset = UNSET, include_properties: bool | Unset = UNSET) -> _t.GetWhiteboardByIdResponse:
        """
        Get whiteboard by id

        Returns a specific whiteboard.

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the whiteboard and its corresponding space.
        """
        return cast('_t.GetWhiteboardByIdResponse', self._runtime.call('get_whiteboard_by_id', call_args({'id': id, 'include_collaborators': include_collaborators, 'include_direct_children': include_direct_children, 'include_operations': include_operations, 'include_properties': include_properties})))

    def delete(self, *, id: int) -> None:
        """
        Delete whiteboard

        Delete a whiteboard by id.

        Deleting a whiteboard moves the whiteboard to the trash, where it can be restored later

        **[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
        Permission to view the whiteboard and its corresponding space.
        Permission to delete whiteboards in the space.
        """
        self._runtime.call('delete_whiteboard', call_args({'id': id}))


class Client:
    """
    The Confluence Cloud REST API v2 client.

    Default base URL: https://your-site.atlassian.net
    """

    def __init__(
        self,
        *,
        base_url: str | None = None,
        auth: AuthProvider | None = None,
        transport: Transport | None = None,
        middleware: Sequence[Middleware] | None = None,
        validate: bool = True,
        timeout: float = 30.0,
        allow_private: bool = False,
        response_validation: str = "strict",
        proxy: str | None = None,
        protocols: Mapping[str, Any] | None = None,
        hooks: Sequence[Any] = (),
    ) -> None:
        self._runtime = RuntimeClient(
            _model(),
            base_url=base_url,
            auth=auth,
            transport=transport,
            middleware=middleware,
            validate=validate,
            timeout=timeout,
            allow_private=allow_private,
            response_validation=response_validation,
            proxy=proxy,
            protocols={**PROTOCOLS, **(protocols or {})},
            hooks=hooks,
        )
        self.admin_key = _AdminKeyResource(self._runtime)
        self.ancestors = _AncestorsResource(self._runtime)
        self.app_properties = _AppPropertiesResource(self._runtime)
        self.attachment = _AttachmentResource(self._runtime)
        self.blog_post = _BlogPostResource(self._runtime)
        self.children = _ChildrenResource(self._runtime)
        self.classification_level = _ClassificationLevelResource(self._runtime)
        self.comment = _CommentResource(self._runtime)
        self.content = _ContentResource(self._runtime)
        self.content_permissions = _ContentPermissionsResource(self._runtime)
        self.content_properties = _ContentPropertiesResource(self._runtime)
        self.custom_content = _CustomContentResource(self._runtime)
        self.data_policies = _DataPoliciesResource(self._runtime)
        self.database = _DatabaseResource(self._runtime)
        self.descendants = _DescendantsResource(self._runtime)
        self.folder = _FolderResource(self._runtime)
        self.label = _LabelResource(self._runtime)
        self.like = _LikeResource(self._runtime)
        self.operation = _OperationResource(self._runtime)
        self.page = _PageResource(self._runtime)
        self.redactions = _RedactionsResource(self._runtime)
        self.smart_link = _SmartLinkResource(self._runtime)
        self.space = _SpaceResource(self._runtime)
        self.space_permission_transition = _SpacePermissionTransitionResource(self._runtime)
        self.space_permissions = _SpacePermissionsResource(self._runtime)
        self.space_properties = _SpacePropertiesResource(self._runtime)
        self.space_roles = _SpaceRolesResource(self._runtime)
        self.task = _TaskResource(self._runtime)
        self.user = _UserResource(self._runtime)
        self.version = _VersionResource(self._runtime)
        self.whiteboard = _WhiteboardResource(self._runtime)
