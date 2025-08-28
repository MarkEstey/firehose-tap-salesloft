from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class AccountTeamMemberRolesStream(SalesloftStream):
    '''Account Team Member Roles Stream, referenced from https://developers.salesloft.com/docs/api/account-team-member-roles-index'''

    name = 'account_team_member_roles'
    path = '/v2/account_team_member_roles'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, required=True, description='ID of CRM Account Team Member Role', examples=[1234]),
        Property('name', StringType, description='Name of CRM Account Team Member Role', examples=['Sales Manager']),
    ).to_dict()
