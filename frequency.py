#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re



def tweet_parse():
    data = []
    tweet = []
    with open(sys.argv[1]) as f:
        for line in f:
            data.append(json.loads(line))
        for item in data:
            tweet.append(item['text'])
    f.close()
    return tweet

def get_frequency(tweets):
    frq = 0
    number_of_terms = 0
    terms = {}
    for tweet in tweets:
        splited = tweet.split(' ')
        for word in splited:
           if word.lower() in terms:
               terms[word.lower()] += 1
               number_of_terms += 1
           else:
               terms[word.lower()] = 1
               number_of_terms += 1
    for item in terms.items():
        terms[item[0]] = terms[item[0]] / float(number_of_terms)

    for item in terms.items():
        print item[0].strip('\r\n').encode('UTF-8'), "%.4f" % item[1]
        

        
        
               
def main():
    tweets = tweet_parse()
    get_frequency(tweets)
    
if __name__ == '__main__':
    main()