import sys
from random import randint, choice, randrange
import time

def time_it(func):
    # Made wth love by Ben :heart: - DS2.3
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str((end - start) * 10000) + ' ms\n')
        return result
    return wrapper

def get_dict_words():
    f = open('/usr/share/dict/words')
    word_list = f.readlines()
    word_list = [word.strip() for word in word_list]
    f.close()
    return word_list

@time_it
def random_words(num_words):
    word_list = get_dict_words()
    
    ran_words = []
    dict_words = 0
    while dict_words < int(num_words):
        # ran_words.append(word_list[randint(0, len(word_list)-1)])
        ran_words.append(word_list[randrange(len(word_list))])
        dict_words += 1

    return ' '.join(ran_words)

params = sys.argv[1:]
print(random_words(params[0]))