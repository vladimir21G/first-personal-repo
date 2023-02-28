from SQAapitest.src.configs.hosts_config import API_HOSTS
from SQAapitest.src.utilities.credentialsUtilities import CredentialUtility
import os
import json
import requests
import logging as logger
from requests_oauthlib import OAuth1


class RequestsUtility(object):

    def __init__(self):
        self.rs_json = ''
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        wc_key = CredentialUtility.get_wc_api_keys()['wc_key']
        wc_secret = CredentialUtility.get_wc_api_keys()['wc_secret']
        self.auth = OAuth1(wc_key, wc_secret)

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad status code."\
            f"Expected {self.expected_status_code}, Actual status code: {self.status_code},"\
            f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):

        if not headers:
            headers = {"Content-type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'POST API response {self.rs_json}')

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        return self.rs_json