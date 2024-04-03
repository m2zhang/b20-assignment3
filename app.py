from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine, text, or_ #import for textual query
from sqlalchemy.sql import exists   #import for exists


app = Flask(__name__)
app.config['SECRET_KEY'] = '84Br5667bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes = 10)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable = False)
    notes = db.relationship('Notes', backref='author', lazy=True)

    def __repr__(self):
        return f"Person('{self.username}', '{self.email}')"

class Notes(db.Model):
    __tablename__ = 'Notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), nullable=False)

    def __repr__(self):
        return f"Notes('{self.title}', '{self.date_posted}')"

with app.app_context():
    db.create_all()


@app.route("/")
@app.route('/home')
def home():
    pagename='home'
    return render_template("create_acc.html", pagename=pagename)


if __name__ == "__main__":
    app.run(debug=True)