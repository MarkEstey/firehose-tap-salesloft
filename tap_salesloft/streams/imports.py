from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class ImportsStream(SalesloftStream):
    '''Imports Stream, referenced from https://developers.salesloft.com/docs/api/imports-index'''

    name = 'imports'
    path = '/v2/imports'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='Import ID', examples=[1]),
        Property('name', StringType, description='Name of Import', examples=['DataProvider -> SalesLoft 9/1/17']),
        Property('created_at', DateTimeType, description='Datetime of when the import was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, description='Datetime of when the import was last updated, ignoring relationship changes', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('current_people_count', IntegerType, description='Count of People that have not been deleted', examples=[5]),
        Property('imported_people_count', IntegerType, description='Count of People that have ever been on this Import', examples=[7]),
        Property('errors_list', ArrayType(ObjectType(additional_properties=True)), description='Array of the errors', examples=['[{"errors":{"email_address":["has already been taken"]},"params":{"email_address":"john.doe@gmail.com"}}]']),
        Property('user_id', IntegerType, description='ID of the user who created the import', examples=[1]),
        Property('import_type', StringType, description='Type of import', examples=['csv, data, manual, public_api, salesforce, hubspot']),
    ).to_dict()
