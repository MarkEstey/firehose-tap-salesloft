from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    CustomType,
    PropertiesList,
    Property,
    StringType,
)

class StepsStream(SalesloftStream):
    '''Steps Stream, referenced from https://developers.salesloft.com/docs/api/steps-index'''

    name = 'steps'
    path = '/v2/steps'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Step', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the Step was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the Step was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('disabled', BooleanType, description='Whether this step is currently active', examples=[True]),
        Property('type', StringType, description='The type of the action scheduled by this step. Valid types are: email, phone, integration, other. New types may be added in the future.', examples=['phone']),
        Property('name', StringType, description='Name of the step', examples=['VP Email Short']),
        Property('display_name', StringType, description='Display name of the step', examples=['Day 1: Step 2 - Phone']),
        Property('day', IntegerType, description='Day this step is associated with up', examples=[1]),
        # Documentation states 'step_number' type is integer, API returns either numeric or string
        Property('step_number', CustomType({'type': ['integer', 'string', 'null']}), description='The number of the step for this day', examples=[1]),
        Property('multitouch_enabled', BooleanType, description='Whether this step is a multitouch cadence step', examples=[False]),

        Property(
            'details',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/action_details/call_instructions/1']),
            ),
            description='Details pertaining to the specific step type',
        ),

        Property(
            'cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='The cadence of the step',
        ),
    ).to_dict()
