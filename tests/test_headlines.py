import unittest
from app.models import Headlines

class SourcesTest(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.top_article = Headlines('U.S. Democrats stockpile lawyers, money to fight Republican voting laws', 'https://www.reuters.com/resizer/xVoQlAc2_v4fDEVQSj-QDckqaP0=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/RERKAQVAVBIJRCUE7R33MCP77M.jpg', 'https://www.reuters.com/world/us/us-democrats-stockpile-lawyers-money-fight-republican-voting-laws-2022-02-27/')

    def test_source(self):
        '''
        test for creation of a new instance
        '''
        self.assertTrue(isinstance(self.top_article, Headlines))

    def test_init(self):
        '''
        '''
        self.top_article.article_title = 'U.S. Democrats stockpile lawyers, money to fight Republican voting laws'
        self.top_article.article_url_to_image='https://www.reuters.com/resizer/xVoQlAc2_v4fDEVQSj-QDckqaP0=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/RERKAQVAVBIJRCUE7R33MCP77M.jpg'
        self.top_article.article_url='https://www.reuters.com/world/us/us-democrats-stockpile-lawyers-money-fight-republican-voting-laws-2022-02-27/'