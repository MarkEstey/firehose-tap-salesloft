from tap_salesloft.client import SalesloftStream

from singer_sdk.helpers._typing import TypeConformanceLevel

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


class AccountsStream(SalesloftStream):
    """Accounts Stream, referenced from https://developers.salesloft.com/docs/api/accounts-index"""

    name = "accounts"
    path = "/v2/accounts"
    primary_keys = ["id"]
    replication_key = "updated_at"

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="ID of Account",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the Account was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the Account was last updated",
        ),
        Property(
            "archived_at",
            DateTimeType,
            description="Datetime of when the Account was archived, if archived",
        ),
        Property(
            "name",
            StringType,
            description="Account Full Name",
        ),
        Property(
            "domain",
            StringType,
            description="Website domain, not a fully qualified URI",
        ),
        Property(
            "conversational_name",
            StringType,
            description="Conversational name of the Account",
        ),
        Property(
            "description",
            StringType,
            description="Description",
        ),
        Property(
            "phone",
            StringType,
            description="Phone number without formatting",
        ),
        Property(
            "website",
            StringType,
            description="Website",
        ),
        Property(
            "linkedin_url",
            StringType,
            description="Full LinkedIn url",
        ),
        Property(
            "twitter_handle",
            StringType,
            description="Twitter handle, with @",
        ),
        Property(
            "street",
            StringType,
            description="Street name and number",
        ),
        Property(
            "city",
            StringType,
            description="City",
        ),
        Property(
            "state",
            StringType,
            description="State",
        ),
        Property(
            "postal_code",
            StringType,
            description="Postal code",
        ),
        Property(
            "country",
            StringType,
            description="Country",
        ),
        Property(
            "locale",
            StringType,
            description="Time locale",
        ),
        Property(
            "industry",
            StringType,
            description="Industry",
        ),
        Property(
            "company_type",
            StringType,
            description="Type of the Account's company",
        ),
        Property(
            "founded",
            StringType,
            description="Date or year of founding",
        ),
        Property(
            "revenue_range",
            StringType,
            description="Estimated revenue range",
        ),
        Property(
            "size",
            StringType,
            description="Estimated number of people in employment",
        ),
        Property(
            "crm_id",
            StringType,
            description="CRM ID",
        ),
        Property(
            "crm_url",
            StringType,
            description="CRM url",
        ),
        Property(
            "crm_object_type",
            StringType,
            description="CRM object type",
        ),
        Property(
            "owner_crm_id",
            StringType,
            description="Mapped owner field from the CRM",
        ),
        Property(
            "last_contacted_at",
            DateTimeType,
            description="Datetime this Account was last contacted",
        ),
        Property(
            "last_contacted_type",
            StringType,
            description="The type of the last touch to this Account. "
            "Can be call, email, other",
        ),
        Property(
            "do_not_contact",
            BooleanType,
            description="Whether this company has opted out of communications. "
            "Do not contact someone at this company when this is set to true",
        ),
        Property(
            "custom_fields",
            ObjectType(),
            description="Custom fields are defined by the user's team. "
            "Only fields with values are presented in the API.",
        ),
        # Documentation states 'user_relationships' type is object, API returns object[]
        Property(
            "user_relationships",
            ArrayType(ObjectType()),
            description="Filters by accounts matching all given user relationship fields, _is_null "
            "or _unmapped can be passed to filter accounts with null or unmapped user relationship values",
        ),
        Property(
            "tags",
            ArrayType(StringType),
            description="All tags applied to this Account",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "people",
                    IntegerType,
                    description="Number of people in SalesLoft associated with this Account",
                ),
            ),
        ),
        Property(
            "owner",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that is marked as the owner of this Account",
        ),
        Property(
            "creator",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that created this Account",
        ),
        Property(
            "last_contacted_by",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that last contacted this Account",
        ),
        Property(
            "last_contacted_person",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Person who was last contacted at this Account",
        ),
        Property(
            "company_stage",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Company Stage that this Account has set. "
            "This is referred to as Account Stage in other parts of the API. "
            "When sorting by account_stage, the company stages order is used",
        ),
        Property(
            "account_tier",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Account Tier that this Account has set",
        ),
    ).to_dict()
