from flask import Flask
from pymongo import MongoClient
import gridfs
from src.instance.mongodb_config import MONGODB_CONFIG

mongo_client = MongoClient(MONGODB_CONFIG['MONGODB_ENDPOINT'])
db = mongo_client['CloudEHR']
files = db['Files']

fs = gridfs.GridFS(db)

a = fs.put(b"hello GridFS")

print(fs.get(a).read())