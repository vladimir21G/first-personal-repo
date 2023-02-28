from SQAapitest.src.utilities.dbUtility import DBUtility
import random


class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        """"
        Args:

        Returns:
        """
        sql = f"SELECT * FROM baharmustafa_com_vladi.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_existing_customer_dao(self, qty=1):
        sql = f"SELECT * FROM baharmustafa_com_vladi.wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))
