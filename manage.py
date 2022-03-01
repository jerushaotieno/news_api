# from unicodedata import name
from app import create_app
from flask_script import Manager, Server
# app = Flask(__name__)

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)
@manager.command

def test():
    '''
    Run unit tests
    '''
    
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()

@app.route('/')
def index():
    return "News Homepage"

@app.route('/sources')
def sources():
    return "Source News Articles"

from app import app

if __name__ == "__main__":
    app.run()
