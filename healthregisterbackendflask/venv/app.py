from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)

class HealthFacility(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   Name = db.Column(db.string(100),nullable=True)
   Province = db.Column(db.string(100),nullable=True)
   District = db.Column(db.string(100),nullable=True)
   Ward = db.Column(db.string(100),nullable=True)
   Coordinates =  db.Column(db.string(250),nullable=True)
   infrastructure = db.Column(db.string(250),nullable=True)

class ContactDetails(db.Model):
   facility = db.Column(db.Integer, db.ForeignKey('healthfacility.id'))
   details = db.Column(db.string(100),nullable=True)

class Services(db.Model):
   facility = db.Column(db.Integer, db.ForeignKey('healthfacility.id'))
   service = db.Column(db.string(100),nullable=True)

class Equipment(db.Model):
   facility = db.Column(db.Integer, db.ForeignKey('healthfacility.id'))
   equipment = db.Column(db.string(100),nullable=True)

class OperatingHours(db.Model):
   facility = db.Column(db.Integer, db.ForeignKey('healthfacility.id'))
   day = db.Column(db.string(50),nullable=True)
   hours = db.Column(db.string(100),nullable=True)