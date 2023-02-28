import pymysql
from SQAapitest.src.utilities.credentialsUtilities import CredentialUtility


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialUtility()
        self.creds = creds_helper.get_db_credentials()

    def create_connection(self):
        connection = pymysql.connect(host=self.creds['db_host'], user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=3306)
        return connection

    def execute_select(self, sql: object) -> object:

        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass
