from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class CalendarEventsStream(SalesloftStream):
    """Calendar Events Stream, referenced from https://developers.salesloft.com/docs/api/calendar-events-index"""

    name = "calendar_events"
    path = "/v2/calendar/events"
    primary_keys = ["id"]

    schema = PropertiesList(
        Property(
            "user_guid",
            StringType,
            description="User GUID of the user calendar.",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Last modification time of the calendar event.",
        ),
        Property(
            "title",
            StringType,
            description="Title of the calendar event",
        ),
        Property(
            "tenant_id",
            IntegerType,
            description="Tenant ID of the user calendar",
        ),
        Property(
            "status",
            StringType,
            description="The status of the calendar event. It can be empty for non-google events.",
        ),
        Property(
            "start_time",
            DateTimeType,
            description="The (inclusive) start time of the calendar event.",
        ),
        Property(
            "recurring",
            BooleanType,
            description="Whether the calendar event is a recurring event.",
        ),
        Property(
            "provider",
            StringType,
            description="The provider of the calendar event.",
        ),
        Property(
            "organizer",
            StringType,
            description="The organizer email of the calendar event.",
        ),
        Property(
            "location",
            StringType,
            description="Location of the calendar event",
        ),
        Property(
            "id",
            StringType,
            required=True,
            description="The calendar event original ID from calendar provider",
        ),
        Property(
            "i_cal_uid",
            StringType,
            description="Calendar event unique identifier (iCalUID)",
        ),
        Property(
            "html_link",
            StringType,
            description="An absolute link to this calendar event in the Google Calendar Web UI.",
        ),
        Property(
            "extended_properties",
            ObjectType(),
            description="Extended properties of the calendar event.",
        ),
        Property(
            "end_time",
            DateTimeType,
            description="The (exclusive) end time of the calendar event.",
        ),
        Property(
            "description",
            StringType,
            description="Description of the calendar event",
        ),
        Property(
            "creator",
            StringType,
            description="The creator email of the calendar event.",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Creation time of the calendar event.",
        ),
        Property(
            "conference_data",
            ObjectType(),
            description="The conference-related information, such as details of a Google Meet conference.",
        ),
        Property(
            "canceled_at",
            DateTimeType,
            description="The canceled date of the calendar event.",
        ),
        Property(
            "calendar_id",
            StringType,
            description="Calendar ID of the user calendar.",
        ),
        Property(
            "busy",
            BooleanType,
            description="Busy/free status of the calendar event",
        ),
        Property(
            "body_html",
            StringType,
            description="Raw body content from Microsoft calendar events",
        ),
        Property(
            "attendees",
            ArrayType(ObjectType()),
            description="The attendees of the calendar event.",
        ),
        Property(
            "all_day",
            BooleanType,
            description="Whether the calendar event is an all-day event.",
        ),
    ).to_dict()
