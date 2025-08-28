from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class CustomFieldsStream(SalesloftStream):
    '''Custom Fields Stream, referenced from https://developers.salesloft.com/docs/api/custom-fields-index'''

    name = 'custom_fields'
    path = '/v2/custom_fields'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Custom Field', examples=[1]),
        Property('name', StringType, description='Name of the Custom Field', examples=['My Custom Field']),
        Property('field_type', StringType, description='Type of the Custom Field. Value must be one of: person, company, opportunity.', examples=['person']),
        Property('value_type', StringType, description='Value Type of the Custom Field. Value must be one of: text, date.', examples=['text']),
        Property('created_at', DateTimeType, description='Datetime of when the Custom Field was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, description='Datetime of when the Custom Field was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
    ).to_dict()
