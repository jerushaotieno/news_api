from app import app
from flask import render_template

@app.route('/')
def index():
    return "News2 Homepage"
    return render_template("index.html")

@app.route('/sources')
def sources():
    return "Source News Articles"
    return render_template("sources.html")