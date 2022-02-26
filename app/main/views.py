from app import app

@app.route('/')
def index():
    return "News2 Homepage"

@app.route('/sources')
def sources():
    return "Source News Articles"