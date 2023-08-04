from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class SavedListViewsStream(SalesloftStream):
    """Saved List Views Stream, referenced from https://developers.salesloft.com/docs/api/saved-list-views-index"""

    name = "saved_list_views"
    path = "/v2/saved_list_views"
    primary_keys = ["id"]

    schema = PropertiesList(
        # Corrected documentation typo
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of saved list view",
        ),
        Property(
            "view",
            StringType,
            description="Type of saved list view",
        ),
        Property(
            "name",
            StringType,
            description="Name of saved list view",
        ),
        Property(
            "view_params",
            ObjectType(),
            description="List of set filters in saved list view",
        ),
        Property(
            "is_default",
            BooleanType,
            description="Whether the saved list view is the default view",
        ),
    ).to_dict()
