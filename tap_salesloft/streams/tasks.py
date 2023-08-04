from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    DateType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class TasksStream(SalesloftStream):
    """Tasks Stream, referenced from https://developers.salesloft.com/docs/api/tasks-index"""

    name = "tasks"
    path = "/v2/tasks"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Task",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Task was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the Task was last updated",
        ),
        Property(
            "description",
            StringType,
            description="A description of the task recorded for person at completion time",
        ),
        Property(
            "due_date",
            DateType,
            description="Date of when the Task is due, ISO-8601 date format required",
        ),
        Property(
            "due_at",
            DateTimeType,
            description="Datetime of when the Task is due, can be null. ISO-8601 datetime format required",
        ),
        Property(
            "subject",
            StringType,
            description="Subject line of the task",
        ),
        Property(
            "current_state",
            StringType,
            description="The state of the task. Valid states are: scheduled, completed",
        ),
        Property(
            "person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The person to be contacted",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User who is assigned the task",
        ),
        Property(
            "created_by_user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User who created the task",
        ),
        Property(
            "task_type",
            StringType,
            description="The type of the task. Valid types are: call, email, general",
        ),
        Property(
            "remind_at",
            DateTimeType,
            description="Datetime of when the user will be reminded of the task, ISO-8601 datetime format required",
        ),
        Property(
            "completed_at",
            DateTimeType,
            description="Datetime of when the task was completed, ISO-8601 datetime format required",
        ),
        Property(
            "completed_by",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User who completed the task",
        ),
    ).to_dict()
