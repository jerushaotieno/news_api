import unittest
from models import Sources

class TestSources(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_source = Sources('Reuters', 'Breaking International News & Views', 'https://www.reuters.com/')

    def test_source(self):
        '''
        test to create a new instance
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init(self):
        '''
        test to check on correct news source picked
        '''
        self.new_source.sourceName = 'Reuters'
        self.new_source.sourceDescription = 'Breaking International News & Views'
        self.new_source.sourceUrl = 'https://www.reuters.com/'

if __name__ == '__main__':
    unittest.main() 