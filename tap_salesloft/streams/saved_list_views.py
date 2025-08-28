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
    '''Saved List Views Stream, referenced from https://developers.salesloft.com/docs/api/saved-list-views-index'''

    name = 'saved_list_views'
    path = '/v2/saved_list_views'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Ssaved list view', examples=[1]),
        Property('view', StringType, description='Type of saved list view', examples=['companies']),
        Property('name', StringType, description='Name of saved list view', examples=['Tom''s Prospects']),
        Property('view_params', ObjectType(additional_properties=True), description='List of set filters in saved list view', examples=['{"owner":"unowned","stage":"28865","unowned":true}']),
        Property('is_default', BooleanType, description='Whether the saved list view is the default view', examples=[True]),
        Property('shared', BooleanType, description='Whether the view is public to the team or not', examples=[False]),
    ).to_dict()
