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

class EmailsStream(SalesloftStream):
    '''Emails Stream, referenced from https://developers.salesloft.com/docs/api/activities-emails-index'''

    name = 'emails'
    path = '/v2/activities/emails'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Email', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the email was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the email was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('recipient_email_address', StringType, description='Email address of the recipient', examples=['bob.smith@example.com']),
        Property('status', StringType, description='Status of this email through the sending process. Possible values are: sent, sent_from_gmail, sent_from_external, pending, pending_reply_check, scheduled, sending, delivering, failed, cancelled, pending_through_gmail, pending_through_external', examples=['sent']),
        Property('bounced', BooleanType, description='Whether this email bounced', examples=[False]),
        Property('send_after', DateTimeType, description='When this email will be sent, or null if already sent', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('sent_at', DateTimeType, description='When this email was sent, or null if it was not sent', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('view_tracking', BooleanType, description='Whether this email had view tracking enabled', examples=[True]),
        Property('click_tracking', BooleanType, description='Whether this email had click tracking enabled', examples=[True]),
        Property('message_id', StringType, description='ID of Client Email Message', examples=['TRHgY3+9g8nDFvnmJyKoNn=xY_qdtAW1fjpMewpbjgJR5qL6pub@mail.gmail.com']),
        Property('headers', ObjectType(additional_properties=True), description='Selected headers that are included if this email used them. Available keys are: cc, bcc', examples=['{"cc":"sb@salesloft.com","bcc":"track@salesforce.com"}']),
        Property('personalization', StringType, description='Percentage of this email that has been personalized', examples=['13.4']),
        Property('subject', StringType, description='Subject of the email. This field has been determined sensitive and requires a specific scope to access it.'),
        Property('body', StringType, description='Email Body', examples=['Hello']),
        Property('error_message', StringType, description='Error message of the email. This field has been determined sensitive and requires a specific scope to access it.'),
        Property('draft_with_ai', BooleanType, description='Whether this email body was drafted with AI assistance', examples=[True]),

        Property(
            'counts',
            ObjectType(
                Property('clicks', IntegerType, description='The number of times links in the email were clicked', examples=[2]),
                Property('views', IntegerType, description='The number of times the email was opened', examples=[3]),
                Property('replies', IntegerType, description='The number of replies the email received', examples=[1]),
                Property('unique_devices', IntegerType, description='The number of unique devices that opened the email', examples=[4]),
                Property('unique_locations', IntegerType, description='The number of unique locations that opened the email', examples=[3]),
                Property('attachments', IntegerType, description='The number of attachments on the email', examples=[0]),
            ),
        ),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that sent this email',
        ),

        Property(
            'recipient',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='The person whom received this email',
        ),

        Property(
            'mailing',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
            ),
            description='The mailing that this email was a part of',
        ),

        Property(
            'action',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
            ),
            description='Action that this email was sent from, or null if not sent through a cadence',
        ),

        Property(
            'task',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
            ),
            description='Task that this email was sent from, or null if not sent through a cadence',
        ),

        Property(
            'crm_activity',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/crm_activities/1']),
            ),
            description='CRM Activity associated with this email',
        ),

        Property(
            'cadence',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/cadences/1']),
            ),
            description='Cadence the email was sent on',
        ),

        Property(
            'step',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/steps/1']),
            ),
            description='Step the email was sent on',
        ),

        Property(
            'email_template',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/email_templates/1']),
            ),
            description='Template used for this email',
        ),

        Property(
            'additional_recipients',
            ArrayType(
                ObjectType(
                    Property('id', IntegerType, examples=[2]),
                    Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/2']),
                )
            ),
            description='The list of people, other than the (primary) recipient, who received this email via TO and CC',
        ),
    ).to_dict()
