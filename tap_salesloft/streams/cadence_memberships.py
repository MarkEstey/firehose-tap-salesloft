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


class CadenceMembershipsStream(SalesloftStream):
    """Cadence Memberships Stream, referenced from https://developer.salesloft.com/docs/api/cadence-memberships-index"""

    name = "cadence_memberships"
    path = "/v2/cadence_memberships"
    primary_keys = ["id"]
    replication_key = "updated_at"

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="Cadence membership ID",
        ),
        Property(
            "added_at",
            DateTimeType,
            description="Datetime of when the person was last added to this cadence",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the person was first added to this cadence",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the record was last updated",
        ),
        Property(
            "person_deleted",
            BooleanType,
            description="Whether the associated person has since been deleted",
        ),
        Property(
            "currently_on_cadence",
            BooleanType,
            description="Whether the person is currently on the cadence",
        ),
        Property(
            "current_state",
            StringType,
            description="The current state of the person on the cadence. Possible values are: "
            "processing: The person is being processed on a cadence. Cadence-related changes cannot be made at this time; "
            "staged: The person is waiting for the first step in the cadence to occur; "
            "active: The cadence has begun processing this person and is still in the process, but idle; "
            "scheduled: The cadence has begun processing this person and is still in the process, with an activity scheduled to occur; "
            "completed: The cadence has been completed for this person; "
            "removed: The person was manually or automatically removed from the cadence; "
            "removed_no_action: The person was removed from the cadence before any action occurred; "
            "reassigned: The person's cadence execution was transferred to a different user, ending this user's interaction; "
            "archived: The cadence this person belonged to has been archived and all actions and people were archived with it",
        ),
        Property(
            "cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The cadence that the person is on",
        ),
        Property(
            "person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The person that is on the cadence",
        ),
        Property(
            "user",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="The user that is acting on the person in the cadence",
        ),
        Property(
            "latest_action",
            ObjectType(
                Property("id", IntegerType),
            ),
            description="The most recent action associated with the record",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "views",
                    IntegerType,
                    description="The number of times emails sent from the cadence to the person were opened",
                ),
                Property(
                    "clicks",
                    IntegerType,
                    description="The number of times emails sent from the cadence to the person were clicked",
                ),
                Property(
                    "replies",
                    IntegerType,
                    description="The number of times emails sent from the cadence to the person were replied to",
                ),
                Property(
                    "calls",
                    IntegerType,
                    description="The number of times a call was logged from the cadence to the person",
                ),
                Property(
                    "sent_emails",
                    IntegerType,
                    description="The number of times emails were sent from the cadence to the person",
                ),
                Property(
                    "bounces",
                    IntegerType,
                    description="The number of times emails sent from the cadence to the person bounced",
                ),
            ),
        ),
    ).to_dict()
