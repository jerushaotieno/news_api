import os

class Config:
    '''
    '''
    # pass
    SOURCE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('API_KEY')
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
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
} 