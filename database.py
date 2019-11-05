import mysql
import json
import csv

import os
from dotenv import load_dotenv
load_dotenv()

MYSQL_TOKEN = os.getenv('MYSQL_TOKEN')

class Db():

    def __init__(self, token=json.loads(MYSQL_TOKEN)):
        self.user = token['user']
        self.password = token['password']
        self.host = token['host']
        self.database = token['database']

        self.cnx = mysql.connector.connect(
                        user=self.user,
                        password=self.password,
                        host=self.host,
                        database=self.database
                        )
        self.cursor = self.cnx.cursor(dictionary=True)

    """  Si on enlève la connexion dans l'initialisation  """
    # def _cnx(self):
    #     self.cnx = mysql.connector.connect(
    #                     user=self.user,
    #                     password=self.password,
    #                     host=self.host,
    #                     database=self.database
    #                     )
    #     self.cursor = self.cnx.cursor(dictionary=True)

    def _dcnx(self):
        self.cursor.close()
        self.cnx.close()

    def _list(self, table):
        self.cursor.execute(self.find_all_query(table))
        results = self.cursor.fetchall()
        self._dcnx()
        return results

    def find_all_query(self, table):
        return f"SELECT * FROM {table}"


if __name__ == '__main__':
    Db()