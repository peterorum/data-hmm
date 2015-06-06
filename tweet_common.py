#!/usr/bin/python3

import os
#import re
import sys
#import json
import pprint

import twitter

#import pudb
#pu.db

# ---- retweet

def retweet(topic):
    search_results = twit.search.tweets(q=topic, lang='en')
    #print('search_results')
    #pp.pprint(search_results)

    texts = [{'id': tweet['id_str'], 'text': tweet['text'], 'retweets': tweet['retweet_count']} for tweet in search_results['statuses']]
    #print(texts)

    if len(texts) > 0:
        # sort by retweet count
        texts = sorted(texts, key=lambda t: t['retweets'], Reverse=True)
        pp.pprint(texts)

        #take most retweeted
        retweet_id = texts[0]['id']

        # retweet
        rtresult = twit.statuses.retweet(id=retweet_id)
        pp.pprint(rtresult)
    else:
        print('nothing to retweet')


#---- main

pp = pprint.PrettyPrinter(indent=4)

auth = twitter.oauth.OAuth(os.environ['tw_hmm_oauth_token'], os.environ['tw_hmm_oauth_token_secret'], os.environ['tw_hmm_consumer_key'], os.environ['tw_hmm_consumer_secret'])

twit = twitter.Twitter(auth=auth)

#---- start

WORLD_WOE_ID = 1
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

# tweet the first topic not in the last 24 topics tweeted
history_count = 24
history_filename = 'history.txt'

topic_history = []

if os.path.isfile(history_filename):
    with open(history_filename, 'rU') as in_file:
        topic_history = in_file.read().split('\n')

print('history')
pp.pprint(topic_history)

new_trends = common_trends.difference(set(topic_history))

print('new')
pp.pprint(new_trends)

if len(new_trends) > 0:
    # pick first
    trend = [t for t in new_trends][0]

    tweet = 'Trending in Australia and The World: ' + trend

    print(tweet)

    # add trend to history

    topic_history.append(trend)

    # save n last
    with open(history_filename, 'w') as out_file:
        out_file.write('\n'.join(topic_history[-history_count:]))

    #tweet
    result = twit.statuses.update(status=tweet)
    pp.pprint(result)

    # retweet the most popular
    retweet(trend)

