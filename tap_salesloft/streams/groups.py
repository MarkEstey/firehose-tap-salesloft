from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class GroupsStream(SalesloftStream):
    '''Groups Stream, referenced from https://developers.salesloft.com/docs/api/groups-index'''

    name = 'groups'
    path = '/v2/groups'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of the Group', examples=[1]),
        Property('name', StringType, description='Name of the Group', examples=['Test name']),
        Property('parent_id', IntegerType, description='ID of the parent Group', examples=[2]),
        Property(
            'accessible_groups',
            ArrayType(
                ObjectType(
                    Property('id', IntegerType, examples=[921]),
                    Property('_href', StringType, examples=['https://api.salesloft.com/v2/groups/921']),
                )
            ),
            description='Groups accessible if any',
        ),
    ).to_dict()
