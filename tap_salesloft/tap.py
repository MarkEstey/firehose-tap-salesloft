from singer_sdk import Tap
from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

from tap_salesloft import streams

class TapSalesloft(Tap):
    name = 'tap-salesloft'

    config_jsonschema = PropertiesList(
        Property('api_base_url', StringType, default='https://api.salesloft.com', description='The base url for the Salesloft API service'),
        Property('api_key', StringType, required=True, secret=True, description='The key to authenticate with the API service'),
        Property('page_size', IntegerType, default=100, description='The number of results to request per page. Must be in the range 1-100.'),
        Property('rate_target_pct', IntegerType, default=80, description='The percentage of the rate limit to consume. Must be in the range 1-100.'),
        Property('start_date', DateTimeType, default='2011-09-01T00:00:00+00:00', description='The earliest record date to sync'),
        Property('stream_type_conformance', StringType, default='root_only', description='The level of type conformance to apply to streams (see: https://sdk.meltano.com/en/latest/classes/singer_sdk.Stream.html#singer_sdk.Stream.TYPE_CONFORMANCE_LEVEL). Defaults to ''root_only''. Must be one of: ''none'', ''root_only'', ''recursive''', allowed_values=['none', 'root_only', 'recursive']),
        Property('stream_maps', ObjectType(), description='Inline stream maps (see: https://sdk.meltano.com/en/latest/stream_maps.html)'),
        Property('stream_maps_config', ObjectType(), description='Inline stream maps config (see: https://sdk.meltano.com/en/latest/stream_maps.html)'),
        Property('user_agent', StringType, default='tap-salesloft', description='The user-agent string provided on outgoing requests'),
    ).to_dict()

    def discover_streams(self):
        return [
            streams.AccountStagesStream(self),
            streams.AccountTeamMemberRolesStream(self),
            streams.AccountTiersStream(self),
            streams.AccountTypesStream(self),
            streams.AccountsStream(self),
            streams.ActionsStream(self),
            streams.ActivityHistoriesStream(self),
            streams.AuditReportsStream(self),
            streams.CadenceMembershipsStream(self),
            streams.CadencesStream(self),
            streams.CalendarEventsStream(self),
            streams.CallDataRecordsStream(self),
            streams.CallDispositionsStream(self),
            streams.CallInstructionsStream(self),
            streams.CallSentimentsStream(self),
            streams.CallsStream(self),
            streams.CrmAccountTeamMembersStream(self),
            streams.CrmActivitiesStream(self),
            streams.CrmActivityFieldsStream(self),
            streams.CrmTeamMembersWithRolesStream(self),
            streams.CrmUsersStream(self),
            streams.CustomFieldsStream(self),
            streams.CustomRolesStream(self),
            streams.EmailTemplateAttachmentsStream(self),
            streams.EmailTemplatesStream(self),
            streams.EmailsStream(self),
            streams.ExternalConfigurationsStream(self),
            streams.ExternalMappingsStream(self),
            streams.GroupsStream(self),
            streams.ImportsStream(self),
            streams.MeetingsStream(self),
            streams.NotesStream(self),
            streams.OpportunitiesStream(self),
            streams.OpportunityPeopleStream(self),
            streams.OpportunityStagesStream(self),
            streams.PendingEmailsStream(self),
            streams.PeopleStream(self),
            streams.PersonStagesStream(self),
            streams.PhoneNumberAssignmentsStream(self),
            streams.RegistrationsPlaysStream(self),
            streams.SavedListViewsStream(self),
            streams.SignalsRegistrationsStream(self),
            streams.StepsStream(self),
            streams.SuccessesStream(self),
            streams.TagsStream(self),
            streams.TasksStream(self),
            streams.TeamTemplateAttachmentsStream(self),
            streams.TeamTemplatesStream(self),
            streams.TranscriptionsStream(self),
            streams.UsersStream(self),
            streams.WebhookSubscriptionsStream(self),
        ]

if __name__ == '__main__':
    TapSalesloft.cli()
