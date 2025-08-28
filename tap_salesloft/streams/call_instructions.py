from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class CallInstructionsStream(SalesloftStream):
    '''Call Instructions Stream, referenced from https://developers.salesloft.com/docs/api/action-details-call-instructions-index'''

    name = 'call_instructions'
    path = '/v2/action_details/call_instructions'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of call instructions', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the call instructions were created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, description='Datetime of when the call instructions were last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('instructions', StringType, description='The instructions', examples=['Call once, leave voicemail if not answered. Conference conversation.']),
    ).to_dict()
