from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class CallDataRecordsStream(SalesloftStream):
    """Call Data Records Stream, referenced from https://developers.salesloft.com/docs/api/call-data-records-index"""

    name = "call_data_records"
    path = "/v2/call_data_records"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of CallDataRecord",
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
            "to",
            StringType,
            description="Phone number that received the call",
        ),
        Property(
            "from",
            StringType,
            description="Phone number that placed the call",
        ),
        Property(
            "duration",
            IntegerType,
            description="Length of the call in seconds",
        ),
        Property(
            "direction",
            StringType,
            description="Direction of the call. Can be one of: inbound, outbound",
        ),
        Property(
            "status",
            StringType,
            description="The outcome of the call. Can be one of: "
            "queued, initiated, ringing, in-progress, completed, busy, no-answer, canceled, failed",
        ),
        Property(
            "call_type",
            StringType,
            description="Type of the call. Can be one of: call, bridge, collaboration. "
            "Though exact values may change over time",
        ),
        Property(
            "call_uuid",
            StringType,
            description="UUID of the call. Legs of the same call will have the same call_uuid.",
        ),
        Property(
            "recording",
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
            ),
        ),
        Property(
            "call",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Call that this record was logged to, if logged to a call",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that made or received the call, if the call was to a user",
        ),
        Property(
            "called_person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The person called",
        ),
    ).to_dict()
