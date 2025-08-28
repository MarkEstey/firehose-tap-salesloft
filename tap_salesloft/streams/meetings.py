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

class MeetingsStream(SalesloftStream):
    '''Meetings Stream, referenced from https://developers.salesloft.com/docs/api/meetings-index'''

    name = 'meetings'
    path = '/v2/meetings'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of the meeting', examples=[1]),
        Property('title', StringType, description='Title of the meeting', examples=['Meeting with John']),
        Property('start_time', DateTimeType, description='Start time of the meeting', examples=['2025-08-28T13:41:30.307428+00:00']),
        Property('end_time', DateTimeType, description='End time of the meeting', examples=['2025-08-28T13:41:30.307454+00:00']),
        Property('calendar_id', StringType, description='Calendar ID of the meeting owner', examples=['calendar-id-google.com']),
        Property('calendar_type', StringType, description='Calendar type of the meeting owner. Possible values are: gmail, azure, nylas, nylas_v3, linkedin_azure, cerebro, external, internal', examples=['gmail']),
        # Documentation states 'meeting_type_id' type is string, API returns numeric
        Property('meeting_type_id', IntegerType, description='Meeting type ID', examples=[123]),
        Property('meeting_type', StringType, description='Meeting type', examples=['Demo call']),
        Property('recipient_name', StringType, description='Name of the meeting invite recipient', examples=['John Doe']),
        Property('recipient_email', StringType, description='Email of the meeting invite recipient', examples=['email@sloft.com']),
        Property('location', StringType, description='Location of the meeting', examples=['Atlanta, GA']),
        Property('description', StringType, description='Description of the meeting', examples=['Introducing interview']),
        Property('event_id', StringType, description='ID of the meeting created by target calendar', examples=['123468796']),
        # Documentation states 'account_id' type is string, API returns numeric
        Property('account_id', IntegerType, description='ID of the account the recipient associated to', examples=[1]),
        # Documentation states 'task_id' type is string, API returns numeric
        Property('task_id', IntegerType, description='ID of the created task', examples=[123]),
        Property('created_at', DateTimeType, description='Datetime of when the meeting was created', examples=['2025-08-28T13:41:30.324504+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the meeting was last updated', examples=['2025-08-28T13:41:30.324539+00:00']),
        Property('guests', ArrayType(StringType), description='The list of attendees emails of the meeting', examples=['["email1@sloft.com","email2@sloft.com"]']),

        Property(
            'attendees',
            ArrayType(
                ObjectType(
                    Property('email', StringType, description='Email of the attendee', examples=['calendar@example.com']),
                    Property('name', StringType, description='Name of the attendee', examples=['John']),
                    Property('organizer', BooleanType, description='Whether the attendee is the organizer of the event.', examples=[False]),
                    Property('status', StringType, description='The attendee''s response status. Possible values are: needsAction, accepted, tentative, declined', examples=['accepted']),
                    Property('status_changed', BooleanType, description='Whether the attendee changed response status', examples=[False]),
                    Property(
                        'person',
                        ObjectType(
                            Property('id', IntegerType, examples=[1]),
                            Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
                        ),
                        description='Salesloft Person record',
                    ),
                    Property('deleted_at', DateTimeType, description='Datetime of when the attendee was deleted', examples=['2025-08-28T13:41:30.324969+00:00']),
                    Property('affiliation', StringType, description='Indicates whether the attendee is internal or external', examples=['internal']),
                )
            ),
            description='The attendees of the meeting. Each attendee includes the following fields: status, email, name, organizer',
        ),

        Property(
            'person',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='Salesloft Person record for the recipient',
        ),

        Property(
            'cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='Salesloft Cadence record associated with meeting',
        ),

        Property(
            'step',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/1']),
            ),
            description='Salesloft Step record associated with meeting',
        ),

        Property(
            'owned_by_user',
            ObjectType(
                Property('id', StringType, examples=['e2bf1d56-fcc9-4145-9af0-247cfaa67959']),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/e2bf1d56-fcc9-4145-9af0-247cfaa67959']),
            ),
            description='Owner of the meeting',
        ),

        Property(
            'booked_by_user',
            ObjectType(
                Property('id', StringType, examples=['e2bf1d56-fcc9-4145-9af0-247cfaa67959']),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/e2bf1d56-fcc9-4145-9af0-247cfaa67959']),
            ),
            description='User who booked the meeting',
        ),

        Property('crm_references', ObjectType(additional_properties=True), description='List of crm references associated with the meeting', examples=['{"who":{"crm_id":"0033X00004GOywtQAD","crm_object_type":"Contact","crm_object_label":"Contact","crm_url":"link_to_salesforce","description1":"John Doe","description2":"john.doe@example.com","description3":null},"what":{"crm_id":"0063X000018fDmMQAU","crm_object_type":"Opportunity","crm_object_label":"Opportunity","crm_url":"link_to_salesforce","description1":"Title of the opportunity","description2":"2032-01-10","description3":"Prospecting"}}']),
        Property('crm', ObjectType(additional_properties=True), description='Crm fields mapping from intake form', examples=['{"person":{"fields":{"first_name":"John","last_name":"Doe"}},"activity":{"fields":{"subject":"Meeting with John"}}}']),
        Property('event_source', StringType, description='Source of the meeting. Possible values are: ''external'' - The event was synced to Salesloft platform via Calendar Sync, ''internal'' - The event was created via Salesloft platform', examples=['external']),
        Property('canceled_at', DateTimeType, description='Datetime of when the meeting was canceled', examples=['2025-08-28T13:41:30.325474+00:00']),
        Property('all_day', BooleanType, description='Whether the meeting is an all-day meeting', examples=[False]),
        Property('no_show', BooleanType, description='Whether the meeting is a No Show meeting', examples=[False]),
        Property('crm_custom_fields', ObjectType(additional_properties=True), description='List of crm custom fields which will be logged to SFDC', examples=['{"Event_Calendar_Type__c":"Google"}']),
        Property('strict_attribution', BooleanType, description='Strict attribution means that we 100% sure which cadence generate the meeting', examples=[False]),
        Property('i_cal_uid', StringType, description='UID of the meeting provided by target calendar provider', examples=['040P00B08200E00074C5B7101A82EF']),
        Property('status', StringType, description='Status of the meeting. Possible values are: pending, booked, failed, retry', examples=['booked']),
        Property('reschedule_status', StringType, description='Status of the meeting rescheduling progress. Possible values are: pending, booked, failed, retry', examples=['booked']),

        Property(
            'owned_by_meetings_settings',
            ObjectType(
                Property('email_address', StringType, description='Calendar owner''s email address', examples=['calendar.owner@example.com']),
            ),
        ),

        Property(
            'booked_by_meetings_settings',
            ObjectType(
                Property('email_address', StringType, description='Calendar owner''s email address', examples=['calendar.owner@example.com']),
            ),
        ),

        Property('reschedule_guid', StringType, description='Unique identifier (GUID) for the reschedule meeting link. Use this GUID as a parameter in the API endpoint to retrieve a meeting link.', examples=['b056fa7d-ae6d-4d41-b95b-2ac28cbf075d']),
        Property('recurring', BooleanType, description='Whether the calendar event is a recurring event', examples=[False]),
        Property('recurrence', ArrayType(StringType), description='List of RRULE for a recurring event, as specified in RFC5545. This field is omitted for single events or instances of recurring events', examples=['["RRULE:FREQ=DAILY;INTERVAL=1"]']),
        Property('recurring_interval', StringType, description='Specifies how often a recurring event repeats (Daily, Weekly, Monthly, Yearly). This field is omitted for single events or instances of recurring events', examples=['Daily']),
        Property('last_occurrence_at', DateTimeType, description='The timestamp of the last occurrence in a series of recurring events', examples=['2025-08-28T13:41:30.329558+00:00']),
        Property('undo_completion_count', IntegerType, description='The number of times a meeting has been rescheduled after completion', examples=[0]),
        Property('count_towards_meetings_attended_metric', BooleanType, description='Whether the meeting counts towards the Meetings Attended configurable metric', examples=[True]),
        Property('count_towards_meetings_booked_metric', BooleanType, description='Whether the meeting counts towards the Meetings Booked configurable metric', examples=[True]),
        Property('created_on_demand', BooleanType, description='Whether the meeting was created on-demand (internal calendar type with do_not_sync_external_calendar)', examples=[True]),
        Property('notes', StringType, description='Notes for the meeting', examples=['Discussion points and follow-ups']),
    ).to_dict()
