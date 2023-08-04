from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class CallsStream(SalesloftStream):
    """Calls Stream, referenced from https://developers.salesloft.com/docs/api/activities-calls-index"""

    name = "calls"
    path = "/v2/activities/calls"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Call",
        ),
        Property(
            "to",
            StringType,
            description="Phone number that received the call",
        ),
        Property(
            "duration",
            IntegerType,
            description="Length of the call in seconds",
        ),
        Property(
            "sentiment",
            StringType,
            description="Outcome of the conversation",
        ),
        Property(
            "disposition",
            StringType,
            description="Result of the call",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the call was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the call was last updated",
        ),
        Property(
            "recordings",
            ArrayType(
                ObjectType(
                    Property(
                        "url",
                        StringType,
                        description="The url of the recording",
                    ),
                    Property(
                        "status",
                        StringType,
                        description="The status of the call that produced this recording. "
                        "Possible values are (but not limited to): "
                        "no-answer: The call was not answered; "
                        "failed: The call was not able to be placed; "
                        "busy: The call was busy; "
                        "ringing: The call is ringing; "
                        "in-progress: The call is ongoing; "
                        "completed: The call is finished",
                    ),
                    Property(
                        "recording_status",
                        StringType,
                        description="The processing status of the recording. Possible values are (but not limited to): "
                        "not_recorded: there is no recording available, and there will not be one becoming available; "
                        "pending: the recording is currently being processed by the system; "
                        "processing: the recording is currently being processed by the system; "
                        "completed: the recording processing has been completed",
                    ),
                )
            ),
            description="The recordings for this this call and their status",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that made the call",
        ),
        Property(
            "action",
            ObjectType(
                Property("id", IntegerType),
            ),
            description="Action associated to the call",
        ),
        Property(
            "called_person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The person called",
        ),
        Property(
            "crm_activity",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="CRM Activity associated with the call",
        ),
        Property(
            "note",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Note for this call",
        ),
        Property(
            "cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Cadence the call was made on",
        ),
        Property(
            "step",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Step the call was made on",
        ),
    ).to_dict()
