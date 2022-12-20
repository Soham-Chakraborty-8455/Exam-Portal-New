from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from questions import insertDocument, readDocuments

#QUESTION PART
#------------------------------------------

app = Flask(__name__)

@app.route('/questions', methods=['POST','GET'])
def add_todo():
    if request.method=='POST':
        ExamName = request.form.get('ExamName')
        SubjectCode = request.form.get('SubjectCode')
        Session = request.form.get('Session')
        Date = request.form.get('Date')
        Semester = request.form.get('Semester')
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
        insertDocument(ExamName, SubjectCode, Session, Date, Semester, StartTime, EndTime, QuestionValue, Option1, Option2,
                       Option3, Option4, CorrectMarks, CorrectAnswer, NegativeMarks)
        return render_template('questions.html')
    else:
        return render_template('questions.html')


if __name__ == "__main__":
    app.run(debug=True)