#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re

    
def affin_parse(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def tweet_parse():
    data = []
    tweet = []
    with open(sys.argv[2]) as f:
        for line in f:
            data.append(json.loads(line))
        for item in data:
            tweet.append(item['text'])
    f.close()
    return tweet

def get_sentiment(affin, tweets):
    for tweet in tweets:
#         print tweet.encode('UTF-8')
        sentiment = 0
        splited = tweet.split(' ')
        for word in splited:
            if word in affin:
#                 print word
                sentiment += affin[word]
        print sentiment
    
def main():
    sent_file = open(sys.argv[1])
    affin = affin_parse(sent_file)
    tweets = tweet_parse()
    get_sentiment(affin, tweets)
    
if __name__ == '__main__':
    main()
