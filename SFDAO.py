__author__ = 'Wahid'

import psycopg2
import sys
import itertools

class SFDAOClass:

    def __init__(self, constr):
        self.connection_string=constr
        self.db_connection = psycopg2.connect(constr)

    def get_salesforce_data(self):
        result = []
        query = "Select * from SalesForceData"

        cursor = self.db_connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
       #result = list(itertools.chain.from_iterable(rows))
        cursor.close()

        for row in rows:
            r = {
            "sfid": row[0],
            "name": row[1]
            }
            result.append(r)

        return  result
