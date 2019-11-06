import random
import re
import string

def get_words(source_text):
    text = open(source_text)
    story = text.read()
    text.close()

    # regex help https://stackoverflow.com/a/13184791/12049271
    delimiters = ' ', '\n'
    regex_pattern = '|'.join(map(re.escape, delimiters))
    words = re.split(regex_pattern, story)
    words = list(filter(None, [word.strip(string.punctuation).lower() for word in words]))
    return words

def histogram_dict(words):
    histogram = {}
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram

def get_word_distribution(words_list):
    histo = histogram_dict(words_list)
    word_distribution = {}
    range_start = 0
    for word in histo:
        freq_percent = histo[word] / len(words_list)
        word_distribution[word] = [range_start, range_start + freq_percent]
        range_start += freq_percent
    
    return word_distribution

def sample(word_distribution):
    ran_num = random.random()
    for word in word_distribution:
        if word_distribution[word][0] <= ran_num <= word_distribution[word][1]:
            return word
