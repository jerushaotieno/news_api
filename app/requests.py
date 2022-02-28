from app import app
from .models import Sources, Articles
import urllib.request, json
from newsapi import NewsApiClient

key = app.config['API_KEY']
url = app.config['SOURCE_URL']
newsapi = NewsApiClient(api_key = key)

def sources():
    '''
    function to get all news sources in a list in English
    '''
    data = newsapi.get_sources(language = 'en', country = 'us')
    data_list = data['sources']
    source_list = []
    for item in data_list:
        new_source = Sources(item['id'], ['name'], item['description'], item['url'])
        source_list.append(new_source)

    return source_list

def headlines():
    '''
    function to get all news sources in English  in a list
    '''
    res = newsapi.get_top_headlines(language='en', page_size=6, sources='reuters')
    res_list =  res['articles']
    trending = []
    for item in res_list:
        top_article = headlines(item['title'], item['urlToImage'], item['url'])
        trending.append(top_article)

    return trending


def articles(source_id):
    '''
    function to get all English news sources in a list
    '''
    source_url = url.format(source_id, key)
    with urllib.request.urlopen(source_url) as uri:
        result = uri.read()
        response = json.loads(result)

        article_results = []

        if response['articles']:
            source_data_list = response['articles']
            article_results = get_data(source_data_list)
    return article_results


def get_data(source_dict):
    '''
    '''
    article_list = []
    for item in source_dict:
        article_title = item.get('article_title')
        article_author = item.get('article_author')
        article_description = item.get('article_description')
        article_url = item.get('article_url')
        article_url_to_image = item.get('article_url_to_image')
        article_published_at = item.get('article_published_at')

        if article_url_to_image and article_url:
            new_article = Articles(article_title, article_author, article_description, article_url, article_url_to_image, article_published_at)
            article_list.append(new_article)     
    return article_list 