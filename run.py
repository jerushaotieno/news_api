from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "News Homepage"

@app.route('/sources')
def sources():
    return "Source News Articles"

from app import app

if __name__ == "__main__":
    app.run(debug=True)
