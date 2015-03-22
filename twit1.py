#!/usr/local/bin/python3

import os
# import sys
import pprint
import json
import twitter

pp = pprint.PrettyPrinter(indent=4)

auth = twitter.oauth.OAuth(os.environ['tw_hmm_oauth_token'], os.environ['tw_hmm_oauth_token_secret'], os.environ['tw_hmm_consumer_key'], os.environ['tw_hmm_consumer_secret'])

twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
SYDNEY_WOE_ID = 1105779

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
sydney_trends = twitter_api.trends.place(_id=SYDNEY_WOE_ID)

print(json.dumps(world_trends, indent=4))
print(json.dumps(sydney_trends, indent=4))

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
sydney_trends_set = set([trend['name'] for trend in sydney_trends[0]['trends']])
common_trends = world_trends_set.intersection(sydney_trends_set)

print('world')
pp.pprint(world_trends_set)

print('sydney')
pp.pprint(sydney_trends_set)

print('common')
pp.pprint(common_trends)

