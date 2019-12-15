# -*- coding: utf-8 -*-
import os.path
import collections
from operator import itemgetter
import csv 
​
class Autocorrect(object):
    def __init__(self, ngram_size=3, len_variance=1):
        self.ngram_size = ngram_size
        self.len_variance = len_variance
​        
        # Add words file here
        wordfile = os.path.join(os.path.dirname(__file__), "words")
        self.words = set(open(wordfile).read().splitlines())
​
        # create dictionary of ngrams and the words that contain them
        self.ngram_words = collections.defaultdict(set)
        for word in self.words:
            for ngram in self.ngrams(word):
                self.ngram_words[ngram].add(word)
        print ("Generated {} ngrams from {} words".format((len(self.ngram_words), len(self.words))))
​
    def exists(self, word):
        "Return True if the word exists in the dictionary."
        return word in self.words
​
    def ngrams(self, word):
        "Return the set of unique ngrams in that word."
        all_ngrams = set()
        for i in range(0, len(word) - self.ngram_size + 1):
            all_ngrams.add(word[i:i + self.ngram_size])
        return all_ngrams
​
    def probabilitic_wp(self, target_word, results=5):
        "Return a list of possible corrections."
        rank = collections.defaultdict(int)
        for ngram in self.ngrams(target_word):
            words = self.ngram_words[ngram]
            for word in words:
                # closest matching length with offset len_variance
                if len(word) >= len(target_word) - self.len_variance and \
                   len(word) <= len(target_word) + self.len_variance:
                    rank[word] += 1
        # Most probablistic
        ranked_word_pairs = sorted(rank.iteritems(), key=itemgetter(1), reverse=True)
        return [word_pair[0] for word_pair in ranked_word_pairs[0:results]]
​
​
if __name__ == '__main__':
    autocorrect = Autocorrect()
    
    while True:
        word = input()
        if autocorrect.exists(word):
            pass
        else:
            suggestions = autocorrect.probabilitic_wp(word)
            print ("Did you mean? ", suggestions)