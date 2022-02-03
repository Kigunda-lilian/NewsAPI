from flask import render_template, render_template_string
from . import main
from ..request import fetch_news
 
 
@main.route('/')
def index():
    
    
    Habari=fetch_news()
   
    
    return render_template ('index.html',articles=Habari)