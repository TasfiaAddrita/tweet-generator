import random
# import histogram
from src.histogram import histogram_dict
import sys

def random_word(source_text):
    words_list = histogram.get_words(source_text)
    return random.choice(words_list)

def get_freq_percent(word_occurance):
    return word_occurance / len(words_list)

def get_word_distribution(words_list):
    histo = histogram_dict(words_list)
    word_distribution = {}
    range_start = 0
    for word in histo:
        # freq_percent = get_freq_percent(histo[word])
        freq_percent = histo[word] / len(words_list)
        word_distribution[word] = [range_start, range_start + freq_percent]
        range_start += freq_percent
    
    return word_distribution

def sample(words_list):
    word_distribution = get_word_distribution(words_list)
    ran_num = random.random()
    for word in word_distribution:
        if word_distribution[word][0] <= ran_num <= word_distribution[word][1]:
            return word

def test(words_list):
    test = []
    word_distribution = get_word_distribution(words_list)
    print(word_distribution, '\n')
    for _ in range(1000):
        test.append(sample(words_list))
    hist_ran_words = histogram.histogram_dict(test)
    print(hist_ran_words, '\n')
    for word in hist_ran_words:
        print(word, 'test', hist_ran_words[word]/1000, 'dist', round(get_freq_percent(histogram.histogram_dict(words_list)[word]), 3))    
    return

if __name__ == '__main__':

    # words_list = histogram.get_words('test.txt')
    # test(words_list)

    params = sys.argv[1:]
    words_list = histogram.get_words(params[0])
    # print(sample(words_list))
    print(test(words_list))

# ------ bad code ------
# def get_freq_percent(word_occurance):
#     return round(word_occurance / len(words_list) * 100)

# def get_word_distribution(words_list):
#     histo = histogram.histogram_dict(words_list)
#     word_distribution = {}
#     range_start = 0
#     for word in histo:
#         freq_percent = get_freq_percent(histo[word])
#         word_distribution[word] = (freq_percent, list(range(range_start, range_start + freq_percent + 1)))
#         range_start += freq_percent
    
#     # print(word_distribution)
#     return word_distribution

# def sample(words_list):
#     word_distribution = get_word_distribution(words_list)

#     ran_num = random.randint(0, 100)
#     for word in word_distribution:
#         if ran_num in word_distribution[word][1]:
#             return word
#         # else:
#         #     return (None, ran_num) # ask Alan why expression doesn't think ran_num is in word_distribution