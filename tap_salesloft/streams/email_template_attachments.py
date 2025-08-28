from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class EmailTemplateAttachmentsStream(SalesloftStream):
    '''Email Template Attachments Stream, referenced from https://developers.salesloft.com/docs/api/email-template-attachments-index'''

    name = 'email_template_attachments'
    path = '/v2/email_template_attachments'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of email template attachment association', examples=[5]),
        Property('attachment_id', IntegerType, description='ID of the email template attachment', examples=[10]),

        Property('email_template',
            ObjectType(
                Property('id', IntegerType, examples=[42]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/email_templates/42']),
            ),
            description='Link and id of specific email template',
        ),

        Property('name', StringType, description='Name of the attachment', examples=['example_attachment.gif']),
        Property('download_url', StringType, description='Download url of the attachment', examples=['https://path/to/example_attachment.gif']),
        Property('attachment_file_size', IntegerType, description='The size of the attachment', examples=[2]),
        Property('scanned', BooleanType, description='Checks if attachment has been scanned', examples=[True]),
        Property('attachment_content_type', StringType, description='Content type of the attachment', examples=['pdf, jpeg']),
        # Documentation states 'attachment_fingerprint' type is integer, API returns string
        Property('attachment_fingerprint', StringType, description='Unique attachment Identifier', examples=['13231232']),
    ).to_dict()
