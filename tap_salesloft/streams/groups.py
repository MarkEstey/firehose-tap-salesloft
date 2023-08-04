from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class GroupsStream(SalesloftStream):
    """Groups Stream, referenced from https://developers.salesloft.com/docs/api/groups-index"""

    name = "groups"
    path = "/v2/groups"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of the Group",
        ),
        Property(
            "name",
            StringType,
            description="Name of the Group",
        ),
        Property(
            "parent_id",
            IntegerType,
            description="ID of the parent Group",
        ),
        Property(
            "accessible_groups",
            ArrayType(
                ObjectType(
                    Property("id", IntegerType),
                    Property("_href", StringType),
                )
            ),
            description="Groups accessible if any",
        ),
    ).to_dict()
