'''
Created on Feb 27, 2017

@author: AlexFeng
'''
from flask import Flask
from flask import render_template
from flask import request
import json




app = Flask(__name__)



@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/index/')
@app.route('/index/<name>')
def index_page(name=None):
    return render_template('index.html', name=name)

    

if __name__ == "__main__":
    app.run()
