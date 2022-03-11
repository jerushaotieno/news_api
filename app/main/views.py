from . import main
from flask import render_template
from ..requests import sources

@main.route('/')
def homepage():
    general_news = sources('general')

    return render_template('index.html', general = general_news)


@main.route('/')
def articles(source_id):
    general_news = sources('general')

    return render_template('index.html', general = general_news)
