from datetime import datetime
from pymongo import MongoClient
from archiveAPI.settings import MONGO_CON_STR,MONGO_DB_NAME,MONGO_COLLECTION_NAME

client = MongoClient(MONGO_CON_STR)
mydb = client[MONGO_DB_NAME]
connection_string = mydb[MONGO_COLLECTION_NAME]

# { "query": {"identifier" : "bnr10010"} }
#db.users.find({awards: {$elemMatch: {award:'National Medal', year:1975}}})
def count_objects(query={}):
    find = query["query"]
    doc_count = connection_string.count_documents(find)
    return doc_count