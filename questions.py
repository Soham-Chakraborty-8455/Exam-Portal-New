from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from mongo import insertDocument, readDocuments

#QUESTION PART
#------------------------------------------

app = Flask(__name__)

@app.route('/questions', methods=['POST','GET'])
def add_todo():
    if request.method=='POST':
        questionList = request.json('Data')
        insertDocument(questionList)
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)