from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class CallDataRecordsStream(SalesloftStream):
    '''Call Data Records Stream, referenced from https://developers.salesloft.com/docs/api/call-data-records-index'''

    name = 'call_data_records'
    path = '/v2/call_data_records'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('user', ObjectType(additional_properties=True), description='User that made or received the call, if the call was to a user', examples=['{"id":2,"_href":"https://api.salesloft.com/v2/users/2"}']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the call was last updated', examples=['2025-08-26T17:29:02.388052Z']),
        Property('to', StringType, description='Phone number that received the call', examples=['7705551234']),
        Property('status', StringType, description='The outcome of the call. Can be one of: queued, initiated, ringing, in-progress, completed, busy, no-answer, canceled, failed', examples=['completed']),
        Property('started_at', DateTimeType, description='Datetime of when the call started', examples=['2025-08-26T17:29:02.388109Z']),
        Property('recording', ObjectType(additional_properties=True), description='The recording for this this call data record, with a status', examples=['{"url":"http://example.com/recording/1","status":"completed","recording_status":"processing"}']),
        Property('id', IntegerType, required=True, description='ID of CallDataRecord', examples=[1]),
        Property('from', StringType, description='Phone number that placed the call', examples=['7705551234']),
        Property('ended_at', DateTimeType, description='Datetime of when the call ended', examples=['2025-08-26T17:29:02.388171Z']),
        Property('duration', IntegerType, description='Length of the call in seconds', examples=[60]),
        Property('direction', StringType, description='Direction of the call. Can be one of: inbound, outbound', examples=['outbound']),
        Property('dialer_recording', ObjectType(additional_properties=True), description='The dialer recording resource for the call recording', examples=['{"uuid":"5c5c1f32-bff1-4b7c-8f2a-bd650b829c67","_href":"https://api.salesloft.com/v2/dialer_recordings/5c5c1f32-bff1-4b7c-8f2a-bd650b829c67"}']),
        Property('created_at', DateTimeType, description='Datetime of when the call was created', examples=['2025-08-26T17:29:02.387982Z']),
        Property('called_person', ObjectType(additional_properties=True), description='The person called', examples=['{"id":3,"_href":"https://api.salesloft.com/v2/people/3"}']),
        Property('call_uuid', StringType, description='UUID of the call. Legs of the same call will have the same call_uuid.', examples=['5c5c1f32-bff1-4b7c-8f2a-bd650b829c67']),
        Property('call_type', StringType, description='Type of the call. Can be one of: call, bridge, collaboration. Though exact values may change over time', examples=['call']),
        Property('call', ObjectType(additional_properties=True), description='Call that this record was logged to, if logged to a call', examples=['{"id":1,"_href":"https://api.salesloft.com/v2/activities/calls/1"}']),
    ).to_dict()
