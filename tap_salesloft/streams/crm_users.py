from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class CrmUsersStream(SalesloftStream):
    '''CRM Users Stream, referenced from https://developers.salesloft.com/docs/api/crm-users-index'''

    name = 'crm_users'
    path = '/v2/crm_users'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='Crm User ID', examples=[1]),
        Property('crm_id', StringType, description='CRM ID', examples=['5003000000D8cuIQAA']),
        Property('created_at', DateTimeType, description='Datetime of when the crm user was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the crm user was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('first_name', StringType, description='Account first name', examples=['Jonh']),
        Property('last_name', StringType, description='Account last name', examples=['Smith']),
        Property('name', StringType, description='Account name', examples=['Jonh Smith']),
        Property('crm_username', StringType, description='CRM Username', examples=['john.smith@salesloft.com']),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User',
        ),
    ).to_dict()
