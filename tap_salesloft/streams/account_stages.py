from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class AccountStagesStream(SalesloftStream):
    """Account Stages Stream, referenced from https://developers.salesloft.com/docs/api/account-stages-index"""

    name = "account_stages"
    path = "/v2/account_stages"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Account Stage",
        ),
        Property(
            "name",
            StringType,
            description="Name of Account Stage",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Account Stage was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the Account Stage was last updated",
        ),
        Property(
            "order",
            IntegerType,
            description="Order of Account Stage",
        ),
    ).to_dict()
