
from SQAapitest.src.utilities.genericUtilites import generate_random_email_and_password
from SQAapitest.src.utilities.requestsUtility import RequestsUtility


class CustomerHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_customer_json = self.request_utility.post('customers', payload=payload)
        return create_customer_json


    def get_customers(self, email=None, password=None, **kwargs):

        get_customers_json = self.request_utility.get('customers')
        return get_customers_json





