from mastodon import Mastodon, StreamListener
import mastodon
import time
from googleapiclient import discovery
import json
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from initialize_db import Prof, Course, Review

#get keys
f = open("./user_token",'r')
access_token = f.readlines()[0]
f = open("./key",'r')
API_KEY = f.readlines()[0]

instance = "https://social.cs.swarthmore.edu"
# Creates an instance of the Masotodon class 
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=instance
)

# Variable to store comment ID and content 
conversation = []
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)

# Define the StreamListener class
class StreamListener(StreamListener): 
    def on_conversation(self, conversation):
        #get only new conversation (not something we post)
        if conversation['unread']:
            test_var = False
            convo_to_send = str(BeautifulSoup(conversation['last_status']['content'],features="html.parser").get_text())
            client = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=API_KEY,
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False,
            )

            analyze_request = {
            'comment': { 'text': convo_to_send },
            'requestedAttributes': {'TOXICITY': {}, 'PROFANITY': {}, 'IDENTITY_ATTACK': {}}
            }
            #try to get prospective analysis
            try:
                response = client.comments().analyze(body=analyze_request).execute()
                response = response['attributeScores']
            except:
                test_var = True
            
            #if flagged or something went wrong, reply to user
            if test_var or float(response['PROFANITY']['summaryScore']['value'])> .6 or float(response['TOXICITY']['summaryScore']['value']) > .5 or float(response['IDENTITY_ATTACK']['summaryScore']['value']) > .08:
                user = conversation['accounts'][0]['username']
                convo_id = conversation['last_status']['id']
                content = "Your review was flagged as potentially harmful, or something went wrong. Please adjust your message and try again."
                m = Mastodon(access_token=access_token, api_base_url="https://social.cs.swarthmore.edu")
                m.status_post("@" + user + " " + content, in_reply_to_id= convo_id, visibility = "direct")


            else:
                #we got review, need to parse and add to database
                text = str(BeautifulSoup(conversation['last_status']['content'],features="html.parser").get_text())
                course_code, text = text.split('Full Name of Professor:')
                course_code = course_code[27:].strip()
                professor_full_name_and_sem, text = text.split('Rating 1-5, 5 being best and most difficult')
                professor_full_name, semester_taken = professor_full_name_and_sem.split('Semester Taken, e.g. Fall 2023:')
                professor_full_name = professor_full_name.strip()
                semester_taken = semester_taken.strip()
                overall_rating_og, text = text.split("Difficulty Rating:")
                overall_rating_og = overall_rating_og.split("Overall Rating: ")[1].strip()
                difficulty_rating_og, text= text.split("Please write your open-ended comment here:")
                difficulty_rating_og = difficulty_rating_og.strip()
                review_message = text.strip()
                # print("\n\n\n")
                # print(course_code)
                # print(professor_full_name)
                # print(overall_rating_og)
                # print(difficulty_rating_og)
                # print(review_message)
                with app.app_context():
                    p = db.session.query(Prof.id).filter_by(prof_full=professor_full_name).all()[0][0]
                    c = db.session.query(Course.id).filter_by(course_code=course_code).filter_by(prof_id = p).all()[0][0]
                    o = int(overall_rating_og)
                    d = int(difficulty_rating_og)
                    r = review_message
                    review = Review(
                        id=conversation['last_status']['id'],\
                        course_id = c,\
                        prof_id = p,\
                        overall_rating = o,\
                        difficulty_rating = d,\
                        review_content = r,\
                        account_username = conversation['accounts'][0]['username'],\
                        account_id = conversation['accounts'][0]['id'],\
                        semester_taken = semester_taken,\
                    )
                    db.session.add(review)
                    db.session.commit()
                    #post new review from our account
                    m = Mastodon(access_token=access_token, api_base_url="https://social.cs.swarthmore.edu")
                    m.toot("New Review!!\n\n" + "Course Code: " + course_code + "\nProfessor Name: " + professor_full_name + "\nSemester Taken: " + semester_taken + "\n\nOverall Rating:" + str(o) + "\nDifficulty Rating: " + str(d) + "\n\n" + review_message)


    

# Creates an instance of custom StreamListener 
listener = StreamListener()

# Start streaming with the custom listener
def getDMs(): 
    mastodon.stream_direct(listener, run_async=True, timeout=300, reconnect_async=False, reconnect_async_wait_sec=5)
    return conversation 

