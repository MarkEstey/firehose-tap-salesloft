"""Salesloft tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_salesloft import streams
from tap_salesloft.client import SalesloftStream


class TapSalesloft(Tap):
    """Salesloft tap class."""

    name = "tap-salesloft"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_base_url",
            th.StringType,
            default="https://api.salesloft.com",
            description="The base url for the Salesloft API service",
        ),
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="The key to authenticate with the API service",
        ),
        th.Property(
            "page_size",
            th.IntegerType,
            default=100,
            description="The number of results to request per page. Must be in the range 1-100.",
        ),
        th.Property(
            "rate_target_pct",
            th.IntegerType,
            default=80,
            description="The percentage of the rate limit to consume. Must be in the range 1-100.",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            default="2011-09-01T00:00:00+00:00",
            description="The earliest record date to sync",
        ),
        th.Property(
            "stream_maps",
            th.ObjectType(),
            description="Inline stream maps (see: https://sdk.meltano.com/en/latest/stream_maps.html)",
        ),
        th.Property(
            "stream_maps_config",
            th.ObjectType(),
            description="Inline stream maps config (see: https://sdk.meltano.com/en/latest/stream_maps.html)",
        ),
        th.Property(
            "user_agent",
            th.StringType,
            default="tap-salesloft",
            description="The user-agent string provided on outgoing requests",
        ),
    ).to_dict()

    def discover_streams(self) -> list[SalesloftStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.AccountStagesStream(self),
            streams.AccountTiersStream(self),
            streams.AccountsStream(self),
            streams.ActionsStream(self),
            streams.ActivityHistoriesStream(self),
            streams.CadenceMembershipsStream(self),
            streams.CadencesStream(self),
            streams.CalendarEventsStream(self),
            streams.CallDataRecordsStream(self),
            streams.CallDispositionsStream(self),
            streams.CallInstructionsStream(self),
            streams.CallSentimentsStream(self),
            streams.CallsStream(self),
            streams.CrmActivitiesStream(self),
            streams.CrmActivityFieldsStream(self),
            streams.CrmUsersStream(self),
            streams.CustomFieldsStream(self),
            streams.CustomRolesStream(self),
            streams.EmailTemplateAttachmentsStream(self),
            streams.EmailTemplatesStream(self),
            streams.EmailsStream(self),
            streams.GroupsStream(self),
            streams.ImportsStream(self),
            streams.MeetingsStream(self),
            streams.NotesStream(self),
            streams.PendingEmailsStream(self),
            streams.PeopleStream(self),
            streams.PersonStagesStream(self),
            streams.PhoneNumberAssignmentsStream(self),
            streams.SavedListViewsStream(self),
            streams.StepsStream(self),
            streams.SuccessesStream(self),
            streams.TagsStream(self),
            streams.TasksStream(self),
            streams.TeamTemplateAttachmentsStream(self),
            streams.TeamTemplatesStream(self),
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    TapSalesloft.cli()
