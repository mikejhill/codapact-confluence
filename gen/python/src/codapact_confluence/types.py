"""Types generated from the semantic model. Do not edit."""

# ruff: noqa: E501, UP013
from __future__ import annotations

from typing import (
    Any,
    Literal,
    NotRequired,
    TypedDict,
)

__all__ = ['AbstractPageLinks', 'AccountStatus', 'AccountType', 'AdminKeyResponse', 'Ancestor', 'AncestorType', 'AttachmentBulk', 'AttachmentCommentModel', 'AttachmentLinks', 'AttachmentSingle', 'AttachmentSingleLabels', 'AttachmentSingleOperations', 'AttachmentSingleProperties', 'AttachmentSingleVersions', 'AttachmentSortOrder', 'AttachmentVersion', 'BlogPostBodyWrite', 'BlogPostBodyWriteRepresentation', 'BlogPostBulk', 'BlogPostCommentModel', 'BlogPostContentStatus', 'BlogPostInlineCommentModel', 'BlogPostNestedBodyWrite', 'BlogPostSingle', 'BlogPostSingleLabels', 'BlogPostSingleLikes', 'BlogPostSingleOperations', 'BlogPostSingleProperties', 'BlogPostSingleVersions', 'BlogPostSortOrder', 'BlogPostVersion', 'BodyBulk', 'BodySingle', 'BodyType', 'BulkAssignRolesRequest', 'BulkRemoveAccessRequest', 'BulkTransitionCombinationEntry', 'BulkTransitionCombinationEntryPrincipalTypesItem', 'BulkTransitionDecodedPermission', 'BulkTransitionPrincipalTypeAssignment', 'BulkTransitionPrincipalTypeAssignmentPrincipalType', 'BulkTransitionRoleAssignment', 'BulkTransitionSpaceSelection', 'BulkTransitionSpaceSelectionSpaceType', 'BulkTransitionSpaceTarget', 'BulkTransitionTaskResponse', 'BulkTransitionTaskResponseStatus', 'BulkTransitionTaskStatusResponse', 'BulkTransitionTaskStatusResponseStatus', 'CheckAccessByEmailBody', 'CheckAccessByEmailResponse', 'ChildCustomContent', 'ChildCustomContentSortOrder', 'ChildPage', 'ChildPageSortOrder', 'ChildrenCommentModel', 'ChildrenResponse', 'ClassificationLevel', 'ClassificationLevelColor', 'ClassificationLevelStatus', 'CommentBodyWrite', 'CommentBodyWriteRepresentation', 'CommentLinks', 'CommentNestedBodyWrite', 'CommentSortOrder', 'CommentVersion', 'ContentIdToContentTypeResponse', 'ContentIdToContentTypeResponseResultsValue', 'ContentIdToContentTypeResponseResultsValueOption1', 'ContentPermissionError', 'ContentPermissionErrorResponse', 'ContentPermissionOutput', 'ContentPermissionOutputOperation', 'ContentPermissionPrincipal', 'ContentPermissionPrincipalPrincipalType', 'ContentPermissionsRequest', 'ContentPermissionsResponse', 'ContentPrincipalInput', 'ContentPrincipalInputPrincipalType', 'ContentProperty', 'ContentPropertyCreateRequest', 'ContentPropertySortOrder', 'ContentPropertyUpdateRequest', 'ContentPropertyUpdateRequestVersion', 'ContentRestrictionState', 'ContentSortOrder', 'ContentStatus', 'ConvertContentIdsToContentTypesBody', 'ConvertContentIdsToContentTypesBodyContentIdsItem', 'CreateBlogPostBody', 'CreateBlogPostBodyBody', 'CreateBlogPostBodyStatus', 'CreateBlogPostResponse', 'CreateBlogPostResponseLinks', 'CreateBulkUserLookupBody', 'CreateBulkUserLookupResponse', 'CreateCustomContentBody', 'CreateCustomContentBodyBody', 'CreateCustomContentBodyStatus', 'CreateCustomContentResponse', 'CreateCustomContentResponseLinks', 'CreateDatabaseBody', 'CreateDatabaseResponse', 'CreateDatabaseResponseLinks', 'CreateFolderBody', 'CreateFolderResponse', 'CreateFolderResponseLinks', 'CreateFooterCommentModel', 'CreateFooterCommentModelBody', 'CreateFooterCommentResponse', 'CreateFooterCommentResponseLinks', 'CreateInlineCommentModel', 'CreateInlineCommentModelBody', 'CreateInlineCommentModelInlineCommentProperties', 'CreateInlineCommentResponse', 'CreateInlineCommentResponseLinks', 'CreatePageBody', 'CreatePageBodyBody', 'CreatePageBodyStatus', 'CreatePageBodySubtype', 'CreatePageResponse', 'CreatePageResponseLinks', 'CreateSmartLinkBody', 'CreateSmartLinkResponse', 'CreateSmartLinkResponseLinks', 'CreateSpaceBody', 'CreateSpaceBodyDescription', 'CreateSpaceBodyRoleAssignmentsItem', 'CreateSpaceResponse', 'CreateSpaceResponseLinks', 'CreateSpaceRoleBody', 'CreateWhiteboardBody', 'CreateWhiteboardBodyLocale', 'CreateWhiteboardBodyTemplateKey', 'CreateWhiteboardResponse', 'CreateWhiteboardResponseLinks', 'CustomContentBodyBulk', 'CustomContentBodyRepresentation', 'CustomContentBodyRepresentationSingle', 'CustomContentBodySingle', 'CustomContentBodyWrite', 'CustomContentBodyWriteRepresentation', 'CustomContentBulk', 'CustomContentCommentModel', 'CustomContentLinks', 'CustomContentNestedBodyWrite', 'CustomContentSingle', 'CustomContentSingleLabels', 'CustomContentSingleOperations', 'CustomContentSingleProperties', 'CustomContentSingleVersions', 'CustomContentSortOrder', 'CustomContentVersion', 'DataPolicyMetadata', 'DataPolicySpace', 'DataPolicySpaceDataPolicy', 'DatabaseAdfDocument', 'DatabaseAdfDocumentType', 'DatabaseAiSummaryField', 'DatabaseAiSummaryFieldSettings', 'DatabaseAiSummaryFieldType', 'DatabaseAiSummaryRunMetadata', 'DatabaseAiSummaryValue', 'DatabaseAiSummaryValueMetadata', 'DatabaseAiSummaryValueMetadataLastUpdatedBy', 'DatabaseAiSummaryValueType', 'DatabaseAttachmentField', 'DatabaseAttachmentFieldType', 'DatabaseAttachmentRef', 'DatabaseAttachmentValue', 'DatabaseAttachmentValueType', 'DatabaseBacklinkField', 'DatabaseBacklinkFieldSettings', 'DatabaseBacklinkFieldType', 'DatabaseCheckboxField', 'DatabaseCheckboxFieldType', 'DatabaseCheckboxValue', 'DatabaseCheckboxValueType', 'DatabaseDateField', 'DatabaseDateFieldSettings', 'DatabaseDateFieldType', 'DatabaseDateValue', 'DatabaseDateValueType', 'DatabaseEmptyFieldSettings', 'DatabaseEntry', 'DatabaseEntryDetailsField', 'DatabaseEntryDetailsFieldSettings', 'DatabaseEntryDetailsFieldType', 'DatabaseEntryLinkField', 'DatabaseEntryLinkFieldType', 'DatabaseEntryLinkValue', 'DatabaseEntryLinkValueType', 'DatabaseEntryListResponse', 'DatabaseEntryRef', 'DatabaseEntrySingleResponse', 'DatabaseError', 'DatabaseErrorCode', 'DatabaseErrorResponse', 'DatabaseField', 'DatabaseFieldBase', 'DatabaseFieldListResponse', 'DatabaseFieldSettings', 'DatabaseFieldType', 'DatabaseFieldValue', 'DatabaseHyperlinkField', 'DatabaseHyperlinkFieldType', 'DatabaseHyperlinkItem', 'DatabaseHyperlinkValue', 'DatabaseHyperlinkValueType', 'DatabaseJiraIssueDetailsField', 'DatabaseJiraIssueDetailsFieldSettings', 'DatabaseJiraIssueDetailsFieldType', 'DatabaseJiraIssueField', 'DatabaseJiraIssueFieldSettings', 'DatabaseJiraIssueFieldType', 'DatabaseJiraIssueRef', 'DatabaseJiraIssueValue', 'DatabaseJiraIssueValueType', 'DatabaseLinks', 'DatabaseNullLookupValue', 'DatabaseNullLookupValueType', 'DatabaseNumberField', 'DatabaseNumberFieldSettings', 'DatabaseNumberFieldType', 'DatabaseNumberFormat', 'DatabaseNumberFormatType', 'DatabaseNumberValue', 'DatabaseNumberValueType', 'DatabasePageDetailsField', 'DatabasePageDetailsFieldSettings', 'DatabasePageDetailsFieldType', 'DatabasePageLabelsField', 'DatabasePageLabelsFieldType', 'DatabasePageLinkField', 'DatabasePageLinkFieldType', 'DatabasePageLinkValue', 'DatabasePageLinkValueType', 'DatabasePageRef', 'DatabasePageStatusField', 'DatabasePageStatusFieldType', 'DatabasePaginationMeta', 'DatabaseSelectField', 'DatabaseSelectFieldSettings', 'DatabaseSelectFieldType', 'DatabaseSelectOption', 'DatabaseSelectValue', 'DatabaseSelectValueType', 'DatabaseSingle', 'DatabaseSourceFieldSettings', 'DatabaseTextField', 'DatabaseTextFieldSettings', 'DatabaseTextFieldType', 'DatabaseTextValue', 'DatabaseTextValueType', 'DatabaseUserField', 'DatabaseUserFieldType', 'DatabaseUserRef', 'DatabaseUserValue', 'DatabaseUserValueType', 'DatabaseView', 'DatabaseViewListResponse', 'DatabaseViewType', 'DatabasesPublicApiLinks', 'DeleteBlogPostPermissionsOperation', 'DeleteBlogPostPermissionsPrincipalType', 'DeleteDatabasePermissionsOperation', 'DeleteDatabasePermissionsPrincipalType', 'DeleteFolderPermissionsOperation', 'DeleteFolderPermissionsPrincipalType', 'DeletePagePermissionsOperation', 'DeletePagePermissionsPrincipalType', 'DeleteSpaceRoleResponse', 'DeleteWhiteboardPermissionsOperation', 'DeleteWhiteboardPermissionsPrincipalType', 'DescendantsResponse', 'DetailedVersion', 'EnableAdminKeyBody', 'FolderLinks', 'FolderSingle', 'FooterCommentModel', 'FooterCommentModelLikes', 'FooterCommentModelOperations', 'FooterCommentModelProperties', 'FooterCommentModelVersions', 'GetAttachmentByIdResponse', 'GetAttachmentByIdResponseLinks', 'GetAttachmentCommentsResponse', 'GetAttachmentContentPropertiesResponse', 'GetAttachmentLabelsPrefix', 'GetAttachmentLabelsResponse', 'GetAttachmentVersionsResponse', 'GetAttachmentsResponse', 'GetAttachmentsStatusItem', 'GetAvailableSpacePermissionsResponse', 'GetAvailableSpaceRolesResponse', 'GetBlogPostByIdResponse', 'GetBlogPostByIdResponseLinks', 'GetBlogPostByIdStatusItem', 'GetBlogPostClassificationLevelStatus', 'GetBlogPostFooterCommentsResponse', 'GetBlogPostFooterCommentsStatusItem', 'GetBlogPostInlineCommentsResolutionStatusItem', 'GetBlogPostInlineCommentsResponse', 'GetBlogPostInlineCommentsStatusItem', 'GetBlogPostLabelsPrefix', 'GetBlogPostLabelsResponse', 'GetBlogPostLikeCountResponse', 'GetBlogPostLikeUsersResponse', 'GetBlogPostPermissionsOperation', 'GetBlogPostPermissionsPrincipalType', 'GetBlogPostPermissionsResponse', 'GetBlogPostVersionsResponse', 'GetBlogPostsInSpaceResponse', 'GetBlogPostsInSpaceStatusItem', 'GetBlogPostsResponse', 'GetBlogPostsStatusItem', 'GetBlogpostAttachmentsResponse', 'GetBlogpostAttachmentsStatusItem', 'GetBlogpostContentPropertiesResponse', 'GetChildCustomContentResponse', 'GetChildPagesResponse', 'GetCommentContentPropertiesResponse', 'GetCustomContentAttachmentsResponse', 'GetCustomContentAttachmentsStatusItem', 'GetCustomContentByIdResponse', 'GetCustomContentByIdResponseLinks', 'GetCustomContentByTypeInBlogPostResponse', 'GetCustomContentByTypeInPageResponse', 'GetCustomContentByTypeInSpaceResponse', 'GetCustomContentByTypeResponse', 'GetCustomContentCommentsResponse', 'GetCustomContentContentPropertiesResponse', 'GetCustomContentLabelsPrefix', 'GetCustomContentLabelsResponse', 'GetCustomContentVersionsResponse', 'GetDataPolicySpacesResponse', 'GetDatabaseAncestorsResponse', 'GetDatabaseByIdResponse', 'GetDatabaseByIdResponseLinks', 'GetDatabaseContentPropertiesResponse', 'GetDatabaseDescendantsResponse', 'GetDatabaseDirectChildrenResponse', 'GetDatabasePermissionsOperation', 'GetDatabasePermissionsPrincipalType', 'GetDatabasePermissionsResponse', 'GetFolderAncestorsResponse', 'GetFolderByIdResponse', 'GetFolderByIdResponseLinks', 'GetFolderContentPropertiesResponse', 'GetFolderDescendantsResponse', 'GetFolderDirectChildrenResponse', 'GetFolderPermissionsOperation', 'GetFolderPermissionsPrincipalType', 'GetFolderPermissionsResponse', 'GetFooterCommentByIdResponse', 'GetFooterCommentByIdResponseLinks', 'GetFooterCommentChildrenResponse', 'GetFooterCommentVersionsResponse', 'GetFooterCommentsResponse', 'GetFooterLikeCountResponse', 'GetFooterLikeUsersResponse', 'GetForgeAppPropertiesResponse', 'GetForgeAppPropertiesResponseResultsItem', 'GetForgeAppPropertyResponse', 'GetInlineCommentByIdResponse', 'GetInlineCommentByIdResponseLinks', 'GetInlineCommentChildrenResponse', 'GetInlineCommentVersionsResponse', 'GetInlineCommentsResponse', 'GetInlineLikeCountResponse', 'GetInlineLikeUsersResponse', 'GetLabelAttachmentsResponse', 'GetLabelBlogPostsResponse', 'GetLabelPagesResponse', 'GetLabelsResponse', 'GetPageAncestorsResponse', 'GetPageAttachmentsResponse', 'GetPageAttachmentsStatusItem', 'GetPageByIdResponse', 'GetPageByIdResponseLinks', 'GetPageByIdStatusItem', 'GetPageClassificationLevelStatus', 'GetPageContentPropertiesResponse', 'GetPageDescendantsResponse', 'GetPageDirectChildrenResponse', 'GetPageFooterCommentsResponse', 'GetPageFooterCommentsStatusItem', 'GetPageInlineCommentsResolutionStatusItem', 'GetPageInlineCommentsResponse', 'GetPageInlineCommentsStatusItem', 'GetPageLabelsPrefix', 'GetPageLabelsResponse', 'GetPageLikeCountResponse', 'GetPageLikeUsersResponse', 'GetPagePermissionsOperation', 'GetPagePermissionsPrincipalType', 'GetPagePermissionsResponse', 'GetPageVersionsResponse', 'GetPagesInSpaceDepth', 'GetPagesInSpaceResponse', 'GetPagesInSpaceStatusItem', 'GetPagesResponse', 'GetPagesStatusItem', 'GetPagesSubtype', 'GetSmartLinkAncestorsResponse', 'GetSmartLinkByIdResponse', 'GetSmartLinkByIdResponseLinks', 'GetSmartLinkContentPropertiesResponse', 'GetSmartLinkDescendantsResponse', 'GetSmartLinkDirectChildrenResponse', 'GetSpaceByIdResponse', 'GetSpaceByIdResponseLinks', 'GetSpaceContentLabelsPrefix', 'GetSpaceContentLabelsResponse', 'GetSpaceLabelsPrefix', 'GetSpaceLabelsResponse', 'GetSpacePermissionsAssignmentsResponse', 'GetSpacePropertiesResponse', 'GetSpaceRoleAssignmentsResponse', 'GetSpaceRoleModeResponse', 'GetSpaceRoleModeResponseMode', 'GetSpaceRolesByIdResponse', 'GetSpaceRolesByIdResponseLinks', 'GetSpacesResponse', 'GetSpacesStatus', 'GetSpacesType', 'GetTasksResponse', 'GetTasksStatus', 'GetWhiteboardAncestorsResponse', 'GetWhiteboardByIdResponse', 'GetWhiteboardByIdResponseLinks', 'GetWhiteboardContentPropertiesResponse', 'GetWhiteboardDescendantsResponse', 'GetWhiteboardDirectChildrenResponse', 'GetWhiteboardPermissionsOperation', 'GetWhiteboardPermissionsPrincipalType', 'GetWhiteboardPermissionsResponse', 'Icon', 'InlineCommentChildrenModel', 'InlineCommentModel', 'InlineCommentModelLikes', 'InlineCommentModelOperations', 'InlineCommentModelProperties', 'InlineCommentModelVersions', 'InlineCommentProperties', 'InlineCommentResolutionStatus', 'InviteByEmailBody', 'Label', 'LabelSortOrder', 'Like', 'ListSpacePermissionCombinationsResponse', 'MultiEntityLinks', 'OnlyArchivedAndCurrentContentStatus', 'Operation', 'OperationPermissionsInput', 'OperationPermissionsInputOperation', 'OptionalFieldLinks', 'OptionalFieldMeta', 'PageBodyWrite', 'PageBodyWriteRepresentation', 'PageBulk', 'PageCommentModel', 'PageInlineCommentModel', 'PageNestedBodyWrite', 'PageSingle', 'PageSingleLabels', 'PageSingleLikes', 'PageSingleOperations', 'PageSingleProperties', 'PageSingleVersions', 'PageSortOrder', 'PageVersion', 'ParentContentType', 'PermittedOperationsResponse', 'PostBlogPostClassificationLevelBody', 'PostBlogPostClassificationLevelBodyStatus', 'PostDatabaseClassificationLevelBody', 'PostDatabaseClassificationLevelBodyStatus', 'PostPageClassificationLevelBody', 'PostPageClassificationLevelBodyStatus', 'PostRedactBlogBody', 'PostRedactBlogBodyBody', 'PostRedactBlogBodyTitle', 'PostRedactPageBody', 'PostRedactPageBodyBody', 'PostRedactPageBodyTitle', 'PostWhiteboardClassificationLevelBody', 'PostWhiteboardClassificationLevelBodyStatus', 'PrimaryBodyRepresentation', 'PrimaryBodyRepresentationSingle', 'Principal', 'PrincipalType', 'PutBlogPostClassificationLevelBody', 'PutBlogPostClassificationLevelBodyStatus', 'PutDatabaseClassificationLevelBody', 'PutDatabaseClassificationLevelBodyStatus', 'PutPageClassificationLevelBody', 'PutPageClassificationLevelBodyStatus', 'PutSpaceDefaultClassificationLevelBody', 'PutWhiteboardClassificationLevelBody', 'PutWhiteboardClassificationLevelBodyStatus', 'Redaction', 'RedactionPointer', 'RedactionPointerResponse', 'RedactionResponse', 'RedactionSectionResponse', 'RestrictionStateResponse', 'RoleType', 'SetBlogPostRestrictionStateBody', 'SetDatabaseRestrictionStateBody', 'SetFolderRestrictionStateBody', 'SetPageRestrictionStateBody', 'SetSpaceRoleAssignmentsBodyItem', 'SetSpaceRoleAssignmentsResponse', 'SetWhiteboardRestrictionStateBody', 'SmartLinkLinks', 'SmartLinkSingle', 'SpaceBulk', 'SpaceDescription', 'SpaceDescriptionBodyRepresentation', 'SpaceIcon', 'SpaceLinks', 'SpacePermission', 'SpacePermissionAssignment', 'SpacePermissionAssignmentOperation', 'SpacePermissionAssignmentOperationKey', 'SpacePermissionAssignmentOperationTargetType', 'SpacePermissionAssignmentPrincipal', 'SpacePermissionAssignmentPrincipalType', 'SpaceProperty', 'SpacePropertyCreateRequest', 'SpacePropertyUpdateRequest', 'SpacePropertyUpdateRequestVersion', 'SpacePropertyVersion', 'SpaceRole', 'SpaceRoleAssignment', 'SpaceSingle', 'SpaceSingleLabels', 'SpaceSingleOperations', 'SpaceSinglePermissions', 'SpaceSingleProperties', 'SpaceSortOrder', 'SpaceStatus', 'SpaceType', 'Task', 'TaskBodySingle', 'TaskStatus', 'UpdateBlogPostBody', 'UpdateBlogPostBodyBody', 'UpdateBlogPostBodyStatus', 'UpdateBlogPostBodyVersion', 'UpdateBlogPostResponse', 'UpdateBlogPostResponseLinks', 'UpdateCustomContentBody', 'UpdateCustomContentBodyBody', 'UpdateCustomContentBodyStatus', 'UpdateCustomContentBodyVersion', 'UpdateCustomContentResponse', 'UpdateCustomContentResponseLinks', 'UpdateFooterCommentBody', 'UpdateFooterCommentBodyLinks', 'UpdateFooterCommentModel', 'UpdateFooterCommentModelBody', 'UpdateFooterCommentModelVersion', 'UpdateInlineCommentModel', 'UpdateInlineCommentModelBody', 'UpdateInlineCommentModelVersion', 'UpdateInlineCommentResponse', 'UpdateInlineCommentResponseLinks', 'UpdatePageBody', 'UpdatePageBodyBody', 'UpdatePageBodyStatus', 'UpdatePageBodyVersion', 'UpdatePageResponse', 'UpdatePageResponseLinks', 'UpdatePageTitleBody', 'UpdatePageTitleBodyStatus', 'UpdatePageTitleResponse', 'UpdatePageTitleResponseLinks', 'UpdateSpaceRoleBody', 'UpdateSpaceRoleResponse', 'UpdateTaskBody', 'UpdateTaskBodyStatus', 'User', 'Version', 'VersionSortOrder', 'VersionedEntity', 'WhiteboardLinks', 'WhiteboardSingle']

AbstractPageLinks = TypedDict(
    'AbstractPageLinks',
    {
    'webui': NotRequired["str"],
    'editui': NotRequired["str"],
    'tinyui': NotRequired["str"],
    },
)

type AccountStatus = Literal['active', 'inactive', 'closed', 'unknown']
"""The account status of the user."""

type AccountType = Literal['atlassian', 'app', 'customer', 'unknown']
"""The account type of the user."""

AdminKeyResponse = TypedDict(
    'AdminKeyResponse',
    {
    'account_id': NotRequired["str"],
    'expiration_time': NotRequired["str"],
    },
)

Ancestor = TypedDict(
    'Ancestor',
    {
    'id': NotRequired["str"],
    'type': NotRequired["AncestorType"],
    },
)

type AncestorType = Literal['page', 'whiteboard', 'database', 'embed', 'folder']
"""The type of ancestor."""

AttachmentBulk = TypedDict(
    'AttachmentBulk',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'created_at': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'media_type': NotRequired["str"],
    'media_type_description': NotRequired["str"],
    'comment': NotRequired["str"],
    'file_id': NotRequired["str"],
    'file_size': NotRequired["int"],
    'webui_link': NotRequired["str"],
    'download_link': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["AttachmentLinks"],
    },
)

AttachmentCommentModel = TypedDict(
    'AttachmentCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'attachment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'links': NotRequired["CommentLinks"],
    },
)

AttachmentLinks = TypedDict(
    'AttachmentLinks',
    {
    'webui': NotRequired["str"],
    'download': NotRequired["str"],
    },
)

AttachmentSingle = TypedDict(
    'AttachmentSingle',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'created_at': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'media_type': NotRequired["str"],
    'media_type_description': NotRequired["str"],
    'comment': NotRequired["str"],
    'file_id': NotRequired["str"],
    'file_size': NotRequired["int"],
    'webui_link': NotRequired["str"],
    'download_link': NotRequired["str"],
    'version': NotRequired["Version"],
    'labels': NotRequired["AttachmentSingleLabels"],
    'properties': NotRequired["AttachmentSingleProperties"],
    'operations': NotRequired["AttachmentSingleOperations"],
    'versions': NotRequired["AttachmentSingleVersions"],
    'links': NotRequired["AttachmentLinks"],
    },
)

AttachmentSingleLabels = TypedDict(
    'AttachmentSingleLabels',
    {
    'results': NotRequired["list[Label]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

AttachmentSingleOperations = TypedDict(
    'AttachmentSingleOperations',
    {
    'results': NotRequired["list[Operation]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

AttachmentSingleProperties = TypedDict(
    'AttachmentSingleProperties',
    {
    'results': NotRequired["list[ContentProperty]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

AttachmentSingleVersions = TypedDict(
    'AttachmentSingleVersions',
    {
    'results': NotRequired["list[Version]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

type AttachmentSortOrder = Literal['created-date', '-created-date', 'modified-date', '-modified-date']
"""The sort fields for attachments. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

AttachmentVersion = TypedDict(
    'AttachmentVersion',
    {
    'created_at': NotRequired["str"],
    'message': NotRequired["str"],
    'number': NotRequired["int"],
    'minor_edit': NotRequired["bool"],
    'author_id': NotRequired["str"],
    'attachment': NotRequired["VersionedEntity"],
    },
)

BlogPostBodyWrite = TypedDict(
    'BlogPostBodyWrite',
    {
    'representation': NotRequired["BlogPostBodyWriteRepresentation"],
    'value': NotRequired["str"],
    },
)

type BlogPostBodyWriteRepresentation = Literal['storage', 'atlas_doc_format', 'wiki']
"""Type of content representation used for the value field."""

BlogPostBulk = TypedDict(
    'BlogPostBulk',
    {
    'id': NotRequired["str"],
    'status': NotRequired["BlogPostContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'links': NotRequired["AbstractPageLinks"],
    },
)

BlogPostCommentModel = TypedDict(
    'BlogPostCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'links': NotRequired["CommentLinks"],
    },
)

type BlogPostContentStatus = Literal['current', 'draft', 'historical', 'trashed', 'deleted', 'any']
"""The status of the content."""

BlogPostInlineCommentModel = TypedDict(
    'BlogPostInlineCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'resolution_status': NotRequired["InlineCommentResolutionStatus"],
    'properties': NotRequired["InlineCommentProperties"],
    'links': NotRequired["CommentLinks"],
    },
)

BlogPostNestedBodyWrite = TypedDict(
    'BlogPostNestedBodyWrite',
    {
    'storage': NotRequired["BlogPostBodyWrite"],
    'atlas_doc_format': NotRequired["BlogPostBodyWrite"],
    'wiki': NotRequired["BlogPostBodyWrite"],
    },
)
"""
Body of the blog post. Only one body format should be specified as the property
for this object, e.g. `storage`.
"""

BlogPostSingle = TypedDict(
    'BlogPostSingle',
    {
    'id': NotRequired["str"],
    'status': NotRequired["BlogPostContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["BlogPostSingleLabels"],
    'properties': NotRequired["BlogPostSingleProperties"],
    'operations': NotRequired["BlogPostSingleOperations"],
    'likes': NotRequired["BlogPostSingleLikes"],
    'versions': NotRequired["BlogPostSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["AbstractPageLinks"],
    },
)

BlogPostSingleLabels = TypedDict(
    'BlogPostSingleLabels',
    {
    'results': NotRequired["list[Label]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

BlogPostSingleLikes = TypedDict(
    'BlogPostSingleLikes',
    {
    'results': NotRequired["list[Like]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

BlogPostSingleOperations = TypedDict(
    'BlogPostSingleOperations',
    {
    'results': NotRequired["list[Operation]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

BlogPostSingleProperties = TypedDict(
    'BlogPostSingleProperties',
    {
    'results': NotRequired["list[ContentProperty]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

BlogPostSingleVersions = TypedDict(
    'BlogPostSingleVersions',
    {
    'results': NotRequired["list[Version]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

type BlogPostSortOrder = Literal['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date']
"""The sort fields for blog posts. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

BlogPostVersion = TypedDict(
    'BlogPostVersion',
    {
    'created_at': NotRequired["str"],
    'message': NotRequired["str"],
    'number': NotRequired["int"],
    'minor_edit': NotRequired["bool"],
    'author_id': NotRequired["str"],
    'blogpost': NotRequired["VersionedEntity"],
    },
)

BodyBulk = TypedDict(
    'BodyBulk',
    {
    'storage': NotRequired["BodyType"],
    'atlas_doc_format': NotRequired["BodyType"],
    },
)
"""Contains fields for each representation type requested."""

BodySingle = TypedDict(
    'BodySingle',
    {
    'storage': NotRequired["BodyType"],
    'atlas_doc_format': NotRequired["BodyType"],
    'view': NotRequired["BodyType"],
    },
)
"""Contains fields for each representation type requested."""

BodyType = TypedDict(
    'BodyType',
    {
    'representation': NotRequired["str"],
    'value': NotRequired["str"],
    },
)

BulkAssignRolesRequest = TypedDict(
    'BulkAssignRolesRequest',
    {
    'assignments': "list[BulkTransitionRoleAssignment]",
    'space_selection': "BulkTransitionSpaceSelection",
    },
)

BulkRemoveAccessRequest = TypedDict(
    'BulkRemoveAccessRequest',
    {
    'permission_combination_ids': "list[str]",
    'space_selection': "BulkTransitionSpaceSelection",
    },
)

BulkTransitionCombinationEntry = TypedDict(
    'BulkTransitionCombinationEntry',
    {
    'combination_id': "str",
    'space_count': "int",
    'principal_count': "int",
    'permissions': "list[BulkTransitionDecodedPermission]",
    'principal_types': "list[BulkTransitionCombinationEntryPrincipalTypesItem]",
    },
)

type BulkTransitionCombinationEntryPrincipalTypesItem = Literal['USER', 'GROUP', 'GUEST', 'ANONYMOUS', 'ALL_LICENSED_USERS_USER_CLASS', 'ALL_PRODUCT_ADMINS_USER_CLASS', 'APP', 'TEAM']

BulkTransitionDecodedPermission = TypedDict(
    'BulkTransitionDecodedPermission',
    {
    'id': "str",
    'display_name': "str",
    },
)

BulkTransitionPrincipalTypeAssignment = TypedDict(
    'BulkTransitionPrincipalTypeAssignment',
    {
    'principal_type': "BulkTransitionPrincipalTypeAssignmentPrincipalType",
    'remove_access': "bool",
    'role_id': NotRequired["str | None"],
    },
)

type BulkTransitionPrincipalTypeAssignmentPrincipalType = Literal['USER', 'GROUP', 'GUEST', 'ANONYMOUS', 'ALL_LICENSED_USERS_USER_CLASS', 'ALL_PRODUCT_ADMINS_USER_CLASS', 'APP']
"""The type of principal."""

BulkTransitionRoleAssignment = TypedDict(
    'BulkTransitionRoleAssignment',
    {
    'permission_combination_id': "str",
    'principal_type_assignments': "list[BulkTransitionPrincipalTypeAssignment]",
    },
)

BulkTransitionSpaceSelection = TypedDict(
    'BulkTransitionSpaceSelection',
    {
    'space_type': "BulkTransitionSpaceSelectionSpaceType",
    'selected_spaces': NotRequired["list[BulkTransitionSpaceTarget]"],
    },
)

type BulkTransitionSpaceSelectionSpaceType = Literal['ALL', 'ALL_EXCEPT_PERSONAL', 'ALL_EXCEPT_SPECIFIC', 'PERSONAL', 'SPECIFIC']
"""The space selection type."""

BulkTransitionSpaceTarget = TypedDict(
    'BulkTransitionSpaceTarget',
    {
    'id': "str",
    'key': "str",
    },
)

BulkTransitionTaskResponse = TypedDict(
    'BulkTransitionTaskResponse',
    {
    'task_id': "str",
    'status': "BulkTransitionTaskResponseStatus",
    'status_url': "str",
    },
)

type BulkTransitionTaskResponseStatus = Literal['IN_PROGRESS', 'COMPLETED', 'FAILED']
"""The current status of the task."""

BulkTransitionTaskStatusResponse = TypedDict(
    'BulkTransitionTaskStatusResponse',
    {
    'task_id': "str",
    'status': "BulkTransitionTaskStatusResponseStatus",
    'error_message': NotRequired["str | None"],
    },
)

type BulkTransitionTaskStatusResponseStatus = Literal['IN_PROGRESS', 'COMPLETED', 'FAILED']
"""The current status of the task."""

CheckAccessByEmailBody = TypedDict(
    'CheckAccessByEmailBody',
    {
    'emails': "list[str]",
    },
)

CheckAccessByEmailResponse = TypedDict(
    'CheckAccessByEmailResponse',
    {
    'emails_without_access': NotRequired["list[str]"],
    'invalid_emails': NotRequired["list[str]"],
    },
)

ChildCustomContent = TypedDict(
    'ChildCustomContent',
    {
    'id': NotRequired["str"],
    'status': NotRequired["OnlyArchivedAndCurrentContentStatus"],
    'title': NotRequired["str"],
    'type': NotRequired["str"],
    'space_id': NotRequired["str"],
    },
)

type ChildCustomContentSortOrder = Literal['created-date', '-created-date', 'id', '-id', 'modified-date', '-modified-date']
"""The sort fields for child custom content. The default sort direction is ascending by id. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

ChildPage = TypedDict(
    'ChildPage',
    {
    'id': NotRequired["str"],
    'status': NotRequired["OnlyArchivedAndCurrentContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'child_position': NotRequired["int | None"],
    },
)

type ChildPageSortOrder = Literal['created-date', '-created-date', 'id', '-id', 'child-position', '-child-position', 'modified-date', '-modified-date']
"""The sort fields for child pages. The default sort direction is ascending by child-position. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

ChildrenCommentModel = TypedDict(
    'ChildrenCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'links': NotRequired["CommentLinks"],
    },
)

ChildrenResponse = TypedDict(
    'ChildrenResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["OnlyArchivedAndCurrentContentStatus"],
    'title': NotRequired["str"],
    'type': NotRequired["str"],
    'space_id': NotRequired["str"],
    'child_position': NotRequired["int | None"],
    },
)

ClassificationLevel = TypedDict(
    'ClassificationLevel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ClassificationLevelStatus"],
    'order': NotRequired["float"],
    'name': NotRequired["str"],
    'description': NotRequired["str"],
    'guideline': NotRequired["str"],
    'color': NotRequired["ClassificationLevelColor"],
    },
)
"""
A unit of [data classification](https://support.atlassian.com/security-and-access-policies/docs/what-is-data-classification/) defined by an organiation. 
A classification level may be associated with specific storage and handling requirements or expectations.
"""

type ClassificationLevelColor = Literal['RED', 'RED_BOLD', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'NAVY', 'TEAL', 'PURPLE', 'GREY', 'LIME']

type ClassificationLevelStatus = Literal['DRAFT', 'PUBLISHED', 'ARCHIVED']

CommentBodyWrite = TypedDict(
    'CommentBodyWrite',
    {
    'representation': NotRequired["CommentBodyWriteRepresentation"],
    'value': NotRequired["str"],
    },
)

type CommentBodyWriteRepresentation = Literal['storage', 'atlas_doc_format', 'wiki']
"""Type of content representation used for the value field."""

CommentLinks = TypedDict(
    'CommentLinks',
    {
    'webui': NotRequired["str"],
    },
)

CommentNestedBodyWrite = TypedDict(
    'CommentNestedBodyWrite',
    {
    'storage': NotRequired["CommentBodyWrite"],
    'atlas_doc_format': NotRequired["CommentBodyWrite"],
    'wiki': NotRequired["CommentBodyWrite"],
    },
)
"""
Body of the comment. Only one body format should be specified as the property
for this object, e.g. `storage`.
"""

type CommentSortOrder = Literal['created-date', '-created-date', 'modified-date', '-modified-date']
"""The sort fields for comments. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

CommentVersion = TypedDict(
    'CommentVersion',
    {
    'created_at': NotRequired["str"],
    'message': NotRequired["str"],
    'number': NotRequired["int"],
    'minor_edit': NotRequired["bool"],
    'author_id': NotRequired["str"],
    'comment': NotRequired["VersionedEntity"],
    },
)

ContentIdToContentTypeResponse = TypedDict(
    'ContentIdToContentTypeResponse',
    {
    'results': NotRequired["dict[str, ContentIdToContentTypeResponseResultsValue]"],
    },
)

type ContentIdToContentTypeResponseResultsValue = ContentIdToContentTypeResponseResultsValueOption1 | str

type ContentIdToContentTypeResponseResultsValueOption1 = Literal['page', 'blogpost', 'attachment', 'footer-comment', 'inline-comment']
"""Built in content types"""

ContentPermissionError = TypedDict(
    'ContentPermissionError',
    {
    'status': "int",
    'code': "str",
    'title': "str",
    'detail': NotRequired["str | None"],
    },
)

ContentPermissionErrorResponse = TypedDict(
    'ContentPermissionErrorResponse',
    {
    'errors': "list[ContentPermissionError]",
    },
)
"""An error response that follows the Atlassian REST API error standard."""

ContentPermissionOutput = TypedDict(
    'ContentPermissionOutput',
    {
    'operation': "ContentPermissionOutputOperation",
    'principal': "ContentPermissionPrincipal",
    'created_at': NotRequired["str"],
    'created_by': NotRequired["str"],
    'created_by_aaid': NotRequired["str"],
    },
)
"""A single direct-permission entry on a content item."""

type ContentPermissionOutputOperation = Literal['read', 'update']
"""The operation the permission grants."""

ContentPermissionPrincipal = TypedDict(
    'ContentPermissionPrincipal',
    {
    'principal_type': "ContentPermissionPrincipalPrincipalType",
    'principal_id': "str",
    },
)
"""A user or group principal on a content permission entry."""

type ContentPermissionPrincipalPrincipalType = Literal['user', 'group']
"""The type of principal."""

ContentPermissionsRequest = TypedDict(
    'ContentPermissionsRequest',
    {
    'permissions': "list[OperationPermissionsInput]",
    },
)
"""
A list of operation-grouped permission assignments.

The resulting direct-permission set cannot exceed 500 entries. Requests that would exceed this limit return a `400` response.
"""

ContentPermissionsResponse = TypedDict(
    'ContentPermissionsResponse',
    {
    'results': "list[ContentPermissionOutput]",
    'links': "MultiEntityLinks",
    },
)
"""
Contains up to 250 direct permissions on a content item. GET responses support cursor pagination to retrieve additional entries.

POST and PUT responses contain only the first 250 permissions from the resulting direct-permission set. Use the corresponding GET permissions endpoint to retrieve any remaining entries.
"""

ContentPrincipalInput = TypedDict(
    'ContentPrincipalInput',
    {
    'principal_type': "ContentPrincipalInputPrincipalType",
    'principal_id': "str",
    },
)
"""Identifies a user or group to assign a permission to."""

type ContentPrincipalInputPrincipalType = Literal['user', 'group']
"""The type of principal."""

ContentProperty = TypedDict(
    'ContentProperty',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    'version': NotRequired["Version"],
    },
)

ContentPropertyCreateRequest = TypedDict(
    'ContentPropertyCreateRequest',
    {
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    },
)

type ContentPropertySortOrder = Literal['key', '-key']
"""The sort fields for content properties. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

ContentPropertyUpdateRequest = TypedDict(
    'ContentPropertyUpdateRequest',
    {
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    'version': NotRequired["ContentPropertyUpdateRequestVersion"],
    },
)

ContentPropertyUpdateRequestVersion = TypedDict(
    'ContentPropertyUpdateRequestVersion',
    {
    'number': NotRequired["int"],
    'message': NotRequired["str"],
    },
)
"""New version number and associated message"""

type ContentRestrictionState = Literal['OPEN', 'EDIT_RESTRICTED', 'VIEW_RESTRICTED']
"""
The direct restriction state of a content item. Inherited restrictions are not represented by this REST enum.
- `OPEN` – No direct restrictions. Effective access may still be restricted by a parent.
- `EDIT_RESTRICTED` – Direct viewing is open but editing is restricted to explicitly granted users/groups.
- `VIEW_RESTRICTED` – Direct viewing and editing are restricted to explicitly granted users/groups.
"""

type ContentSortOrder = Literal['created-date', '-created-date', 'id', '-id', 'modified-date', '-modified-date', 'child-position', '-child-position', 'title', '-title']
"""The sort fields for hierarchical content types. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

type ContentStatus = Literal['current', 'draft', 'archived', 'historical', 'trashed', 'deleted', 'any']
"""The status of the content."""

ConvertContentIdsToContentTypesBody = TypedDict(
    'ConvertContentIdsToContentTypesBody',
    {
    'content_ids': "list[ConvertContentIdsToContentTypesBodyContentIdsItem]",
    },
)

type ConvertContentIdsToContentTypesBodyContentIdsItem = str | float

CreateBlogPostBody = TypedDict(
    'CreateBlogPostBody',
    {
    'space_id': "str",
    'status': NotRequired["CreateBlogPostBodyStatus"],
    'title': NotRequired["str"],
    'body': NotRequired["CreateBlogPostBodyBody"],
    'created_at': NotRequired["str"],
    },
)

type CreateBlogPostBodyBody = BlogPostBodyWrite | BlogPostNestedBodyWrite

type CreateBlogPostBodyStatus = Literal['current', 'draft']
"""The status of the blog post, specifies if the blog post will be created as a new blog post or a draft"""

CreateBlogPostResponse = TypedDict(
    'CreateBlogPostResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["BlogPostContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["BlogPostSingleLabels"],
    'properties': NotRequired["BlogPostSingleProperties"],
    'operations': NotRequired["BlogPostSingleOperations"],
    'likes': NotRequired["BlogPostSingleLikes"],
    'versions': NotRequired["BlogPostSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["CreateBlogPostResponseLinks"],
    },
)

CreateBlogPostResponseLinks = TypedDict(
    'CreateBlogPostResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateBulkUserLookupBody = TypedDict(
    'CreateBulkUserLookupBody',
    {
    'account_ids': "list[str]",
    },
)

CreateBulkUserLookupResponse = TypedDict(
    'CreateBulkUserLookupResponse',
    {
    'results': NotRequired["list[User]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<User>"""

CreateCustomContentBody = TypedDict(
    'CreateCustomContentBody',
    {
    'type': "str",
    'status': NotRequired["CreateCustomContentBodyStatus"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'title': "str",
    'body': "CreateCustomContentBodyBody",
    },
)

type CreateCustomContentBodyBody = CustomContentBodyWrite | CustomContentNestedBodyWrite

type CreateCustomContentBodyStatus = Literal['current', 'draft']
"""The status of the custom content. Defaults to `current` when status not provided."""

CreateCustomContentResponse = TypedDict(
    'CreateCustomContentResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'labels': NotRequired["CustomContentSingleLabels"],
    'properties': NotRequired["CustomContentSingleProperties"],
    'operations': NotRequired["CustomContentSingleOperations"],
    'versions': NotRequired["CustomContentSingleVersions"],
    'body': NotRequired["CustomContentBodySingle"],
    'links': NotRequired["CreateCustomContentResponseLinks"],
    },
)

CreateCustomContentResponseLinks = TypedDict(
    'CreateCustomContentResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateDatabaseBody = TypedDict(
    'CreateDatabaseBody',
    {
    'space_id': "str",
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    },
)

CreateDatabaseResponse = TypedDict(
    'CreateDatabaseResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["CreateDatabaseResponseLinks"],
    },
)

CreateDatabaseResponseLinks = TypedDict(
    'CreateDatabaseResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateFolderBody = TypedDict(
    'CreateFolderBody',
    {
    'space_id': "str",
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    },
)

CreateFolderResponse = TypedDict(
    'CreateFolderResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["CreateFolderResponseLinks"],
    },
)

CreateFolderResponseLinks = TypedDict(
    'CreateFolderResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateFooterCommentModel = TypedDict(
    'CreateFooterCommentModel',
    {
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'attachment_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'body': NotRequired["CreateFooterCommentModelBody"],
    },
)

type CreateFooterCommentModelBody = CommentBodyWrite | CommentNestedBodyWrite

CreateFooterCommentResponse = TypedDict(
    'CreateFooterCommentResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'attachment_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'properties': NotRequired["FooterCommentModelProperties"],
    'operations': NotRequired["FooterCommentModelOperations"],
    'likes': NotRequired["FooterCommentModelLikes"],
    'versions': NotRequired["FooterCommentModelVersions"],
    'body': NotRequired["BodySingle"],
    'links': NotRequired["CreateFooterCommentResponseLinks"],
    },
)

CreateFooterCommentResponseLinks = TypedDict(
    'CreateFooterCommentResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateInlineCommentModel = TypedDict(
    'CreateInlineCommentModel',
    {
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'body': NotRequired["CreateInlineCommentModelBody"],
    'inline_comment_properties': NotRequired["CreateInlineCommentModelInlineCommentProperties"],
    },
)

type CreateInlineCommentModelBody = CommentBodyWrite | CommentNestedBodyWrite

CreateInlineCommentModelInlineCommentProperties = TypedDict(
    'CreateInlineCommentModelInlineCommentProperties',
    {
    'text_selection': NotRequired["str"],
    'text_selection_match_count': NotRequired["int"],
    'text_selection_match_index': NotRequired["int"],
    },
)
"""Object describing the text to highlight on the page/blog post. Only applicable for top level inline comments (not replies) and required in that case."""

CreateInlineCommentResponse = TypedDict(
    'CreateInlineCommentResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'resolution_last_modifier_id': NotRequired["str"],
    'resolution_last_modified_at': NotRequired["str"],
    'resolution_status': NotRequired["InlineCommentResolutionStatus"],
    'properties': NotRequired["InlineCommentModelProperties"],
    'operations': NotRequired["InlineCommentModelOperations"],
    'likes': NotRequired["InlineCommentModelLikes"],
    'versions': NotRequired["InlineCommentModelVersions"],
    'links': NotRequired["CreateInlineCommentResponseLinks"],
    },
)

CreateInlineCommentResponseLinks = TypedDict(
    'CreateInlineCommentResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreatePageBody = TypedDict(
    'CreatePageBody',
    {
    'space_id': "str",
    'status': NotRequired["CreatePageBodyStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'body': NotRequired["CreatePageBodyBody"],
    'subtype': NotRequired["CreatePageBodySubtype"],
    },
)

type CreatePageBodyBody = PageBodyWrite | PageNestedBodyWrite

type CreatePageBodyStatus = Literal['current', 'draft']
"""The status of the page, published or draft."""

type CreatePageBodySubtype = Literal['live']
"""The subtype of the page. Provide the subtype live to create a live doc or no subtype to create a page."""

CreatePageResponse = TypedDict(
    'CreatePageResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str | None"],
    'last_owner_id': NotRequired["str | None"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["PageSingleLabels"],
    'properties': NotRequired["PageSingleProperties"],
    'operations': NotRequired["PageSingleOperations"],
    'likes': NotRequired["PageSingleLikes"],
    'versions': NotRequired["PageSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["CreatePageResponseLinks"],
    },
)

CreatePageResponseLinks = TypedDict(
    'CreatePageResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateSmartLinkBody = TypedDict(
    'CreateSmartLinkBody',
    {
    'space_id': "str",
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'embed_url': NotRequired["str"],
    },
)

CreateSmartLinkResponse = TypedDict(
    'CreateSmartLinkResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'embed_url': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["CreateSmartLinkResponseLinks"],
    },
)

CreateSmartLinkResponseLinks = TypedDict(
    'CreateSmartLinkResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateSpaceBody = TypedDict(
    'CreateSpaceBody',
    {
    'name': "str",
    'key': NotRequired["str"],
    'alias': NotRequired["str"],
    'description': NotRequired["CreateSpaceBodyDescription"],
    'role_assignments': NotRequired["list[CreateSpaceBodyRoleAssignmentsItem]"],
    'copy_space_access_configuration': NotRequired["int"],
    'create_private_space': NotRequired["bool"],
    'template_key': NotRequired["str"],
    },
)

CreateSpaceBodyDescription = TypedDict(
    'CreateSpaceBodyDescription',
    {
    'value': NotRequired["str"],
    'representation': NotRequired["str"],
    },
)
"""The description of the new/updated space. Note, only the 'plain' representation is currently supported."""

CreateSpaceBodyRoleAssignmentsItem = TypedDict(
    'CreateSpaceBodyRoleAssignmentsItem',
    {
    'principal': NotRequired["Principal"],
    'role_id': NotRequired["str"],
    },
)
"""The role assignments for the new space. If none are provided, the Default Space Roles are applied. If roles are provided, the space is created with exactly the provided set of roles. A private space is created if only the creator is assigned to a role and it’s the Admin role. At least one Admin role assignment must be specified."""

CreateSpaceResponse = TypedDict(
    'CreateSpaceResponse',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'type': NotRequired["SpaceType"],
    'status': NotRequired["SpaceStatus"],
    'author_id': NotRequired["str"],
    'space_owner_id': NotRequired["str"],
    'current_active_alias': NotRequired["str"],
    'created_at': NotRequired["str"],
    'homepage_id': NotRequired["str"],
    'description': NotRequired["SpaceDescription"],
    'icon': NotRequired["SpaceIcon"],
    'links': NotRequired["CreateSpaceResponseLinks"],
    },
)

CreateSpaceResponseLinks = TypedDict(
    'CreateSpaceResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CreateSpaceRoleBody = TypedDict(
    'CreateSpaceRoleBody',
    {
    'name': "str",
    'description': "str",
    'space_permissions': "list[str]",
    },
)

CreateWhiteboardBody = TypedDict(
    'CreateWhiteboardBody',
    {
    'space_id': "str",
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'template_key': NotRequired["CreateWhiteboardBodyTemplateKey"],
    'locale': NotRequired["CreateWhiteboardBodyLocale"],
    },
)

type CreateWhiteboardBodyLocale = Literal['de-DE', 'cs-CZ', 'ko-KR', 'fr-FR', 'it-IT', 'ja-JP', 'nl-NL', 'nb-NO', 'da-DK', 'sv-SE', 'fi-FI', 'ru-RU', 'pl-PL', 'tr-TR', 'hu-HU', 'en-GB', 'en-US', 'pt-BR', 'zh-CN', 'zh-TW', 'es-ES']
"""If templateKey is provided, locale will decide which language the template will be created with. If locale is omitted, the user's locale will be used."""

type CreateWhiteboardBodyTemplateKey = Literal['2x2-prioritization', '4ls-retro', 'annual-calendar', 'brainwriting', 'concept-map', 'crazy-8s', 'daily-sync', 'disruptive-brainstorm', 'dot-voting', 'elevator-pitch', 'flow-chart', 'gap-analysis', 'ice-breakers', 'incident-postmortem', 'journey-mapping-kit', 'kanban-board', 'lean-coffee', 'network-of-teams', 'org-chart', 'pi-planning', 'prioritization', 'prioritization-experiment', 'product-roadmap', 'product-vision-board', 'rice', 'sailboat-retro', 'service-blueprint', 'simple-retrospective', 'sprint-planning', 'sticky-note-pack', 'swimlanes', 'team-formation-guide', 'timeline', 'timeline-workflow', 'user-story-map', 'workflow', 'vision-board', 'venn-diagram', 'storyboard', 'action-plan', 'root-cause-analysis', 'executive-summary', 'stakeholder-mapping', 'annual-calendar-2025-2026', 'health-monitor', 'okr-planning', 'swot-analysis', 'poker-planning', 'fishbone-diagram', 'risk-assessment', 'bounded-context', 'hopes-and-fears', 'swimlane-vertical']
"""Providing a template key will add that template to the new whiteboard."""

CreateWhiteboardResponse = TypedDict(
    'CreateWhiteboardResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["CreateWhiteboardResponseLinks"],
    },
)

CreateWhiteboardResponseLinks = TypedDict(
    'CreateWhiteboardResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

CustomContentBodyBulk = TypedDict(
    'CustomContentBodyBulk',
    {
    'raw': NotRequired["BodyType"],
    'storage': NotRequired["BodyType"],
    'atlas_doc_format': NotRequired["BodyType"],
    },
)
"""Contains fields for each representation type requested."""

type CustomContentBodyRepresentation = Literal['raw', 'storage', 'atlas_doc_format']
"""The formats a custom content body can be represented as. A subset of BodyRepresentation."""

type CustomContentBodyRepresentationSingle = Literal['raw', 'storage', 'atlas_doc_format', 'view', 'export_view', 'anonymous_export_view']
"""The formats a custom content body can be represented as. A subset of BodyRepresentation."""

CustomContentBodySingle = TypedDict(
    'CustomContentBodySingle',
    {
    'raw': NotRequired["BodyType"],
    'storage': NotRequired["BodyType"],
    'atlas_doc_format': NotRequired["BodyType"],
    'view': NotRequired["BodyType"],
    },
)
"""Contains fields for each representation type requested."""

CustomContentBodyWrite = TypedDict(
    'CustomContentBodyWrite',
    {
    'representation': NotRequired["CustomContentBodyWriteRepresentation"],
    'value': NotRequired["str"],
    },
)

type CustomContentBodyWriteRepresentation = Literal['storage', 'atlas_doc_format', 'raw']
"""Type of content representation used for the value field."""

CustomContentBulk = TypedDict(
    'CustomContentBulk',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["CustomContentBodyBulk"],
    'links': NotRequired["CustomContentLinks"],
    },
)

CustomContentCommentModel = TypedDict(
    'CustomContentCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'links': NotRequired["CommentLinks"],
    },
)

CustomContentLinks = TypedDict(
    'CustomContentLinks',
    {
    'webui': NotRequired["str"],
    },
)

CustomContentNestedBodyWrite = TypedDict(
    'CustomContentNestedBodyWrite',
    {
    'storage': NotRequired["CustomContentBodyWrite"],
    'atlas_doc_format': NotRequired["CustomContentBodyWrite"],
    'raw': NotRequired["CustomContentBodyWrite"],
    },
)
"""
Body of the custom content. Only one body format should be specified as the property
for this object, e.g. `storage`.
"""

CustomContentSingle = TypedDict(
    'CustomContentSingle',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'labels': NotRequired["CustomContentSingleLabels"],
    'properties': NotRequired["CustomContentSingleProperties"],
    'operations': NotRequired["CustomContentSingleOperations"],
    'versions': NotRequired["CustomContentSingleVersions"],
    'body': NotRequired["CustomContentBodySingle"],
    'links': NotRequired["CustomContentLinks"],
    },
)

CustomContentSingleLabels = TypedDict(
    'CustomContentSingleLabels',
    {
    'results': NotRequired["list[Label]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

CustomContentSingleOperations = TypedDict(
    'CustomContentSingleOperations',
    {
    'results': NotRequired["list[Operation]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

CustomContentSingleProperties = TypedDict(
    'CustomContentSingleProperties',
    {
    'results': NotRequired["list[ContentProperty]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

CustomContentSingleVersions = TypedDict(
    'CustomContentSingleVersions',
    {
    'results': NotRequired["list[Version]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

type CustomContentSortOrder = Literal['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title']
"""The sort fields for custom content. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

CustomContentVersion = TypedDict(
    'CustomContentVersion',
    {
    'created_at': NotRequired["str"],
    'message': NotRequired["str"],
    'number': NotRequired["int"],
    'minor_edit': NotRequired["bool"],
    'author_id': NotRequired["str"],
    'custom': NotRequired["VersionedEntity"],
    },
)

DataPolicyMetadata = TypedDict(
    'DataPolicyMetadata',
    {
    'any_content_blocked': NotRequired["bool"],
    },
)
"""Details about data policies."""

DataPolicySpace = TypedDict(
    'DataPolicySpace',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'description': NotRequired["SpaceDescription"],
    'data_policy': NotRequired["DataPolicySpaceDataPolicy"],
    'icon': NotRequired["SpaceIcon"],
    'links': NotRequired["SpaceLinks"],
    },
)

DataPolicySpaceDataPolicy = TypedDict(
    'DataPolicySpaceDataPolicy',
    {
    'any_content_blocked': NotRequired["bool"],
    },
)

DatabaseAdfDocument = TypedDict(
    'DatabaseAdfDocument',
    {
    'version': "int",
    'type': "DatabaseAdfDocumentType",
    'content': NotRequired["list[Any]"],
    },
)
"""Minimal Atlassian Document Format envelope."""

type DatabaseAdfDocumentType = Literal['doc']

DatabaseAiSummaryField = TypedDict(
    'DatabaseAiSummaryField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseAiSummaryFieldType",
    'settings': "DatabaseAiSummaryFieldSettings",
    },
)

DatabaseAiSummaryFieldSettings = TypedDict(
    'DatabaseAiSummaryFieldSettings',
    {
    'ai_run_metadata': NotRequired["DatabaseAiSummaryRunMetadata"],
    },
)

type DatabaseAiSummaryFieldType = Literal['aiSummary']

DatabaseAiSummaryRunMetadata = TypedDict(
    'DatabaseAiSummaryRunMetadata',
    {
    'last_ai_run_user_account_id': "str | None",
    },
)

DatabaseAiSummaryValue = TypedDict(
    'DatabaseAiSummaryValue',
    {
    'type': "DatabaseAiSummaryValueType",
    'plain': "str | None",
    'rich': "DatabaseAdfDocument | None",
    'metadata': "DatabaseAiSummaryValueMetadata | None",
    },
)

DatabaseAiSummaryValueMetadata = TypedDict(
    'DatabaseAiSummaryValueMetadata',
    {
    'last_updated_at': "str | None",
    'last_updated_by': "DatabaseAiSummaryValueMetadataLastUpdatedBy | None",
    'last_updated_user_account_id': "str | None",
    },
)

type DatabaseAiSummaryValueMetadataLastUpdatedBy = Literal['ai', 'user']

type DatabaseAiSummaryValueType = Literal['aiSummary']

DatabaseAttachmentField = TypedDict(
    'DatabaseAttachmentField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseAttachmentFieldType",
    'settings': "DatabaseEmptyFieldSettings",
    },
)

type DatabaseAttachmentFieldType = Literal['attachment']

DatabaseAttachmentRef = TypedDict(
    'DatabaseAttachmentRef',
    {
    'media_id': "str",
    },
)

DatabaseAttachmentValue = TypedDict(
    'DatabaseAttachmentValue',
    {
    'type': "DatabaseAttachmentValueType",
    'value': "list[DatabaseAttachmentRef] | None",
    },
)

type DatabaseAttachmentValueType = Literal['attachment']

DatabaseBacklinkField = TypedDict(
    'DatabaseBacklinkField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseBacklinkFieldType",
    'settings': "DatabaseBacklinkFieldSettings",
    },
)

DatabaseBacklinkFieldSettings = TypedDict(
    'DatabaseBacklinkFieldSettings',
    {
    'source_database_content_id': NotRequired["str"],
    },
)

type DatabaseBacklinkFieldType = Literal['backlink']

DatabaseCheckboxField = TypedDict(
    'DatabaseCheckboxField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseCheckboxFieldType",
    'settings': "DatabaseEmptyFieldSettings",
    },
)

type DatabaseCheckboxFieldType = Literal['checkbox']

DatabaseCheckboxValue = TypedDict(
    'DatabaseCheckboxValue',
    {
    'type': "DatabaseCheckboxValueType",
    'value': "bool | None",
    },
)

type DatabaseCheckboxValueType = Literal['checkbox']

DatabaseDateField = TypedDict(
    'DatabaseDateField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseDateFieldType",
    'settings': "DatabaseDateFieldSettings",
    },
)

DatabaseDateFieldSettings = TypedDict(
    'DatabaseDateFieldSettings',
    {
    'includes_time': "bool",
    },
)

type DatabaseDateFieldType = Literal['date']

DatabaseDateValue = TypedDict(
    'DatabaseDateValue',
    {
    'type': "DatabaseDateValueType",
    'value': "str | None",
    },
)

type DatabaseDateValueType = Literal['date']

type DatabaseEmptyFieldSettings = dict[str, Any]
"""Field types with no type-specific settings."""

DatabaseEntry = TypedDict(
    'DatabaseEntry',
    {
    'id': "str",
    'database_id': "str",
    'values': "dict[str, DatabaseFieldValue]",
    },
)
"""A single entry (row) within a database."""

DatabaseEntryDetailsField = TypedDict(
    'DatabaseEntryDetailsField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseEntryDetailsFieldType",
    'settings': "DatabaseEntryDetailsFieldSettings",
    },
)

DatabaseEntryDetailsFieldSettings = TypedDict(
    'DatabaseEntryDetailsFieldSettings',
    {
    'source_field_id': NotRequired["str"],
    'lookup_field_id': NotRequired["str"],
    },
)

type DatabaseEntryDetailsFieldType = Literal['entryDetails']

DatabaseEntryLinkField = TypedDict(
    'DatabaseEntryLinkField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseEntryLinkFieldType",
    'settings': "DatabaseEmptyFieldSettings",
    },
)

type DatabaseEntryLinkFieldType = Literal['entryLink']

DatabaseEntryLinkValue = TypedDict(
    'DatabaseEntryLinkValue',
    {
    'type': "DatabaseEntryLinkValueType",
    'value': "list[DatabaseEntryRef] | None",
    },
)

type DatabaseEntryLinkValueType = Literal['entryLink']

DatabaseEntryListResponse = TypedDict(
    'DatabaseEntryListResponse',
    {
    'results': "list[DatabaseEntry]",
    'links': "DatabasesPublicApiLinks",
    'meta': "DatabasePaginationMeta",
    },
)

DatabaseEntryRef = TypedDict(
    'DatabaseEntryRef',
    {
    'entry_id': "str",
    'database_content_id': NotRequired["str"],
    },
)

DatabaseEntrySingleResponse = TypedDict(
    'DatabaseEntrySingleResponse',
    {
    'id': "str",
    'database_id': "str",
    'values': "dict[str, DatabaseFieldValue]",
    'links': "DatabasesPublicApiLinks",
    },
)
"""
A single entry, not wrapped in a `results` array, with a `_links.self`
path and an absolute `_links.base` URL.
"""

DatabaseError = TypedDict(
    'DatabaseError',
    {
    'id': NotRequired["str"],
    'status': "int",
    'code': "DatabaseErrorCode",
    'title': "str",
    'detail': NotRequired["str | None"],
    },
)

type DatabaseErrorCode = Literal['INVALID_CURSOR', 'UNSUPPORTED_CURSOR_VERSION', 'CURSOR_QUERY_MISMATCH', 'INVALID_FILTER', 'UNSUPPORTED_FILTER_OPERATOR', 'FIELD_NOT_FILTERABLE', 'FIELD_NOT_SORTABLE', 'UNSUPPORTED_SORT_MODIFIER', 'INVALID_SORT', 'INVALID_PAGE_LIMIT', 'DATABASE_NOT_FOUND', 'ENTRY_NOT_FOUND', 'DATABASE_TOO_LARGE', 'SERVICE_DISABLED', 'SERVICE_UNAVAILABLE', 'REQUEST_TIMEOUT']
"""Stable machine-readable error code."""

DatabaseErrorResponse = TypedDict(
    'DatabaseErrorResponse',
    {
    'errors': "list[DatabaseError]",
    },
)
"""
Structured Confluence V2 error envelope. The HTTP status and `code` are
the stable machine-readable contract. `title` and `detail` are
human-readable, and their exact text is not stable; clients must not use
them for program logic.
"""

type DatabaseField = DatabaseTextField | DatabaseAiSummaryField | DatabaseNumberField | DatabaseCheckboxField | DatabaseDateField | DatabaseSelectField | DatabaseHyperlinkField | DatabaseUserField | DatabaseAttachmentField | DatabaseJiraIssueField | DatabasePageLinkField | DatabaseEntryLinkField | DatabaseEntryDetailsField | DatabaseBacklinkField | DatabasePageDetailsField | DatabasePageLabelsField | DatabasePageStatusField | DatabaseJiraIssueDetailsField
"""A field definition whose strict settings shape is selected by `type`."""

DatabaseFieldBase = TypedDict(
    'DatabaseFieldBase',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    },
)

DatabaseFieldListResponse = TypedDict(
    'DatabaseFieldListResponse',
    {
    'results': "list[DatabaseField]",
    'links': "DatabasesPublicApiLinks",
    'meta': "DatabasePaginationMeta",
    },
)

type DatabaseFieldSettings = DatabaseTextFieldSettings | DatabaseAiSummaryFieldSettings | DatabaseNumberFieldSettings | DatabaseSelectFieldSettings | DatabaseDateFieldSettings | DatabaseJiraIssueFieldSettings | DatabaseEntryDetailsFieldSettings | DatabaseJiraIssueDetailsFieldSettings | DatabasePageDetailsFieldSettings | DatabaseSourceFieldSettings | DatabaseBacklinkFieldSettings | DatabaseEmptyFieldSettings
"""
Strict settings shape selected by the parent `DatabaseField.type`.
Lookup-field settings expose source identifiers but lookup values remain
`null` in this representation version. Types without projected settings
return an empty object.
"""

type DatabaseFieldType = Literal['text', 'aiSummary', 'number', 'checkbox', 'date', 'select', 'hyperlink', 'user', 'attachment', 'jiraIssue', 'pageLink', 'entryLink', 'entryDetails', 'backlink', 'pageDetails', 'pageLabels', 'pageStatus', 'jiraIssueDetails']
"""The type of a database field."""

type DatabaseFieldValue = DatabaseTextValue | DatabaseAiSummaryValue | DatabaseNumberValue | DatabaseCheckboxValue | DatabaseDateValue | DatabaseSelectValue | DatabaseHyperlinkValue | DatabaseUserValue | DatabaseAttachmentValue | DatabaseJiraIssueValue | DatabasePageLinkValue | DatabaseEntryLinkValue | DatabaseNullLookupValue
"""
The value of a single field on an entry, discriminated on `type`. Shape
varies by field type: some are stored directly, some are stable references
to other resources, and lookup-derived field values are objects with a
`value` property of `null`.
"""

DatabaseHyperlinkField = TypedDict(
    'DatabaseHyperlinkField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseHyperlinkFieldType",
    'settings': "DatabaseEmptyFieldSettings",
    },
)

type DatabaseHyperlinkFieldType = Literal['hyperlink']

DatabaseHyperlinkItem = TypedDict(
    'DatabaseHyperlinkItem',
    {
    'url': "str",
    'label': NotRequired["str"],
    },
)

DatabaseHyperlinkValue = TypedDict(
    'DatabaseHyperlinkValue',
    {
    'type': "DatabaseHyperlinkValueType",
    'value': "list[DatabaseHyperlinkItem] | None",
    },
)

type DatabaseHyperlinkValueType = Literal['hyperlink']

DatabaseJiraIssueDetailsField = TypedDict(
    'DatabaseJiraIssueDetailsField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseJiraIssueDetailsFieldType",
    'settings': "DatabaseJiraIssueDetailsFieldSettings",
    },
)

DatabaseJiraIssueDetailsFieldSettings = TypedDict(
    'DatabaseJiraIssueDetailsFieldSettings',
    {
    'source_field_id': NotRequired["str"],
    'jira_field_key': NotRequired["str"],
    },
)

type DatabaseJiraIssueDetailsFieldType = Literal['jiraIssueDetails']

DatabaseJiraIssueField = TypedDict(
    'DatabaseJiraIssueField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseJiraIssueFieldType",
    'settings': "DatabaseJiraIssueFieldSettings",
    },
)

DatabaseJiraIssueFieldSettings = TypedDict(
    'DatabaseJiraIssueFieldSettings',
    {
    'cloud_id': NotRequired["str"],
    'server_id': NotRequired["str"],
    },
)

type DatabaseJiraIssueFieldType = Literal['jiraIssue']

DatabaseJiraIssueRef = TypedDict(
    'DatabaseJiraIssueRef',
    {
    'key': "str",
    'cloud_id': NotRequired["str"],
    'server_id': NotRequired["str"],
    },
)

DatabaseJiraIssueValue = TypedDict(
    'DatabaseJiraIssueValue',
    {
    'type': "DatabaseJiraIssueValueType",
    'value': "list[DatabaseJiraIssueRef] | None",
    },
)

type DatabaseJiraIssueValueType = Literal['jiraIssue']

DatabaseLinks = TypedDict(
    'DatabaseLinks',
    {
    'webui': NotRequired["str"],
    },
)

DatabaseNullLookupValue = TypedDict(
    'DatabaseNullLookupValue',
    {
    'type': "DatabaseNullLookupValueType",
    'value': "None | None",
    },
)
"""
Lookup-derived field types (entryDetails, backlink, pageDetails,
pageLabels, pageStatus, jiraIssueDetails) return objects with a `value`
property of `null`.
"""

type DatabaseNullLookupValueType = Literal['entryDetails', 'backlink', 'pageDetails', 'pageLabels', 'pageStatus', 'jiraIssueDetails']

DatabaseNumberField = TypedDict(
    'DatabaseNumberField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseNumberFieldType",
    'settings': "DatabaseNumberFieldSettings",
    },
)

DatabaseNumberFieldSettings = TypedDict(
    'DatabaseNumberFieldSettings',
    {
    'format': NotRequired["DatabaseNumberFormat"],
    },
)

type DatabaseNumberFieldType = Literal['number']

DatabaseNumberFormat = TypedDict(
    'DatabaseNumberFormat',
    {
    'type': "DatabaseNumberFormatType",
    'prefix': NotRequired["str"],
    'suffix': NotRequired["str"],
    'decimal_places': NotRequired["int"],
    },
)

type DatabaseNumberFormatType = Literal['number', 'percent', 'currency', 'custom']

DatabaseNumberValue = TypedDict(
    'DatabaseNumberValue',
    {
    'type': "DatabaseNumberValueType",
    'value': "str | None",
    },
)

type DatabaseNumberValueType = Literal['number']

DatabasePageDetailsField = TypedDict(
    'DatabasePageDetailsField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabasePageDetailsFieldType",
    'settings': "DatabasePageDetailsFieldSettings",
    },
)

DatabasePageDetailsFieldSettings = TypedDict(
    'DatabasePageDetailsFieldSettings',
    {
    'source_field_id': NotRequired["str"],
    'page_property_key': NotRequired["str"],
    },
)

type DatabasePageDetailsFieldType = Literal['pageDetails']

DatabasePageLabelsField = TypedDict(
    'DatabasePageLabelsField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabasePageLabelsFieldType",
    'settings': "DatabaseSourceFieldSettings",
    },
)

type DatabasePageLabelsFieldType = Literal['pageLabels']

DatabasePageLinkField = TypedDict(
    'DatabasePageLinkField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabasePageLinkFieldType",
    'settings': "DatabaseEmptyFieldSettings",
    },
)

type DatabasePageLinkFieldType = Literal['pageLink']

DatabasePageLinkValue = TypedDict(
    'DatabasePageLinkValue',
    {
    'type': "DatabasePageLinkValueType",
    'value': "list[DatabasePageRef] | None",
    },
)

type DatabasePageLinkValueType = Literal['pageLink']

DatabasePageRef = TypedDict(
    'DatabasePageRef',
    {
    'content_id': "str",
    },
)

DatabasePageStatusField = TypedDict(
    'DatabasePageStatusField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabasePageStatusFieldType",
    'settings': "DatabaseSourceFieldSettings",
    },
)

type DatabasePageStatusFieldType = Literal['pageStatus']

DatabasePaginationMeta = TypedDict(
    'DatabasePaginationMeta',
    {
    'page_size': "int",
    'cursor': NotRequired["str"],
    'has_more': "bool",
    },
)

DatabaseSelectField = TypedDict(
    'DatabaseSelectField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseSelectFieldType",
    'settings': "DatabaseSelectFieldSettings",
    },
)

DatabaseSelectFieldSettings = TypedDict(
    'DatabaseSelectFieldSettings',
    {
    'options': "list[DatabaseSelectOption]",
    },
)

type DatabaseSelectFieldType = Literal['select']

DatabaseSelectOption = TypedDict(
    'DatabaseSelectOption',
    {
    'id': "str",
    'label': "str",
    },
)

DatabaseSelectValue = TypedDict(
    'DatabaseSelectValue',
    {
    'type': "DatabaseSelectValueType",
    'value': "list[DatabaseSelectOption] | None",
    },
)

type DatabaseSelectValueType = Literal['select']

DatabaseSingle = TypedDict(
    'DatabaseSingle',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["DatabaseLinks"],
    },
)

DatabaseSourceFieldSettings = TypedDict(
    'DatabaseSourceFieldSettings',
    {
    'source_field_id': NotRequired["str"],
    },
)

DatabaseTextField = TypedDict(
    'DatabaseTextField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseTextFieldType",
    'settings': "DatabaseTextFieldSettings",
    },
)

DatabaseTextFieldSettings = TypedDict(
    'DatabaseTextFieldSettings',
    {
    'rich_text': "bool",
    },
)

type DatabaseTextFieldType = Literal['text']

DatabaseTextValue = TypedDict(
    'DatabaseTextValue',
    {
    'type': "DatabaseTextValueType",
    'plain': "str | None",
    'rich': "DatabaseAdfDocument | None",
    },
)

type DatabaseTextValueType = Literal['text']

DatabaseUserField = TypedDict(
    'DatabaseUserField',
    {
    'id': "str",
    'name': "str",
    'description': "str | None",
    'type': "DatabaseUserFieldType",
    'settings': "DatabaseEmptyFieldSettings",
    },
)

type DatabaseUserFieldType = Literal['user']

DatabaseUserRef = TypedDict(
    'DatabaseUserRef',
    {
    'account_id': "str",
    },
)

DatabaseUserValue = TypedDict(
    'DatabaseUserValue',
    {
    'type': "DatabaseUserValueType",
    'value': "list[DatabaseUserRef] | None",
    },
)

type DatabaseUserValueType = Literal['user']

DatabaseView = TypedDict(
    'DatabaseView',
    {
    'id': "str",
    'name': "str",
    'type': "DatabaseViewType",
    },
)
"""Metadata for a named view on a database."""

DatabaseViewListResponse = TypedDict(
    'DatabaseViewListResponse',
    {
    'results': "list[DatabaseView]",
    'links': "DatabasesPublicApiLinks",
    'meta': "DatabasePaginationMeta",
    },
)

type DatabaseViewType = Literal['table', 'gallery', 'board', 'calendar', 'timeline']

DatabasesPublicApiLinks = TypedDict(
    'DatabasesPublicApiLinks',
    {
    'self': "str",
    'base': "str",
    'next': NotRequired["str"],
    },
)
"""
Links for a Databases API representation. `self` and `next` are
path-only URLs. `base` is the absolute canonical Confluence site base URL.
`next` is present only when another page exists. Additional future link
relations may be added without a representation-version bump.
"""

type DeleteBlogPostPermissionsOperation = Literal['read', 'update']

type DeleteBlogPostPermissionsPrincipalType = Literal['user', 'group']

type DeleteDatabasePermissionsOperation = Literal['read', 'update']

type DeleteDatabasePermissionsPrincipalType = Literal['user', 'group']

type DeleteFolderPermissionsOperation = Literal['read', 'update']

type DeleteFolderPermissionsPrincipalType = Literal['user', 'group']

type DeletePagePermissionsOperation = Literal['read', 'update']

type DeletePagePermissionsPrincipalType = Literal['user', 'group']

DeleteSpaceRoleResponse = TypedDict(
    'DeleteSpaceRoleResponse',
    {
    'task_id': NotRequired["str"],
    },
)

type DeleteWhiteboardPermissionsOperation = Literal['read', 'update']

type DeleteWhiteboardPermissionsPrincipalType = Literal['user', 'group']

DescendantsResponse = TypedDict(
    'DescendantsResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["OnlyArchivedAndCurrentContentStatus"],
    'title': NotRequired["str"],
    'type': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'depth': NotRequired["int"],
    'child_position': NotRequired["int | None"],
    },
)

DetailedVersion = TypedDict(
    'DetailedVersion',
    {
    'number': NotRequired["int"],
    'author_id': NotRequired["str"],
    'message': NotRequired["str"],
    'created_at': NotRequired["str"],
    'minor_edit': NotRequired["bool"],
    'content_type_modified': NotRequired["bool"],
    'collaborators': NotRequired["list[str]"],
    'prev_version': NotRequired["int"],
    'next_version': NotRequired["int"],
    },
)

EnableAdminKeyBody = TypedDict(
    'EnableAdminKeyBody',
    {
    'duration_in_minutes': NotRequired["int"],
    },
)

FolderLinks = TypedDict(
    'FolderLinks',
    {
    'webui': NotRequired["str"],
    },
)

FolderSingle = TypedDict(
    'FolderSingle',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["FolderLinks"],
    },
)

FooterCommentModel = TypedDict(
    'FooterCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'attachment_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'properties': NotRequired["FooterCommentModelProperties"],
    'operations': NotRequired["FooterCommentModelOperations"],
    'likes': NotRequired["FooterCommentModelLikes"],
    'versions': NotRequired["FooterCommentModelVersions"],
    'body': NotRequired["BodySingle"],
    'links': NotRequired["CommentLinks"],
    },
)

FooterCommentModelLikes = TypedDict(
    'FooterCommentModelLikes',
    {
    'results': NotRequired["list[Like]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

FooterCommentModelOperations = TypedDict(
    'FooterCommentModelOperations',
    {
    'results': NotRequired["list[Operation]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

FooterCommentModelProperties = TypedDict(
    'FooterCommentModelProperties',
    {
    'results': NotRequired["list[ContentProperty]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

FooterCommentModelVersions = TypedDict(
    'FooterCommentModelVersions',
    {
    'results': NotRequired["list[Version]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

GetAttachmentByIdResponse = TypedDict(
    'GetAttachmentByIdResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'created_at': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'media_type': NotRequired["str"],
    'media_type_description': NotRequired["str"],
    'comment': NotRequired["str"],
    'file_id': NotRequired["str"],
    'file_size': NotRequired["int"],
    'webui_link': NotRequired["str"],
    'download_link': NotRequired["str"],
    'version': NotRequired["Version"],
    'labels': NotRequired["AttachmentSingleLabels"],
    'properties': NotRequired["AttachmentSingleProperties"],
    'operations': NotRequired["AttachmentSingleOperations"],
    'versions': NotRequired["AttachmentSingleVersions"],
    'links': NotRequired["GetAttachmentByIdResponseLinks"],
    },
)

GetAttachmentByIdResponseLinks = TypedDict(
    'GetAttachmentByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetAttachmentCommentsResponse = TypedDict(
    'GetAttachmentCommentsResponse',
    {
    'results': NotRequired["list[AttachmentCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<AttachmentCommentModel>"""

GetAttachmentContentPropertiesResponse = TypedDict(
    'GetAttachmentContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

type GetAttachmentLabelsPrefix = Literal['my', 'team', 'global', 'system']

GetAttachmentLabelsResponse = TypedDict(
    'GetAttachmentLabelsResponse',
    {
    'results': NotRequired["list[Label]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Label>"""

GetAttachmentVersionsResponse = TypedDict(
    'GetAttachmentVersionsResponse',
    {
    'results': NotRequired["list[AttachmentVersion]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Version>"""

GetAttachmentsResponse = TypedDict(
    'GetAttachmentsResponse',
    {
    'results': NotRequired["list[AttachmentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Attachment>"""

type GetAttachmentsStatusItem = Literal['current', 'archived', 'trashed']

GetAvailableSpacePermissionsResponse = TypedDict(
    'GetAvailableSpacePermissionsResponse',
    {
    'results': NotRequired["list[SpacePermission]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<SpacePermission>"""

GetAvailableSpaceRolesResponse = TypedDict(
    'GetAvailableSpaceRolesResponse',
    {
    'results': NotRequired["list[SpaceRole]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<SpaceRole>"""

GetBlogPostByIdResponse = TypedDict(
    'GetBlogPostByIdResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["BlogPostContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["BlogPostSingleLabels"],
    'properties': NotRequired["BlogPostSingleProperties"],
    'operations': NotRequired["BlogPostSingleOperations"],
    'likes': NotRequired["BlogPostSingleLikes"],
    'versions': NotRequired["BlogPostSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["GetBlogPostByIdResponseLinks"],
    },
)

GetBlogPostByIdResponseLinks = TypedDict(
    'GetBlogPostByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

type GetBlogPostByIdStatusItem = Literal['current', 'trashed', 'deleted', 'historical', 'draft']

type GetBlogPostClassificationLevelStatus = Literal['current', 'draft', 'archived']

GetBlogPostFooterCommentsResponse = TypedDict(
    'GetBlogPostFooterCommentsResponse',
    {
    'results': NotRequired["list[BlogPostCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<BlogPostCommentModel>"""

type GetBlogPostFooterCommentsStatusItem = Literal['current', 'deleted', 'trashed', 'historical', 'draft']

type GetBlogPostInlineCommentsResolutionStatusItem = Literal['resolved', 'open', 'dangling', 'reopened']

GetBlogPostInlineCommentsResponse = TypedDict(
    'GetBlogPostInlineCommentsResponse',
    {
    'results': NotRequired["list[BlogPostInlineCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<BlogPostInlineCommentModel>"""

type GetBlogPostInlineCommentsStatusItem = Literal['current', 'deleted', 'trashed', 'historical', 'draft']

type GetBlogPostLabelsPrefix = Literal['my', 'team', 'global', 'system']

GetBlogPostLabelsResponse = TypedDict(
    'GetBlogPostLabelsResponse',
    {
    'results': NotRequired["list[Label]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Label>"""

GetBlogPostLikeCountResponse = TypedDict(
    'GetBlogPostLikeCountResponse',
    {
    'count': NotRequired["int"],
    },
)
"""Integer"""

GetBlogPostLikeUsersResponse = TypedDict(
    'GetBlogPostLikeUsersResponse',
    {
    'results': NotRequired["list[Like]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<String>"""

type GetBlogPostPermissionsOperation = Literal['read', 'update']

type GetBlogPostPermissionsPrincipalType = Literal['user', 'group']

GetBlogPostPermissionsResponse = TypedDict(
    'GetBlogPostPermissionsResponse',
    {
    'results': NotRequired["list[ContentPermissionOutput]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentPermissionOutput>"""

GetBlogPostVersionsResponse = TypedDict(
    'GetBlogPostVersionsResponse',
    {
    'results': NotRequired["list[BlogPostVersion]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Version>"""

GetBlogPostsInSpaceResponse = TypedDict(
    'GetBlogPostsInSpaceResponse',
    {
    'results': NotRequired["list[BlogPostBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<BlogPost>"""

type GetBlogPostsInSpaceStatusItem = Literal['current', 'deleted', 'trashed']

GetBlogPostsResponse = TypedDict(
    'GetBlogPostsResponse',
    {
    'results': NotRequired["list[BlogPostBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<BlogPost>"""

type GetBlogPostsStatusItem = Literal['current', 'deleted', 'trashed']

GetBlogpostAttachmentsResponse = TypedDict(
    'GetBlogpostAttachmentsResponse',
    {
    'results': NotRequired["list[AttachmentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Attachment>"""

type GetBlogpostAttachmentsStatusItem = Literal['current', 'archived', 'trashed']

GetBlogpostContentPropertiesResponse = TypedDict(
    'GetBlogpostContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

GetChildCustomContentResponse = TypedDict(
    'GetChildCustomContentResponse',
    {
    'results': NotRequired["list[ChildCustomContent]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildCustomContent>"""

GetChildPagesResponse = TypedDict(
    'GetChildPagesResponse',
    {
    'results': NotRequired["list[ChildPage]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildPage>"""

GetCommentContentPropertiesResponse = TypedDict(
    'GetCommentContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

GetCustomContentAttachmentsResponse = TypedDict(
    'GetCustomContentAttachmentsResponse',
    {
    'results': NotRequired["list[AttachmentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Attachment>"""

type GetCustomContentAttachmentsStatusItem = Literal['current', 'archived', 'trashed']

GetCustomContentByIdResponse = TypedDict(
    'GetCustomContentByIdResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'labels': NotRequired["CustomContentSingleLabels"],
    'properties': NotRequired["CustomContentSingleProperties"],
    'operations': NotRequired["CustomContentSingleOperations"],
    'versions': NotRequired["CustomContentSingleVersions"],
    'body': NotRequired["CustomContentBodySingle"],
    'links': NotRequired["GetCustomContentByIdResponseLinks"],
    },
)

GetCustomContentByIdResponseLinks = TypedDict(
    'GetCustomContentByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetCustomContentByTypeInBlogPostResponse = TypedDict(
    'GetCustomContentByTypeInBlogPostResponse',
    {
    'results': NotRequired["list[CustomContentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<CustomContent>"""

GetCustomContentByTypeInPageResponse = TypedDict(
    'GetCustomContentByTypeInPageResponse',
    {
    'results': NotRequired["list[CustomContentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<CustomContent>"""

GetCustomContentByTypeInSpaceResponse = TypedDict(
    'GetCustomContentByTypeInSpaceResponse',
    {
    'results': NotRequired["list[CustomContentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<CustomContent>"""

GetCustomContentByTypeResponse = TypedDict(
    'GetCustomContentByTypeResponse',
    {
    'results': NotRequired["list[CustomContentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<CustomContent>"""

GetCustomContentCommentsResponse = TypedDict(
    'GetCustomContentCommentsResponse',
    {
    'results': NotRequired["list[CustomContentCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<CustomContentCommentModel>"""

GetCustomContentContentPropertiesResponse = TypedDict(
    'GetCustomContentContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

type GetCustomContentLabelsPrefix = Literal['my', 'team', 'global', 'system']

GetCustomContentLabelsResponse = TypedDict(
    'GetCustomContentLabelsResponse',
    {
    'results': NotRequired["list[Label]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Label>"""

GetCustomContentVersionsResponse = TypedDict(
    'GetCustomContentVersionsResponse',
    {
    'results': NotRequired["list[CustomContentVersion]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Version>"""

GetDataPolicySpacesResponse = TypedDict(
    'GetDataPolicySpacesResponse',
    {
    'results': NotRequired["list[DataPolicySpace]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<DataPolicySpace>"""

GetDatabaseAncestorsResponse = TypedDict(
    'GetDatabaseAncestorsResponse',
    {
    'results': NotRequired["list[Ancestor]"],
    },
)
"""MultiEntityResult<Ancestor>"""

GetDatabaseByIdResponse = TypedDict(
    'GetDatabaseByIdResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["GetDatabaseByIdResponseLinks"],
    },
)

GetDatabaseByIdResponseLinks = TypedDict(
    'GetDatabaseByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetDatabaseContentPropertiesResponse = TypedDict(
    'GetDatabaseContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

GetDatabaseDescendantsResponse = TypedDict(
    'GetDatabaseDescendantsResponse',
    {
    'results': NotRequired["list[DescendantsResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<DescendantsResponse>"""

GetDatabaseDirectChildrenResponse = TypedDict(
    'GetDatabaseDirectChildrenResponse',
    {
    'results': NotRequired["list[ChildrenResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildrenResponse>"""

type GetDatabasePermissionsOperation = Literal['read', 'update']

type GetDatabasePermissionsPrincipalType = Literal['user', 'group']

GetDatabasePermissionsResponse = TypedDict(
    'GetDatabasePermissionsResponse',
    {
    'results': NotRequired["list[ContentPermissionOutput]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentPermissionOutput>"""

GetFolderAncestorsResponse = TypedDict(
    'GetFolderAncestorsResponse',
    {
    'results': NotRequired["list[Ancestor]"],
    },
)
"""MultiEntityResult<Ancestor>"""

GetFolderByIdResponse = TypedDict(
    'GetFolderByIdResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["GetFolderByIdResponseLinks"],
    },
)

GetFolderByIdResponseLinks = TypedDict(
    'GetFolderByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetFolderContentPropertiesResponse = TypedDict(
    'GetFolderContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

GetFolderDescendantsResponse = TypedDict(
    'GetFolderDescendantsResponse',
    {
    'results': NotRequired["list[DescendantsResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<DescendantsResponse>"""

GetFolderDirectChildrenResponse = TypedDict(
    'GetFolderDirectChildrenResponse',
    {
    'results': NotRequired["list[ChildrenResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildrenResponse>"""

type GetFolderPermissionsOperation = Literal['read', 'update']

type GetFolderPermissionsPrincipalType = Literal['user', 'group']

GetFolderPermissionsResponse = TypedDict(
    'GetFolderPermissionsResponse',
    {
    'results': NotRequired["list[ContentPermissionOutput]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentPermissionOutput>"""

GetFooterCommentByIdResponse = TypedDict(
    'GetFooterCommentByIdResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'attachment_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'properties': NotRequired["FooterCommentModelProperties"],
    'operations': NotRequired["FooterCommentModelOperations"],
    'likes': NotRequired["FooterCommentModelLikes"],
    'versions': NotRequired["FooterCommentModelVersions"],
    'body': NotRequired["BodySingle"],
    'links': NotRequired["GetFooterCommentByIdResponseLinks"],
    },
)

GetFooterCommentByIdResponseLinks = TypedDict(
    'GetFooterCommentByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetFooterCommentChildrenResponse = TypedDict(
    'GetFooterCommentChildrenResponse',
    {
    'results': NotRequired["list[ChildrenCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildrenCommentModel>"""

GetFooterCommentVersionsResponse = TypedDict(
    'GetFooterCommentVersionsResponse',
    {
    'results': NotRequired["list[CommentVersion]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Version>"""

GetFooterCommentsResponse = TypedDict(
    'GetFooterCommentsResponse',
    {
    'results': NotRequired["list[FooterCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<FooterCommentModel>"""

GetFooterLikeCountResponse = TypedDict(
    'GetFooterLikeCountResponse',
    {
    'count': NotRequired["int"],
    },
)
"""Integer"""

GetFooterLikeUsersResponse = TypedDict(
    'GetFooterLikeUsersResponse',
    {
    'results': NotRequired["list[Like]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<String>"""

GetForgeAppPropertiesResponse = TypedDict(
    'GetForgeAppPropertiesResponse',
    {
    'results': NotRequired["list[GetForgeAppPropertiesResponseResultsItem]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<AppProperty>"""

GetForgeAppPropertiesResponseResultsItem = TypedDict(
    'GetForgeAppPropertiesResponseResultsItem',
    {
    'key': NotRequired["str"],
    'value': NotRequired["dict[str, Any]"],
    },
)

GetForgeAppPropertyResponse = TypedDict(
    'GetForgeAppPropertyResponse',
    {
    'key': NotRequired["str"],
    'value': NotRequired["dict[str, Any]"],
    },
)

GetInlineCommentByIdResponse = TypedDict(
    'GetInlineCommentByIdResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'resolution_last_modifier_id': NotRequired["str"],
    'resolution_last_modified_at': NotRequired["str"],
    'resolution_status': NotRequired["InlineCommentResolutionStatus"],
    'properties': NotRequired["InlineCommentModelProperties"],
    'operations': NotRequired["InlineCommentModelOperations"],
    'likes': NotRequired["InlineCommentModelLikes"],
    'versions': NotRequired["InlineCommentModelVersions"],
    'links': NotRequired["GetInlineCommentByIdResponseLinks"],
    },
)

GetInlineCommentByIdResponseLinks = TypedDict(
    'GetInlineCommentByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetInlineCommentChildrenResponse = TypedDict(
    'GetInlineCommentChildrenResponse',
    {
    'results': NotRequired["list[InlineCommentChildrenModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<InlineCommentChildrenModel>"""

GetInlineCommentVersionsResponse = TypedDict(
    'GetInlineCommentVersionsResponse',
    {
    'results': NotRequired["list[CommentVersion]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Version>"""

GetInlineCommentsResponse = TypedDict(
    'GetInlineCommentsResponse',
    {
    'results': NotRequired["list[InlineCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<InlineCommentModel>"""

GetInlineLikeCountResponse = TypedDict(
    'GetInlineLikeCountResponse',
    {
    'count': NotRequired["int"],
    },
)
"""Integer"""

GetInlineLikeUsersResponse = TypedDict(
    'GetInlineLikeUsersResponse',
    {
    'results': NotRequired["list[Like]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<String>"""

GetLabelAttachmentsResponse = TypedDict(
    'GetLabelAttachmentsResponse',
    {
    'results': NotRequired["list[AttachmentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Attachment>"""

GetLabelBlogPostsResponse = TypedDict(
    'GetLabelBlogPostsResponse',
    {
    'results': NotRequired["list[BlogPostBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<BlogPost>"""

GetLabelPagesResponse = TypedDict(
    'GetLabelPagesResponse',
    {
    'results': NotRequired["list[PageBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Page>"""

GetLabelsResponse = TypedDict(
    'GetLabelsResponse',
    {
    'results': NotRequired["list[Label]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Label>"""

GetPageAncestorsResponse = TypedDict(
    'GetPageAncestorsResponse',
    {
    'results': NotRequired["list[Ancestor]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Ancestor>"""

GetPageAttachmentsResponse = TypedDict(
    'GetPageAttachmentsResponse',
    {
    'results': NotRequired["list[AttachmentBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Attachment>"""

type GetPageAttachmentsStatusItem = Literal['current', 'archived', 'trashed']

GetPageByIdResponse = TypedDict(
    'GetPageByIdResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str | None"],
    'last_owner_id': NotRequired["str | None"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["PageSingleLabels"],
    'properties': NotRequired["PageSingleProperties"],
    'operations': NotRequired["PageSingleOperations"],
    'likes': NotRequired["PageSingleLikes"],
    'versions': NotRequired["PageSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["GetPageByIdResponseLinks"],
    },
)

GetPageByIdResponseLinks = TypedDict(
    'GetPageByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

type GetPageByIdStatusItem = Literal['current', 'archived', 'trashed', 'deleted', 'historical', 'draft']

type GetPageClassificationLevelStatus = Literal['current', 'draft', 'archived']

GetPageContentPropertiesResponse = TypedDict(
    'GetPageContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

GetPageDescendantsResponse = TypedDict(
    'GetPageDescendantsResponse',
    {
    'results': NotRequired["list[DescendantsResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<DescendantsResponse>"""

GetPageDirectChildrenResponse = TypedDict(
    'GetPageDirectChildrenResponse',
    {
    'results': NotRequired["list[ChildrenResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildrenResponse>"""

GetPageFooterCommentsResponse = TypedDict(
    'GetPageFooterCommentsResponse',
    {
    'results': NotRequired["list[PageCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<PageCommentModel>"""

type GetPageFooterCommentsStatusItem = Literal['current', 'archived', 'trashed', 'deleted', 'historical', 'draft']

type GetPageInlineCommentsResolutionStatusItem = Literal['resolved', 'open', 'dangling', 'reopened']

GetPageInlineCommentsResponse = TypedDict(
    'GetPageInlineCommentsResponse',
    {
    'results': NotRequired["list[PageInlineCommentModel]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<PageInlineCommentModel>"""

type GetPageInlineCommentsStatusItem = Literal['current', 'archived', 'trashed', 'deleted', 'historical', 'draft']

type GetPageLabelsPrefix = Literal['my', 'team', 'global', 'system']

GetPageLabelsResponse = TypedDict(
    'GetPageLabelsResponse',
    {
    'results': NotRequired["list[Label]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Label>"""

GetPageLikeCountResponse = TypedDict(
    'GetPageLikeCountResponse',
    {
    'count': NotRequired["int"],
    },
)
"""Integer"""

GetPageLikeUsersResponse = TypedDict(
    'GetPageLikeUsersResponse',
    {
    'results': NotRequired["list[Like]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<String>"""

type GetPagePermissionsOperation = Literal['read', 'update']

type GetPagePermissionsPrincipalType = Literal['user', 'group']

GetPagePermissionsResponse = TypedDict(
    'GetPagePermissionsResponse',
    {
    'results': NotRequired["list[ContentPermissionOutput]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentPermissionOutput>"""

GetPageVersionsResponse = TypedDict(
    'GetPageVersionsResponse',
    {
    'results': NotRequired["list[PageVersion]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Version>"""

type GetPagesInSpaceDepth = Literal['all', 'root']

GetPagesInSpaceResponse = TypedDict(
    'GetPagesInSpaceResponse',
    {
    'results': NotRequired["list[PageBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Page>"""

type GetPagesInSpaceStatusItem = Literal['current', 'archived', 'deleted', 'trashed']

GetPagesResponse = TypedDict(
    'GetPagesResponse',
    {
    'results': NotRequired["list[PageBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Page>"""

type GetPagesStatusItem = Literal['current', 'archived', 'deleted', 'trashed']

type GetPagesSubtype = Literal['live', 'page']

GetSmartLinkAncestorsResponse = TypedDict(
    'GetSmartLinkAncestorsResponse',
    {
    'results': NotRequired["list[Ancestor]"],
    },
)
"""MultiEntityResult<Ancestor>"""

GetSmartLinkByIdResponse = TypedDict(
    'GetSmartLinkByIdResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'embed_url': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["GetSmartLinkByIdResponseLinks"],
    },
)

GetSmartLinkByIdResponseLinks = TypedDict(
    'GetSmartLinkByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetSmartLinkContentPropertiesResponse = TypedDict(
    'GetSmartLinkContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

GetSmartLinkDescendantsResponse = TypedDict(
    'GetSmartLinkDescendantsResponse',
    {
    'results': NotRequired["list[DescendantsResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<DescendantsResponse>"""

GetSmartLinkDirectChildrenResponse = TypedDict(
    'GetSmartLinkDirectChildrenResponse',
    {
    'results': NotRequired["list[ChildrenResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildrenResponse>"""

GetSpaceByIdResponse = TypedDict(
    'GetSpaceByIdResponse',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'type': NotRequired["SpaceType"],
    'status': NotRequired["SpaceStatus"],
    'author_id': NotRequired["str"],
    'space_owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'homepage_id': NotRequired["str"],
    'description': NotRequired["SpaceDescription"],
    'icon': NotRequired["SpaceIcon"],
    'labels': NotRequired["SpaceSingleLabels"],
    'properties': NotRequired["SpaceSingleProperties"],
    'operations': NotRequired["SpaceSingleOperations"],
    'permissions': NotRequired["SpaceSinglePermissions"],
    'links': NotRequired["GetSpaceByIdResponseLinks"],
    },
)

GetSpaceByIdResponseLinks = TypedDict(
    'GetSpaceByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

type GetSpaceContentLabelsPrefix = Literal['my', 'team']

GetSpaceContentLabelsResponse = TypedDict(
    'GetSpaceContentLabelsResponse',
    {
    'results': NotRequired["list[Label]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Label>"""

type GetSpaceLabelsPrefix = Literal['my', 'team']

GetSpaceLabelsResponse = TypedDict(
    'GetSpaceLabelsResponse',
    {
    'results': NotRequired["list[Label]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Label>"""

GetSpacePermissionsAssignmentsResponse = TypedDict(
    'GetSpacePermissionsAssignmentsResponse',
    {
    'results': NotRequired["list[SpacePermissionAssignment]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<SpacePermissionAssignment>"""

GetSpacePropertiesResponse = TypedDict(
    'GetSpacePropertiesResponse',
    {
    'results': NotRequired["list[SpaceProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<SpaceProperty>"""

GetSpaceRoleAssignmentsResponse = TypedDict(
    'GetSpaceRoleAssignmentsResponse',
    {
    'results': NotRequired["list[SpaceRoleAssignment]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<SpaceRoleAssignment>"""

GetSpaceRoleModeResponse = TypedDict(
    'GetSpaceRoleModeResponse',
    {
    'mode': NotRequired["GetSpaceRoleModeResponseMode"],
    },
)

type GetSpaceRoleModeResponseMode = Literal['PRE_ROLES', 'ROLES_TRANSITION', 'ROLES']
"""The space role mode."""

GetSpaceRolesByIdResponse = TypedDict(
    'GetSpaceRolesByIdResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["RoleType"],
    'name': NotRequired["str"],
    'description': NotRequired["str"],
    'space_permissions': NotRequired["list[str]"],
    'links': NotRequired["GetSpaceRolesByIdResponseLinks"],
    },
)

GetSpaceRolesByIdResponseLinks = TypedDict(
    'GetSpaceRolesByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetSpacesResponse = TypedDict(
    'GetSpacesResponse',
    {
    'results': NotRequired["list[SpaceBulk]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Space>"""

type GetSpacesStatus = Literal['current', 'archived', 'trashed']

type GetSpacesType = Literal['global', 'collaboration', 'knowledge_base', 'personal', 'system', 'onboarding', 'xflow_sample_space']

GetTasksResponse = TypedDict(
    'GetTasksResponse',
    {
    'results': NotRequired["list[Task]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<Task>"""

type GetTasksStatus = Literal['complete', 'incomplete']

GetWhiteboardAncestorsResponse = TypedDict(
    'GetWhiteboardAncestorsResponse',
    {
    'results': NotRequired["list[Ancestor]"],
    },
)
"""MultiEntityResult<Ancestor>"""

GetWhiteboardByIdResponse = TypedDict(
    'GetWhiteboardByIdResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["GetWhiteboardByIdResponseLinks"],
    },
)

GetWhiteboardByIdResponseLinks = TypedDict(
    'GetWhiteboardByIdResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

GetWhiteboardContentPropertiesResponse = TypedDict(
    'GetWhiteboardContentPropertiesResponse',
    {
    'results': NotRequired["list[ContentProperty]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentProperty>"""

GetWhiteboardDescendantsResponse = TypedDict(
    'GetWhiteboardDescendantsResponse',
    {
    'results': NotRequired["list[DescendantsResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<DescendantsResponse>"""

GetWhiteboardDirectChildrenResponse = TypedDict(
    'GetWhiteboardDirectChildrenResponse',
    {
    'results': NotRequired["list[ChildrenResponse]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ChildrenResponse>"""

type GetWhiteboardPermissionsOperation = Literal['read', 'update']

type GetWhiteboardPermissionsPrincipalType = Literal['user', 'group']

GetWhiteboardPermissionsResponse = TypedDict(
    'GetWhiteboardPermissionsResponse',
    {
    'results': NotRequired["list[ContentPermissionOutput]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<ContentPermissionOutput>"""

Icon = TypedDict(
    'Icon',
    {
    'path': "str",
    'is_default': "bool",
    },
)
"""This object represents an icon. If used as a profilePicture, this may be returned as null, depending on the user's privacy setting."""

InlineCommentChildrenModel = TypedDict(
    'InlineCommentChildrenModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'resolution_status': NotRequired["InlineCommentResolutionStatus"],
    'properties': NotRequired["InlineCommentProperties"],
    'links': NotRequired["CommentLinks"],
    },
)

InlineCommentModel = TypedDict(
    'InlineCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'resolution_last_modifier_id': NotRequired["str"],
    'resolution_last_modified_at': NotRequired["str"],
    'resolution_status': NotRequired["InlineCommentResolutionStatus"],
    'properties': NotRequired["InlineCommentModelProperties"],
    'operations': NotRequired["InlineCommentModelOperations"],
    'likes': NotRequired["InlineCommentModelLikes"],
    'versions': NotRequired["InlineCommentModelVersions"],
    'links': NotRequired["CommentLinks"],
    },
)

InlineCommentModelLikes = TypedDict(
    'InlineCommentModelLikes',
    {
    'results': NotRequired["list[Like]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

InlineCommentModelOperations = TypedDict(
    'InlineCommentModelOperations',
    {
    'results': NotRequired["list[Operation]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

InlineCommentModelProperties = TypedDict(
    'InlineCommentModelProperties',
    {
    'results': NotRequired["list[ContentProperty]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    'inline_marker_ref': NotRequired["str"],
    'inline_original_selection': NotRequired["str"],
    },
)

InlineCommentModelVersions = TypedDict(
    'InlineCommentModelVersions',
    {
    'results': NotRequired["list[Version]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

InlineCommentProperties = TypedDict(
    'InlineCommentProperties',
    {
    'inline_marker_ref': NotRequired["str"],
    'inline_original_selection': NotRequired["str"],
    },
)

type InlineCommentResolutionStatus = Literal['open', 'reopened', 'resolved', 'dangling']
"""Inline comment resolution status"""

InviteByEmailBody = TypedDict(
    'InviteByEmailBody',
    {
    'emails': "list[str]",
    },
)

Label = TypedDict(
    'Label',
    {
    'id': NotRequired["str"],
    'name': NotRequired["str"],
    'prefix': NotRequired["str"],
    },
)

type LabelSortOrder = Literal['created-date', '-created-date', 'id', '-id', 'name', '-name']
"""The sort fields for labels. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

Like = TypedDict(
    'Like',
    {
    'account_id': NotRequired["str"],
    },
)

ListSpacePermissionCombinationsResponse = TypedDict(
    'ListSpacePermissionCombinationsResponse',
    {
    'results': "list[BulkTransitionCombinationEntry]",
    'generated_at': NotRequired["str | None"],
    'cursor': NotRequired["str | None"],
    },
)

MultiEntityLinks = TypedDict(
    'MultiEntityLinks',
    {
    'next': NotRequired["str"],
    'base': NotRequired["str"],
    },
)

type OnlyArchivedAndCurrentContentStatus = Literal['current', 'archived']
"""The status of the content."""

Operation = TypedDict(
    'Operation',
    {
    'operation': NotRequired["str"],
    'target_type': NotRequired["str"],
    },
)

OperationPermissionsInput = TypedDict(
    'OperationPermissionsInput',
    {
    'operation': "OperationPermissionsInputOperation",
    'principals': "list[ContentPrincipalInput]",
    },
)
"""A set of principals to assign a given operation permission to."""

type OperationPermissionsInputOperation = Literal['read', 'update']
"""The operation to grant."""

OptionalFieldLinks = TypedDict(
    'OptionalFieldLinks',
    {
    'self': NotRequired["str"],
    },
)

OptionalFieldMeta = TypedDict(
    'OptionalFieldMeta',
    {
    'has_more': NotRequired["bool"],
    'cursor': NotRequired["str"],
    },
)

PageBodyWrite = TypedDict(
    'PageBodyWrite',
    {
    'representation': NotRequired["PageBodyWriteRepresentation"],
    'value': NotRequired["str"],
    },
)

type PageBodyWriteRepresentation = Literal['storage', 'atlas_doc_format', 'wiki']
"""Type of content representation used for the value field."""

PageBulk = TypedDict(
    'PageBulk',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str | None"],
    'last_owner_id': NotRequired["str | None"],
    'subtype': NotRequired["str | None"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'links': NotRequired["AbstractPageLinks"],
    },
)

PageCommentModel = TypedDict(
    'PageCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'page_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'links': NotRequired["CommentLinks"],
    },
)

PageInlineCommentModel = TypedDict(
    'PageInlineCommentModel',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'page_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodyBulk"],
    'resolution_status': NotRequired["InlineCommentResolutionStatus"],
    'properties': NotRequired["InlineCommentProperties"],
    'links': NotRequired["CommentLinks"],
    },
)

PageNestedBodyWrite = TypedDict(
    'PageNestedBodyWrite',
    {
    'storage': NotRequired["PageBodyWrite"],
    'atlas_doc_format': NotRequired["PageBodyWrite"],
    'wiki': NotRequired["PageBodyWrite"],
    },
)
"""
Body of the page. Only one body format should be specified as the property
for this object, e.g. `storage`.
"""

PageSingle = TypedDict(
    'PageSingle',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str | None"],
    'last_owner_id': NotRequired["str | None"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["PageSingleLabels"],
    'properties': NotRequired["PageSingleProperties"],
    'operations': NotRequired["PageSingleOperations"],
    'likes': NotRequired["PageSingleLikes"],
    'versions': NotRequired["PageSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["AbstractPageLinks"],
    },
)

PageSingleLabels = TypedDict(
    'PageSingleLabels',
    {
    'results': NotRequired["list[Label]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

PageSingleLikes = TypedDict(
    'PageSingleLikes',
    {
    'results': NotRequired["list[Like]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

PageSingleOperations = TypedDict(
    'PageSingleOperations',
    {
    'results': NotRequired["list[Operation]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

PageSingleProperties = TypedDict(
    'PageSingleProperties',
    {
    'results': NotRequired["list[ContentProperty]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

PageSingleVersions = TypedDict(
    'PageSingleVersions',
    {
    'results': NotRequired["list[Version]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

type PageSortOrder = Literal['id', '-id', 'created-date', '-created-date', 'modified-date', '-modified-date', 'title', '-title']
"""The sort fields for pages. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

PageVersion = TypedDict(
    'PageVersion',
    {
    'created_at': NotRequired["str"],
    'message': NotRequired["str"],
    'number': NotRequired["int"],
    'minor_edit': NotRequired["bool"],
    'author_id': NotRequired["str"],
    'page': NotRequired["VersionedEntity"],
    },
)

type ParentContentType = Literal['page', 'whiteboard', 'database', 'embed', 'folder']
"""Content type of the parent, or null if there is no parent."""

PermittedOperationsResponse = TypedDict(
    'PermittedOperationsResponse',
    {
    'operations': NotRequired["list[Operation]"],
    },
)
"""The list of operations permitted on entity."""

PostBlogPostClassificationLevelBody = TypedDict(
    'PostBlogPostClassificationLevelBody',
    {
    'status': "PostBlogPostClassificationLevelBodyStatus",
    },
)

type PostBlogPostClassificationLevelBodyStatus = Literal['current', 'draft']
"""Status of the content."""

PostDatabaseClassificationLevelBody = TypedDict(
    'PostDatabaseClassificationLevelBody',
    {
    'status': "PostDatabaseClassificationLevelBodyStatus",
    },
)

type PostDatabaseClassificationLevelBodyStatus = Literal['current']
"""Status of the content."""

PostPageClassificationLevelBody = TypedDict(
    'PostPageClassificationLevelBody',
    {
    'status': "PostPageClassificationLevelBodyStatus",
    },
)

type PostPageClassificationLevelBodyStatus = Literal['current', 'draft']
"""Status of the content."""

PostRedactBlogBody = TypedDict(
    'PostRedactBlogBody',
    {
    'created_at': "str",
    'clean_history': NotRequired["bool | None"],
    'version_number': NotRequired["int | None"],
    'body': NotRequired["PostRedactBlogBodyBody"],
    'title': NotRequired["PostRedactBlogBodyTitle"],
    },
)

PostRedactBlogBodyBody = TypedDict(
    'PostRedactBlogBodyBody',
    {
    'redactions': NotRequired["list[RedactionPointer]"],
    },
)

PostRedactBlogBodyTitle = TypedDict(
    'PostRedactBlogBodyTitle',
    {
    'redactions': NotRequired["list[RedactionPointer]"],
    },
)

PostRedactPageBody = TypedDict(
    'PostRedactPageBody',
    {
    'created_at': "str",
    'clean_history': NotRequired["bool | None"],
    'version_number': NotRequired["int | None"],
    'body': NotRequired["PostRedactPageBodyBody"],
    'title': NotRequired["PostRedactPageBodyTitle"],
    },
)

PostRedactPageBodyBody = TypedDict(
    'PostRedactPageBodyBody',
    {
    'redactions': NotRequired["list[RedactionPointer]"],
    },
)

PostRedactPageBodyTitle = TypedDict(
    'PostRedactPageBodyTitle',
    {
    'redactions': NotRequired["list[RedactionPointer]"],
    },
)

PostWhiteboardClassificationLevelBody = TypedDict(
    'PostWhiteboardClassificationLevelBody',
    {
    'status': "PostWhiteboardClassificationLevelBodyStatus",
    },
)

type PostWhiteboardClassificationLevelBodyStatus = Literal['current']
"""Status of the content."""

type PrimaryBodyRepresentation = Literal['storage', 'atlas_doc_format']
"""The primary formats a body can be represented as. A subset of BodyRepresentation. These formats are the only allowed formats in certain use cases."""

type PrimaryBodyRepresentationSingle = Literal['storage', 'atlas_doc_format', 'view', 'export_view', 'anonymous_export_view', 'styled_view', 'editor']
"""The primary formats a body can be represented as. A subset of BodyRepresentation. These formats are the only allowed formats in certain use cases."""

Principal = TypedDict(
    'Principal',
    {
    'principal_type': NotRequired["PrincipalType"],
    'principal_id': NotRequired["str"],
    },
)
"""The principal of the role assignment."""

type PrincipalType = Literal['USER', 'GROUP', 'ACCESS_CLASS']
"""The principal type."""

PutBlogPostClassificationLevelBody = TypedDict(
    'PutBlogPostClassificationLevelBody',
    {
    'id': "str",
    'status': "PutBlogPostClassificationLevelBodyStatus",
    },
)

type PutBlogPostClassificationLevelBodyStatus = Literal['current', 'draft']
"""Status of the content."""

PutDatabaseClassificationLevelBody = TypedDict(
    'PutDatabaseClassificationLevelBody',
    {
    'id': "str",
    'status': "PutDatabaseClassificationLevelBodyStatus",
    },
)

type PutDatabaseClassificationLevelBodyStatus = Literal['current']
"""Status of the content."""

PutPageClassificationLevelBody = TypedDict(
    'PutPageClassificationLevelBody',
    {
    'id': "str",
    'status': "PutPageClassificationLevelBodyStatus",
    },
)

type PutPageClassificationLevelBodyStatus = Literal['current', 'draft']
"""Status of the content."""

PutSpaceDefaultClassificationLevelBody = TypedDict(
    'PutSpaceDefaultClassificationLevelBody',
    {
    'id': "str",
    },
)

PutWhiteboardClassificationLevelBody = TypedDict(
    'PutWhiteboardClassificationLevelBody',
    {
    'id': "str",
    'status': "PutWhiteboardClassificationLevelBodyStatus",
    },
)

type PutWhiteboardClassificationLevelBodyStatus = Literal['current']
"""Status of the content."""

Redaction = TypedDict(
    'Redaction',
    {
    'redactions': NotRequired["list[RedactionPointer]"],
    },
)

RedactionPointer = TypedDict(
    'RedactionPointer',
    {
    'pointer': "str",
    'from': NotRequired["int"],
    'to': NotRequired["int"],
    'reason': NotRequired["str | None"],
    },
)

RedactionPointerResponse = TypedDict(
    'RedactionPointerResponse',
    {
    'pointer': NotRequired["str"],
    'from': NotRequired["int"],
    'to': NotRequired["int"],
    'reason': NotRequired["str"],
    'redaction_id': NotRequired["str"],
    },
)

RedactionResponse = TypedDict(
    'RedactionResponse',
    {
    'body': NotRequired["RedactionSectionResponse"],
    'title': NotRequired["RedactionSectionResponse"],
    },
)
"""
Response containing details of all redactions that were applied to the content.
Each redaction includes a unique ID for restoration, except that code block redactions cannot be restored.
"""

RedactionSectionResponse = TypedDict(
    'RedactionSectionResponse',
    {
    'redactions': NotRequired["list[RedactionPointerResponse]"],
    },
)

RestrictionStateResponse = TypedDict(
    'RestrictionStateResponse',
    {
    'state': "ContentRestrictionState",
    'created_at': NotRequired["str"],
    'created_by': NotRequired["str"],
    'created_by_aaid': NotRequired["str"],
    },
)
"""The direct restriction state of a content item. Inherited restrictions are not included."""

type RoleType = Literal['SYSTEM', 'CUSTOM']
"""The role type."""

SetBlogPostRestrictionStateBody = TypedDict(
    'SetBlogPostRestrictionStateBody',
    {
    'state': "ContentRestrictionState",
    },
)

SetDatabaseRestrictionStateBody = TypedDict(
    'SetDatabaseRestrictionStateBody',
    {
    'state': "ContentRestrictionState",
    },
)

SetFolderRestrictionStateBody = TypedDict(
    'SetFolderRestrictionStateBody',
    {
    'state': "ContentRestrictionState",
    },
)

SetPageRestrictionStateBody = TypedDict(
    'SetPageRestrictionStateBody',
    {
    'state': "ContentRestrictionState",
    },
)

SetSpaceRoleAssignmentsBodyItem = TypedDict(
    'SetSpaceRoleAssignmentsBodyItem',
    {
    'principal': "Principal",
    'role_id': NotRequired["str"],
    },
)

SetSpaceRoleAssignmentsResponse = TypedDict(
    'SetSpaceRoleAssignmentsResponse',
    {
    'results': NotRequired["list[SpaceRoleAssignment]"],
    'links': NotRequired["MultiEntityLinks"],
    },
)
"""MultiEntityResult<SpaceRoleAssignment>"""

SetWhiteboardRestrictionStateBody = TypedDict(
    'SetWhiteboardRestrictionStateBody',
    {
    'state': "ContentRestrictionState",
    },
)

SmartLinkLinks = TypedDict(
    'SmartLinkLinks',
    {
    'webui': NotRequired["str"],
    },
)

SmartLinkSingle = TypedDict(
    'SmartLinkSingle',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'embed_url': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["SmartLinkLinks"],
    },
)

SpaceBulk = TypedDict(
    'SpaceBulk',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'type': NotRequired["SpaceType"],
    'status': NotRequired["SpaceStatus"],
    'author_id': NotRequired["str"],
    'space_owner_id': NotRequired["str"],
    'current_active_alias': NotRequired["str"],
    'created_at': NotRequired["str"],
    'homepage_id': NotRequired["str"],
    'description': NotRequired["SpaceDescription"],
    'icon': NotRequired["SpaceIcon"],
    'links': NotRequired["SpaceLinks"],
    },
)

SpaceDescription = TypedDict(
    'SpaceDescription',
    {
    'plain': NotRequired["BodyType"],
    'view': NotRequired["BodyType"],
    },
)
"""Contains fields for each representation type requested."""

type SpaceDescriptionBodyRepresentation = Literal['plain', 'view']
"""The formats a space description can be represented as. A subset of BodyRepresentation."""

SpaceIcon = TypedDict(
    'SpaceIcon',
    {
    'path': NotRequired["str"],
    'api_download_link': NotRequired["str"],
    },
)
"""The icon of the space"""

SpaceLinks = TypedDict(
    'SpaceLinks',
    {
    'webui': NotRequired["str"],
    },
)

SpacePermission = TypedDict(
    'SpacePermission',
    {
    'id': NotRequired["str"],
    'display_name': NotRequired["str"],
    'description': NotRequired["str"],
    'required_permission_ids': NotRequired["list[str]"],
    },
)

SpacePermissionAssignment = TypedDict(
    'SpacePermissionAssignment',
    {
    'id': NotRequired["str"],
    'principal': NotRequired["SpacePermissionAssignmentPrincipal"],
    'operation': NotRequired["SpacePermissionAssignmentOperation"],
    },
)

SpacePermissionAssignmentOperation = TypedDict(
    'SpacePermissionAssignmentOperation',
    {
    'key': NotRequired["SpacePermissionAssignmentOperationKey"],
    'target_type': NotRequired["SpacePermissionAssignmentOperationTargetType"],
    },
)
"""The operation the space permission corresponds to."""

type SpacePermissionAssignmentOperationKey = Literal['use', 'create', 'read', 'update', 'delete', 'copy', 'move', 'export', 'purge', 'purge_version', 'administer', 'restore', 'create_space', 'restrict_content', 'archive']
"""The type of operation."""

type SpacePermissionAssignmentOperationTargetType = Literal['page', 'blogpost', 'comment', 'attachment', 'whiteboard', 'database', 'embed', 'folder', 'space', 'application', 'userProfile']
"""The type of entity the operation type targets."""

SpacePermissionAssignmentPrincipal = TypedDict(
    'SpacePermissionAssignmentPrincipal',
    {
    'type': NotRequired["SpacePermissionAssignmentPrincipalType"],
    'id': NotRequired["str"],
    },
)
"""The entity the space permissions corresponds to."""

type SpacePermissionAssignmentPrincipalType = Literal['user', 'group', 'role']

SpaceProperty = TypedDict(
    'SpaceProperty',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    'created_at': NotRequired["str"],
    'created_by': NotRequired["str"],
    'version': NotRequired["SpacePropertyVersion"],
    },
)

SpacePropertyCreateRequest = TypedDict(
    'SpacePropertyCreateRequest',
    {
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    },
)

SpacePropertyUpdateRequest = TypedDict(
    'SpacePropertyUpdateRequest',
    {
    'key': NotRequired["str"],
    'value': NotRequired["Any"],
    'version': NotRequired["SpacePropertyUpdateRequestVersion"],
    },
)

SpacePropertyUpdateRequestVersion = TypedDict(
    'SpacePropertyUpdateRequestVersion',
    {
    'number': NotRequired["int"],
    'message': NotRequired["str"],
    },
)
"""New version number and associated message"""

SpacePropertyVersion = TypedDict(
    'SpacePropertyVersion',
    {
    'created_at': NotRequired["str"],
    'created_by': NotRequired["str"],
    'message': NotRequired["str"],
    'number': NotRequired["int"],
    },
)

SpaceRole = TypedDict(
    'SpaceRole',
    {
    'id': NotRequired["str"],
    'type': NotRequired["RoleType"],
    'name': NotRequired["str"],
    'description': NotRequired["str"],
    'space_permissions': NotRequired["list[str]"],
    },
)

SpaceRoleAssignment = TypedDict(
    'SpaceRoleAssignment',
    {
    'principal': NotRequired["Principal"],
    'role_id': NotRequired["str"],
    },
)

SpaceSingle = TypedDict(
    'SpaceSingle',
    {
    'id': NotRequired["str"],
    'key': NotRequired["str"],
    'name': NotRequired["str"],
    'type': NotRequired["SpaceType"],
    'status': NotRequired["SpaceStatus"],
    'author_id': NotRequired["str"],
    'space_owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'homepage_id': NotRequired["str"],
    'description': NotRequired["SpaceDescription"],
    'icon': NotRequired["SpaceIcon"],
    'labels': NotRequired["SpaceSingleLabels"],
    'properties': NotRequired["SpaceSingleProperties"],
    'operations': NotRequired["SpaceSingleOperations"],
    'permissions': NotRequired["SpaceSinglePermissions"],
    'links': NotRequired["SpaceLinks"],
    },
)

SpaceSingleLabels = TypedDict(
    'SpaceSingleLabels',
    {
    'results': NotRequired["list[Label]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

SpaceSingleOperations = TypedDict(
    'SpaceSingleOperations',
    {
    'results': NotRequired["list[Operation]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

SpaceSinglePermissions = TypedDict(
    'SpaceSinglePermissions',
    {
    'results': NotRequired["list[SpacePermissionAssignment]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

SpaceSingleProperties = TypedDict(
    'SpaceSingleProperties',
    {
    'results': NotRequired["list[SpaceProperty]"],
    'meta': NotRequired["OptionalFieldMeta"],
    'links': NotRequired["OptionalFieldLinks"],
    },
)

type SpaceSortOrder = Literal['id', '-id', 'key', '-key', 'name', '-name']
"""The sort fields for spaces. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

type SpaceStatus = Literal['current', 'archived', 'trashed']
"""The status of the space."""

type SpaceType = Literal['global', 'collaboration', 'knowledge_base', 'personal', 'system', 'onboarding', 'xflow_sample_space']
"""The type of space."""

Task = TypedDict(
    'Task',
    {
    'id': NotRequired["str"],
    'local_id': NotRequired["str"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'status': NotRequired["TaskStatus"],
    'body': NotRequired["TaskBodySingle"],
    'created_by': NotRequired["str"],
    'assigned_to': NotRequired["str"],
    'completed_by': NotRequired["str"],
    'created_at': NotRequired["str"],
    'updated_at': NotRequired["str"],
    'due_at': NotRequired["str"],
    'completed_at': NotRequired["str"],
    },
)

TaskBodySingle = TypedDict(
    'TaskBodySingle',
    {
    'storage': NotRequired["BodyType"],
    'atlas_doc_format': NotRequired["BodyType"],
    },
)
"""Contains fields for each representation type requested."""

type TaskStatus = Literal['complete', 'incomplete']
"""Status of the task."""

UpdateBlogPostBody = TypedDict(
    'UpdateBlogPostBody',
    {
    'id': "str",
    'status': "UpdateBlogPostBodyStatus",
    'title': "str",
    'space_id': NotRequired["str"],
    'body': "UpdateBlogPostBodyBody",
    'version': "UpdateBlogPostBodyVersion",
    'created_at': NotRequired["str"],
    },
)

type UpdateBlogPostBodyBody = BlogPostBodyWrite | BlogPostNestedBodyWrite

type UpdateBlogPostBodyStatus = Literal['current', 'draft']
"""
The updated status of the blog post.

Note, if you change the status of a blog post from 'current' to 'draft' and it has an existing draft, the existing draft will be deleted in favor of the updated draft.
Additionally, this endpoint can be used to restore a 'trashed' or 'deleted' blog post to 'current' status. For restoration, blog post contents will not be updated and only the blog post status will be changed.
"""

UpdateBlogPostBodyVersion = TypedDict(
    'UpdateBlogPostBodyVersion',
    {
    'number': NotRequired["int"],
    'message': NotRequired["str"],
    },
)

UpdateBlogPostResponse = TypedDict(
    'UpdateBlogPostResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["BlogPostContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["BlogPostSingleLabels"],
    'properties': NotRequired["BlogPostSingleProperties"],
    'operations': NotRequired["BlogPostSingleOperations"],
    'likes': NotRequired["BlogPostSingleLikes"],
    'versions': NotRequired["BlogPostSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["UpdateBlogPostResponseLinks"],
    },
)

UpdateBlogPostResponseLinks = TypedDict(
    'UpdateBlogPostResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

UpdateCustomContentBody = TypedDict(
    'UpdateCustomContentBody',
    {
    'id': "str",
    'type': "str",
    'status': "UpdateCustomContentBodyStatus",
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'title': "str",
    'body': "UpdateCustomContentBodyBody",
    'version': "UpdateCustomContentBodyVersion",
    },
)

type UpdateCustomContentBodyBody = CustomContentBodyWrite | CustomContentNestedBodyWrite

type UpdateCustomContentBodyStatus = Literal['current']
"""The status of the custom content."""

UpdateCustomContentBodyVersion = TypedDict(
    'UpdateCustomContentBodyVersion',
    {
    'number': NotRequired["int"],
    'message': NotRequired["str"],
    },
)

UpdateCustomContentResponse = TypedDict(
    'UpdateCustomContentResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'custom_content_id': NotRequired["str"],
    'author_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'labels': NotRequired["CustomContentSingleLabels"],
    'properties': NotRequired["CustomContentSingleProperties"],
    'operations': NotRequired["CustomContentSingleOperations"],
    'versions': NotRequired["CustomContentSingleVersions"],
    'body': NotRequired["CustomContentBodySingle"],
    'links': NotRequired["UpdateCustomContentResponseLinks"],
    },
)

UpdateCustomContentResponseLinks = TypedDict(
    'UpdateCustomContentResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

UpdateFooterCommentBody = TypedDict(
    'UpdateFooterCommentBody',
    {
    'version': NotRequired["UpdateFooterCommentModelVersion"],
    'body': NotRequired["UpdateFooterCommentModelBody"],
    'links': NotRequired["UpdateFooterCommentBodyLinks"],
    },
)

UpdateFooterCommentBodyLinks = TypedDict(
    'UpdateFooterCommentBodyLinks',
    {
    'base': NotRequired["str"],
    },
)

UpdateFooterCommentModel = TypedDict(
    'UpdateFooterCommentModel',
    {
    'version': NotRequired["UpdateFooterCommentModelVersion"],
    'body': NotRequired["UpdateFooterCommentModelBody"],
    },
)

type UpdateFooterCommentModelBody = CommentBodyWrite | CommentNestedBodyWrite

UpdateFooterCommentModelVersion = TypedDict(
    'UpdateFooterCommentModelVersion',
    {
    'number': NotRequired["int"],
    'message': NotRequired["str"],
    },
)

UpdateInlineCommentModel = TypedDict(
    'UpdateInlineCommentModel',
    {
    'version': NotRequired["UpdateInlineCommentModelVersion"],
    'body': NotRequired["UpdateInlineCommentModelBody"],
    'resolved': NotRequired["bool"],
    },
)

type UpdateInlineCommentModelBody = CommentBodyWrite | CommentNestedBodyWrite

UpdateInlineCommentModelVersion = TypedDict(
    'UpdateInlineCommentModelVersion',
    {
    'number': NotRequired["int"],
    'message': NotRequired["str"],
    },
)

UpdateInlineCommentResponse = TypedDict(
    'UpdateInlineCommentResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'parent_comment_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'resolution_last_modifier_id': NotRequired["str"],
    'resolution_last_modified_at': NotRequired["str"],
    'resolution_status': NotRequired["InlineCommentResolutionStatus"],
    'properties': NotRequired["InlineCommentModelProperties"],
    'operations': NotRequired["InlineCommentModelOperations"],
    'likes': NotRequired["InlineCommentModelLikes"],
    'versions': NotRequired["InlineCommentModelVersions"],
    'links': NotRequired["UpdateInlineCommentResponseLinks"],
    },
)

UpdateInlineCommentResponseLinks = TypedDict(
    'UpdateInlineCommentResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

UpdatePageBody = TypedDict(
    'UpdatePageBody',
    {
    'id': "str",
    'status': "UpdatePageBodyStatus",
    'title': "str",
    'space_id': NotRequired["Any"],
    'parent_id': NotRequired["Any"],
    'owner_id': NotRequired["Any"],
    'body': "UpdatePageBodyBody",
    'version': "UpdatePageBodyVersion",
    },
)

type UpdatePageBodyBody = PageBodyWrite | PageNestedBodyWrite

type UpdatePageBodyStatus = Literal['current', 'draft']
"""
The updated status of the page.

Note, if you change the status of a page from 'current' to 'draft' and it has an existing draft, the existing draft will be deleted in favor of the updated draft.
Additionally, this endpoint can be used to restore a 'trashed' or 'deleted' page to 'current' status. For restoration, page contents will not be updated and only the page status will be changed.
"""

UpdatePageBodyVersion = TypedDict(
    'UpdatePageBodyVersion',
    {
    'number': NotRequired["int"],
    'message': NotRequired["str"],
    },
)

UpdatePageResponse = TypedDict(
    'UpdatePageResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str | None"],
    'last_owner_id': NotRequired["str | None"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["PageSingleLabels"],
    'properties': NotRequired["PageSingleProperties"],
    'operations': NotRequired["PageSingleOperations"],
    'likes': NotRequired["PageSingleLikes"],
    'versions': NotRequired["PageSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["UpdatePageResponseLinks"],
    },
)

UpdatePageResponseLinks = TypedDict(
    'UpdatePageResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

UpdatePageTitleBody = TypedDict(
    'UpdatePageTitleBody',
    {
    'status': "UpdatePageTitleBodyStatus",
    'title': "str",
    },
)

type UpdatePageTitleBodyStatus = Literal['current', 'draft']
"""The status of the page, current or draft."""

UpdatePageTitleResponse = TypedDict(
    'UpdatePageTitleResponse',
    {
    'id': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'space_id': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str | None"],
    'last_owner_id': NotRequired["str | None"],
    'created_at': NotRequired["str"],
    'version': NotRequired["Version"],
    'body': NotRequired["BodySingle"],
    'labels': NotRequired["PageSingleLabels"],
    'properties': NotRequired["PageSingleProperties"],
    'operations': NotRequired["PageSingleOperations"],
    'likes': NotRequired["PageSingleLikes"],
    'versions': NotRequired["PageSingleVersions"],
    'is_favorited_by_current_user': NotRequired["bool"],
    'links': NotRequired["UpdatePageTitleResponseLinks"],
    },
)

UpdatePageTitleResponseLinks = TypedDict(
    'UpdatePageTitleResponseLinks',
    {
    'base': NotRequired["str"],
    },
)

UpdateSpaceRoleBody = TypedDict(
    'UpdateSpaceRoleBody',
    {
    'name': "str",
    'description': "str",
    'space_permissions': "list[str]",
    'anonymous_reassignment_role_id': NotRequired["str"],
    'guest_reassignment_role_id': NotRequired["str"],
    },
)

UpdateSpaceRoleResponse = TypedDict(
    'UpdateSpaceRoleResponse',
    {
    'id': NotRequired["str"],
    'type': NotRequired["RoleType"],
    'name': NotRequired["str"],
    'description': NotRequired["str"],
    'task_id': NotRequired["str"],
    },
)

UpdateTaskBody = TypedDict(
    'UpdateTaskBody',
    {
    'id': NotRequired["str"],
    'local_id': NotRequired["str"],
    'space_id': NotRequired["str"],
    'page_id': NotRequired["str"],
    'blog_post_id': NotRequired["str"],
    'status': "UpdateTaskBodyStatus",
    'created_by': NotRequired["str"],
    'assigned_to': NotRequired["str"],
    'completed_by': NotRequired["str"],
    'created_at': NotRequired["str"],
    'updated_at': NotRequired["str"],
    'due_at': NotRequired["str"],
    'completed_at': NotRequired["str"],
    },
)

type UpdateTaskBodyStatus = Literal['complete', 'incomplete']
"""Status of the task."""

User = TypedDict(
    'User',
    {
    'display_name': NotRequired["str"],
    'time_zone': NotRequired["str"],
    'personal_space_id': NotRequired["str"],
    'is_external_collaborator': NotRequired["bool"],
    'account_status': NotRequired["AccountStatus"],
    'account_id': NotRequired["str"],
    'email': NotRequired["str"],
    'account_type': NotRequired["AccountType"],
    'public_name': NotRequired["str"],
    'profile_picture': NotRequired["Icon | None"],
    },
)

Version = TypedDict(
    'Version',
    {
    'created_at': NotRequired["str"],
    'message': NotRequired["str"],
    'number': NotRequired["int"],
    'minor_edit': NotRequired["bool"],
    'author_id': NotRequired["str"],
    },
)

type VersionSortOrder = Literal['modified-date', '-modified-date']
"""The sort fields for versions. The default sort direction is ascending. To sort in descending order, append a `-` character before the sort field. For example, `fieldName` or `-fieldName`."""

VersionedEntity = TypedDict(
    'VersionedEntity',
    {
    'title': NotRequired["str"],
    'id': NotRequired["str"],
    'body': NotRequired["BodyBulk"],
    },
)

WhiteboardLinks = TypedDict(
    'WhiteboardLinks',
    {
    'webui': NotRequired["str"],
    'editui': NotRequired["str"],
    },
)

WhiteboardSingle = TypedDict(
    'WhiteboardSingle',
    {
    'id': NotRequired["str"],
    'type': NotRequired["str"],
    'status': NotRequired["ContentStatus"],
    'title': NotRequired["str"],
    'parent_id': NotRequired["str"],
    'parent_type': NotRequired["ParentContentType"],
    'position': NotRequired["int | None"],
    'author_id': NotRequired["str"],
    'owner_id': NotRequired["str"],
    'created_at': NotRequired["str"],
    'space_id': NotRequired["str"],
    'version': NotRequired["Version"],
    'links': NotRequired["WhiteboardLinks"],
    },
)
