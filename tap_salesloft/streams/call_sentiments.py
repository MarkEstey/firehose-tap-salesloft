from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)


class CallSentimentsStream(SalesloftStream):
    """Call Sentiments Stream, referenced from https://developers.salesloft.com/docs/api/call-sentiments-index"""

    name = "call_sentiments"
    path = "/v2/call_sentiments"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of CallSentiment",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the call sentiment was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the call sentiment was last updated",
        ),
        Property(
            "name",
            StringType,
            description="An available call sentiment text",
        ),
    ).to_dict()
