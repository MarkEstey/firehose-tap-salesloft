from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    PropertiesList,
    Property,
    StringType,
)

class CrmTeamMembersWithRolesStream(SalesloftStream):
    '''CRM Account Team Members With Roles, referenced from https://developers.salesloft.com/docs/api/crm-team-members-with-roles-index'''

    name = 'crm_team_members_with_roles'
    path = '/v2/crm_team_members_with_roles'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('user_crm_id', StringType, description='CRM ID of the associated user', examples=['12345abcde']),
        Property('team_member_role', StringType, description='Role of the CRM Account Team Member', examples=['Sales Manager']),
        Property('account_email', StringType, description='Email address of the associated account', examples=['john.doe@example.com']),
        Property('account_name', StringType, description='Name of the associated account', examples=['John Doe']),
    ).to_dict()
