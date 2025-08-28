from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    PropertiesList,
    Property,
    StringType,
)

class CustomRolesStream(SalesloftStream):
    '''Custom Roles Stream, referenced from https://developers.salesloft.com/docs/api/custom-roles-index'''

    name = 'custom_roles'
    path = '/v2/custom_roles'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', StringType, required=True, description='ID of the custom role', examples=[1]),
        Property('name', StringType, description='Name of the custom role', examples=['Test name']),
    ).to_dict()
