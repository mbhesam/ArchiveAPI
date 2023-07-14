from datetime import datetime
from pymongo import MongoClient
from archiveAPI.settings import DOMAIN_NAME,MONGO_CON_STR,MONGO_DB_NAME,MONGO_COLLECTION_NAME
import json
from bson import json_util,ObjectId

client = MongoClient(MONGO_CON_STR)
mydb = client[MONGO_DB_NAME]
connection_string = mydb[MONGO_COLLECTION_NAME]

# { "query": {"identifier" : "bnr10010"} }
#db.users.find({awards: {$elemMatch: {award:'National Medal', year:1975}}})
def count_objects(query={},exact=True):
    if exact == True:
        find = query["query"]
    else:
        find = convert_exact_to_regex_query(query=query["query"])
    doc_count = connection_string.count_documents(find)
    return doc_count

def search_objects(query={},exact=True):
    if exact == True:
        find = query["query"]
    else:
        find = convert_exact_to_regex_query(query=query["query"])
    mongo_obj = connection_string.find(find)
    dict_result = {}
    for count,value in enumerate(mongo_obj):
        dict_result[f'{count}'] = value
    docs = json.loads(json_util.dumps(dict_result))
    return docs

def convert_exact_to_regex_query(query):
    new_query = {}
    for key, value in query.items():
        if isinstance(value, str): # if query is simple key value
            new_query[key] = {"$regex": f".*{value}.*"}
        elif isinstance(value, list):  # if query has operator at first
            innernew_query={}
            list_innernew_query=[]
            for element in value:
                innerkey=list(element.keys())[0]
                innervalue=list(element.values())[0]
                if isinstance(innervalue, str):
                    innernew_query[innerkey] = {"$regex": f".*{innervalue}.*"}
                list_innernew_query.append(innernew_query)
            new_query[key] = list_innernew_query
    return new_query

def search_range_objects(query):
    start_hexadecimal = query["identifier"]
    range = query["range"]
    mongo_obj = connection_string.find({"_id": {"$gte": ObjectId(f'{start_hexadecimal}')}}).limit(range)
    dict_result = {}
    for count,value in enumerate(mongo_obj):
        dict_result[f'{count}'] = value
    docs = json.loads(json_util.dumps(dict_result))
    return docs

def delete_objects(query,exact=True):
    if exact == True:
        find = query["query"]
    else:
        find = convert_exact_to_regex_query(query=query["query"])
    d = connection_string.delete_many(find)
    dict_result = { "object_deleted_count" : f"{d.deleted_count}"}
    docs = json.loads(json_util.dumps(dict_result))
    return docs

def delete_range_objects(query):
    start_hexadecimal = query["identifier"]
    range = query["range"]
    docs_to_delete = connection_string.find({"_id": {"$gte": ObjectId(f'{start_hexadecimal}')}}).limit(range)
    ids_to_delete = [doc["_id"] for doc in docs_to_delete]
    for doc in ids_to_delete:
        try:
            connection_string.delete_one({"_id": doc})
        except:
            dict_result = {"object_deleted_ids": f"NO ID"}
            docs = json.loads(json_util.dumps(dict_result))
            return docs
    dict_result = {"object_deleted_ids": f"{ids_to_delete}"}
    docs = json.loads(json_util.dumps(dict_result))
    return docs

def create_object(query):
    object = query["query"]
    requiered_keys = ["attachments","ocr_status","description","local_address","topics","identifier","collections"]
    for key in requiered_keys:
        if key not in object.keys():
            return False
        else:
            pass
    result = connection_string.insert_one(object)
    new_id = result.inserted_id
    dict_result = { "new_object_id" : f"{new_id}"}
    docs = json.loads(json_util.dumps(dict_result))
    return docs

def update_object(query,exact=False):
    update_query = {}
    if exact == True:
        find_query = query["find_query"]
    else:
        find_query = convert_exact_to_regex_query(query=query["find_query"])
    user_update_query = query["update_query"]
    update_query['$set'] = user_update_query
    result = connection_string.update_many(find_query,update_query)
    modified_ids = []
    if result.modified_count > 0:
        modified_documents = connection_string.find(find_query)
        for doc in modified_documents:
            modified_ids.append(doc['_id'])
    dict_result = { "modified_object_id" : f"{modified_ids}"}
    docs = json.loads(json_util.dumps(dict_result))
    return docs

def get_img_info(entity,collection,pdf_name):
    find = { 'identifier' : entity }
    doc = connection_string.find(find)
    option = {}
    fields = [field for field in doc][0]
    for attachment in fields["attachments"]:
        if attachment['name'] == pdf_name:
            bookTitle = attachment['name'] + '-' + attachment['caption']
            thumbnail = attachment['thumbnail']
            data = []
            for counter,img in enumerate(attachment['files_inside']):
                dics_info = {}
                dics_info['width'] = img['width']
                dics_info['height'] = img['height']
                name_page = img['local_address'].split('/')[-1]
                uri = '//' + DOMAIN_NAME + '/' + 'bookreader' + collection + '/' + entity + '/' + 'images' + '/' + name_page
                dics_info['uri'] = uri
                data.append([dics_info])
    option['data'] = data
    option['bookTitle'] = bookTitle
    option['thumbnail'] = thumbnail
    result_json = json.loads(json_util.dumps(option))
    return result_json

