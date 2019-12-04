# -*- coding: utf-8 -*-

import mysql.connector
import socket
import time
import os
import json

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('MYSQL_TOKEN')
MYSQL_TOKEN = json.loads(token)

class Db(object):

    def __init__(self, token=MYSQL_TOKEN):
        self.user = token['user']
        self.password = token['password']
        self.host = token['host']
        self.database = token['database']

        self.is_ready = self.connectToDatabase()

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


    def isOpen(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False

    def connectToDatabase(self):
        host = MYSQL_TOKEN['host'] or 'localhost'
        while self.isOpen(host, 3306) == False:
            print("En attente de la BDD...")
            time.sleep(5)


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
        request, data = self.insert_query(table, object)
        self.cursor = self.cnx.cursor(prepared=True)
        self.cursor.execute(request, data)
        self.cnx.commit()
        return self.cursor.lastrowid


    def find_query(self, table, id):
        return f"SELECT * FROM {table} WHERE `id` = {id}"


    def find_all_query(self, table):
        return f"SELECT * FROM {table}"


    def insert_query(self, table, object):
        if table == 'movies':
            return (f"INSERT INTO `{table}` (`title`, `duration`, `imdb_id`, `original_title`, `release_date`, `rating`, `synopsis`, `production_budget`, `marketing_budget`, `actors`, `directors`, `productors`, `is_3d`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                    (object.title, object.duration, object.imdb_id, object.original_title, object.release_date, object.rating, object.synopsis, object.production_budget, object.marketing_budget, object.actors, object.directors, object.productors, object.is_3d))
        elif table == "people":
            return (f"INSERT INTO `{table}` (`imdb_id`, `firstname`, `lastname`) VALUES (%s, %s, %s)", (object.imdb_id, object.firstname, object.lastname))


if __name__ == '__main__':
    Db()