from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class NotesStream(SalesloftStream):
    '''Notes Stream, referenced from https://developers.salesloft.com/docs/api/notes-index'''

    name = 'notes'
    path = '/v2/notes'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='Note ID', examples=[1]),
        Property('content', StringType, description='The content of the note', examples=['Was very interested in a demo at a later time']),
        Property('created_at', DateTimeType, description='Datetime of when the note was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the note was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('associated_type', StringType, description='Type of associated resource (''person'' or ''account'')', examples=['person']),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User that wrote this note',
        ),

        Property(
            'associated_with',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='Item on which the note was made',
        ),

        Property(
            'call',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/activities/calls/1']),
            ),
            description='Call linked to the note',
        ),
    ).to_dict()
