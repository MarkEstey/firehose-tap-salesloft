import re
import requests
import time

from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers._typing import TypeConformanceLevel
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator, JSONPathPaginator
from singer_sdk.streams import RESTStream

second_match = re.compile('[0-9]{2}:[0-9]{2}:([0-9]{2})')

class SalesloftReplicationKeyPaginator(BaseAPIPaginator):
    def __init__(self, replication_key):
        super().__init__(start_value=None)
        self.replication_key = replication_key

    def has_more(self, response):
        next_page = extract_jsonpath('$.metadata.paging.next_page', response.json())
        return next(next_page, None) is not None

    def get_next(self, response):
        updated_ats = extract_jsonpath(f'$.data[*].{self.replication_key}', response.json())
        return next(iter(sorted(updated_ats, reverse=True)), None)

class SalesloftStream(RESTStream):
    records_jsonpath = '$.data[*]'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.TYPE_CONFORMANCE_LEVEL = {
            'none': TypeConformanceLevel.NONE,
            'root_only': TypeConformanceLevel.ROOT_ONLY,
            'recursive': TypeConformanceLevel.RECURSIVE,
        }.get(self.config['stream_type_conformance'])

    @property
    def url_base(self):
        return self.config.get('api_base_url')

    @property
    def authenticator(self):
        return BearerTokenAuthenticator(self, self.config.get('api_key'))

    def get_new_paginator(self):
        if self.replication_key:
            return SalesloftReplicationKeyPaginator(self.replication_key)
        else:
            return JSONPathPaginator('$.metadata.paging.next_page')

    def get_url_params(self, context, next_page_token):
        params = {'per_page': self.config.get('page_size')}

        if self.replication_key:
            params['sort_direction'] = 'asc'
            params['sort_by'] = self.replication_key
            if next_page_token is not None:
                params[f'{self.replication_key}[gt]'] = next_page_token
            else:
                params[f'{self.replication_key}[gt]'] = self.get_starting_timestamp(context).isoformat()

        elif next_page_token is not None:
            params['page'] = next_page_token

        return params

    def parse_response(self, response: requests.Response):
        rate_seconds_remaining = 61 - int(second_match.findall(response.headers.get('Date', '00:00:61'))[0])
        if rate_seconds_remaining == 61:
            rate_seconds_remaining = 1

        rate_last_request_cost = int(response.headers.get('x-ratelimit-endpoint-cost', 0))

        rate_points_remaining = int(response.headers.get('x-ratelimit-remaining-minute', 0))

        # Calculate delay according to current usage versus target rate
        if rate_points_remaining > rate_last_request_cost:
            delay = min(
                rate_seconds_remaining,
                rate_seconds_remaining
                * rate_last_request_cost
                * 100
                / rate_points_remaining
                / self.config.get('rate_target_pct'),
            )
        else:
            delay = rate_seconds_remaining

        delay -= response.elapsed.total_seconds()

        if delay > 0:
            time.sleep(delay)

        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
