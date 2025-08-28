from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class CallsStream(SalesloftStream):
    '''Calls Stream, referenced from https://developers.salesloft.com/docs/api/activities-calls-index'''

    name = 'calls'
    path = '/v2/activities/calls'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Call', examples=[1]),
        Property('to', StringType, description='Phone number that received the call', examples=['7705551234']),
        Property('duration', IntegerType, description='Length of the call in seconds', examples=[60]),
        Property('sentiment', StringType, description='Outcome of the conversation', examples=['Demo Scheduled']),
        Property('disposition', StringType, description='Result of the call', examples=['Connected']),
        Property('positive', BooleanType, description='Indicates if the call is positive (according to current Positive Calls metric configuration)', examples=[True]),
        Property('connected', BooleanType, description='Indicates if the call is connected (according to current Connected Calls metric configuration)', examples=[True]),
        Property('created_at', DateTimeType, description='Datetime of when the call was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the call was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),

        Property(
            'recordings',
            ArrayType(
                ObjectType(
                    Property('url', StringType, description='The url of the recording', examples=['http://example.com/recording/1']),
                    Property(
                        'status',
                        StringType,
                        description='The status of the call that produced this recording. Possible values are (but not limited to):\n'
                            'no-answer: The call was not answered\n'
                            'failed: The call was not able to be placed\n'
                            'busy: The call was busy\n'
                            'ringing: The call is ringing\n'
                            'in-progress: The call is ongoing\n'
                            'completed: The call is finished',
                        examples=['completed'],
                    ),
                    Property(
                        'recording_status',
                        StringType,
                        description='The processing status of the recording. Possible values are (but not limited to):\n'
                            'not_recorded: there is no recording available, and there will not be one becoming available\n'
                            'pending: the recording is currently being processed by the system\n'
                            'processing: the recording is currently being processed by the system\n'
                            'completed: the recording processing has been completed',
                        examples=['completed'],
                    ),
                )
            ),
            description='The recordings for this this call and their status',
        ),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that made the call',
        ),

        Property(
            'action',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
            ),
            description='Action associated to the call',
        ),

        Property(
            'task',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
            ),
            description='Task that this call was loged from, or null if not sent through a cadence',
        ),

        Property(
            'called_person',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='The person called',
        ),

        Property(
            'crm_activity',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/crm_activities/1']),
            ),
            description='CRM Activity associated with the call',
        ),

        Property(
            'note',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/notes/1']),
            ),
            description='Note for this call',
        ),

        Property(
            'cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='Cadence the call was made on',
        ),

        Property(
            'step',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/1']),
            ),
            description='Step the call was made on',
        ),
    ).to_dict()
