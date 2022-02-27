from app import app
from flask import render_template
# from .requests import sources, articles
from requests import sources, articles
import datetime as dt

@app.route('/')
def homepage():
    # print(app.config)
    news_sources= sources()

    '''
    View root page function that returns the index page and its data
    '''
    
    # return "News2 Homepage"
    return render_template("index.html", news_sources=news_sources)

# @app.route('/articles')
# def articles():
#     # return "Source News Articles"
#     source_articles = articles()
#     return render_template("articles.html", source_articles=source_articles)
@app.route('/articles/<id>')
def all_articles(id):
    article_source = articles(id)
    print(article_source)
    return render_template("articles.html", article_source=article_source)