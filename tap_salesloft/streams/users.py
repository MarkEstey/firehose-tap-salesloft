from tap_salesloft.client import SalesloftStream

from singer_sdk.helpers._typing import TypeConformanceLevel

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)


class UsersStream(SalesloftStream):
    """Users Stream, referenced from https://developers.salesloft.com/docs/api/users-index"""

    name = "users"
    path = "/v2/users"
    primary_keys = ["id"]

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="User ID",
        ),
        Property(
            "guid",
            StringType,
            description="Globally unique user ID. New endpoints will explicitly accept this over id",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the user was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            description="Datetime of when the user was last updated",
        ),
        Property(
            "name",
            StringType,
            description="Display name of user",
        ),
        Property(
            "first_name",
            StringType,
            description="First name of user",
        ),
        Property(
            "last_name",
            StringType,
            description="Last name of user",
        ),
        Property(
            "job_role",
            StringType,
            description="Job role of user",
        ),
        Property(
            "active",
            BooleanType,
            description="Whether an user is currently active in SalesLoft",
        ),
        Property(
            "time_zone",
            StringType,
            description="User Time Zone",
        ),
        Property(
            "locale_utc_offset",
            IntegerType,
            description="User's UTC Offset",
        ),
        Property(
            "slack_username",
            StringType,
            description="Slack username",
        ),
        Property(
            "twitter_handle",
            StringType,
            description="Twitter handle",
        ),
        Property(
            "email",
            StringType,
            description="Email address provided to accounts.salesloft.com",
        ),
        Property(
            "email_client_email_address",
            StringType,
            description="Email address associated with the email client of the user",
        ),
        Property(
            "sending_email_address",
            StringType,
            description="The email address that email of the user will be sent from, resolved "
            "in the following resolution order: from_user, email_client_email_address, email",
        ),
        Property(
            "from_address",
            StringType,
            description="The from address of this user",
        ),
        Property(
            "full_email_address",
            StringType,
            description="RFC 5322 compliant email address",
        ),
        Property(
            "bcc_email_address",
            StringType,
            description="Address that will be BBC'd on all emails from this user",
        ),
        Property(
            "work_country",
            StringType,
            description="Work Country",
        ),
        Property(
            "email_signature",
            StringType,
            description="Email signature",
        ),
        Property(
            "email_signature_type",
            StringType,
            description="Email signature type",
        ),
        Property(
            "email_signature_click_tracking_disabled",
            BooleanType,
            description="Whether this user has click tracking disabled in email signature",
        ),
        Property(
            "team_admin",
            BooleanType,
            description="Team Admin",
        ),
        Property(
            "local_dial_enabled",
            BooleanType,
            description="Whether this user has Local Dial enabled",
        ),
        Property(
            "click_to_call_enabled",
            BooleanType,
            description="Whether this user has click to call enabled",
        ),
        Property(
            "email_client_configured",
            BooleanType,
            description="Whether this user has a email client configured",
        ),
        Property(
            "crm_connected",
            BooleanType,
            description="Whether the user has a crm connected",
        ),
        Property(
            "external_feature_flags",
            ObjectType(),
            description="Feature flags that are for this user. "
            "New flags may appear or disappear at any time",
        ),
        Property(
            "phone_client",
            ObjectType(
                Property("id", IntegerType),
            ),
            description="Phone Client of user",
        ),
        Property(
            "phone_number_assignment",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Phone number assignment of user",
        ),
        Property(
            "group",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Group of user",
        ),
        Property(
            "team",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Team of user",
        ),
        Property(
            "role",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Role of user",
        ),
    ).to_dict()
