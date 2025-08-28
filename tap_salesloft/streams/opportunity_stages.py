from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class OpportunityStagesStream(SalesloftStream):
    '''Opportunity Stages Stream, referenced from https://developers.salesloft.com/docs/api/opportunity-stages-index'''

    name = 'opportunity_stages'
    path = '/v2/opportunity_stages'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Opportunity Stage', examples=[1]),
        Property('name', StringType, description='Name of Opportunity Stage', examples=['Entry Stage']),
        Property('created_at', DateTimeType, description='Datetime of when the Opportunity Stage was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the Opportunity Stage was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('order', IntegerType, description='Sortable value of Opportunity Stage order', examples=[16]),
        Property('active', BooleanType, description='Flag signalizing whether the Opportunity Stage is active', examples=[True]),
    ).to_dict()
