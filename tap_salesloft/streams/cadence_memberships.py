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

class CadenceMembershipsStream(SalesloftStream):
    '''Cadence Memberships Stream, referenced from https://developer.salesloft.com/docs/api/cadence-memberships-index'''

    name = 'cadence_memberships'
    path = '/v2/cadence_memberships'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='Cadence membership ID', examples=[1]),
        Property('added_at', DateTimeType, description='Datetime of when the person was last added to this cadence', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('created_at', DateTimeType, description='Datetime of when the person was first added to this cadence', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the record was last updated',examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('person_deleted', BooleanType, description='Whether the associated person has since been deleted', examples=[False]),
        Property('currently_on_cadence', BooleanType, description='Whether the person is currently on the cadence', examples=[False]),
        Property(
            'current_state',
            StringType,
            description='The current state of the person on the cadence. Possible values are:\n'
                'processing: The person is being processed on a cadence. Cadence-related changes cannot be made at this time\n'
                'staged: The person is waiting for the first step in the cadence to occur\n'
                'active: The cadence has begun processing this person and is still in the process, but idle\n'
                'scheduled: The cadence has begun processing this person and is still in the process, with an activity scheduled to occur\n'
                'completed: The cadence has been completed for this person\n'
                'removed: The person was manually or automatically removed from the cadence\n'
                'removed_no_action: The person was removed from the cadence before any action occurred\n'
                'reassigned: The person''s cadence execution was transferred to a different user, ending this user''s interaction\n'
                'archived: The cadence this person belonged to has been archived and all actions and people were archived with it',
            examples=['staged'],
        ),

        Property(
            'cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='The cadence that the person is on',
        ),

        Property(
            'step',
            ObjectType(
                Property('id', IntegerType, examples=[5]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/5']),
            ),
            description='The cadence step that the person is on',
        ),

        Property(
            'person',
            ObjectType(
                Property('id', IntegerType, examples=[2]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/2']),
            ),
            description='The person that is on the cadence',
        ),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[3]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/3']),
            ),
            description='The user that is acting on the person in the cadence',
        ),

        Property(
            'latest_action',
            ObjectType(
                Property('id', IntegerType, examples=[4])
            ),
            description='The most recent action associated with the record',
        ),

        Property(
            'counts',
            ObjectType(
                Property('views', IntegerType, description='The number of times emails sent from the cadence to the person were opened', examples=[10]),
                Property('clicks', IntegerType, description='The number of times emails sent from the cadence to the person were clicked', examples=[5]),
                Property('replies', IntegerType, description='The number of times emails sent from the cadence to the person were replied to', examples=[2]),
                Property('calls', IntegerType, description='The number of times a call was logged from the cadence to the person', examples=[2]),
                Property('sent_emails', IntegerType, description='The number of times emails were sent from the cadence to the person', examples=[4]),
                Property('bounces', IntegerType, description='The number of times emails sent from the cadence to the person bounced', examples=[0]),
            ),
        ),
    ).to_dict()
