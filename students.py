from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
db.init_app(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

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