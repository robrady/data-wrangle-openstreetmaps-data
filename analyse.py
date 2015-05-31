import pprint
import re
from collections import defaultdict

__author__ = 'ronanbrady2'

'''
Various address fields:
 'addr:city',
 'addr:city:ga',
 'addr:country',
 'addr:county',
 'addr:full',
 'addr:housename',
 'addr:housename:en',
 'addr:housename:ga',
 'addr:housename:it',
 'addr:housenumber',
 'addr:housenumber:source',
 'addr:interpolation',
 'addr:place',
 'addr:postal_district',
 'addr:postcode',
 'addr:street',
 'addr:street:ga',
 'addr:street:name',
 'addr:terracename',
 'addr:town',
 'addr:unit'
 '''
if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.udwrangle
    pipeline = [
                 { "$group" : {
                      "_id" : "$address.street" ,
                      "count" : { "$sum" : 1 } }},
        { "$sort" : { "_id" : 1 }}]

    result = db.openmap.aggregate(pipeline)
    #result = db.openmap.find_one()
    #result = db.openmap.find({"created.user" : "Joe E" })

    #result = db.openmap.find({"address.postcode" : { "$exists" : "true"} })
    #result = db.openmap.find({"address.street" : "Terenure Road East"})
    #result = db.openmap.find({ "address.county" : { "$exists" : "true" } }).count()


    valsfound = defaultdict(int)
    regx = re.compile("\s(\w+)$", re.IGNORECASE)
    for r in result:
        val = r['_id']


        if(not val is None):
            i = regx.finditer(val)
            for match in i:
                streettype = match.group(0).strip()
                valsfound[streettype] += 1
    pprint.pprint(valsfound)



