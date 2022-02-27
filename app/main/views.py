from app import app
from flask import render_template

@app.route('/')
def homepage():
    print(app.config)

    '''
    View root page function that returns the index page and its data
    '''
    
    # return "News2 Homepage"
    return render_template("index.html")

@app.route('/articles/<name>')
def articles(name):
    # return "Source News Articles"
    return render_template("articles.html")