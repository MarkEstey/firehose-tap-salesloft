from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class CrmAccountTeamMembersStream(SalesloftStream):
    '''CRM Account Team Members, referenced from https://developers.salesloft.com/docs/api/crm-account-team-members-index'''

    name = 'crm_account_team_members'
    path = '/v2/crm_account_team_members'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('id', IntegerType, description='ID of CRM Account Team Member', examples=[1234]),
        Property('crm_id', StringType, description='ID of CRM Account Team Member', examples=['1234']),
        Property('account_crm_id', StringType, description='ID of CRM Account', examples=['1234']),
        Property('user_crm_id', StringType, description='ID of CRM User', examples=['1234']),
        Property('team_member_role', StringType, description='Role of CRM Account Team Member', examples=['Sales Manager']),
        Property('account_access_level', StringType, description='Access level for Account', examples=['full']),
        Property('user_crm_name', StringType, description='Name of CRM User', examples=['John Doe']),
    ).to_dict()
