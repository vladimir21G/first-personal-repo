
import pytest
from datetime import datetime, timedelta
from SQAapitest.src.helpers.products_helper import ProductsHelper
from SQAapitest.src.dao.products_dao import ProductsDAO

@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):

        # create data
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()
        payload = dict()
        payload['after'] = after_created_date
        # make the call
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, f"Empty response for 'list products with filter'"

        # get data from db
        db_rs = ProductsDAO().get_product_list_filtered(payload['after'])
        assert db_rs, f"DB response is empty for 'list products with filter'"

        # verify the response
        assert len(rs_api) == len(db_rs), f"Length of API list and DB list is not equal!!!"\
                        f"API Response list length: {len(rs_api)}"\
                        f"DB Response list length: {len(db_rs)}"

        # verify the ids in the list
        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_rs]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, f"List products with filter. Product ids in response mismatch in db."

