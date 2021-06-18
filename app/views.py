from flask import render_template
from app import app
from .request import get_quotes

#Views
@app.route("/")
def index():
    #Getting our quotes
    quotes = get_quotes()
    return render_template("index.html",quotes=quotes)