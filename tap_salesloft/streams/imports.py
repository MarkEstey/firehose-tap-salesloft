from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class ImportsStream(SalesloftStream):
    """Imports Stream, referenced from https://developers.salesloft.com/docs/api/imports-index"""

    name = "imports"
    path = "/v2/imports"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="Import ID",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the import was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the import was last updated, ignoring relationship changes",
        ),
        Property(
            "name",
            StringType,
            description="Name of Import",
        ),
        Property(
            "current_people_count",
            IntegerType,
            description="Count of People that have not been deleted",
        ),
        Property(
            "imported_people_count",
            IntegerType,
            description="Count of People that have ever been on this Import",
        ),
    ).to_dict()
