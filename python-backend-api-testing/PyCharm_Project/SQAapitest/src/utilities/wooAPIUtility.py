import os
from woocommerce import  API
from SQAapitest.src.configs.hosts_config import API_HOSTS
from SQAapitest.src.utilities.credentialsUtilities import CredentialUtility


class WooAPIUtility(object):

    def __init__(self):
        wc_creds = CredentialUtility.get_wc_api_keys()

        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

        self.wcapi = API(
            url = self.base_url,
            consumer_key=os.environ.get('WC_KEY'),
            consumer_secret=os.environ.get('WC_SECRET'),
            version="wc/v3"
        )