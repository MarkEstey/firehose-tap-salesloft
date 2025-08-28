from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class CrmActivityFieldsStream(SalesloftStream):
    '''CRM Activity Fields Stream, referenced from https://developers.salesloft.com/docs/api/crm-activity-fields-index'''

    name = 'crm_activity_fields'
    path = '/v2/crm_activity_fields'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of CrmActivityField', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the CrmActivityField was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, description='Datetime of when the CrmActivityField was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('title', StringType, description='A human friendly title for this field', examples=['Field Name']),
        Property('salesforce_object_type', StringType, description='The Salesforce object type that this field maps to. Valid object types are: Task. More object types may be added in the future.', examples=['Task']),
        Property('crm_object_type', StringType, description='The CRM object type that this field maps to. Valid object types are CRM dependent: Task, Phonecall, Email.', examples=['Task']),
        Property('source', StringType, description='SalesLoft object that this field is mapped for. Valid sources are: email, phone', examples=['phone']),
        Property('field', StringType, description='The CRM field name', examples=['orgName__Field_Name__c']),
        Property('field_type', StringType, description='The type of this field in your CRM. Certain field types can only accept structured input.', examples=['boolean']),
        Property('value', StringType, description='A value to always be written. This value does not need to be sent to other endpoints'' crm params, but must be the exact value if sent. Email source fields will always have a value present.', examples=['Email']),
        Property('picklist_values', ObjectType(additional_properties=True), description='Valid picklist values, if present for this field. The format is {label => value}. If present, only values in the picklist structure can be used as a crm param.', examples=['{"High":"High","Low":"Low"}']),
    ).to_dict()
