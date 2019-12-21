import os
from flask import Flask
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

#using the OS library to set a constant by using the getenv() method to read in the environment variable
#also using the Python constants to access the database and collection
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "knowledge_is_power"
COLLECTION_NAME = "fundraisers"

#Mongo connect function to print message is connection is successful or there is an error
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
#calling the connect function to print everything in the database when called in terminal      
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)   
        


