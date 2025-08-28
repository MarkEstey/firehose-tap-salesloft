from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class ActionsStream(SalesloftStream):
    '''Actions Stream, referenced from https://developers.salesloft.com/docs/api/actions-index'''

    name = 'actions'
    path = '/v2/actions'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Action', examples=[1]),
        Property('due', BooleanType, description='Whether this step is due', examples=[True]),
        Property('created_at', DateTimeType, description='Datetime of when the Action was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the Action was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('type', StringType, description='The type of this action. Valid types are: email, phone, other. New types may be added in the future.', examples=['phone']),
        Property('status', StringType, description='The current state of the person on the cadence. Possible values are:\nin_progress: this action has not been completed\npending_activity: this action has been acted upon, but the action has not been completed. (i.e. the email is scheduled to send, but has not been delivered yet)', examples=['in_progress']),
        Property('due_on', DateTimeType, description='When action is due', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('multitouch_group_id', IntegerType, description='ID of the multitouch group', examples=[1]),

        Property(
            'action_details',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/action_details/call_instructions/1']),
            ),
            description='The type specific action details',
        ),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User assigned to action',
        ),

        Property(
            'person',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='The subject of an action',
        ),

        Property(
            'cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='The cadence of an action',
        ),

        Property(
            'step',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/1']),
            ),
            description='The step of an action',
        ),

        Property(
            'task',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/tasks/1']),
            ),
            description='The task associated with an action',
        ),
    ).to_dict()
