from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
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

@app.route("/")
def hello_world():
    return "<p>Student Table</p>"

if __name__ == "__main__":
    app.run(debug=True)