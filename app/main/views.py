# from app import app
from . import main
from flask import render_template
from ..requests import sources, headlines, articles

@main.route('/')
def homepage():
    # print(app.config)
    news_sources= sources()
    trending_article = headlines()
    
    '''
    View root page function that returns the index page and its data
    '''
    # return "News2 Homepage"
    return render_template("index.html", news_sources=news_sources, trending_article=trending_article)

# @app.route('/articles')
# def articles():
#     # return "Source News Articles"
#     source_articles = articles()
#     return render_template("articles.html", source_articles=source_articles)

@main.route('/articles/<id>')
def all_articles(id):
    article_source = articles(id)
    return render_template("articles.html", article_source=article_source)