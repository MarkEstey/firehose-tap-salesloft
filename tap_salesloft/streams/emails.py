from tap_salesloft.client import SalesloftStream

from singer_sdk.helpers._typing import TypeConformanceLevel

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class EmailsStream(SalesloftStream):
    """Emails Stream, referenced from https://developers.salesloft.com/docs/api/activities-emails-index"""

    name = "emails"
    path = "/v2/activities/emails"
    primary_keys = ["id"]
    replication_key = "updated_at"

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Email",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the email was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the email was last updated",
        ),
        Property(
            "recipient_email_address",
            StringType,
            description="Email address of the recipient",
        ),
        Property(
            "status",
            StringType,
            description="Status of this email through the sending process. "
            "Possible values are: sent, sent_from_gmail, sent_from_external, pending, "
            "pending_reply_check, scheduled, sending, delivering, failed, cancelled, "
            "pending_through_gmail, pending_through_external",
        ),
        Property(
            "bounced",
            BooleanType,
            description="Whether this email bounced",
        ),
        Property(
            "send_after",
            DateTimeType,
            description="When this email will be sent, or null if already sent",
        ),
        Property(
            "sent_at",
            DateTimeType,
            description="When this email was sent, or null if it was not sent",
        ),
        Property(
            "view_tracking",
            BooleanType,
            description="Whether this email had view tracking enabled",
        ),
        Property(
            "click_tracking",
            BooleanType,
            description="Whether this email had click tracking enabled",
        ),
        Property(
            "headers",
            ObjectType(),
            description="Selected headers that are included if this email used them. Available keys are: cc, bcc",
        ),
        Property(
            "personalization",
            StringType,
            description="Percentage of this email that has been personalized",
        ),
        Property(
            "subject",
            StringType,
            description="Subject of the email. "
            "This field has been determined sensitive and requires a specific scope to access it.",
        ),
        Property(
            "body",
            StringType,
            description="Email Body",
        ),
        Property(
            "error_message",
            StringType,
            description="Error message of the email. "
            "This field has been determined sensitive and requires a specific scope to access it.",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "clicks",
                    IntegerType,
                    description="The number of times links in the email were clicked",
                ),
                Property(
                    "views",
                    IntegerType,
                    description="The number of times the email was opened",
                ),
                Property(
                    "replies",
                    IntegerType,
                    description="The number of replies the email received",
                ),
                Property(
                    "unique_devices",
                    IntegerType,
                    description="The number of unique devices that opened the email",
                ),
                Property(
                    "unique_locations",
                    IntegerType,
                    description="The number of unique locations that opened the email",
                ),
                Property(
                    "attachments",
                    IntegerType,
                    description="The number of attachments on the email",
                ),
            ),
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that sent this email",
        ),
        Property(
            "recipient",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The person whom received this email",
        ),
        Property(
            "mailing",
            ObjectType(
                Property("id", IntegerType),
            ),
            description="The mailing that this email was a part of",
        ),
        Property(
            "action",
            ObjectType(
                Property("id", IntegerType),
            ),
            description="Action that this email was sent from, or null if not sent through a cadence",
        ),
        Property(
            "task",
            ObjectType(
                Property("id", IntegerType),
            ),
            description="Task that this email was sent from, or null if not sent through a cadence",
        ),
        Property(
            "crm_activity",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="CRM Activity associated with this email",
        ),
        Property(
            "cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Cadence the email was sent on",
        ),
        Property(
            "step",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Step the email was sent on",
        ),
        Property(
            "email_template",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Template used for this email",
        ),
    ).to_dict()
