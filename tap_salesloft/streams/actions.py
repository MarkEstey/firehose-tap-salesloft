from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class ActionsStream(SalesloftStream):
    """Actions Stream, referenced from https://developers.salesloft.com/docs/api/actions-index"""

    name = "actions"
    path = "/v2/actions"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Action",
        ),
        Property(
            "due",
            BooleanType,
            description="Whether this step is due",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Action was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the Action was last updated",
        ),
        Property(
            "type",
            StringType,
            description="The type of this action. Valid types are: email, phone, other. New types may be added in the future.",
        ),
        Property(
            "status",
            StringType,
            description="The current state of the person on the cadence. Possible values are: in_progress: this action has not been completed; "
            "pending_activity: this action has been acted upon, but the action has not been completed. (i.e. the email is scheduled to send, but has not been delivered yet)",
        ),
        Property(
            "due_on",
            DateTimeType,
            description="When action is due",
        ),
        Property(
            "multitouch_group_id",
            IntegerType,
            description="ID of the multitouch group",
        ),
        Property(
            "action_details",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The type specific action details",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User assigned to action",
        ),
        Property(
            "person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The subject of an action",
        ),
        Property(
            "cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The cadence of an action",
        ),
        Property(
            "step",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The step of an action",
        ),
    ).to_dict()
