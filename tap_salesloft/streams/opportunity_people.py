from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class OpportunityPeopleStream(SalesloftStream):
    '''Opportunity People Stream, referenced from https://developers.salesloft.com/docs/api/opportunity-people-index'''

    name = 'opportunity_people'
    path = '/v2/opportunity_people'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of OpportunityPerson record', examples=[1]),
        Property('person_id', IntegerType, description='ID of the Salesloft Person', examples=[1]),
        Property('opportunity_id', IntegerType, description='ID of the Salesloft Opportunity', examples=[1]),
        Property('opportunity_crm_id', StringType, description='Opportunity CRM ID', examples=['0060t00002gHyZAAB']),
        Property('person_crm_id', StringType, description='Person CRM ID', examples=['0030R00002fHqiMAAA']),
        Property('created_at', DateTimeType, description='Datetime of when the OpportunityPerson was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the OpportunityPerson was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
    ).to_dict()
