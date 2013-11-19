#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json
'''
Short demo on how to get tweets and print them out
'''

for i in range(10):
    page = i + 1
#     print "---PAGE:", page
    url = "http://search.twitter.com/search.json?q=microsoft&page=" + str(page)
    response = urllib.urlopen(url)
    tweet = json.load(response)
    results = tweet['results']
    
    for j in range(len(results)):
#         print "-----TWEET:", j+1
        print results[j]['text'].encode('utf-8')