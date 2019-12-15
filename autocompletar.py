# -*- coding: utf-8 -*-
import simplejson as json
import sys 
from nltk.corpus import brown
import nltk
from nltk.corpus import PlaintextCorpusReader

new_corpus = PlaintextCorpusReader('./','.*')
tokens = brown.words() 

def bigram_freq(tokens):
    bgs = list(nltk.bigrams(tokens))
    return nltk.ConditionalFreqDist(bgs)

def appendwithcheck (preds, to_append):
    for pred in preds:
        if pred[0] == to_append[0]:
            return
    preds.append(to_append)

#compute frequency distribution for all the bigrams in the corpus
bgs_freq = bigram_freq(tokens)


def main():
    string = input('string')
    words=string.split()
    n=len(words)
    print (n)
    print (bgs_freq[(string)].most_common(5))

if __name__=="__main__":
    main()
