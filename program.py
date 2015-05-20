__author__ = 'Wahid'

import bottle
import  SFDAO

@bottle.route('/index')

def Index():

    message ="welcome to python era"
    salesforcedata = sfdaocall.get_salesforce_data()
    return bottle.template("index.html", dict(myData=salesforcedata))

@bottle.route('/groups')

def groups():

    message ="Salesforce Group Data"
    gdata = sfdaocall.get_groups_data()
    return bottle.template("groups.html", dict(groupdata=gdata))

sfdaocall = SFDAO.SFDAOClass("host='52.74.171.222' dbname='postgres' user='pureprofile' password='pureprofile'")

bottle.debug(True)
bottle.run(host='localhost', port=8080)