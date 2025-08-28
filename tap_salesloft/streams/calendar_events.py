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
    '''Calendar Events Stream, referenced from https://developers.salesloft.com/docs/api/calendar-events-index'''

    name = 'calendar_events'
    path = '/v2/calendar/events'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('user_guid', StringType, description='User GUID of the user calendar.', examples=['9ccb7701-52e7-4d3e-91b0-b142a2fef2ec']),
        Property('updated_at', DateTimeType, description='Last modification time of the calendar event.', examples=['2025-08-22T14:26:35.122863Z']),
        Property('title', StringType, description='Title of the calendar event', examples=['Calendar event title']),
        Property('tenant_id', IntegerType, description='Tenant ID of the user calendar', examples=[1]),
        Property('status', StringType, description='The status of the calendar event. It can be empty for non-google events.', examples=['confirmed']),
        Property('start_time', DateTimeType, description='The (inclusive) start time of the calendar event.', examples=['2025-08-22T14:26:35.122430Z']),
        Property('series_master_event_id', StringType, description='INTERNAL: The ID of the recurring event series master event. This field is omitted for single events or instances of recurring events.', examples=['ID']),
        Property('recurring_interval', StringType, description='Specifies how often a recurring event repeats (Daily, Weekly, Monthly, Yearly). This field is omitted for single events or instances of recurring events.', examples=['Daily']),
        Property('recurring', BooleanType, description='Whether the calendar event is a recurring event.', examples=[False]),
        Property('recurrence', ArrayType(StringType), description='List of RRULE for a recurring event, as specified in RFC5545. This field is omitted for single events or instances of recurring events.', examples=['["RRULE:FREQ=DAILY;INTERVAL=1"]']),
        Property('provider', StringType, description='The provider of the calendar event.', examples=['google']),
        Property('organizer', StringType, description='The organizer email of the calendar event.', examples=['organizer@example.com']),
        Property('location', StringType, description='Location of the calendar event', examples=['Event location']),
        Property('last_occurrence_at', DateTimeType, description='The timestamp of the last occurrence in a series of recurring events.', examples=['2025-08-22T14:26:35.123011Z']),
        Property('id', StringType, required=True, description='The calendar event original ID from calendar provider', examples=['AAMkADQ0NjE4YmY5LTc3ZDYtNDc5NC1-UlgAAAAAAENAAB3eGoN5TIDTp8dXXDpxUlgAACQlfLuAAA=']),
        Property('i_cal_uid', StringType, description='Calendar event unique identifier (iCalUID)', examples=['1p1oilmc4mt3m6ah6rmf6ik8mm@google.com']),
        Property('html_link', StringType, description='An absolute link to this calendar event in the Google Calendar Web UI.', examples=['https://www.google.com/calendar/event?eid=Y2N']),
        Property('extended_properties', ObjectType(additional_properties=True), description='Extended properties of the calendar event.', examples=['{}']),
        Property('end_time', DateTimeType, description='The (exclusive) end time of the calendar event.', examples=['2025-08-22T14:26:35.122544Z']),
        Property('description', StringType, description='Description of the calendar event', examples=['Calendar event description']),
        Property('creator', StringType, description='The creator email of the calendar event.', examples=['creator@example.com']),
        Property('created_at', DateTimeType, description='Creation time of the calendar event.', examples=['2025-08-22T14:26:35.122807Z']),
        Property('conference_data', ObjectType(additional_properties=True), description='The conference-related information, such as details of a Google Meet conference.', examples=['{}']),
        Property('canceled_at', DateTimeType, description='The canceled date of the calendar event.', examples=['2025-08-22T14:26:35.122942Z']),
        Property('calendar_id', StringType, description='Calendar ID of the user calendar.', examples=['test@example.com']),
        Property('busy', BooleanType, description='Busy/free status of the calendar event', examples=[False]),
        Property('body_html', StringType, description='Raw body content from Microsoft calendar events', examples=['some html text']),
        Property('attendees', ArrayType(ObjectType(additional_properties=True)), description='The attendees of the calendar event.'),
        Property('all_day', BooleanType, description='Whether the calendar event is an all-day event.', examples=[False]),
    ).to_dict()
