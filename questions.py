from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from mongo import insertDocument, readDocuments

#QUESTION PART
#------------------------------------------

app = Flask(__name__)

@app.route('/data', methods=['POST','GET'])
def questions():
    if request.method=='POST':
        questionList = request.json['ExamPaper']
        insertDocument(questionList)
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/examtiming', methods=['POST', 'GET'])
def timecheker():
    if request.method=="POST":
        examid= request.json['examid']



if __name__ == "__main__":
    app.run(debug=True)