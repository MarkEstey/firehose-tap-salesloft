from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class PhoneNumberAssignmentsStream(SalesloftStream):
    """Phone Number Assignments Stream, referenced from https://developers.salesloft.com/docs/api/phone-number-assignments-index"""

    name = "phone_number_assignments"
    path = "/v2/phone_number_assignments"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="PhoneNumberAssignment ID",
        ),
        Property(
            "number",
            StringType,
            description="The phone number associated with this assignment",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User associated with this phone number assignment",
        ),
    ).to_dict()
