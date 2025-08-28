from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    DateType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class RegistrationsPlaysStream(SalesloftStream):
    '''Registrations Plays Stream, referenced from https://developers.salesloft.com/docs/api/integrations-signals-registrations-plays-index'''

    name = 'registrations_plays'
    path = '/v2/integrations/signals/registrations/plays'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('state', StringType, description='State of play registration, either ''draft'' or ''enabled''. ''draft'' means Play is only available to your team and Play can be updated as needed. ''enabled'' means Play is available to all teams, and only certain properties of the Play (name, label, etc.) can be updated.', examples=['draft']),
        Property('signal_type', StringType, description='Signal Type', examples=['contract_engagement']),
        Property('signal_registration', ObjectType(additional_properties=True), description='Associated signal registration', examples=['{"id":1,"href":"https://api.salesloft.com/integrations/signals/registrations/1"}']),
        Property('owner_user_guid', StringType, description='User GUID of Play Registration owner', examples=['aa767504-c6c6-426e-824e-7402a70531e7']),
        Property('owner_tenant_id', IntegerType, description='Tenant ID of Play Registration owner', examples=[123681]),
        Property('name', ObjectType(additional_properties=True), description='Localized mapping of the Play Registration''s name, which is displayed as a title for the Play', examples=['{"en-us":"Meeting Reminder"}']),
        Property('label', ObjectType(additional_properties=True), description='Localized mapping of the Play Registration''s label, which provides a short description used to explain the signal action combination', examples=['{"en-us":"Meeting Reminder Play"}']),
        Property('integration', ObjectType(additional_properties=True), description='Associated integration', examples=['{"id":2,"_href":"https://api.salesloft.com/integrations/2"}']),
        Property('indicators', ArrayType(StringType), description='List of Play Indicators. Come from Signal Registration Indicators. An Indicator set by a Play must be a part of its Signal Registration i.e. if this Indicator is present, then that Play will execute.', examples=['["indicator_key_0"]']),
        Property('identifier', StringType, description='Play Identifier', examples=['integration.oauth_with_scopes.video_watched.play_enabled']),
        Property('id', IntegerType, required=True, description='ID of Play Registration', examples=[1]),
        Property('enabled_at', DateType, description='ISO8601 timestamp of when play registration was enabled', examples=['2025-08-05']),
        Property('description', ObjectType(additional_properties=True), description='Localized mapping of the Play Registration''s description, which provides a more detailed description of the signal action combination', examples=['{"en-us":"A Play to remind people of meetings."}']),
        Property('created_at', DateType, description='ISO8601 timestamp of when play registration was created', examples=['2025-08-05']),
        Property('attributes', ObjectType(additional_properties=True), description='Describe the Task that will get generated, when it will be due, and instructions/template provided to the seller at execution time. (If task_type is email, then you can optionally set an email_subject and email_body.)', examples=['{"task_type":"call","task_subject":{"es-es":"Llamar a {{name}}","en-us":"Call {{name}}"}}']),
    ).to_dict()
