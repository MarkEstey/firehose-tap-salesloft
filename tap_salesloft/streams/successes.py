from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class SuccessesStream(SalesloftStream):
    """Successes Stream, referenced from https://developers.salesloft.com/docs/api/successes-index"""

    name = "successes"
    path = "/v2/successes"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of success",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the success was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the success was last updated",
        ),
        Property(
            "succeeded_at",
            DateTimeType,
            description="Datetime of when the success was recorded",
        ),
        Property(
            "success_window_started_at",
            DateTimeType,
            description="Datetime of when this person was first worked, leading up to the success",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that created this success",
        ),
        Property(
            "person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The person who a success occurred on",
        ),
        Property(
            "latest_email",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The email that was most recently sent to this person before the success",
        ),
        Property(
            "latest_call",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The call that was most recently made to this person before the success",
        ),
        Property(
            "latest_action",
            ObjectType(
                Property("id", IntegerType),
            ),
            description="The action that was most recently completed on this person before the success",
        ),
        Property(
            "latest_cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The cadence with the action that was most recently completed on this person before the success",
        ),
        Property(
            "latest_step",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The step of the cadence's action that was most recently completed on this person before the success",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "total_emails",
                    IntegerType,
                    description="The total number of emails made in this success window",
                ),
                Property(
                    "total_calls",
                    IntegerType,
                    description="The total number of calls made in this success window",
                ),
                Property(
                    "total_other_touches",
                    IntegerType,
                    description="The total number of other touches made in this success window",
                ),
            ),
        ),
    ).to_dict()
