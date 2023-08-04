from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class PendingEmailsStream(SalesloftStream):
    """Pending Emails Stream, referenced from https://developers.salesloft.com/docs/api/pending-emails-index"""

    name = "pending_emails"
    path = "/v2/pending_emails"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of the email",
        ),
        Property(
            "mailbox",
            StringType,
            description="Email Address of the pending email",
        ),
        Property(
            "mime_email_payload",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The email MIME payload",
        ),
    ).to_dict()
