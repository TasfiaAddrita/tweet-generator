from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# from bson.objectid import ObjectId
import os
from datetime import datetime
from src.sample import * 

# local deployment
# client = MongoClient()
# db = client.Playlister # replace Playlister with database name
# playlists = db.playlists # replace playlists with collection name

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def random_words(words=[]):
    if request.method == 'GET':
        return render_template('index.html')
    else:
        num_words = request.form.get('num')
        if num_words == '':
            num_words = 1
        else:
            num_words = int(num_words)
        word_distribution = get_word_distribution(get_words('text/test.txt'))
        random_words_list = []
        for _ in range(num_words):
            random_word = sample(word_distribution)
            random_words_list.append(random_word)
        return render_template('index.html', words_list=random_words_list)

if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('PORT', 5000))