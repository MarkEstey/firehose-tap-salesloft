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


class PeopleStream(SalesloftStream):
    """People Stream, referenced from https://developers.salesloft.com/docs/api/people-index"""

    name = "people"
    path = "/v2/people"
    primary_keys = ["id"]
    replication_key = "updated_at"

    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    schema = PropertiesList(
        Property(
            "id",
            IntegerType,
            required=True,
            description="Person ID",
        ),
        Property(
            "created_at",
            DateTimeType,
            description="Datetime of when the person was created",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of when the person was last updated",
        ),
        Property(
            "last_contacted_at",
            DateTimeType,
            description="Last datetime this person was contacted",
        ),
        Property(
            "last_replied_at",
            DateTimeType,
            description="Last datetime this person replied to an email",
        ),
        Property(
            "first_name",
            StringType,
            description="First name",
        ),
        Property(
            "last_name",
            StringType,
            description="Last name",
        ),
        Property(
            "display_name",
            StringType,
            description="Either the full name or the email address. "
            "Use this when showing a person's name",
        ),
        Property(
            "email_address",
            StringType,
            description="Email address",
        ),
        Property(
            "full_email_address",
            StringType,
            description="Full email address with name",
        ),
        Property(
            "secondary_email_address",
            StringType,
            description="Alternate email address",
        ),
        Property(
            "personal_email_address",
            StringType,
            description="Personal email address",
        ),
        Property(
            "phone",
            StringType,
            description="Phone without formatting",
        ),
        Property(
            "phone_extension",
            StringType,
            description="Phone extension without formatting",
        ),
        Property(
            "home_phone",
            StringType,
            description="Home phone without formatting",
        ),
        Property(
            "mobile_phone",
            StringType,
            description="Mobile phone without formatting",
        ),
        Property(
            "linkedin_url",
            StringType,
            description="Linkedin URL",
        ),
        Property(
            "title",
            StringType,
            description="Job title",
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
            "country",
            StringType,
            description="Country",
        ),
        Property(
            "work_city",
            StringType,
            description="Work location - city",
        ),
        Property(
            "work_state",
            StringType,
            description="Work location - state",
        ),
        Property(
            "work_country",
            StringType,
            description="Work location - country",
        ),
        Property(
            "crm_url",
            StringType,
            description="CRM url",
        ),
        Property(
            "crm_id",
            StringType,
            description="CRM ID",
        ),
        Property(
            "crm_object_type",
            StringType,
            description="CRM object type",
        ),
        Property(
            "owner_crm_id",
            StringType,
            description="Mapped owner field from your CRM",
        ),
        Property(
            "person_company_name",
            StringType,
            description="Company name. This property is specific to this person, unrelated to the company object. "
            "Updating the company object associated with this person is recommended",
        ),
        Property(
            "person_company_website",
            StringType,
            description="Company website. This property is specific to this person, unrelated to the company object. "
            "Updating the company object associated with this person is recommended",
        ),
        Property(
            "person_company_industry",
            StringType,
            description="Company industry. This property is specific to this person, unrelated to the company object. "
            "Updating the company object associated with this person is recommended",
        ),
        Property(
            "do_not_contact",
            BooleanType,
            description="Whether or not this person has opted out of all communication. "
            "Setting this value to true prevents this person from being called, emailed, or added to a cadence in SalesLoft. "
            "If this person is currently in a cadence, they will be removed.",
        ),
        Property(
            "bouncing",
            BooleanType,
            description="Whether this person's current email address has bounced",
        ),
        Property(
            "locale",
            StringType,
            description="Time locale of the person",
        ),
        Property(
            "locale_utc_offset",
            IntegerType,
            description="The locale's timezone offset from UTC in minutes",
        ),
        Property(
            "eu_resident",
            BooleanType,
            description="Whether this person is marked as a European Union Resident or not",
        ),
        Property(
            "personal_website",
            StringType,
            description="The website of this person",
        ),
        Property(
            "twitter_handle",
            StringType,
            description="The twitter handle of this person",
        ),
        Property(
            "last_contacted_type",
            StringType,
            description="The type of the last touch to this person. Can be call, email, other",
        ),
        Property(
            "job_seniority",
            StringType,
            description="The Job Seniority of a Person, must be one of director, executive, "
            "individual_contributor, manager, vice_president, unknown",
        ),
        Property(
            "custom_fields",
            ObjectType(),
            description="Custom fields are defined by the user's team. "
            "Only fields with values are presented in the API.",
        ),
        Property(
            "tags",
            ArrayType(StringType),
            description="All tags applied to this person",
        ),
        Property(
            "contact_restrictions",
            ArrayType(StringType),
            description="Specific methods of communication to prevent for this person. "
            "This will prevent individual execution of these communication types as well as "
            "automatically skip cadence steps of this communication type for this person in SalesLoft. "
            "Values currently accepted: call, email, message",
        ),
        Property(
            "success_count",
            IntegerType,
            description="The person's success count. 1 if person has any active successes, 0 otherwise.",
        ),
        Property(
            "starred",
            BooleanType,
            description="Whether this person is starred by the current user",
        ),
        Property(
            "untouched",
            BooleanType,
            description="The person's untouched status",
        ),
        Property(
            "counts",
            ObjectType(
                Property(
                    "emails_sent",
                    IntegerType,
                    description="The number of emails sent to this person",
                ),
                Property(
                    "emails_viewed",
                    IntegerType,
                    description="The number of unique emails viewed by this person",
                ),
                Property(
                    "emails_clicked",
                    IntegerType,
                    description="The number of unique emails clicked by this person",
                ),
                Property(
                    "emails_replied_to",
                    IntegerType,
                    description="The number of unique emails replied to by this person",
                ),
                Property(
                    "emails_bounced",
                    IntegerType,
                    description="The number of unique emails sent to this person that bounced",
                ),
                Property(
                    "calls",
                    IntegerType,
                    description="The number of calls logged to this person",
                ),
            ),
        ),
        Property(
            "account",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Account that this person is associated to",
        ),
        Property(
            "owner",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that is marked as the owner of this person",
        ),
        Property(
            "last_contacted_by",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="User that last contacted this person",
        ),
        Property(
            "import",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Import that this person was a part of",
        ),
        Property(
            "person_stage",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Person stage that this person has set",
        ),
        Property(
            "most_recent_cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Cadence this person was most recently added to",
        ),
        Property(
            "last_completed_step_cadence",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Cadence of the last completed step this person",
        ),
        Property(
            "last_completed_step",
            ObjectType(
                Property("id", IntegerType),
                Property("_href", StringType),
            ),
            description="Last completed step of the cadence",
        ),
        Property(
            "cadences",
            ArrayType(
                ObjectType(
                    Property("id", IntegerType),
                    Property("_href", StringType),
                )
            ),
            description="The list of active cadences person is added to",
        ),
    ).to_dict()
