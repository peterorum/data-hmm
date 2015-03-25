#!/usr/bin/python3

import os
import re
# import sys
import pprint
import json
import twitter

#import pudb
#pu.db

pp = pprint.PrettyPrinter(indent=4)

auth = twitter.oauth.OAuth(os.environ['tw_hmm_oauth_token'], os.environ['tw_hmm_oauth_token_secret'], os.environ['tw_hmm_consumer_key'], os.environ['tw_hmm_consumer_secret'])

twit = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
#SYDNEY_WOE_ID = 1105779
AUSTRALIA_WOE_ID = 23424748

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twit.trends.place(_id=WORLD_WOE_ID)
australia_trends = twit.trends.place(_id=AUSTRALIA_WOE_ID)

#print(json.dumps(world_trends, indent=4))
#print(json.dumps(australia_trends, indent=4))

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
australia_trends_set = set([trend['name'] for trend in australia_trends[0]['trends']])
common_trends = world_trends_set.intersection(australia_trends_set)

print('world')
pp.pprint(world_trends_set)

print('australia')
pp.pprint(australia_trends_set)

print('common')
pp.pprint(common_trends)

if len(common_trends) > 0:
    tweet = 'Trending in Australia and The World: '

    for x in common_trends:
        if len(tweet) + len(x) + 2 <= 140:
            tweet += x + ', '

    tweet = re.compile(', $').sub('', tweet)

    print(tweet)

    lasttweet = ''
    filename = 'last-tweet.txt'

    if os.path.isfile(filename):
        f = open(filename, 'r')
        lasttweet = f.read()
        f.close()

    if lasttweet.lower() != tweet.lower():
        f = open(filename, 'w')
        f.write(tweet)
        f.close()

        result = twit.statuses.update(status=tweet)
        pp.pprint(result)

