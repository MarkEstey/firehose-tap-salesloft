from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class SuccessesStream(SalesloftStream):
    '''Successes Stream, referenced from https://developers.salesloft.com/docs/api/successes-index'''

    name = 'successes'
    path = '/v2/successes'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of success', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the success was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the success was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('succeeded_at', DateTimeType, description='Datetime of when the success was recorded', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('success_window_started_at', DateTimeType, description='Datetime of when this person was first worked, leading up to the success', examples=['2025-01-01T00:00:00.000000+00:00']),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that created this success',
        ),

        Property(
            'person',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='The person who a success occurred on',
        ),

        Property(
            'latest_email',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/activities/emails/1']),
            ),
            description='The email that was most recently sent to this person before the success',
        ),

        Property(
            'latest_call',
            ObjectType(
                Property('id', IntegerType, examples=[2]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/activities/calls/2']),
            ),
            description='The call that was most recently made to this person before the success',
        ),

        Property(
            'latest_action',
            ObjectType(
                Property('id', IntegerType, examples=[3]),
            ),
            description='The action that was most recently completed on this person before the success',
        ),

        Property(
            'latest_cadence',
            ObjectType(
                Property('id', IntegerType, examples=[4]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/4']),
            ),
            description='The cadence with the action that was most recently completed on this person before the success',
        ),

        Property(
            'latest_step',
            ObjectType(
                Property('id', IntegerType, examples=[5]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/5']),
            ),
            description='The step of the cadence''s action that was most recently completed on this person before the success',
        ),

        Property(
            'counts',
            ObjectType(
                Property('total_emails', IntegerType, description='The total number of emails made in this success window', examples=[2]),
                Property('total_calls', IntegerType, description='The total number of calls made in this success window', examples=[5]),
                Property('total_other_touches', IntegerType, description='The total number of other touches made in this success window', examples=[3]),
            ),
        ),
    ).to_dict()
