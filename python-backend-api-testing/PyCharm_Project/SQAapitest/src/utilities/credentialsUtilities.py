
import os

class CredentialUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')
        if not wc_key or not wc_secret:
            raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be in env variable")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():
        db_user = "remote_office"
        db_password = "vladievofisa123"

        # db_user = 'remote_home'
        # db_password = 'vladiisworkingfromhome'
        db_host = '116.202.22.87'
        if not db_user or not db_password:
            raise Exception("The DB credentials 'DB_USER' and 'DB_PASSWORD' must be in env variable")
        else:
            return {'db_user': db_user, 'db_password': db_password, 'db_host': db_host}