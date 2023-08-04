from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    CustomType,
    PropertiesList,
    Property,
    StringType,
)


class StepsStream(SalesloftStream):
    """Steps Stream, referenced from https://developers.salesloft.com/docs/api/steps-index"""

    name = "steps"
    path = "/v2/steps"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Step",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Step was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the Step was last updated",
        ),
        Property(
            "disabled",
            BooleanType,
            description="Whether this step is currently active",
        ),
        Property(
            "type",
            StringType,
            description="The type of the action scheduled by this step. "
            "Valid types are: email, phone, integration, other. New types may be added in the future.",
        ),
        Property(
            "name",
            StringType,
            description="Name of the step",
        ),
        Property(
            "display_name",
            StringType,
            description="Display name of the step",
        ),
        Property(
            "day",
            IntegerType,
            description="Day this step is associated with up",
        ),
        # Documentation states 'step_number' type is integer, API returns either numeric or string
        Property(
            "step_number",
            CustomType({"type": ["integer", "string", "null"]}),
            description="The number of the step for this day",
        ),
        Property(
            "multitouch_enabled",
            BooleanType,
            description="Whether this step is a multitouch cadence step",
        ),
        Property(
            "details",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Details pertaining to the specific step type",
        ),
        Property(
            "cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The cadence of the step",
        ),
    ).to_dict()
