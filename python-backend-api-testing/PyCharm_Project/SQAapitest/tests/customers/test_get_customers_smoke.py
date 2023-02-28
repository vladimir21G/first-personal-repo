

import pytest
import logging as logger
from SQAapitest.src.helpers.customers_helper import CustomerHelper


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    logger.info("Get list of all customers")

    #make the call
    cust_obj = CustomerHelper()
    cust_response = cust_obj.get_customers()

    assert cust_response, f"Response of all customers is empty"