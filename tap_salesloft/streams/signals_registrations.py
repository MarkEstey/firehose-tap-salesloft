from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class SignalsRegistrationsStream(SalesloftStream):
    '''Signals Registrations Stream, referenced from https://developers.salesloft.com/docs/api/integrations-signals-registrations-index'''

    name = 'signals_registrations'
    path = '/v2/integrations/signals/registrations'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('type', StringType, description='Signal registration type.', examples=['video_watched']),
        Property('signal_name', StringType, description='Signal name.', examples=['Video Watched']),
        Property('owner_user_guid', StringType, description='User GUID of the Registration owner.', examples=['20cea35e-3511-461a-9a6f-88d56ad0d320']),
        Property('integration_slug', StringType, description='Integration Slug linked to the signal registration.', examples=['my-integration']),
        Property('integration', ObjectType(additional_properties=True), description='Integration linked to signal registration.', examples=['{"id":1,"_href":"https://api.salesloft.com/v2/integrations/1/"}']),
        Property('indicators', ArrayType(ObjectType(additional_properties=True)), description='Array of signal indicators registrations.'),
        Property('id', IntegerType, required=True, description='Registration ID.', examples=[1]),
        Property('globally_installed_at', StringType, description='ISO8601 timestamp of when the registration was globally installed.', examples=['2023-01-01T10:00:00.000000Z']),
        Property('description', ObjectType(additional_properties=True), description='Localized signal description.', examples=['{"fr-fr":"The Eras Tour film-concert","es-es":"The Eras Tour Concierto la Pelicula","en-us":"The Eras Tour Concert Film","en-gb":"The Eras Tour Concert Film London","de-de":"The Eras Tour Konzertfilm"}']),
        Property('data_shape', ObjectType(additional_properties=True), description='JSON schema of the signal data.', examples=['{"shared_at":{"type":"string","format":"date-time"},"recipient_count":{"type":"number","min":1},"pitch_url":{"type":"string","pattern":"^https://","format":"uri"}}']),
        Property('created_at', StringType, description='ISO8601 timestamp of when the signal registration was created.', examples=['2023-01-01T10:00:00.000000Z']),
        Property('updated_at', DateTimeType, required=True),
        Property('attribution', ArrayType(StringType), description='Array of possible attributions.', examples=['["person","tracked_email_content"]']),
    ).to_dict()
