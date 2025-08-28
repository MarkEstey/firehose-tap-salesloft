from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    DateType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class CadencesStream(SalesloftStream):
    '''Cadences Stream, referenced from https://developers.salesloft.com/docs/api/cadences-index'''

    name = 'cadences'
    path = '/v2/cadences'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of cadence', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the cadence was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the cadence was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('archived_at', DateTimeType, description='Datetime of when the cadence was archived, if archived', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('latest_active_date', DateType, description='Date of when the cadence was last used', examples=['2026-01-01']),
        Property('team_cadence', BooleanType, description='Whether this cadence is a team cadence. A team cadence is created by an admin and can be run by all users', examples=[False]),
        Property('shared', BooleanType, description='Whether this cadence is visible to team members (shared)', examples=[False]),
        Property('archived', BooleanType, description='Whether this cadence is archived', examples=[False]),
        Property('remove_bounces_enabled', BooleanType, description='Whether this cadence is configured to automatically remove people who have bounced', examples=[True]),
        Property('remove_replies_enabled', BooleanType, description='Whether this cadence is configured to automatically remove people who have replied', examples=[True]),
        Property('opt_out_link_included', BooleanType, description='Whether this cadence is configured to include an opt-out link by default', examples=[True]),
        Property('draft', BooleanType, description='Whether this cadence is in draft mode', examples=[False]),
        Property('override_contact_restrictions', BooleanType, description='Whether this cadence is an Operational Cadence. An operational cadence is only created by an admin and accounts with the correct permission', examples=[False]),
        Property('cadence_framework_id', IntegerType, description='ID of the cadence framework used to create steps for the cadence', examples=[1]),
        Property('archived_by', StringType, description='Name or email of the user who archived the cadence', examples=['John']),
        Property(
            'cadence_function',
            StringType,
            description='The use case of the cadence. Possible values are:\n'
                'outbound: Denotes an outbound cadence, typically for sales purposes\n'
                'inbound: Denotes an inbound sales cadence\n'
                'event: Denotes a cadence used for an upcoming event\n'
                'other: Denotes a cadence outside of the standard process',
            examples=['outbound'],
        ),
        Property('name', StringType, description='Cadence name', examples=['Prospecting - VP of Sales']),
        Property('external_identifier', StringType, description='Cadence External ID', examples=['This is my external id']),
        Property('tags', ArrayType(StringType), description='All tags applied to this cadence', examples=['["7-23-2017","dreamforce"]']),
        Property('current_state', StringType, description='The state of the Cadence. Read Only. Valid states are: draft, active, archived, expired, deleted', examples=['active']),

        Property(
            'creator',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that created this cadence',
        ),

        Property(
            'owner',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that is marked as the owner of this cadence',
        ),

        Property(
            'bounced_stage',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/person_stages/1']),
            ),
            description='Stage set when person on cadence bounces',
        ),

        Property(
            'replied_stage',
            ObjectType(
                Property('id', IntegerType, examples=[2]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/person_stages/2']),
            ),
            description='Stage set when person on cadence replies',
        ),

        Property(
            'added_stage',
            ObjectType(
                Property('id', IntegerType, examples=[3]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/person_stages/3']),
            ),
            description='Stage set when person is added to cadence',
        ),

        Property(
            'finished_stage',
            ObjectType(
                Property('id', IntegerType, examples=[3]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/person_stages/3']),
            ),
            description='Stage set when person is finished with cadence',
        ),

        Property(
            'cadence_priority',
            ObjectType(
                Property('id', IntegerType, examples=[2]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadence_priorities']),
            ),
            description='Priority of the cadence',
        ),

        Property(
            'groups',
            ArrayType(
                ObjectType(
                    Property('id', IntegerType, examples=[921]),
                    Property('_href', StringType, examples=['https://api.salesloft.com/v2/groups/921']),
                )
            ),
            description='Groups to which this cadence is assigned, if any',
        ),

        Property(
            'counts',
            ObjectType(
                Property('cadence_people', IntegerType, description='The number of people that have ever been added to the cadence', examples=[59]),
                Property('people_acted_on_count', IntegerType, description='The number of people that have been skipped, scheduled, or advanced in a cadence', examples=[1]),
                Property('target_daily_people', IntegerType, description='The user defined target for number of people to add to the cadence each day', examples=[10]),
                Property('opportunities_created', IntegerType, description='The number of opportunities created and attributed to the cadence', examples=[10]),
                Property('meetings_booked', IntegerType, description='The number of meetings booked and attributed to the cadence', examples=[10]),
            ),
        ),
    ).to_dict()
