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
    try:
        with open(sys.argv[2]) as f:
            for line in f:
                data.append(json.loads(line))
            for item in data:
                if 'text' in item:
                    tweet.append(item['text'])
    except (IOError, OSError) as e:
         sys.exit('Could not open file %s' % sys.argv[2])
        
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
    if len(sys.argv) < 3:
        sys.exit('Usage: %s AFFIN-111.txt output.txt' % sys.argv[0])
    try:
        sent_file = open(sys.argv[1])
    except:
        sys.exit('Could not open file %s' % sys.argv[1])

    affin = affin_parse(sent_file)
    tweets = tweet_parse()
    get_sentiment(affin, tweets)
    
if __name__ == '__main__':
    main()
