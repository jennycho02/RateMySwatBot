import os, sys, google
from mastodon import Mastodon
from flask import Flask, render_template, request, redirect, url_for, flash
from googleapiclient import discovery
import json
from my_app.stream import getDMs
from mastodon import Mastodon
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

getDMs()


API_KEY = 'AIzaSyBPNKZiVOvFrXQtgSz55X9sFtb2eoovKvI'

f = open("./user_token",'r')
token = f.readlines()[0]


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    from initialize_db import Course, Prof, Review

    #get dropdown classes to prefill search box
    with app.app_context():
        dropdown_classes = []
        seen = set()
        all_classes = db.session.query(Course.id, Course.course_title, Course.course_code, Course.prof_id).all()
        for class_id, class_title, class_code, prof_id in all_classes:
            professor_name = db.session.query(Prof.prof_full).filter_by(id=prof_id).scalar()
            text_string = class_code + ": " + class_title + " - " + professor_name
            
            if text_string not in seen:
                dropdown_classes.append(text_string)
                seen.add(text_string)

    #homepage
    @app.route('/',  methods=['GET'])
    def homepage():
        return render_template('/home.html', dropdown_classes = dropdown_classes)

    #if we posted a review
    @app.route("/success/",  methods=['GET', 'POST'])
    def no_reviews():
        if request.method == "POST":
            print(request.form)
            course_name = request.form['course']
            m = Mastodon(access_token=token, api_base_url="https://social.cs.swarthmore.edu")
            m.toot("Please post reviews for: "+ course_name)
            return render_template('/home.html', dropdown_classes = dropdown_classes)
        return render_template('/home.html', dropdown_classes = dropdown_classes)
    
    #for reviews
    @app.route("/reviews/<path:course_input>/", methods=['GET', 'POST'])
    def reviews(course_input):
        #parse to get course code and prof, look up from database and get reviews
        print('whooop')
        try:
            course_code, rest = course_input.split(": ", 1)
            course_title, prof_name = rest.split(" - ")
            p = db.session.query(Prof.id).filter_by(prof_full=prof_name).all()[0][0]
            selected_course_id = db.session.query(Course.id).filter_by(course_code=course_code).filter_by(prof_id = p).all()[0][0]
            reviews_for_class = db.session.query(Review).filter_by(course_id=selected_course_id).all()
            content = []
            for review in reviews_for_class:
                content.append({'semester_taken': review.semester_taken, 'overall_rating': review.overall_rating, 'difficulty_rating': review.difficulty_rating, 'review_content':review.review_content})
            course_reviews = content
            #if reviews vs no reviews send to different htmls
            if len(reviews_for_class) == 0:
                return render_template('no_reviews.html', dropdown_classes = dropdown_classes, course_name = course_code, course_title = course_title, professor_name = prof_name)
            else:
                return render_template('reviews.html', dropdown_classes = dropdown_classes, course_name = course_code, course_title = course_title, professor_name = prof_name, course_reviews = course_reviews)
        except:
            return redirect('/')

    return app