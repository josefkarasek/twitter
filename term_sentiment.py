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
#             if item['lang'] == 'en':
            tweet.append(item['text'])
    f.close()
    return tweet

def get_sentiment(affin, tweets):
    new_dict = {}
    appereances = {}
    for tweet in tweets:
        missed = []
#         print tweet.encode('UTF-8')
        sentiment = 0
        splited = tweet.split(' ')
        for word in splited:
            if word in affin:
#                 print word
                sentiment += affin[word]
            else:
                missed.append(word)
                
        for word in missed:
            if word in new_dict:
#                 print word.encode('UTF-8')
                if word in appereances:
                    appereances[word.lower()] += 1
                else:
                    appereances[word.lower()] = 1
                new_dict[word.lower()] += sentiment
            else:
                new_dict[word.lower()] = sentiment
#         print sentiment
        
    for word in appereances.items():
        new_dict[word[0]] /= word[1]
    for item in new_dict.items():
        print item[0].encode('UTF-8'), item[1]
#     print new_dict
#     print appereances
    
def main():
    sent_file = open(sys.argv[1])
    affin = affin_parse(sent_file)
    tweets = tweet_parse()
    get_sentiment(affin, tweets)
    
if __name__ == '__main__':
    main()