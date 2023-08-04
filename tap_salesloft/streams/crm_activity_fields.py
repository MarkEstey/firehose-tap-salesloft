from tap_salesloft.client import SalesloftStream

from singer_sdk.helpers._typing import TypeConformanceLevel

from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class CrmActivityFieldsStream(SalesloftStream):
    """CRM Activity Fields Stream, referenced from https://developers.salesloft.com/docs/api/crm-activity-fields-index"""

    name = "crm_activity_fields"
    path = "/v2/crm_activity_fields"
    primary_keys = ["id"]

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of CrmActivityField",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the CrmActivityField was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the CrmActivityField was last updated",
        ),
        Property(
            "title",
            StringType,
            description="A human friendly title for this field",
        ),
        Property(
            "salesforce_object_type",
            StringType,
            description="The Salesforce object type that this field maps to. "
            "Valid object types are: Task. More object types may be added in the future.",
        ),
        Property(
            "crm_object_type",
            StringType,
            description="The CRM object type that this field maps to. "
            "Valid object types are CRM dependent: Task, Phonecall, Email.",
        ),
        Property(
            "source",
            StringType,
            description="SalesLoft object that this field is mapped for. Valid sources are: email, phone",
        ),
        Property(
            "field",
            StringType,
            description="The CRM field name",
        ),
        Property(
            "field_type",
            StringType,
            description="The type of this field in your CRM. Certain field types can only accept structured input.",
        ),
        Property(
            "value",
            StringType,
            description="A value to always be written. "
            "This value does not need to be sent to other endpoints' crm params, but must be the exact value if sent. "
            "Email source fields will always have a value present.",
        ),
        Property(
            "picklist_values",
            ObjectType(),
            description="Valid picklist values, if present for this field. The format is {label => value}. "
            "If present, only values in the picklist structure can be used as a crm param.",
        ),
    ).to_dict()
