import pytest
import logging as logger
from SQAapitest.src.utilities.genericUtilites import generate_random_email_and_password
from SQAapitest.src.helpers.customers_helper import CustomerHelper
from SQAapitest.src.dao.customers_dao import CustomersDAO
from SQAapitest.src.utilities.requestsUtility import RequestsUtility

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("Create customer with email and password only.")

    rand_info = generate_random_email_and_password()
    logger.info(rand_info)
    email = rand_info['email']
    password = rand_info['password']

    #create payload
    payload = {'email': email, 'password': password}

    #make a call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    #verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', f"Create customer api returned value for first_name, but should be empty"

    #verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api == id_in_db, f"Create customer database \"id\" not same as \"ID\" from API. Email: {cust_info['ID']}"

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():

    #get existing email from db
    cust_dao = CustomersDAO()
    existing_cust = cust_dao.get_existing_customer_dao()
    existing_email = existing_cust[0]['user_email']
    payload = dict()
    payload['email'] = existing_email
    payload['password'] = 'Password1'

    #make a call to create the customer with existing email
    req_helper = RequestsUtility()
    cust_api_info = req_helper.post(endpoint='customers',payload=payload, expected_status_code=400)
    logger.info(cust_api_info['message'])
    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with existing email " \
            f"error 'code' is incorrect. Expected: 'registration-error-email-exists', Actual: '{cust_api_info}'"



