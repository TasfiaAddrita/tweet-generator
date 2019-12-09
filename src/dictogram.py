#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random

class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        if word not in self:
            self[word] = count
            self.types += 1
        else:
            self[word] += count
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        if word not in self:
            return 0
        return self[word]

    
    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        word_distribution = {}
        range_start = 0
        for word in self:
            freq_percent = self[word] / self.tokens
            word_distribution[word] = [range_start, range_start + freq_percent]
            range_start += freq_percent

        ran_num = random.random()
        for word in word_distribution:
            if word_distribution[word][0] <= ran_num <= word_distribution[word][1]:
                return word
