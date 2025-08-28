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

class PeopleStream(SalesloftStream):
    '''People Stream, referenced from https://developers.salesloft.com/docs/api/people-index'''

    name = 'people'
    path = '/v2/people'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='Person ID', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the person was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the person was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('last_contacted_at', DateTimeType, description='Last datetime this person was contacted', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('last_replied_at', DateTimeType, description='Last datetime this person replied to an email', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('first_name', StringType, description='First name', examples=['Pat']),
        Property('last_name', StringType, description='Last name', examples=['Johnson']),
        Property('display_name', StringType, description='Either the full name or the email address. Use this when showing a person''s name', examples=['Pat Johnson']),
        Property('email_address', StringType, description='Email address', examples=['pat.johnson@example.com']),
        Property('full_email_address', StringType, description='Full email address with name', examples=['Pat Johnson <pat.johnson@example.com>']),
        Property('secondary_email_address', StringType, description='Alternate email address', examples=['pat.johnson@example.com']),
        Property('personal_email_address', StringType, description='Personal email address', examples=['pat.johnson@example.com']),
        Property('phone', StringType, description='Phone without formatting', examples=['+1 444 555 6666']),
        Property('phone_extension', StringType, description='Phone extension without formatting', examples=['x123']),
        Property('home_phone', StringType, description='Home phone without formatting', examples=['+1 444 555 6666']),
        Property('mobile_phone', StringType, description='Mobile phone without formatting', examples=['+1 444 555 6666']),
        Property('linkedin_url', StringType, description='Linkedin URL', examples=['https://www.linkedin.com/in/username']),
        Property('title', StringType, description='Job title', examples=['Sales Development Representative']),
        Property('city', StringType, description='City', examples=['Atlanta']),
        Property('state', StringType, description='State', examples=['Georgia']),
        Property('country', StringType, description='Country', examples=['United States']),
        Property('work_city', StringType, description='Work location - city', examples=['Atlanta']),
        Property('work_state', StringType, description='Work location - state', examples=['Georgia']),
        Property('work_country', StringType, description='Work location - country', examples=['United States']),
        Property('crm_url', StringType, description='CRM url', examples=['https://na15.salesforce.com/003i000001mnhpD']),
        Property('crm_id', StringType, description='CRM ID', examples=['003i000001mnhpD']),
        Property('account_crm_id', StringType, description='Account CRM ID', examples=['0000R00002fHqiMAAA']),
        Property('crm_object_type', StringType, description='CRM object type', examples=['Lead']),
        Property('owner_crm_id', StringType, description='Mapped owner field from your CRM', examples=['003i000001mnhpD']),
        Property('person_company_name', StringType, description='Company name. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended', examples=['SalesLoft']),
        Property('person_company_website', StringType, description='Company website. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended', examples=['https://salesloft.com']),
        Property('person_company_industry', StringType, description='Company industry. This property is specific to this person, unrelated to the company object. Updating the company object associated with this person is recommended', examples=['Information Technology']),
        Property('do_not_contact', BooleanType, description='Whether or not this person has opted out of all communication. Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. If this person is currently in a cadence, they will be removed.', examples=[True]),
        Property('bouncing', BooleanType, description='Whether this person''s current email address has bounced', examples=[False]),
        Property('locale', StringType, description='Time locale of the person', examples=['US/Eastern']),
        Property('locale_utc_offset', IntegerType, description='The locale''s timezone offset from UTC in minutes', examples=[-480]),
        Property('eu_resident', BooleanType, description='Whether this person is marked as a European Union Resident or not', examples=[False]),
        Property('personal_website', StringType, description='The website of this person', examples=['https://salesloft.com']),
        Property('twitter_handle', StringType, description='The twitter handle of this person', examples=['@kyleporter']),
        Property('last_contacted_type', StringType, description='The type of the last touch to this person. Can be call, email, other', examples=['call']),
        Property('job_seniority', StringType, description='The Job Seniority of a Person, must be one of director, executive, individual_contributor, manager, vice_president, unknown', examples=['vice_president']),
        Property('job_function', StringType, description='The Job Function of a Person', examples=['marketing']),
        Property('custom_fields', ObjectType(additional_properties=True), description='Custom fields are defined by the user''s team. Only fields with values are presented in the API.', examples=['{"MyField":"A Value","Other":"Field"}']),
        Property('tags', ArrayType(StringType), description='All tags applied to this person', examples=['["7-23-2017","dreamforce"]']),
        Property('contact_restrictions', ArrayType(StringType), description='Specific methods of communication to prevent for this person. This will prevent individual execution of these communication types as well as automatically skip cadence steps of this communication type for this person in SalesLoft. Values currently accepted: call, email, message', examples=['["call","email","message"]']),
        Property('success_count', IntegerType, description='The person''s success count. 1 if person has any active successes, 0 otherwise.', examples=[1]),
        Property('starred', BooleanType, description='Whether this person is starred by the current user', examples=[True]),
        Property('untouched', BooleanType, description='The person''s untouched status', examples=[False]),
        Property('hot_lead', BooleanType, description='Whether this person is marked as a hot lead', examples=[True]),
        Property('external_source', StringType, description='The external source from where a person was imported', examples=['zoominfo']),

        Property(
            'counts',
            ObjectType(
                Property('emails_sent', IntegerType, description='The number of emails sent to this person', examples=[3]),
                Property('emails_viewed', IntegerType, description='The number of unique emails viewed by this person', examples=[2]),
                Property('emails_clicked', IntegerType, description='The number of unique emails clicked by this person', examples=[1]),
                Property('emails_replied_to', IntegerType, description='The number of unique emails replied to by this person', examples=[0]),
                Property('emails_bounced', IntegerType, description='The number of unique emails sent to this person that bounced', examples=[0]),
                Property('calls', IntegerType, description='The number of calls logged to this person', examples=[4]),
            ),
        ),

        Property(
            'account',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/accounts/1']),
            ),
            description='Account that this person is associated to',
        ),

        Property(
            'owner',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that is marked as the owner of this person',
        ),

        Property(
            'last_contacted_by',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that last contacted this person',
        ),

        Property(
            'import',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/imports/1']),
            ),
            description='Import that this person was a part of',
        ),

        Property(
            'person_stage',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/person_stages/1']),
            ),
            description='Person stage that this person has set',
        ),

        Property(
            'most_recent_cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='Cadence this person was most recently added to',
        ),

        Property(
            'last_completed_step_cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='Cadence of the last completed step this person',
        ),

        Property(
            'last_completed_step',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/1']),
            ),
            description='Last completed step of the cadence',
        ),

        Property(
            'cadences',
            ArrayType(
                ObjectType(
                    Property('id', IntegerType, examples=[1]),
                    Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
                )
            ),
            description='The list of active cadences person is added to',
        ),
    ).to_dict()
