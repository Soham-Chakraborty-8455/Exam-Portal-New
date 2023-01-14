from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from mongo import insertDocument, readDocuments

#QUESTION PART
#------------------------------------------

app = Flask(__name__)

@app.route('/addQ', methods=['POST','GET'])
def questions():
    if request.method=='POST':
        questionList = request.json['ExamPaper']
        insertDocument(questionList)
        return render_template('index1.html')
    else:
        return render_template('index1.html')



if __name__ == "__main__":
    app.run(debug=True)