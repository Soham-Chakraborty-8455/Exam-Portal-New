from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

#QUESTION PART
#------------------------------------------

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://IEMITDEPT:DepartmentofIT@cluster0.exh0dky.mongodb.net/?retryWrites=true&w=majority"
mongo = PyMongo(app)
questions = mongo.db.questions
@app.route('/add', methods=['POST'])
def add_todo():
    ExamName = request.form.get('ExamName')
    SubjectCode = request.form.get('SubjectCode')
    Session = request.form.get('Session')
    Date = request.form.get('Date')
    StartTime = request.form.get('StartTime')
    EndTime = request.form.get('EndTime')
    QuestionValue = request.form.get('QuestionValue')
    Option1 = request.form.get('Option1')
    Option2 = request.form.get('Option2')
    Option3 = request.form.get('Option3')
    Option4 = request.form.get('Option4')
    CorrectMarks = request.form.get('CorrectMarks')
    CorrectAnswer = request.form.get('CorrectAnswer')
    NegativeMarks = request.form.get('NegativeMarks')
    questions.insert_one({'ExamName':ExamName,
        'SubjectCode':SubjectCode,
        'Session':Session,
        'Date':Date,
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
})
    return redirect(render_template(questions.html))







#STUDENT RECORD PART
#-------------------------------------------------------------------
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
db.init_app(app)
class Students(db.Model):
    enrollment_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route("/", methods=["GET", "POST"])
def user_create():
    return jsonify(request.json)

if __name__ == "__main__":
    app.run(debug=True)