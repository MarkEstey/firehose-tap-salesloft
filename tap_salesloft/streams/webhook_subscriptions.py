from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class WebhookSubscriptionsStream(SalesloftStream):
    '''Webhook Subscriptions Stream, referenced from https://developers.salesloft.com/docs/api/webhook-subscriptions-index'''

    name = 'webhook_subscriptions'
    path = '/v2/webhook_subscriptions'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('user_guid', StringType, description='UUID of the user the token is associated with', examples=['51398ccd-309e-467f-aae2-4b0f66b5c11d']),
        Property('tenant_id', IntegerType, description='ID for the tenant to which user is assigned', examples=[16]),
        Property('id', IntegerType, required=True, description='ID for the Webhook Subscription', examples=[1]),
        Property('event_type', StringType, description='Type of event the subscription is for', examples=['link_swap']),
        Property('enabled', BooleanType, description='Is the Webhook Subscription enabled or not', examples=[True]),
        Property('callback_url', StringType, description='URL for your callback handler', examples=['https://mycompany.com/api/person_called_handler']),
        Property('callback_token', StringType, description='SalesLoft will include this token in the webhook event payload when calling your callback_url. It is strongly encouraged for your handler to verify this value in order to ensure the request came from SalesLoft.', examples=['xT7/Buu0Vz2ffiIPuMlBGu+cwku1dr7G5jeiM0iyfYIT0l4z3azNGjiXWTOX/8OT']),
    ).to_dict()
