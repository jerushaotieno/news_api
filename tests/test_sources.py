import unittest
from app.models import Sources

class TestSources(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_source = Sources('reuters', 'Reuters')

    def test_source(self):
        '''
        test to create a new instance
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init(self):
        '''
        test to check on correct news source picked
        '''
        self.new_source.source_id = 'reuters'
        self.new_source.sourceName = 'Reuters'
        
# if __name__ == '__main__':
#     unittest.main() 