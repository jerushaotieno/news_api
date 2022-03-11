import os

class Config:
    '''
    '''
    # pass
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'

    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProductionConfig(Config):
    '''
    '''
    pass


class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True 

config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
} 