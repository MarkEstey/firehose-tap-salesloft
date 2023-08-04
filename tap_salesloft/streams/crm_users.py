from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class CrmUsersStream(SalesloftStream):
    """CRM Users Stream, referenced from https://developers.salesloft.com/docs/api/crm-users-index"""

    name = "crm_users"
    path = "/v2/crm_users"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="Crm User ID",
        ),
        Property(
            "crm_id",
            StringType,
            description="CRM ID",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the crm user was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the crm user was last updated",
        ),
        Property(
            "first_name",
            StringType,
            description="Account first name",
        ),
        Property(
            "last_name",
            StringType,
            description="Account last name",
        ),
        Property(
            "name",
            StringType,
            description="Account name",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User",
        ),
    ).to_dict()
