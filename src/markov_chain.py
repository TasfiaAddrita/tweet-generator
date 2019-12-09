from .dictogram import Dictogram
from .queue import Queue
import sys
import random

'''
STRETCH CHALLENGES
- Handle beginning and end of sentences with special start and stop tokens
'''

class MarkovChain(Dictogram):
    def __init__(self, n=1):
        super(MarkovChain, self).__init__()  
        self.n = n
        
    def build_state_histogram(self, words_list):
        tokens = Queue(words_list[0:self.n])
        for index in range(self.n-1, len(words_list)):
            if tokens not in self:
                self[tuple(tokens)] = Dictogram()
            try:
                self[tuple(tokens)].add_count(words_list[index + 1])
                tokens.enqueue(words_list[index + 1])
            except:
                self[tuple(tokens)] = Dictogram(['**STOP**'])
            tokens.dequeue()

    def get_next_word(self, tokens):
        return self[tokens].sample()

    def build_sentence(self, num_words, words_list):
        self.build_state_histogram(words_list)
        sentence = []
        first_words = random.choice(list(self.keys()))
        tokens = Queue(first_words)
        sentence.extend(first_words)
        total_words = len(first_words)

        while total_words < num_words:
            next_word = self.get_next_word(tuple(tokens.items()))
            if next_word == '**STOP**':
                sentence.append(next_word)
                break
            sentence.append(next_word)
            tokens.dequeue()
            tokens.enqueue(next_word)
            total_words += 1
        return ' '.join(sentence)
