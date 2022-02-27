class Sources:
    '''
    '''
    def __init__(self, source_id, source_name, source_description, source_url):
        '''
        '''
        self.source_id = source_id
        self.source_name = source_name
        self.source_description = source_description
        self.source_url = source_url

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