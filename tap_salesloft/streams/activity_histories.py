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


class ActivityHistoriesStream(SalesloftStream):
    """Activity Histories Stream, referenced from https://developers.salesloft.com/docs/api/activity-histories-index"""

    name = "activity_histories"
    path = "/v2/activity_histories"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "user_guid",
            StringType,
            description="UUID of the user this activity is for",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="When this record was updated",
        ),
        Property(
            "type",
            StringType,
            description="The type of activity",
        ),
        Property(
            "static_data",
            ObjectType(),
            description="The static data for this activity",
        ),
        Property(
            "resource_type",
            StringType,
            description="Type of the resource this activity is for. One of: account, person",
        ),
        Property(
            "resource_id",
            IntegerType,
            description="ID of the resource this activity is for. It will be a string for the following resource types: crm_opportunity",
        ),
        Property(
            "pinned_at",
            DateTimeType,
            description="When this record was pinned",
        ),
        Property(
            "occurred_at",
            DateTimeType,
            description="When this activity occurred",
        ),
        Property(
            "id",
            StringType,
            required=True,
            description="ID of this activity in {type}-{id} format",
        ),
        Property(
            "failed_dynamic_resources",
            ArrayType(StringType),
            description="A list of remote resource names that failed to load.",
        ),
        Property(
            "dynamic_data",
            ObjectType(),
            description="Attributes from associated records. "
            "This is specific to the type of activity and may change over time. Not returned for create requests",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="When this record was created",
        ),
    ).to_dict()
