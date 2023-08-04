from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class CustomFieldsStream(SalesloftStream):
    """Custom Fields Stream, referenced from https://developers.salesloft.com/docs/api/custom-fields-index"""

    name = "custom_fields"
    path = "/v2/custom_fields"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Custom Field",
        ),
        Property(
            "name",
            StringType,
            description="Name of the Custom Field",
        ),
        Property(
            "field_type",
            StringType,
            description="Type of the Custom Field. Value must be one of: person, company, opportunity.",
        ),
        Property(
            "value_type",
            StringType,
            description="Value Type of the Custom Field. Value must be one of: text, date.",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Custom Field was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the Custom Field was last updated",
        ),
    ).to_dict()
