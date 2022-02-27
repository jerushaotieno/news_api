from app import app
from .models import Sources, Articles, Headlines
from newsapi import NewsApiClient

key = app.config['API_KEY']
newsapi = NewsApiClient(api_key = key)

def sources():
    '''
    function to get all news sources in a list in English
    '''
    data = newsapi.get_sources(language = 'en', country = 'us')
    data_list = data['sources']
    source_list = []
    for item in data_list:
        new_source = Sources(item['name'], item['description'], item['url'])
        source_list.append(new_source)

    return source_list