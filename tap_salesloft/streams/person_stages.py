from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class PersonStagesStream(SalesloftStream):
    '''Person Stages Stream, referenced from https://developers.salesloft.com/docs/api/person-stages-index'''

    name = 'person_stages'
    path = '/v2/person_stages'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Person Stage', examples=[1]),
        Property('name', StringType, description='Name of Person Stage', examples=['Entry Stage']),
        Property('created_at', DateTimeType, description='Datetime of when the Person Stage was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, description='Datetime of when the Person Stage was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('order', IntegerType, description='Sortable value of Person Stage order', examples=[16]),
        Property('active', BooleanType, description='Flag signalizing whether the Person Stage is active', examples=[True]),
    ).to_dict()
