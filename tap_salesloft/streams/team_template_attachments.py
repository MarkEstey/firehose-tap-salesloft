from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class TeamTemplateAttachmentsStream(SalesloftStream):
    """Team Template Attachments Stream, referenced from https://developers.salesloft.com/docs/api/team-template-attachments-index"""

    name = "team_template_attachments"
    path = "/v2/team_template_attachments"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of team template attachment association",
        ),
        Property(
            "attachment_id",
            IntegerType,
            description="ID of the team template attachment",
        ),
        Property(
            "team_template",
            ObjectType(
                # Documentation states 'team_template'.'id' type is integer, API returns string
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Details pertaining to the specific team template",
        ),
        Property(
            "name",
            StringType,
            description="Name of the attachment",
        ),
        Property(
            "download_url",
            StringType,
            description="Download url of the attachment",
        ),
        Property(
            "attachment_file_size",
            IntegerType,
            description="The size of the attachment",
        ),
    ).to_dict()
