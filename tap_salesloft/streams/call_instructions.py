from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class CallInstructionsStream(SalesloftStream):
    """Call Instructions Stream, referenced from https://developers.salesloft.com/docs/api/action-details-call-instructions-index"""

    name = "call_instructions"
    path = "/v2/action_details/call_instructions"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of call instructions",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the call instructions were created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the call instructions were last updated",
        ),
        Property(
            "instructions",
            StringType,
            description="The instructions",
        ),
    ).to_dict()
