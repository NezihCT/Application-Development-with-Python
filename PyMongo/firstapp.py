# from pymongo import MongoClient

# client = MongoClient()

import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')
myDb = myClient["Northwind"]
myCollection = myDb["Products"]

products = myCollection.find({})

for x in products:
    print(x)

# python -m pip install pymongo    => hata veriyorsa
# python3 -m pip install pymongo