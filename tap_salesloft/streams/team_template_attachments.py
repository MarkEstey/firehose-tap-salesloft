from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class TeamTemplateAttachmentsStream(SalesloftStream):
    '''Team Template Attachments Stream, referenced from https://developers.salesloft.com/docs/api/team-template-attachments-index'''

    name = 'team_template_attachments'
    path = '/v2/team_template_attachments'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of team template attachment association', examples=[5]),
        Property('attachment_id', IntegerType, description='ID of the team template attachment'),

        Property(
            'team_template',
            ObjectType(
                # Documentation states 'team_template'.'id' type is integer, API returns string
                Property('id', StringType, examples=['21']),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/team_templates/21']),
            ),
            description='Details pertaining to the specific team template',
        ),

        Property('name', StringType, description='Name of the attachment', examples=['example_attachment.gif']),
        Property('download_url', StringType, description='Download url of the attachment', examples=['https://path/to/example_attachment.gif']),
        Property('attachment_file_size', IntegerType, description='The size of the attachment', examples=[2]),
    ).to_dict()
