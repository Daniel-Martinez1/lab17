# run with: flask --app hello_flask --debug run 

from flask import Flask ,  render_template

app = Flask(__name__)
import requests, json
from pprint import pprint
from flask_bootstrap import Bootstrap5


# meowfacts- An API that returns a random fact about cats on a request


@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2

@app.route('/matty')
def mn():
    
    return render_template('index.html')
    

@app.route('/mom')
def test():
    return render_template('index.html')
