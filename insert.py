__author__ = 'ronanbrady2'

import json

""" This file inserts the data from the JSON file (created by data.py) into an OpenMap collection in the Mongo Database 'udwrangle'
"""

def insert_data(data, db):

    # Insert the data into a collection
    db.openmap.insert(data)

if __name__ == "__main__":

    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.udwrangle

    deleted_count = db.openmap.delete_many({}).deleted_count
    print("deleted count: {}".format(deleted_count))

    with open('dublin_ireland.osm2.json') as f:

        data = json.load(f)

        insert_data(data, db)

        print(db.openmap.find_one())