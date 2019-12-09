from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# from bson.objectid import ObjectId
import os
from datetime import datetime
from src import util
from src import markov_chain

# local deployment
# client = MongoClient()
# db = client.Playlister # replace Playlister with database name
# playlists = db.playlists # replace playlists with collection name

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_sentence():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        num_words = request.form.get('num')
        if num_words == '':
            num_words = 1
        else:
            num_words = int(num_words)
        text = './corpus/three_wishes.txt'
        words_list = util.get_words(text)
        markov = markov_chain.MarkovChain(4)
        return render_template('index.html', sentence=markov.build_sentence(num_words, words_list))

if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('PORT', 5000))