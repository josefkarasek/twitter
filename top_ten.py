#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re

'''
Script to determine top ten hashtags
'''    


def tweet_parse():
    data = []
    hashtag = []
    try:
        with open(sys.argv[1]) as f:
            for line in f:
                data.append(json.loads(line))
            for item in data:
                if 'entities' in item and 'hashtags' in item['entities']:
                    if item['entities']['hashtags']:
                        hashtag.append(item['entities']['hashtags'][0]['text'])
    except (IOError, OSError) as e:
         sys.exit('Could not open file %s' % sys.argv[1])
         
    return hashtag

def get_top(hashtags):
    top = {}
    final = []
    for hashtag in hashtags:
        if hashtag.lower() in top:
            top[hashtag.lower()] += 1
        else:
            top[hashtag.lower()] = 1
    return top

def get_top_ten(top):
    tv = sorted(top, key=top.get, reverse=True)
    for i in range(len(tv)):
        if i > 9:
            break
        if top[tv[i]]:
            print tv[i].encode('UTF-8'), top[tv[i]]

    
def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s output.txt' % sys.argv[0])
    hashtags = tweet_parse()
    top = get_top(hashtags)
    get_top_ten(top)
    
if __name__ == '__main__':
    main()