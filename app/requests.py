from .models import Sources, Articles
import urllib.request, json
# from newsapi import NewsApiClient

# key = app.config['API_KEY']
# url = app.config['SOURCE_URL']
# newsapi = NewsApiClient(api_key = key)

# Getting api key
apiKey = None

#get base url for news api
base_url =None

article_base_url = None

def configure_request(app):
    global apiKey, base_url, article_base_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLE_API_BASE_URL']


def sources(category):
    
    '''function that gets json response to url format'''

    get_news_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''Function  that processes the movie result and transform them to a list of Objects'''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        
        news_object = Sources(id, name,  description, url, category, language, country)
        news_results.append(news_object)
    return news_results


def articles(source_id):
    '''
    function to get all English news sources in a list
    '''
    source_url = article_base_url.format(source_id, apiKey)
    with urllib.request.urlopen(source_url) as url:
        result = url.read()
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
        article_title = item.get('title')
        article_author = item.get('author')
        article_description = item.get('description')
        article_url = item.get('url')
        article_url_to_image = item.get('urlToImage')
        article_published_at = item.get('publishedAt')

        if article_url_to_image and article_url:
            new_article = Articles(article_title, article_author, article_description, article_url, article_url_to_image, article_published_at)
            article_list.append(new_article)     
    return article_list 