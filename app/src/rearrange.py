import sys
from random import randint

def fisher_yates(list_):
    last_index = len(list_) - 1
    while last_index > 0:
        random_index = randint(0, last_index)
        temp = list_[random_index]
        list_[random_index] = list_[last_index]
        list_[last_index] = temp
        
        last_index -= 1
    
    return list_

# def random_params(params_list):
#     return fisher_yates(params_list)

def reverse_word(word):
    # return word[::-1]
    reverse = ""
    for letter in range(len(word), 0, -1):
        reverse += letter
    return reverse

def reverse_sentences(sen_list):
    reverse = []
    for word in range(len(sen_list), 0, -1):
        reverse.append(sen_list[word-1])
    return reverse

def anagram(word):
    ana_list = []
    ana_word = ""
    for first_letter in range(len(word)):
        ana_word += word[first_letter]
        for other_letters in range(len(word)):
            if other_letters != first_letter:
                ana_word += word[other_letters]
        ana_list.append(ana_word)
        ana_word = ""
    return ana_list

params = sys.argv[1:]
# # print(params)

ran_params = fisher_yates(params)
ran_params_string = ""
for param in ran_params:
    ran_params_string += str(param) + " "
print(ran_params_string)

# rev_word = reverse_word(ran_params[randint(0, len(ran_params) - 1)])
# print(rev_word)

# rev_sen = reverse_sentences(ran_params)
# print(rev_sen)

# ana_word = anagram("randomize")
# print(ana_word)