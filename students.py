from flask import Flask,  request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)