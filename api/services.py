from datetime import datetime
from pymongo import MongoClient
from archiveAPI.settings import MONGO_CON_STR,MONGO_DB_NAME,MONGO_COLLECTION_NAME
import json
from bson import json_util

client = MongoClient(MONGO_CON_STR)
mydb = client[MONGO_DB_NAME]
connection_string = mydb[MONGO_COLLECTION_NAME]

# { "query": {"identifier" : "bnr10010"} }
#db.users.find({awards: {$elemMatch: {award:'National Medal', year:1975}}})
def count_objects(query={}):
    find = query["query"]
    doc_count = connection_string.count_documents(find)
    return doc_count
def mongo_obj_to_json(mongo_obj):
    result = list(mongo_obj)
    result_json = [ dict(i) for i in result]
    result_final = []
    for dict in result_json:
        result_final.append(dict)
    json_response = json.dumps(result_final)
    return json_response

def search_objects(query={}):
    find = query["query"]
    mongo_obj = connection_string.find(find)
    dict_result = {}
    for count,value in enumerate(mongo_obj):
        dict_result[f'{count}'] = value
    docs = json.loads(json_util.dumps(dict_result))
    return docs