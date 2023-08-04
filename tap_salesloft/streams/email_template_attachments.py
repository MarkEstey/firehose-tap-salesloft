from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class EmailTemplateAttachmentsStream(SalesloftStream):
    """Email Template Attachments Stream, referenced from https://developers.salesloft.com/docs/api/email-template-attachments-index"""

    name = "email_template_attachments"
    path = "/v2/email_template_attachments"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of email template attachment association",
        ),
        Property(
            "attachment_id",
            IntegerType,
            description="ID of the email template attachment",
        ),
        Property(
            "email_template",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Link and id of specific email template",
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
        Property(
            "scanned",
            BooleanType,
            description="Checks if attachment has been scanned",
        ),
        Property(
            "attachment_content_type",
            StringType,
            description="Content type of the attachment",
        ),
        # Documentation states 'attachment_fingerprint' type is integer, API returns string
        Property(
            "attachment_fingerprint",
            StringType,
            description="Unique attachment Identifier",
        ),
    ).to_dict()
