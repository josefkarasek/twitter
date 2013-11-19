#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re

'''
Script to determine how many times a word is in one tweet
'''


def tweet_parse():
    '''
    Parse JSON tweets
    Returns list of parsed tweets and all metadata
    '''
    data = []
    tweet = []
    try:
        with open(sys.argv[1]) as f:
            for line in f:
                data.append(json.loads(line))
            for item in data:
                if 'text' in item:
                    tweet.append(item['text'])
    except (IOError, OSError) as e:
         sys.exit('Could not open file %s' % sys.argv[1])
        
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
    if len(sys.argv) < 2:
        sys.exit('Usage: %s output.txt' % sys.argv[0])
    tweets = tweet_parse()
    get_frequency(tweets)
    
if __name__ == '__main__':
    main()
