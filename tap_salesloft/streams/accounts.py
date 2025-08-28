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

class AccountsStream(SalesloftStream):
    '''Accounts Stream, referenced from https://developers.salesloft.com/docs/api/accounts-index'''

    name = 'accounts'
    path = '/v2/accounts'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Account', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the Account was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the Account was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('archived_at', DateTimeType, description='Datetime of when the Account was archived, if archived', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('name', StringType, description='Account Full Name', examples=['Hogwarts School of Witchcraft and Wizardry']),
        Property('domain', StringType, description='Website domain, not a fully qualified URI', examples=['salesloft.com']),
        Property('conversational_name', StringType, description='Conversational name of the Account', examples=['Hogwarts']),
        Property('description', StringType, description='Description', examples=['British school of magic for students']),
        Property('phone', StringType, description='Phone number without formatting', examples=['+1 444 555 6666']),
        Property('website', StringType, description='Website', examples=['https://salesloft.com']),
        Property('linkedin_url', StringType, description='Full LinkedIn url', examples=['https://www.linkedin.com/company/2296178/']),
        Property('twitter_handle', StringType, description='Twitter handle, with @', examples=['@kyleporter']),
        Property('street', StringType, description='Street name and number', examples=['4 Picket Drive']),
        Property('city', StringType, description='City', examples=['Dufftown']),
        Property('state', StringType, description='State', examples=['Mortlach']),
        Property('postal_code', StringType, description='Postal code', examples=['55555']),
        Property('country', StringType, description='Country', examples=['Scotland']),
        Property('locale', StringType, description='Time locale', examples=['Europe/London']),
        Property('industry', StringType, description='Industry', examples=['Education']),
        Property('company_type', StringType, description='Type of the Account\'s company', examples=['Private']),
        Property('founded', StringType, description='Date or year of founding', examples=['March 1st, 1820']),
        Property('revenue_range', StringType, description='Estimated revenue range', examples=['1,000,000-2,000,000']),
        Property('size', StringType, description='Estimated number of people in employment', examples=['1500']),
        Property('crm_id', StringType, description='CRM ID', examples=['003i000001mnhpD']),
        Property('crm_url', StringType, description='CRM url', examples=['https://na15.salesforce.com/003i000001mnhpD']),
        Property('crm_object_type', StringType, description='CRM object type', examples=['account']),
        Property('owner_crm_id', StringType, description='Mapped owner field from the CRM', examples=['003i000001mnhpD']),
        Property('prospector_engagement_score', StringType, description='Prospector engagement score for this account, normalized on a scale of 0.0 to 5.0. For the customers that do not opt-in to account engagement scoring, it will always be null', examples=['4.15']),
        Property('prospector_engagement_level', StringType, description='Prospector engagement level for this account, derived from prospector_engagement_score. For the customers that do not opt-in to account engagement scoring, it will always be null', examples=['high']),
        Property('last_contacted_at', DateTimeType, description='Datetime this Account was last contacted', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('last_contacted_type', StringType, description='The type of the last touch to this Account. Can be call, email, other', examples=['call']),
        Property('do_not_contact', BooleanType, description='Whether this company has opted out of communications. Do not contact someone at this company when this is set to true', examples=[True]),
        Property('custom_fields', ObjectType(additional_properties=True), description='Custom fields are defined by the user''s team. Only fields with values are presented in the API.', examples=['{"MyField":"A Value","Other":"Field"}']),
        # Documentation states 'user_relationships' type is object, API returns object[]
        Property('user_relationships', ArrayType(ObjectType(additional_properties=True)), description='Filters by accounts matching all given user relationship fields, _is_null or _unmapped can be passed to filter accounts with null or unmapped user relationship values', examples=['{"bff":"0037h00000d78aAAAQ","Other":"_is_null"}']),
        Property('tags', ArrayType(StringType), description='All tags applied to this Account', examples=['["7-23-2017","dreamforce"]']),

        Property(
            'counts',
            ObjectType(
                Property('people', IntegerType, description='Number of people in SalesLoft associated with this Account', examples=[15]),
            ),
        ),

        Property(
            'owner',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that is marked as the owner of this Account',
        ),

        Property(
            'creator',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that created this Account',
        ),

        Property(
            'last_contacted_by',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that last contacted this Account',
        ),

        Property(
            'last_contacted_person',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='Person who was last contacted at this Account',
        ),

        Property(
            'company_stage',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/account_stages/1']),
            ),
            description='Company Stage that this Account has set. This is referred to as Account Stage in other parts of the API. When sorting by account_stage, the company stage''s order is used',
        ),

        Property(
            'account_tier',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/account_tiers/1']),
            ),
            description='Account Tier that this Account has set',
        ),
    ).to_dict()
