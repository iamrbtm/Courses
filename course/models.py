from course import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime, os
from sqlalchemy.orm import backref, relationship
from sqlalchemy import ForeignKey


# Users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    address = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(150), unique=True)
    dob = db.Column(db.Date)
    avatar_filename = db.Column(db.Text)
    avatar_url = db.Column(db.String(250))
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())


class apitoken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    token = db.Column(db.String(200))


class States(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(50))
    abr = db.Column(db.String(2))

class Catalog(db.Model):
    course_code = db.Column(db.String(25), primary_key=True)
    course_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    prerequisites = db.Column(db.String(25))
    credits = db.Column(db.Integer)
    proctor_Class = db.Column(db.Boolean, default=False)
    userid = db.Column(db.Integer)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)



# class <name>(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     userid = db.Column(db.Integer)
#     update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#     date_created = db.Column(db.DateTime(timezone=True), default=func.now())
