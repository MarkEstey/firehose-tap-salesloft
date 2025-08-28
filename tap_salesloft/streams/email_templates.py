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

class EmailTemplatesStream(SalesloftStream):
    '''Email Templates Stream, referenced from https://developers.salesloft.com/docs/api/email-templates-index'''

    name = 'email_templates'
    path = '/v2/email_templates'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of email template', examples=[5]),
        Property('title', StringType, description='Title of the email template', examples=['Welcome email']),
        Property('subject', StringType, description='Subject of the email template', examples=['Welcome to SalesLoft!']),
        Property('body', StringType, description='Sanitized body of the email template without email signature', examples=['<div><div>Welcome to the SalesLoft family! My name is Sarah and I''m your implementation consultant. I''m here to get you up and running. It''s my job to help you configure your team''s SalesLoft access, provide customized training for your specific goals, and make sure that you and your team are ready to crush your goals.</div><div dir="ltr"><br></div>Thank you,<br></div>']),
        Property('body_preview', StringType, description='A plain text version of the first 100 characters of the body of the email template', examples=['hello hey sounds good ok ok with an edit ok now i''m comic sans 14']),
        Property('created_at', DateTimeType, description='Datetime of when the email template was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the email template was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('last_used_at', DateTimeType, description='Datetime of when the email template was last used', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('archived_at', DateTimeType, description='Datetime of when the email template was archived, if archived', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('shared', BooleanType, description='Whether this email template is visible to team members (shared)', examples=[False]),
        Property('open_tracking_enabled', BooleanType, description='Whether open tracking is enabled for this email template', examples=[True]),
        Property('click_tracking_enabled', BooleanType, description='Whether click tracking is enabled for this email template', examples=[True]),
        Property('cadence_template', BooleanType, description='Whether this email template is only used on a cadence step. These templates are not visible in the SalesLoft application template list. If false, this email template is visible in the SalesLoft application, and may be used when composing an email or creating a cadence step.', examples=[True]),

        Property(
            'counts',
            ObjectType(
                Property('sent_emails', IntegerType, description='The number of times the email template was sent out', examples=[59]),
                Property('views', IntegerType, description='The number of times the email template was opened', examples=[3]),
                Property('clicks', IntegerType, description='The number of times links in the email template were clicked', examples=[20]),
                Property('replies', IntegerType, description='The number of replies the email template received', examples=[1]),
                Property('bounces', IntegerType, description='The number of bounces the email template received', examples=[10]),
            ),
        ),

        Property(
            'template_owner',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that owns this email template',
        ),

        Property(
            'team_template',
            ObjectType(
                Property('id', StringType, examples=['00000000-0000-0000-0000-000000000000']),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/team_templates/00000000-0000-0000-0000-000000000000']),
            ),
            description='Associated team template, if any',
        ),

        Property('_links', ObjectType(additional_properties=True), description='Links to attachments and tags resources for this email template.', examples=['{"attachments":"https://api.salesloft.com/v2/email_template_attachments?email_template_id[]=1"}']),
        Property('tags', ArrayType(StringType), description='All tags applied to this email template', examples=['["7-23-2017","internal"]']),

        Property(
            'groups',
            ArrayType(
                ObjectType(
                    Property('id', IntegerType, examples=[921]),
                    Property('_href', StringType, examples=['https://api.salesloft.com/v2/groups/921']),
                )
            ),
            description='Groups to which this template is assigned, if any',
        ),
    ).to_dict()
