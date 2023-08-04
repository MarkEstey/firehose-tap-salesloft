from tap_salesloft.client import SalesloftStream

from singer_sdk.helpers._typing import TypeConformanceLevel

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


class MeetingsStream(SalesloftStream):
    """Meetings Stream, referenced from https://developers.salesloft.com/docs/api/meetings-index"""

    name = "meetings"
    path = "/v2/meetings"
    primary_keys = ["id"]

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of the meeting",
        ),
        Property(
            "title",
            StringType,
            description="Title of the meeting",
        ),
        Property(
            "start_time",
            DateTimeType,
            description="Start time of the meeting",
        ),
        Property(
            "end_time",
            DateTimeType,
            description="End time of the meeting",
        ),
        Property(
            "calendar_id",
            StringType,
            description="Calendar ID of the meeting owner",
        ),
        Property(
            "calendar_type",
            StringType,
            description="Calendar type of the meeting owner. "
            "Possible values are: gmail, azure, nylas, linkedin_azure, cerebro, external",
        ),
        Property(
            "meeting_type",
            StringType,
            description="Meeting type",
        ),
        Property(
            "recipient_name",
            StringType,
            description="Name of the meeting invite recipient",
        ),
        Property(
            "recipient_email",
            StringType,
            description="Email of the meeting invite recipient",
        ),
        Property(
            "location",
            StringType,
            description="Location of the meeting",
        ),
        Property(
            "description",
            StringType,
            description="Description of the meeting",
        ),
        Property(
            "event_id",
            StringType,
            description="ID of the meeting created by target calendar",
        ),
        # Documentation states 'account_id' type is string, API returns numeric
        Property(
            "account_id",
            IntegerType,
            description="ID of the account the recipient associated to",
        ),
        # Documentation states 'task_id' type is string, API returns numeric
        Property(
            "task_id",
            IntegerType,
            description="ID of the created task",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the meeting was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the meeting was last updated",
        ),
        Property(
            "guests",
            ArrayType(StringType),
            description="The list of attendees emails of the meeting",
        ),
        Property(
            "attendees",
            ArrayType(
                ObjectType(
                    Property(
                        "email",
                        StringType,
                        description="Email of the attendee",
                    ),
                    Property(
                        "name",
                        StringType,
                        description="Name of the attendee",
                    ),
                    Property(
                        "organizer",
                        BooleanType,
                        description="Whether the attendee is the organizer of the event.",
                    ),
                    Property(
                        "status",
                        StringType,
                        description="The attendee's response status. "
                        "Possible values are: needsAction, accepted, tentative, declined",
                    ),
                    Property(
                        "status_changed",
                        BooleanType,
                        description="Whether the attendee changed response status",
                    ),
                    Property(
                        "deleted_at",
                        DateTimeType,
                        description="Datetime of when the attendee was deleted",
                    ),
                )
            ),
            description="The attendees of the meeting. "
            "Each attendee includes the following fields: status, email, name, organizer",
        ),
        Property(
            "person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Salesloft Person record for the recipient",
        ),
        Property(
            "cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Salesloft Cadence record associated with meeting",
        ),
        Property(
            "step",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Salesloft Step record associated with meeting",
        ),
        Property(
            "owned_by_user",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Owner of the meeting",
        ),
        Property(
            "booked_by_user",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="User who booked the meeting",
        ),
        Property(
            "crm_references",
            ObjectType(),
            description="List of crm references associated with the meeting",
        ),
        Property(
            "event_source",
            StringType,
            description="Source of the meeting. Possible values are: "
            "'external' - The event was synced to Salesloft platform via Calendar Sync, "
            "'internal' - The event was created via Salesloft platform",
        ),
        Property(
            "canceled_at",
            DateTimeType,
            description="Datetime of when the meeting was canceled",
        ),
        Property(
            "all_day",
            BooleanType,
            description="Whether the meeting is an all-day meeting",
        ),
        Property(
            "no_show",
            BooleanType,
            description="Whether the meeting is a No Show meeting",
        ),
        Property(
            "crm_custom_fields",
            ObjectType(),
            description="List of crm custom fields which will be logged to SFDC",
        ),
        Property(
            "strict_attribution",
            BooleanType,
            description="Strict attribution means that we 100% sure which cadence generate the meeting",
        ),
        Property(
            "i_cal_uid",
            StringType,
            description="UID of the meeting provided by target calendar provider",
        ),
        Property(
            "status",
            StringType,
            description="Status of the meeting. Possible values are: pending, booked, failed, retry",
        ),
        Property(
            "reschedule_status",
            StringType,
            description="Status of the meeting rescheduling progress. "
            "Possible values are: pending, booked, failed, retry",
        ),
        Property(
            "owned_by_meetings_settings",
            ObjectType(
                Property(
                    "email_address",
                    StringType,
                    description="Calendar owner's email address",
                ),
            ),
        ),
        Property(
            "booked_by_meetings_settings",
            ObjectType(
                Property(
                    "email_address",
                    StringType,
                    description="Calendar owner's email address",
                ),
            ),
        ),
    ).to_dict()
