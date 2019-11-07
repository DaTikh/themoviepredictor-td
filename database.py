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

    def _find(self, table, id):
        self.cursor.execute(self.find_query(table, id))
        results = self.cursor.fetchall()
        self._dcnx()
        return results

    def _list(self, table):
        self.cursor.execute(self.find_all_query(table))
        results = self.cursor.fetchall()
        self._dcnx()
        return results

    def _insert(self, table, object):
        print(object.release_date)
        self.cursor.execute(self.query_insert(table, object))
        self.cnx.commit()
        return self.cursor.lastrowid

    def _insert_person(self, table, person):
        self.cursor.execute(f"INSERT INTO `{table}` (`firstname`, `lastname`) VALUES ('{person.firstname}', '{person.lastname}')")
        self.cnx.commit()
        return self.cursor.lastrowid
    
    def find_query(self, table, id):
        return f"SELECT * FROM {table} WHERE `id` = {id}"

    def find_all_query(self, table):
        return f"SELECT * FROM {table}"
    
    def query_insert(self, table, object):
        if table == 'movies':
            return f"INSERT INTO `{table}` (`title`, `original_title`, `rating`, `duration`, `release_date`) VALUES ('{object.title}', '{object.original_title}', '{object.rating}', {object.duration}, '{object.release_date}')"
        else:
            return f"INSERT INTO `{table}` (`firstname`, `lastname`) VALUES ('{object.firstname}', '{object.lastname}')"

if __name__ == '__main__':
    Db()