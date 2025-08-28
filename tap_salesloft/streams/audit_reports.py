from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    BooleanType,
    DateType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

class AuditReportsStream(SalesloftStream):
    '''Audit Reports Stream, referenced from https://developers.salesloft.com/docs/api/audit-reports-index'''

    name = 'audit_reports'
    path = '/v2/audit_reports'
    primary_keys = ['id']

    schema = PropertiesList(
        Property('user_guid', StringType, description='Uuid of the user who requested report'),
        Property('until', DateType, description='End time for Date range'),
        Property('status', StringType, description='The staus of the report'),
        Property('started_on', DateType, description='The date the report request was started'),
        Property('since', DateType, description='Start time for Date range'),
        Property('requestor_name', StringType, description='Name of user who requested report'),
        Property('requestor_email', StringType, description='Email of who requested report'),
        Property('requested_on', DateType, description='Requested on date', examples=['2025-07-16']),
        Property('record_type', StringType, description='The type of the record requested. E.G. ''Account'''),
        Property('record_ids', IntegerType, description='Salesloft object ids for record type'),
        Property('name', StringType, description='The name of the repor'),
        Property('id', IntegerType, required=True, description='Primary key ID'),
        Property('error', StringType, description='Any error message that was returned'),
        Property('email_notification', BooleanType, description='Whether or not an email notication will be sent'),
        Property('download_url', StringType, description='The download url from aws'),
        Property('data_source', StringType, description='The primary source of the data. E.G. ''Database'''),
        Property('completed_on', DateType, description='The date the report request was completed'),
        Property('audited_user_guids', StringType, description='the user that made the audited action'),
        Property('actions', StringType, description='the action that was audited'),
    ).to_dict()
