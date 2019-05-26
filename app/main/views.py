from flask import render_template
from app import app
# Creating our views 
@app.route('/')
def index ():
    '''
    View root function that renders the index page
    '''
    tittle = 'Home-Welcome to the home of Pitchori'
    return render_template ('index.html',title=title)