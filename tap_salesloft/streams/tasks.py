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
    '''Tasks Stream, referenced from https://developers.salesloft.com/docs/api/tasks-index'''

    name = 'tasks'
    path = '/v2/tasks'
    primary_keys = ['id']
    replication_key = 'updated_at'

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of Task', examples=[1]),
        Property('created_at', DateTimeType, description='Datetime of when the Task was created', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('updated_at', DateTimeType, required=True, description='Datetime of when the Task was last updated', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('description', StringType, description='A description of the task recorded for person at completion time', examples=['Ask John Wick about his dog.']),
        Property('due_date', DateType, description='Date of when the Task is due, ISO-8601 date format required', examples=['2026-01-01']),
        Property('due_at', DateTimeType, description='Datetime of when the Task is due, can be null. ISO-8601 datetime format required', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('subject', StringType, description='Subject line of the task', examples=['Call John Wick']),

        Property('current_state', StringType, description='The state of the task. Valid states are: scheduled, completed', examples=['scheduled']),

        Property(
            'person',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/people/1']),
            ),
            description='The person to be contacted',
        ),

        Property(
            'opportunity',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/opportunities/1']),
            ),
            description='The opportunity associated with task',
        ),

        Property(
            'user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User who is assigned the task',
        ),

        Property(
            'created_by_user',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User who created the task',
        ),

        Property('task_type', StringType, description='The type of the task. Valid types are: call, email, general', examples=['call']),
        Property('remind_at', DateTimeType, description='Datetime of when the user will be reminded of the task, ISO-8601 datetime format required', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('expires_after', DateTimeType, description='Datetime of when the the task will expire, ISO-8601 datetime format required', examples=['2025-01-01T00:00:00.000000+00:00']),
        Property('completed_at', DateTimeType, description='Datetime of when the task was completed, ISO-8601 datetime format required', examples=['2025-01-01T00:00:00.000000+00:00']),

        Property(
            'completed_by',
            ObjectType(
                Property('id', IntegerType, examples=[1]),
                Property('_href', StringType, examples=['https://api.salesloft.com/v2/users/1']),
            ),
            description='User who completed the task',
        ),
    ).to_dict()
