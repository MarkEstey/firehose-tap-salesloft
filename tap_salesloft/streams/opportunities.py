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

class OpportunitiesStream(SalesloftStream):
    '''Opportunities Stream, referenced from https://developers.salesloft.com/docs/api/opportunities-index'''

    name = 'opportunities'
    path = '/v2/opportunities'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Opportunity', examples=[1]),
        Property('name', StringType, description='Opportunity Name', examples=['Mega Corp - Professional Services']),
        Property('amount', StringType, description='Estimated total sale amount', examples=['5000.00']),
        Property('stage_name', StringType, description='Stage name', examples=['Qualification']),
        Property('probability', StringType, description='Probability', examples=['50']),
        Property('crm_id', StringType, description='The identifier for this record in the CRM', examples=['006i000001mnhpD']),
        Property('crm_type', StringType, description='CRM type', examples=['hubspot']),
        Property('account_crm_id', StringType, description='Account CRM id', examples=['0000R00002fHqiMAAA']),
        Property('owner_crm_id', StringType, description='Owner CRM id', examples=['1111A11111aAaaAAAA']),
        Property('account_name', StringType, description='Account Full Name', examples=['Hogwarts School of Witchcraft and Wizardry']),
        Property('created_by_crm_id', StringType, description='Created By CRM id', examples=['1111A11111aAaaAAAA']),
        Property('opportunity_type', StringType, description='Opportunity Type', examples=['New Customer']),
        Property('owner_crm_name', StringType, description='Owner CRM Name', examples=['John Doe']),
        Property('crm_last_updated_date', DateTimeType, description='Datetime of when the Opportunity was most recently updated in CRM', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('close_date', DateTimeType, description='Date when the opportunity is expected to close', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('is_closed', BooleanType, description='Whether the opportunity is closed', examples=[False]),
        Property('is_won', BooleanType, description='Whether the opportunity is closed won', examples=[False]),
        Property('crm_url', StringType, description='CRM url, currently Salesforce.com only', examples=['https://na15.salesforce.com/006i000001mnhpD']),
        Property('created_at', DateTimeType, description='Datetime of when the Opportunity was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the Opportunity was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('created_date', DateTimeType, description='Datetime of when the Opportunity was created in CRM', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('opportunity_window_person_id', IntegerType, description='ID of when the attributed person was created in Salesloft', examples=[1]),
        Property('opportunity_window_started_at', DateTimeType, description='Datetime of when the attributed person was created in Salesloft', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('custom_fields', ObjectType(additional_properties=True), description='Custom fields are defined by the user''s team. Only fields with values are presented in the API.', examples=['{"MyField":"A Value","Other":"Field"}']),
        Property('currency_iso_code', StringType, description='Currency ISO Code', examples=['USD']),
        Property('tags', ArrayType(StringType), description='All tags applied to this Opportunities', examples=['["7-23-2017","dreamforce"]']),

        Property(
            'most_recent_cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='The most recent cadence associated with the Opportunity',
        ),

        Property(
            'most_recent_step',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/1']),
            ),
            description='The most recent step associated with the Opportunity',
        ),

        Property('most_recent_step_number', IntegerType, description='The most recent step number associated with the Opportunity'),

        Property(
            'most_recent_step_account',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='The most recent step account id associated with the Opportunity',
        ),

        Property(
            'owner',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='The owner associated with the Opportunity',
        ),

        Property(
            'creator',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='The creator associated with the Opportunity',
        ),

        Property(
            'account',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/accounts/1']),
            ),
            description='The account that this opportunity is associated to',
        ),
    ).to_dict()
