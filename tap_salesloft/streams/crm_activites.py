from tap_salesloft.client import SalesloftStream

from singer_sdk.helpers._typing import TypeConformanceLevel

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class CrmActivitiesStream(SalesloftStream):
    """CRM Activities Stream, referenced from https://developers.salesloft.com/docs/api/crm-activities-index"""

    name = "crm_activities"
    path = "/v2/crm_activities"
    primary_keys = ["id"]
    replication_key = "updated_at"

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="CrmActivity ID",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the crm activity was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the crm activity was last updated",
        ),
        Property(
            "subject",
            StringType,
            description="The subject field of the activity in your CRM",
        ),
        Property(
            "description",
            StringType,
            description="The description field of the activity in your CRM",
        ),
        Property(
            "crm_id",
            StringType,
            description="The ID of the activity in your CRM, if written to your CRM",
        ),
        Property(
            "activity_type",
            StringType,
            description="The type of activity that is being recorded, if available. "
            "The values can change over time, but could be one of: email, phone, email reminder, inmail",
        ),
        Property(
            "error",
            StringType,
            description="Information about why this crm activity failed to sync, if it did fail to sync. "
            "Failed activities will be automatically retried and may become successful in the future",
        ),
        Property(
            "custom_crm_fields",
            ObjectType(),
            description="Additional fields that are logged to your CRM, if mapped by the team at the time of writing to your CRM",
        ),
        Property(
            "person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Person that this crm activity is for",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that triggered this crm activity",
        ),
    ).to_dict()
