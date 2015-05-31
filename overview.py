import pprint
__author__ = 'ronanbrady2'

""" This file identifies some key statistics from the OpenMap Collection for the data for Dublin, Ireland"""

if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.udwrangle
    count = db.openmap.find().count()
    print("Count: {0}".format(count))
    count = db.openmap.find({"type":"node"}).count()
    print("Nodes: {0}".format(count))
    count = db.openmap.find({"type":"way"}).count()
    print("Ways: {0}".format(count))
    count = len(db.openmap.distinct("created.user"))
    print("Distinct Users: {0}".format(count))
    result = db.openmap.aggregate([{"$group":
                                        {"_id" : "$created.user", "count" : { "$sum" : 1 } } },
                                   { "$sort" : {"count": -1} },
                                   {"$limit":1 }  ] )
    for r in result:

        pprint.pprint(r)

    result = db.openmap.aggregate([{"$group":
                                        {"_id" : "$created.user", "count" : { "$sum" : 1 } } },
                                   {"$group":
                                        {"_id" : "$count", "num_users" : { "$sum" : 1 } } },
                                   { "$sort" : {"num_users": -1} },
                                   {"$limit":1 }  ] )
    for r in result:

        pprint.pprint(r)

