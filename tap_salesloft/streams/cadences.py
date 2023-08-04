from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    DateType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class CadencesStream(SalesloftStream):
    """Cadences Stream, referenced from https://developers.salesloft.com/docs/api/cadences-index"""

    name = "cadences"
    path = "/v2/cadences"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of cadence",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the cadence was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the cadence was last updated",
        ),
        Property(
            "archived_at",
            DateTimeType,
            description="Datetime of when the cadence was archived, if archived",
        ),
        Property(
            "latest_active_date",
            DateType,
            description="Date of when the cadence was last used",
        ),
        Property(
            "team_cadence",
            BooleanType,
            description="Whether this cadence is a team cadence. "
            "A team cadence is created by an admin and can be run by all users",
        ),
        Property(
            "shared",
            BooleanType,
            description="Whether this cadence is visible to team members (shared)",
        ),
        Property(
            "remove_bounces_enabled",
            BooleanType,
            description="Whether this cadence is configured to automatically remove people who have bounced",
        ),
        Property(
            "remove_replies_enabled",
            BooleanType,
            description="Whether this cadence is configured to automatically remove people who have replied",
        ),
        Property(
            "opt_out_link_included",
            BooleanType,
            description="Whether this cadence is configured to include an opt-out link by default",
        ),
        Property(
            "draft",
            BooleanType,
            description="Whether this cadence is in draft mode",
        ),
        Property(
            "override_contact_restrictions",
            BooleanType,
            description="Whether this cadence is an Operational Cadence. "
            "An operational cadence is only created by an admin and accounts with the correct permission",
        ),
        Property(
            "cadence_framework_id",
            IntegerType,
            description="ID of the cadence framework used to create steps for the cadence",
        ),
        Property(
            "cadence_function",
            StringType,
            description="The use case of the cadence. Possible values are: "
            "outbound: Denotes an outbound cadence, typically for sales purposes; "
            "inbound: Denotes an inbound sales cadence; "
            "event: Denotes a cadence used for an upcoming event; "
            "other: Denotes a cadence outside of the standard process",
        ),
        Property(
            "name",
            StringType,
            description="Cadence name",
        ),
        Property(
            "external_identifier",
            StringType,
            description="Cadence External ID",
        ),
        Property(
            "tags",
            ArrayType(StringType),
            description="All tags applied to this cadence",
        ),
        # Documentation does not list this property
        Property(
            "current_state",
            StringType,
            description="[Undocumented]",
        ),
        Property(
            "creator",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that created this cadence",
        ),
        Property(
            "owner",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that is marked as the owner of this cadence",
        ),
        Property(
            "bounced_stage",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Stage set when person on cadence bounces",
        ),
        Property(
            "replied_stage",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Stage set when person on cadence replies",
        ),
        Property(
            "added_stage",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Stage set when person is added to cadence",
        ),
        Property(
            "finished_stage",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Stage set when person is finished with cadence",
        ),
        Property(
            "cadence_priority",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Priority of the cadence",
        ),
        Property(
            "groups",
            ArrayType(
                ObjectType(
                    Property("id", IntegerType),
                    Property("_href", StringType),
                )
            ),
            description="Groups to which this cadence is assigned, if any",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "cadence_people",
                    IntegerType,
                    description="The number of people that have ever been added to the cadence",
                ),
                Property(
                    "people_acted_on_count",
                    IntegerType,
                    description="The number of people that have been skipped, scheduled, or advanced in a cadence",
                ),
                Property(
                    "target_daily_people",
                    IntegerType,
                    description="The user defined target for number of people to add to the cadence each day",
                ),
                Property(
                    "opportunities_created",
                    IntegerType,
                    description="The number of opportunities created and attributed to the cadence",
                ),
                Property(
                    "meetings_booked",
                    IntegerType,
                    description="The number of meetings booked and attributed to the cadence",
                ),
            ),
        ),
    ).to_dict()
