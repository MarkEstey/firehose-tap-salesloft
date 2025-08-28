from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class TagsStream(SalesloftStream):
    '''Tags Stream, referenced from https://developers.salesloft.com/docs/api/tags-index'''

    name = 'tags'
    path = '/v2/tags'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Tag', examples=[1]),
        Property('name', StringType, description='Name of the tag', examples=['marketing']),
    ).to_dict()
