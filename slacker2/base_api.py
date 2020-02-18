import json
import time
import requests

from slacker2.utilities import get_api_url
from slacker2.constants import DEFAULT_TIMEOUT, DEFAULT_RETRIES, DEFAULT_WAIT


class BaseAPI(object):
    def __init__(self, token=None, timeout=DEFAULT_TIMEOUT, proxies=None,
                 session=None, rate_limit_retries=DEFAULT_RETRIES):
        self.token = token
        self.timeout = timeout
        self.proxies = proxies
        self.session = session
        self.rate_limit_retries = rate_limit_retries

    def _request(self, request_method, method, **kwargs):
        if self.token:
            kwargs.setdefault('params', {})['token'] = self.token

        url = get_api_url(method)

        # while we have rate limit retries left, fetch the resource and back
        # off as Slack's HTTP response suggests
        for retry_num in range(self.rate_limit_retries):
            response = request_method(
                url, timeout=self.timeout, proxies=self.proxies, **kwargs
            )

            if response.status_code == requests.codes.ok:
                break

            # handle HTTP 429 as documented at
            # https://api.slack.com/docs/rate-limits
            if response.status_code == requests.codes.too_many:
                time.sleep(int(
                    response.headers.get('retry-after', DEFAULT_WAIT)
                ))
                continue

            response.raise_for_status()
        else:
            # with no retries left, make one final attempt to fetch the
            # resource, but do not handle too_many status differently
            response = request_method(
                url, timeout=self.timeout, proxies=self.proxies, **kwargs
            )
            response.raise_for_status()

        response = Response(response.text)
        if not response.successful:
            raise Error(response.error)

        return response

    def _session_get(self, url, params=None, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.session.request(
            method='get', url=url, params=params, **kwargs
        )

    def _session_post(self, url, data=None, **kwargs):
        return self.session.request(
            method='post', url=url, data=data, **kwargs
        )

    def get(self, api, **kwargs):
        return self._request(
            self._session_get if self.session else requests.get,
            api, **kwargs
        )

    def post(self, api, **kwargs):
        return self._request(
            self._session_post if self.session else requests.post,
            api, **kwargs
        )


class Response(object):
    def __init__(self, body):
        self.raw = body
        self.body = json.loads(body)
        self.successful = self.body['ok']
        self.error = self.body.get('error')

    def __str__(self):
        return json.dumps(self.body)


class Error(Exception):
    pass