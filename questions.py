import pymongo

connectionString = "mongodb+srv://IEM:IT@examinationportal.7tsx0kt.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connectionString)
db = client['IEM_Kolkata']
collection = db['IEM_Questions']

# Creating a Document
def insertDocument(ExamName, SubjectCode, Session, Date, Semester, StartTime, EndTime, QuestionValue,Option1,Option2,Option3,Option4, CorrectMarks, CorrectAnswer, NegativeMarks):
    questionlist = {'ExamName':ExamName,
            'SubjectCode':SubjectCode,
            'Session':Session,
            'Date':Date,
            'Semester': Semester,
            'StartTime':StartTime,
            'EndTime':EndTime,
            'QuestionData': [
                {
                    'Question': QuestionValue,
                    'Options':[{'1':Option1,'2':Option2,'3':Option3,'4':Option4}],
                    'CorrectMarks':CorrectMarks,
                    'CorrectAnswer':CorrectAnswer,
                    'NegativeMarks':NegativeMarks,
                },
            ]
    }
    q=collection.insert_one(questionlist)
    question_id=q.inserted_id
    print(f"Question Paper with id {question_id} has been created")


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



