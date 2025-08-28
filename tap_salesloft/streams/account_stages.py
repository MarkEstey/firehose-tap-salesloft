from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class AccountStagesStream(SalesloftStream):
    '''Account Stages Stream, referenced from https://developers.salesloft.com/docs/api/account-stages-index'''

    name = 'account_stages'
    path = '/v2/account_stages'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Account Stage', examples=[1]),
        Property('name', StringType, description='Name of Account Stage', examples=['In Progress']),
        Property('created_at', DateTimeType, description='Datetime of when the Account Stage was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the Account Stage was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('order', IntegerType, description='Order of Account Stage', examples=[3]),
        Property('active', BooleanType, description='Flag signalizing whether the Account Stage is active', examples=[True]),
    ).to_dict()
