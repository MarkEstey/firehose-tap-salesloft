from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class AccountTiersStream(SalesloftStream):
    '''Account Tiers Stream, referenced from https://developers.salesloft.com/docs/api/account-tiers-index'''

    name = 'account_tiers'
    path = '/v2/account_tiers'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Account Tier', examples=[1]),
        Property('name', StringType, description='Name of the Account Tier', examples=['High Priority']),
        Property('order', IntegerType, description='The order of the account tier', examples=[2]),
        Property('created_at', DateTimeType, description='Datetime of when the Account Tier was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, description='Datetime of when the Account Tier was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('active', BooleanType, description='Flag signalizing whether the Person Stage is active', examples=[True]),
    ).to_dict()
