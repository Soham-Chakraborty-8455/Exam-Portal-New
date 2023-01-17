import pymongo
from flask import  jsonify

connectionString = "mongodb+srv://IEM:IT@examinationportal.7tsx0kt.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connectionString)
db = client['IEM_Kolkata']
collection = db['IEM_Questions']

# Creating a Document
def insertDocument(anything):
    q=collection.insert_one(anything)
    id=q.inserted_id
    print(f"Document with id {id} has been created")

def appendDoc(marks, examid, enrollemntNo):
    json2={"examid": examid, "marks":marks}
    collection.update_one({"enrollment_number": enrollemntNo}, {"$push": json2}, upsert=True)
    print("done")

# Reading a Collection
def readDocuments(ExamId):
    questions = collection.find_one({'examid':ExamId})
    return questions

