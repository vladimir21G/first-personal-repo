from SQAapitest.src.utilities.dbUtility import DBUtility
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        sql = f"SELECT * FROM baharmustafa_com_vladi.wp_posts WHERE post_type = \"product\";"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, qty)

    def get_product_by_id_from_db(self, id):
        sql = f"SELECT * FROM baharmustafa_com_vladi.wp_posts WHERE id = \"{id}\"";
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_product_list_filtered(self, payload=None):
        sql = f"SELECT * FROM baharmustafa_com_vladi.wp_posts WHERE post_type=\"product\" and post_date>\"{payload}\";"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql
