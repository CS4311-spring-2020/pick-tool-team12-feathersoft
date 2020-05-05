import pymongo
from pymongo import MongoClient

# A cluster is the machine that holds our database
cluster = \
    MongoClient("mongodb+srv://Feathersoft:stevenroach@cluster0-700yf.mongodb.net/test?retryWrites=true&w=majority")


# Defining our DB
db = cluster["test"]

collection = db["test"]

# Add data to database example
doc = {"_id": 0, "name":"tim", "score":5}
collection.insert_one(doc)

# Retrieve data
results = collection.find({})

for result in results:
    print(result)


