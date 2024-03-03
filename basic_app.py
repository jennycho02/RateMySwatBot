from flask import Flask
app = Flask(__name__) # create an instance of the Flask class called "app" that will handle your website
# @ is a python decorator that allows you to "wrap" a function and modify its behavior
@app.route('/') # specify which URL route (e.g., website.com/ vs. website.com/app/) will activate the following function
def hello(): # define a function called "hello" that is passed to "app.route" above
    return 'Hello World!'

