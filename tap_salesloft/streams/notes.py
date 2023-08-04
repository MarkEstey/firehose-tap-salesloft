from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class NotesStream(SalesloftStream):
    """Notes Stream, referenced from https://developers.salesloft.com/docs/api/notes-index"""

    name = "notes"
    path = "/v2/notes"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="Note ID",
        ),
        Property(
            "content",
            StringType,
            description="The content of the note",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the note was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the note was last updated",
        ),
        Property(
            "associated_type",
            StringType,
            description="Type of associated resource ('person' or 'account')",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that wrote this note",
        ),
        Property(
            "associated_with",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Item on which the note was made",
        ),
        Property(
            "call",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Call linked to the note",
        ),
    ).to_dict()
