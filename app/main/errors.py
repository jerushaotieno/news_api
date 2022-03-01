from flask import render_template
from . import main

@main.app.errorhandler(404)
def not_found(errors):
    '''
    '''
    return render_template('errors.html'), 404 