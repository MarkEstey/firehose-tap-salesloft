from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class PendingEmailsStream(SalesloftStream):
    '''Pending Emails Stream, referenced from https://developers.salesloft.com/docs/api/pending-emails-index'''

    name = 'pending_emails'
    path = '/v2/pending_emails'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of the email', examples=[1]),
        Property('mailbox', StringType, description='Email Address of the pending email', examples=['example@salesloft.com']),

        Property(
            'mime_email_payload',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/mime_email_payloads/1']),
            ),
            description='The email MIME payload',
        ),
    ).to_dict()
