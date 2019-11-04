from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# from bson.objectid import ObjectId
import os
from datetime import datetime
from src.histogram import *
from src.sample import * 

# local deployment
# client = MongoClient()
# db = client.Playlister # replace Playlister with database name
# playlists = db.playlists # replace playlists with collection name

app = Flask(__name__)

@app.route('/')
def index():
    words_list = get_words('text/test.txt')
    random_word = sample(words_list)
    return render_template('index.html', word=random_word)

if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('PORT', 5000))