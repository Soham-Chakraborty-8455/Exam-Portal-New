from flask import Flask,  request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from mongo import insertDocument, appendDoc
from flask_pymongo import PyMongo
from mongo import insertDocument, readDocuments


app = Flask(__name__, static_folder='../build', static_url_path='/')

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
db.init_app(app)

class Students(db.Model):
    enrollment_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)

class Exams(db.Model):
    examid= db.Column(db.Integer, primary_key= True)
    exam_name = db.Column(db.String, nullable= False)
    exam_startDate= db.Column(db.Date, nullable = False)
    exam_startTime = db.Column(db.Time, nullable=False)
    semester= db.Column(db.Integer, nullable= False)
    ## 2022-03-21 19:04:14
    exam_duration = db.Column(db.Integer, nullable = False)
    subject_code= db.Column(db.Integer, nullable = False)
    session= db.Column(db.Integer, nullable = False)

class Teacher(db.Model):
    teacherid= db.Column(db.String, nullable = False, primary_key=True)
    name= db.Column(db.String, nullable= False)
    phoneNumber= db.Column(db.String, nullable = False)
    email= db.Column(db.String, nullable = False)

with app.app_context():
    db.create_all()
    db.session.commit()

####=======================DATABASE ENDS HERE=========================================================================####


####==================================STUDENT SECTION STARTS==========================================================================####
@app.route("/signup", methods=["GET", "POST"])
def user_create():
    if request.method == 'POST':
        enrollment_number = request.json['enrollment_number']
        name = request.json['name']
        email = request.json['email']
        phone_number = request.json['phone_number']
        users = Students(enrollment_number=enrollment_number, name=name, email=email, phone_number=phone_number)
        with app.app_context():
            db.session.add(users)
            db.session.commit()
        j=jsonify({"enrollment_number":enrollment_number, "name":name, "email":email, "phone":phone_number})
        insertDocument(j)
        return render_template('Signup.html')
    else:
        return render_template('Signup.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        enrollment_number = request.json['enrollment_number']
        phone_number = request.json['phone_number']
        with app.app_context():
            enrol=Students.query.filter_by(phone_number=phone_number).first()
            phone=Students.query.filter_by(enrollment_number=enrollment_number).first()
            if(enrol==phone):
                print("SUCCESS")
            else:
                print("FAIL")
    return render_template('login.html')

####===========================STUDENT SECTION ENDS========================================================================================####

@app.route("/marks/<int:enrollment_number>", methods=["POST", "GET"])
def marksadd(enrollment_number):
    if request.method=="POST":
        marks=request.json['marks']
        examid=request.json["examid"]
        appendDoc(marks, examid, enrollment_number)
    return render_template('index1.html')


@app.route("/createTest", methods=["POST", "GET"])
def create_test():
    if request.method=="POST":
        ExamName=request.json['ExamName']
        SubjectCode= request.json['SubjectCode']
        Session= request.json['Session']
        Date= request.json['Date']
        StartTime= request.json['StartTime']
        semester= request.json['semester']
        duration= request.json['duration']
        examstartDate= datetime.strptime(Date, "%Y-%m-%d")
        exams= Exams(exam_name=ExamName, subject_code=SubjectCode, exam_startDate= examstartDate, exam_startTime=StartTime, exam_duration= duration, session= Session, semester=semester)
        with app.app_context():
            db.session.add(exams)
            db.session.commit()
            examid= f"select examid from Exams where exam_name={ExamName}"
            print(examid)
        return jsonify({'examid': examid})
    return render_template('index1.html')

@app.route("/startcheck", methods=["POST","GET"])
def startcheck():
    if request.method=="POST":
        starttest=False
        examid= request.json['examid']
        with app.app_context():
            time= f"select exam_startTime from Exams where examid={examid}"
            date= f"select exam_startDate from Exams where examid={examid}"
            dur= f"select exam_duration from Exams where examid={examid}"
        nw=datetime.now()
        currdate=nw.date()
        currtime= nw.time()
        if(currdate== date):
            if(time>currtime):
                starttest=True
        if(starttest==True):
            return jsonify({"examid": examid})

@app.route('/addQ', methods=['POST','GET'])
def questions():
    if request.method=='POST':
        questionList = request.json['ExamPaper']
        insertDocument(questionList)
        return render_template('index1.html')
    else:
        return render_template('index1.html')

@app.route('/teachersignup', methods=["POST", "GET"])
def teachersignup():
    if request.method=="POST":
        teacherid=request.json["teacherid"]
        phoneNumber=request.json["phoneNumber"]
        email=request.json["email"]
        name= request.json['name']
        addT=Teacher(teacherid=teacherid, phoneNumber=phoneNumber, email=email, name=name)
        with app.app_context():
            db.session.add(addT)
            db.session.commit()
        return  jsonify({'teachername': name})

@app.route('/teacherlogin', methods=["POST","GET"])
def teacherlogin():
    if request.method=="POST":
        teacherid=request.json["teacherid"]
        phoneNumber=request.json["phoneNumber"]
        with app.app_context():
            q1=f"select phoneNumber from Teacher where teacherid={teacherid}"
            if(phoneNumber==q1):
                print("Success")
            else:
                print("Fail")
            q2=f"select name from Teacher where teacherid={teacherid}"

        return jsonify({'teachername': q2})

@app.route('/entercode', methods=["POST", "GET"])
def enterexamcode():
    if request.method=="POST":
        examCode= request.json['examCode']



if __name__ == "__main__":
    app.run(debug=True)