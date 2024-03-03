import os
from mastodon import Mastodon, StreamListener
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from werkzeug.utils import import_string
import requests
from bs4 import BeautifulSoup
import json


# create and configure the app
app = Flask(__name__, instance_relative_config=True)

### START DB CONFIG 

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
migrate = Migrate(app, db) # database migrations are used to keep the database up to date when new models are added or existing ones are changed
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer(), primary_key=True)
    course_code = db.Column(db.String(100), unique=False, nullable=False)
    course_title = db.Column(db.String(200), unique=False, nullable=False)
    prof_id = db.Column(db.Integer(), db.ForeignKey('profs.id'), nullable= False)
    def __repr__(self):
        return f"id: {self.id}, course_code: {self.course_code}, course_title: {self.course_title}, prof_id: {self.prof_id}"

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key = True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable= False)
    prof_id = db.Column(db.Integer, db.ForeignKey('profs.id'), nullable= False)
    overall_rating = db.Column(db.Integer, unique = False, nullable = False)
    difficulty_rating = db.Column(db.Integer, unique = False, nullable = False)
    review_content = db.Column(db.String(5000), unique=False, nullable=False)
    account_username = db.Column(db.String(100), unique = False, nullable = False)
    account_id = db.Column(db.String(100), unique=False, nullable=False)
    semester_taken = db.Column(db.String(100), unique=False, nullable=False)
    def __repr__(self):
        return f"id: {self.id}, course_id: {self.course_id}, prof_id: {self.prof_id}, overall_rating: {self.overall_rating}, difficulty_rating: {self.difficulty_rating}, review_content: {self.review_content}, account_username: {self.account_username}, account_id: {self.account_id}, semester_taken: {self.semester_taken}"

class Prof(db.Model):
    __tablename__ = 'profs'
    id = db.Column(db.Integer, primary_key = True)
    prof = db.Column(db.String(200), unique=False, nullable=False)
    prof_full = db.Column(db.String(200), unique=False, nullable=True)
    prof_ln = db.Column(db.String(200), unique=False, nullable=True)
    def __repr__(self):
        return f"id: {self.id}, prof: {self.prof}, prof_full: {self.prof_full}  prof_ln: {self.prof_ln}"
    
#CODE BELOW IS USED TO PREPOPULATE DATABASE -- LEAVE COMMENTED OUT
# with app.app_context():
#     what = db.session.query(Prof.id).filter_by(prof_full='Lila Fontes').all()
#     print(what[0][0])
# reviews = [['CPSC041', "Lila Fontes", 4, 3, "I really like the labs in this class"]]
# #Read in JSON and make dict
# with open('courses.json') as json_file:
#     classes = json.load(json_file)
# with open('profs.json') as json_file:
#     profs_data = json.load(json_file)
# #For every course in dict
# with app.app_context():
#     db.create_all()

#     for prof in list(profs_data.items()):
#         if db.session.get(Prof,prof[0]) is None:
#             new_prof = Prof(
#                 id = prof[0],\
#                 prof = prof[1][0],\
#                 prof_full = prof[1][1],\
#                 prof_ln = prof[1][2],\
#             )
#             db.session.add(new_prof)
#             db.session.commit()

#     for course in list(classes.items()):

#         print(course[0])
#         if db.session.get(Course,course[0]) is None: # query the db to make sure post doesn't already exist
#                     new_class = Course(
#                             id = course[0],\
#                             course_code=course[1][0],\
#                             course_title = course[1][1],\
#                             prof_id = course[1][2],\
#                         )
#                     print("Added to database.\n\n",new_class) # for debugging purposes, see console
#                     db.session.add(new_class)
#                     db.session.commit()
    

# with app.app_context():
#     db.create_all()
#     prof_id_to_add = db.session.query(Prof.id).filter_by(prof_full='Lila Fontes').all()[0][0]
#     course_id_to_add = db.session.query(Course.id).filter_by(course_code='CPSC041').all()[0][0]
#     new_review = Review(
#         id = 3,\
#         course_id = course_id_to_add,\
#         prof_id = prof_id_to_add,\
#         overall_rating = 3,\
#         difficulty_rating = 5,\
#         review_content =  "Umi is the cutest",\
#         account_username = "admin",\
#         account_id = "admin",\
#         semester_taken = "Fall 2023",\
#         )
#     db.session.add(new_review)
#     db.session.commit()