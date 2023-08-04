from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class PersonStagesStream(SalesloftStream):
    """Person Stages Stream, referenced from https://developers.salesloft.com/docs/api/person-stages-index"""

    name = "person_stages"
    path = "/v2/person_stages"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Person Stage",
        ),
        Property(
            "name",
            StringType,
            description="Name of Person Stage",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Person Stage was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the Person Stage was last updated",
        ),
        Property(
            "order",
            IntegerType,
            description="Sortable value of Person Stage order",
        ),
    ).to_dict()
