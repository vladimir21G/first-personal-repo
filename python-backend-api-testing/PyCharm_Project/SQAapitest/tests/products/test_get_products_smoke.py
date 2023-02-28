import pytest
import logging as logger
from SQAapitest.src.utilities.requestsUtility import RequestsUtility
from SQAapitest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
    rs_helper = RequestsUtility()
    list_of_all_products = rs_helper.get('products')
    assert list_of_all_products, f"Get all products end point return nothing."

@pytest.mark.tcid25
def test_get_product_by_id():
    # get product from db
    logger.info('Get product by id verify response')
    dao_helper = ProductsDAO().get_random_product_from_db()
    db_product_id = dao_helper[0]['ID']
    # make the call
    rs_helper = RequestsUtility()
    rs_api = rs_helper.get(f'products/{db_product_id}')
    # verify the response
    assert dao_helper[0]['post_name'] == rs_api['slug'], "DB product name and API product name are not equal!"\
    f"Expected result: {dao_helper[0]['post_name']}, Actual result: {rs_api['slug']}"
