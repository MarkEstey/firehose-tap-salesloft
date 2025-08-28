from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    PropertiesList,
    Property,
    StringType,
)

class AccountTypesStream(SalesloftStream):
    '''Account Types Stream, referenced from https://developers.salesloft.com/docs/api/account-types-index'''

    name = 'account_types'
    path = '/v2/account_types'
    primary_keys = ['name']

    schema = PropertiesList(
        Property('name', StringType, description='Name of Account Type', examples=['Corporation']),
    ).to_dict()
