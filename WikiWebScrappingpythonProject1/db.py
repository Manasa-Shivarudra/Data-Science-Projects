from flask import Flask
import pymongo

CONNECTION_STRING = "mongodb+srv://<Username>:<password>@cluster0.jsq7s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Wiki_Scrapper')
user_collection = db['Wiki_Scrapper']
