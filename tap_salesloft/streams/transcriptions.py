from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class TranscriptionsStream(SalesloftStream):
    '''Transcriptions Stream, referenced from https://developers.salesloft.com/docs/api/conversations-transcriptions-find-all-transcripts'''

    name = 'transcriptions'
    path = '/v2/transcriptions'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', StringType, required=True, description='Transcription Id'),
        Property('language_code', StringType, description='The text''s BCP-47 language code, such as "en-US" or "sr-Latn".\nReference: http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.\nPossible values: [en-AU, en-AB, en-GB, en-IN, en-IE, en-NZ, en-ZA, en-US, en-WL, es-ES, es-US, nl-NL, it-IT, fr-FR, fr-CA, de-DE, de-CH]'),
        Property('created_at', DateTimeType, description='Date transcription was created'),
        Property('updated_at', DateTimeType, required=True, description='Date transcription was last updated'),

        Property(
            'conversation',
            ObjectType(
                Property('id', StringType),
                Property('_href', StringType),
            ),
            description='Reference to the Conversation',
        ),

        Property(
            'transcription_sentences',
            ObjectType(
                Property('id', StringType),
                Property('_href', StringType),
            ),
            description='Reference to the transcription sentences',
        ),

        Property(
            'transcription_artifact',
            ObjectType(
                Property('id', StringType),
                Property('_href', StringType),
            ),
            description='Reference to the transcription artifact',
        ),
    ).to_dict()
