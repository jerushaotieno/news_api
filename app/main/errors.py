from flask import render_template
from app import app

@app.errorhandler(404)
def not_found(errors):
    '''
    '''
    return render_template('errors.html'), 404 