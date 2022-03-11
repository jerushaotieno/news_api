class Sources:
    '''
    '''
    def __init__(self, id, name, description, url, category, language, country):
        '''
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Articles:
    '''
    '''
    def __init__(self, article_title, article_author, article_description, article_url, article_url_to_image, article_published_at):
        '''
        '''
        self.article_title = article_title
        self.article_author = article_author
        self.article_description = article_description
        self.article_url = article_url
        self.article_url_to_image = article_url_to_image
        self.article_published_at = article_published_at

class Headlines:
    '''
    '''
    def __init__(self, article_title, article_url_to_image, article_url):
        '''
        '''
        self.article_title = article_title
        self.article_url_to_image = article_url_to_image
        self.article_url = article_url