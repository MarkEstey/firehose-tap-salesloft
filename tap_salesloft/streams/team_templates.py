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

class TeamTemplatesStream(SalesloftStream):
    '''Team Templates Stream, referenced from https://developers.salesloft.com/docs/api/team-templates-index'''

    name = 'team_templates'
    path = '/v2/team_templates'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', StringType, required=True, description='ID of team template', examples=['51226150-3108-4dea-883b-0c0d7388f456']),
        Property('title', StringType, description='Title of the team template', examples=['VP Breakup Email']),
        Property('subject', StringType, description='Subject of the team template', examples=['It''s time to say goodbye']),
        Property('body', StringType, description='Body of the team template', examples=['<div>Do you know about birds?</div><div>You can find them here: <a href="https://www.allaboutbirds.org/guide/search/" target="_blank">https://www.allaboutbirds.org/guide/search/</a></div>']),
        Property('body_preview', StringType, description='A plain text version of the first 100 characters of the body of the team template', examples=['hello hey sounds good ok ok with an edit ok now i''m comic sans 14']),
        Property('created_at', DateTimeType, description='Datetime of when the team template was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the team template was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('last_used_at', DateTimeType, description='Datetime of when the team template was last used', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('archived_at', DateTimeType, description='Datetime of when the team template was archived, if archived', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('last_modified_at', DateTimeType, description='Datetime of when the team template was last modified', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('open_tracking_enabled', BooleanType, description='Whether open tracking is enabled for this team template', examples=[True]),
        Property('click_tracking_enabled', BooleanType, description='Whether click tracking is enabled for this team template', examples=[True]),

        Property(
            'counts',
            ObjectType(
                Property('sent_emails', IntegerType, description='The number of times the team template was sent out', examples=[59]),
                Property('views', IntegerType, description='The number of times the team template was opened', examples=[3]),
                Property('clicks', IntegerType, description='The number of times links in the team template were clicked', examples=[20]),
                Property('replies', IntegerType, description='The number of replies the team template received', examples=[1]),
                Property('bounces', IntegerType, description='The number of bounces the team template received', examples=[10]),
            ),
        ),

        Property(
            'last_modified_user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that last modified this team template',
        ),

        Property(
            'groups',
            ArrayType(
                ObjectType(
                    Property('id', IntegerType, examples=[921]),
                    Property('_href', StringType, examples=['https://api.salesloft.com/v2/groups/921']),
                )
            ),
            description='Groups to which this team template is assigned, if any',
        ),

        Property('_links', ObjectType(additional_properties=True), description='Links to attachments resource for this template', examples=['{"attachments":"https://api.salesloft.com/v2/team_template_attachments?team_template_id[]=1"}']),
        Property('tags', ArrayType(StringType), description='All tags applied to this team template', examples=['["7-23-2017","internal"]']),
    ).to_dict()
