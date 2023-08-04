from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class AccountTiersStream(SalesloftStream):
    """Account Tiers Stream, referenced from https://developers.salesloft.com/docs/api/account-tiers-index"""

    name = "account_tiers"
    path = "/v2/account_tiers"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Account Tier",
        ),
        Property(
            "name",
            StringType,
            description="Name of the Account Tier",
        ),
        Property(
            "order",
            IntegerType,
            description="The order of the account tier",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Account Tier was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the Account Tier was last updated",
        ),
    ).to_dict()
