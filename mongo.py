import pymongo

connectionString = "mongodb+srv://IEM:IT@examinationportal.7tsx0kt.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connectionString)
db = client['IEM_Kolkata']
collection = db['IEM_Questions']

# Creating a Document
def insertDocument(anything):
    q=collection.insert_one(anything)
    id=q.inserted_id
    print(f"Document with id {id} has been created")


# Reading a Collection
def readDocuments(ExamName, SubjectCode, Session, Date, Semester,StartTime, EndTime):
    questions = collection.find({'ExamName':ExamName,
            'SubjectCode':SubjectCode,
            'Session':Session,
            'Date':Date,
            'Semester': Semester,
            'StartTime':StartTime,
            'EndTime':EndTime,})
    for element in questions:
        print(element)



