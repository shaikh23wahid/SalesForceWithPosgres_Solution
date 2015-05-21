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

@bottle.route('/productcategories')

def productcategories():

    message ="Salesforce Product Categories Data"
    pcdata = sfdaocall.get_productcategories_data()
    return bottle.template("productcategories.html", dict(productcategoriesdata=pcdata))

@bottle.route('/brands')

def brands():

    message ="Salesforce Brands Data"
    bdata = sfdaocall.get_brands_data()
    return bottle.template("brands.html", dict(brandsdata=bdata))

sfdaocall = SFDAO.SFDAOClass("host='52.74.171.222' dbname='postgres' user='pureprofile' password='pureprofile'")

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080)