from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class ActivityHistoriesStream(SalesloftStream):
    '''Activity Histories Stream, referenced from https://developers.salesloft.com/docs/api/activity-histories-index'''

    name = 'activity_histories'
    path = '/v2/activity_histories'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('user_guid', StringType, description='UUID of the user this activity is for', examples=['51398ccd-309e-467f-aae2-4b0f66b5c11d']),
        Property('updated_at', DateTimeType, required=True, description='When this record was updated', examples=['2019-01-01T00:00:00.000000Z']),
        Property('type', StringType, description='The type of activity', examples=['email']),
        Property('tags', ArrayType(StringType), description='A list of tags for this activity', examples=['["primary"]']),
        Property('static_data', ObjectType(additional_properties=True), description='The static data for this activity', examples=['{"email_id":2}']),
        Property('resource_type', StringType, description='Type of the resource this activity is for. One of: account, person', examples=['person']),
        Property('resource_id', IntegerType, description='ID of the resource this activity is for. It will be a string for the following resource types: crm_opportunity', examples=[1]),
        Property('pinned_at', DateTimeType, description='When this record was pinned', examples=['2019-01-01T00:00:00.000000Z']),
        Property('occurred_at', DateTimeType, description='When this activity occurred', examples=['2019-01-01T00:00:00.000000Z']),
        Property('id', StringType, required=True, description='ID of this activity in {type}-{id} format', examples=['sent_email-722488662']),
        Property('failed_dynamic_resources', ArrayType(StringType), description='A list of remote resource names that failed to load.', examples=['["email"]']),
        Property('dynamic_data', ObjectType(additional_properties=True), description='Attributes from associated records. This is specific to the type of activity and may change over time. Not returned for create requests', examples=['{"subject":"Welcome to SalesLoft","status":"sent","counts":{"views":3,"replies":1,"clicks":2}}']),

        Property('created_at', DateTimeType, description='When this record was created', examples=['2019-01-01T00:00:00.000000Z']),
    ).to_dict()
