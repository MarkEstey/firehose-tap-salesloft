from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class CrmActivitiesStream(SalesloftStream):
    '''CRM Activities Stream, referenced from https://developers.salesloft.com/docs/api/crm-activities-index'''

    name = 'crm_activities'
    path = '/v2/crm_activities'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='CrmActivity ID', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the crm activity was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the crm activity was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('subject', StringType, description='The subject field of the activity in your CRM', examples=['Call: Connected | Interested']),
        Property('description', StringType, description='The description field of the activity in your CRM', examples=['Timeline is 2 weeks for demo, set with Kate']),
        Property('crm_id', StringType, description='The ID of the activity in your CRM, if written to your CRM', examples=['00T0H00003w2FBhUAM']),
        Property('activity_type', StringType, description='The type of activity that is being recorded, if available. The values can change over time, but could be one of: email, phone, email reminder, inmail', examples=['phone']),
        Property('error', StringType, description='Information about why this crm activity failed to sync, if it did fail to sync. Failed activities will be automatically retried and may become successful in the future', examples=['Could not find a CRM account link.']),
        Property('custom_crm_fields', ObjectType(additional_properties=True), description='Additional fields that are logged to your CRM, if mapped by the team at the time of writing to your CRM', examples=['{"ecorp__Call_Type__c":"inbound follow up"}']),
        Property('crm_record_type', StringType, description='The object type in the CRM for the activity', examples=['Task']),

        Property('person',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='Person that this crm activity is for',
        ),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[2]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/2']),
            ),
            description='User that triggered this crm activity',
        ),
    ).to_dict()
