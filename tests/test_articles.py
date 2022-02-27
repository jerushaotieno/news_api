import unittest
from models import Articles

class TestArticles(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_article=Articles('U.S. Democrats stockpile lawyers, money to fight Republican voting laws', 'Trevor Hunnicutt', 'https://www.reuters.com/world/us/us-democrats-stockpile-lawyers-money-fight-republican-voting-laws-2022-02-27/', 'https://www.reuters.com/resizer/xVoQlAc2_v4fDEVQSj-QDckqaP0=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/RERKAQVAVBIJRCUE7R33MCP77M.jpg', '2022-02-27 4:21 PM GMT+3')

    def test_instance(self):
        '''
        '''
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_init(self):
        '''
        '''
        self.new_article.title = 'U.S. Democrats stockpile lawyers, money to fight Republican voting laws'
        self.new_article.author = 'Trevor Hunnicutt'
        self.new_article.url = 'https://www.reuters.com/world/us/us-democrats-stockpile-lawyers-money-fight-republican-voting-laws-2022-02-27/'
        self.new_article.url_to_image = 'https://www.reuters.com/resizer/xVoQlAc2_v4fDEVQSj-QDckqaP0=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/RERKAQVAVBIJRCUE7R33MCP77M.jpg'
        self.new_article.published_at = '2022-02-27 4:21 PM GMT+3'

if __name__ == '__main__':
    unittest.main() 