"""REST client handling, including SalesloftStream base class."""

from __future__ import annotations

from typing import Any, Callable, Iterable

import logging
import re
import requests
import time

from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]
second_match = re.compile("[0-9]{2}:[0-9]{2}:([0-9]{2})")


class SalesloftStream(RESTStream):
    """Salesloft stream class."""

    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.metadata.paging.next_page"  # noqa: S105

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config.get("api_base_url")

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("api_key"),
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")

        return headers

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """

        params = {"per_page": self.config.get("page_size")}

        if next_page_token:
            params["page"] = next_page_token

        if self.replication_key:
            params["sort_direction"] = "asc"
            params["sort_by"] = self.replication_key
            params[f"{self.replication_key}[gt]"] = self.get_starting_timestamp(
                context
            ).isoformat()

        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """

        # API returns data about remaining rate limit
        rate_seconds_remaining = 61 - int(
            second_match.findall(response.headers.get("Date", "00:00:61"))[0]
        )
        if rate_seconds_remaining == 61:
            rate_seconds_remaining = 1

        rate_last_request_cost = int(
            response.headers.get("x-ratelimit-endpoint-cost", 0)
        )

        rate_points_remaining = int(
            response.headers.get("x-ratelimit-remaining-minute", 0)
        )

        # Calculate delay according to current usage versus target rate
        if rate_points_remaining > rate_last_request_cost:
            delay = min(
                rate_seconds_remaining,
                rate_seconds_remaining
                * rate_last_request_cost
                * 100
                / rate_points_remaining
                / self.config.get("rate_target_pct"),
            )
        else:
            delay = rate_seconds_remaining

        # Discount the time it took to get the response
        delay -= response.elapsed.total_seconds()

        if delay > 0:
            time.sleep(delay)

        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
