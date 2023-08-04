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


class TeamTemplatesStream(SalesloftStream):
    """Team Templates Stream, referenced from https://developers.salesloft.com/docs/api/team-templates-index"""

    name = "team_templates"
    path = "/v2/team_templates"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            StringType,
            required=True,
            description="ID of team template",
        ),
        Property(
            "title",
            StringType,
            description="Title of the team template",
        ),
        Property(
            "subject",
            StringType,
            description="Subject of the team template",
        ),
        Property(
            "body",
            StringType,
            description="Body of the team template",
        ),
        Property(
            "body_preview",
            StringType,
            description="A plain text version of the first 100 characters of the body of the team template",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the team template was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the team template was last updated",
        ),
        Property(
            "last_used_at",
            DateTimeType,
            description="Datetime of when the team template was last used",
        ),
        Property(
            "archived_at",
            DateTimeType,
            description="Datetime of when the team template was archived, if archived",
        ),
        Property(
            "last_modified_at",
            DateTimeType,
            description="Datetime of when the team template was last modified",
        ),
        Property(
            "open_tracking_enabled",
            BooleanType,
            description="Whether open tracking is enabled for this team template",
        ),
        Property(
            "click_tracking_enabled",
            BooleanType,
            description="Whether click tracking is enabled for this team template",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "sent_emails",
                    IntegerType,
                    description="The number of times the team template was sent out",
                ),
                Property(
                    "views",
                    IntegerType,
                    description="The number of times the team template was opened",
                ),
                Property(
                    "clicks",
                    IntegerType,
                    description="The number of times links in the team template were clicked",
                ),
                Property(
                    "replies",
                    IntegerType,
                    description="The number of replies the team template received",
                ),
                Property(
                    "bounces",
                    IntegerType,
                    description="The number of bounces the team template received",
                ),
            ),
        ),
        Property(
            "last_modified_user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that last modified this team template",
        ),
        Property(
            "_links",
            ObjectType(),
            description="Links to attachments resource for this template",
        ),
        Property(
            "tags",
            ArrayType(StringType),
            description="All tags applied to this team template",
        ),
    ).to_dict()
