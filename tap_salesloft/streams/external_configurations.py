from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class ExternalConfigurationsStream(SalesloftStream):
    '''External ID Configurations Stream, referenced from https://developers.salesloft.com/docs/api/external-configurations-index'''

    name = 'external_configurations'
    path = '/v2/external/configurations'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('source_type', StringType, description='The type of source that owns the configuration if applicable', examples=['integration']),
        Property('source_id', IntegerType, description='The ID of the source integration if applicable', examples=[10]),
        Property('object_type', StringType, description='The Salesloft object that should be associated with the external type', examples=['people']),
        Property('id', IntegerType, required=True, description='ID of the configuration', examples=[42]),
        Property('external_type', StringType, description='The type of external', examples=['zendesk']),
        Property('deleted', BooleanType, description='Whether or not the configuration is deleted.', examples=[False]),
    ).to_dict()
