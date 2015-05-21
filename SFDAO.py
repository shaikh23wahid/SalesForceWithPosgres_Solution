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

    def get_groups_data(self):
        groupresult = []
        groupquery = "Select * from groupcriteriawithanswers"

        cursor = self.db_connection.cursor()
        cursor.execute(groupquery)
        grows = cursor.fetchall()
        cursor.close()

        for row in grows:
            r = {
            "autoid": row[0],
            "sfgroupid": row[1],
            "groupname": row[2],
            "groupdescription":row[3],
            "country":row[4],
            "isavailabletothepublic":row[5],
            "groupcriteriaid":row[6],
            "question":row[7],
            "answerid":row[8],
            "answertext":row[9],
            "answercode":[10]
            }
            groupresult.append(r)

        return  groupresult

    def get_productcategories_data(self):
        pcresult = []
        pcquery = "Select * from productcategories"

        cursor = self.db_connection.cursor()
        cursor.execute(pcquery)
        pcrows = cursor.fetchall()
        cursor.close()

        for row in pcrows:
            r = {
            "autoid": row[0],
            "productcategoryid": row[1],
            "productcategoryname": row[2],
            "productcategorybrandid":row[3],
            "brandname":row[4],
            "questionid":row[5],
            "questionlabel":row[6],
            "questiontext":row[7],
            "countryname":row[8],
            "answers":row[9],
            "answerid":[10],
            "answercode":[11],
            "answertext":[12]
            }
            pcresult.append(r)

        return  pcresult

    def get_brands_data(self):
        bresult = []
        bquery = "Select * from brands"

        cursor = self.db_connection.cursor()
        cursor.execute(bquery)
        pcrows = cursor.fetchall()
        cursor.close()

        for row in pcrows:
            r = {
            "autoid": row[0],
            "brandid": row[1],
            "brandname": row[2],
            "brandaccount":row[3],
            "brandbriefandnotes":row[4],
            "brandimageurl":row[5],
            "brandtrackingurl":row[6],
            "countofproductcategories":row[7],
            "facebooklikes":row[8]
            }
            bresult.append(r)

        return  bresult