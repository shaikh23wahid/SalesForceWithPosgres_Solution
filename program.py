__author__ = 'Wahid'

import bottle
import  SFDAO

@bottle.route('/home')
def Index():

    message ="welcome to python era"
    salesforcedata = sfdaocall.get_salesforce_data()
    return bottle.template("index.html", dict(SFData=salesforcedata))

sfdaocall = SFDAO.SFDAOClass("host='52.74.171.222' dbname='postgres' user='pureprofile' password='pureprofile'")

bottle.debug(True)
bottle.run(host="52.74.171.222",port=3000)