from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class CallDispositionsStream(SalesloftStream):
    '''Call Dispositions Stream, referenced from https://developers.salesloft.com/docs/api/call-dispositions-index'''

    name = 'call_dispositions'
    path = '/v2/call_dispositions'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of CallDisposition', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the call disposition was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, description='Datetime of when the call disposition was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('name', StringType, description='An available call disposition text', examples=['Connected']),
    ).to_dict()
