from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class CallDispositionsStream(SalesloftStream):
    """Call Dispositions Stream, referenced from https://developers.salesloft.com/docs/api/call-dispositions-index"""

    name = "call_dispositions"
    path = "/v2/call_dispositions"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of CallDisposition",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the call disposition was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the call disposition was last updated",
        ),
        Property(
            "name",
            StringType,
            description="An available call disposition text",
        ),
    ).to_dict()
