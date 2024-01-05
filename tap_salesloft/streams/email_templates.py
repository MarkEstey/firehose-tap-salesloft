from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class EmailTemplatesStream(SalesloftStream):
    """Email Templates Stream, referenced from https://developers.salesloft.com/docs/api/email-templates-index"""

    name = "email_templates"
    path = "/v2/email_templates"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of email template",
        ),
        Property(
            "title",
            StringType,
            description="Title of the email template",
        ),
        Property(
            "subject",
            StringType,
            description="Subject of the email template",
        ),
        Property(
            "body",
            StringType,
            description="Sanitized body of the email template without email signature",
        ),
        Property(
            "body_preview",
            StringType,
            description="A plain text version of the first 100 characters of the body of the email template",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the email template was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the email template was last updated",
        ),
        Property(
            "last_used_at",
            DateTimeType,
            description="Datetime of when the email template was last used",
        ),
        Property(
            "archived_at",
            DateTimeType,
            description="Datetime of when the email template was archived, if archived",
        ),
        Property(
            "shared",
            BooleanType,
            description="Whether this email template is visible to team members (shared)",
        ),
        Property(
            "open_tracking_enabled",
            BooleanType,
            description="Whether open tracking is enabled for this email template",
        ),
        Property(
            "click_tracking_enabled",
            BooleanType,
            description="Whether click tracking is enabled for this email template",
        ),
        Property(
            "cadence_template",
            BooleanType,
            description="Whether this email template is only used on a cadence step. "
            "These templates are not visible in the SalesLoft application template list. "
            "If false, this email template is visible in the SalesLoft application, "
            "and may be used when composing an email or creating a cadence step.",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "sent_emails",
                    IntegerType,
                    description="The number of times the email template was sent out",
                ),
                Property(
                    "views",
                    IntegerType,
                    description="The number of times the email template was opened",
                ),
                Property(
                    "clicks",
                    IntegerType,
                    description="The number of times links in the email template were clicked",
                ),
                Property(
                    "replies",
                    IntegerType,
                    description="The number of replies the email template received",
                ),
                Property(
                    "bounces",
                    IntegerType,
                    description="The number of bounces the email template received",
                ),
            ),
        ),
        Property(
            "template_owner",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that owns this email template",
        ),
        Property(
            "team_template",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Associated team template, if any",
        ),
        Property(
            "_links",
            ObjectType(),
            description="Links to attachments and tags resources for this email template.",
        ),
        Property(
            "tags",
            ArrayType(StringType),
            description="All tags applied to this email template",
        ),
        Property(
            "groups",
            ArrayType(
                ObjectType(
                    Property("id", IntegerType),
                    Property("_href", StringType),
                )
            ),
            description="Groups to which this template is assigned, if any",
        ),
    ).to_dict()
