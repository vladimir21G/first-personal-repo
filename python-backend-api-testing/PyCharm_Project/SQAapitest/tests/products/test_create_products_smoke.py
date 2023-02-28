import pytest

from SQAapitest.src.utilities.genericUtilites import generate_random_string
from SQAapitest.src.helpers.products_helper import ProductsHelper
from SQAapitest.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid26
def test_create_1_simple_product():

    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = '10.99'
    # make the call
    product_rs = ProductsHelper().call_create_product(payload)
    # verify the response is not empty
    assert product_rs, f"Create product API response is empty. Payload: {payload}"
    assert product_rs['slug'] == payload['name'], f"Create product api call response has"\
                                                  f"unexpected name. Expected: {payload['name']} "\
                                                                   f"Actual: {product_rs['slug']}"
    # verify the product exists in db
    db_rs = ProductsDAO().get_product_by_id_from_db(product_rs['id'])
    assert db_rs, f"The product does not exist in the Database."
    assert db_rs[0]['post_title'] == payload['name'], f"DB product with this ID has unexpected name."\
                                             f"Expected: {payload['name']} Actual: {db_rs['post_title']}"