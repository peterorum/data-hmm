#!/usr/bin/python3

import os
# import re
# import sys
import json
import pprint

import twitter

# import pudb
# pu.db

# ---- retweet


def retweet(topic):
    search_results = twit.search.tweets(q=topic, lang='en', result_type='popular')
    # print('search_results')
    # pp.pprint(search_results)

    min_retweets = 500

    texts = [{'id': tweet['id_str'], 'text': tweet['text'], 'retweets': tweet['retweet_count'], 'favorites': tweet['favorite_count']}
             for tweet in search_results['statuses'] if tweet['retweet_count'] >= min_retweets]
    # print(texts)

    if len(texts) > 0:
        # sort by retweet count
        texts = sorted(texts, key=lambda t: t['retweets'], reverse=True)
        pp.pprint(texts)

        # take most retweeted
        result = {'retweets': texts[0]['retweets'], 'favorites': texts[0]['favorites'], 'id': texts[0]['id']}

        return result
    else:
        print('nothing to retweet')


def get_location_trend(location, australia_trends_set, topic_history):
    found = False

    location_trends = twit.trends.place(_id=location['woeid'])
    print(location['name'])
    print(json.dumps(location_trends, indent=4))

    location_trends_set = set([trend['name'] for trend in location_trends[0]['trends']])
    common_trends = location_trends_set.intersection(australia_trends_set)

    print('common')
    pp.pprint(common_trends)

    new_trends = common_trends.difference(set(topic_history))

    print('new')
    pp.pprint(new_trends)

    if len(new_trends) > 0:
        found = True
        # pick first
        trend = [t for t in new_trends][0]

        # retweet the most popular
        retweet_result = retweet(trend)

        if retweet_result is not None:
            tweet = 'Trending in Australia and ' + location['name'] + ': ' + trend

            print(tweet)

            # add trend to history

            topic_history.append(trend)

            # save n last
            with open(history_filename, 'w') as out_file:
                out_file.write('\n'.join(topic_history[-history_count:]))

            tweet = tweet + '. ' + str(retweet_result['retweets']) + \
                " retweets and " + str(retweet_result['favorites']) + " favorites so far."

            print(tweet)

            # tweet
            result = twit.statuses.update(status=tweet)
            pp.pprint(result)

            # retweet
            rtresult = twit.statuses.retweet(id=retweet_result['id'])
            pp.pprint(rtresult)

    return found

#---- global
pp = pprint.PrettyPrinter(indent=4)
auth = twitter.oauth.OAuth(os.environ['tw_hmm_oauth_token'], os.environ['tw_hmm_oauth_token_secret'], os.environ[
    'tw_hmm_consumer_key'], os.environ['tw_hmm_consumer_secret'])
twit = twitter.Twitter(auth=auth)

# tweet the first topic not in the last 24 topics tweeted
history_count = 24
history_filename = 'history.txt'


#---- main

def main():

    topic_history = []

    if os.path.isfile(history_filename):
        with open(history_filename, 'rU') as in_file:
            topic_history = in_file.read().split('\n')

    print('history')
    pp.pprint(topic_history)

    #---- start

    # keep to 15 for rate limit
    locations = [
        {'name': 'The World', 'woeid': 1},
        {'name': 'the USA', 'woeid': 23424977},
        {'name': 'the UK', 'woeid': 23424975},
        {'name': 'Canada', 'woeid': 23424775},
        {'name': 'Ireland', 'woeid': 23424803},
        {'name': 'South Africa', 'woeid': 23424942},
        {'name': 'France', 'woeid': 23424819},
        {'name': 'Germany', 'woeid': 23424829},
        {'name': 'Italy', 'woeid': 23424853},
        {'name': 'Spain', 'woeid': 23424950},
        {'name': 'Denmark', 'woeid': 23424796}
    ]

    AUSTRALIA_WOE_ID = 23424748

    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special case keyword argument.

    australia_trends = twit.trends.place(_id=AUSTRALIA_WOE_ID)
    australia_trends_set = set([trend['name'] for trend in australia_trends[0]['trends']])

    print('australia')
    print(json.dumps(australia_trends, indent=4))

    # try until a trend is found
    for location in locations:
        if get_location_trend(location, australia_trends_set, topic_history):
            break

# execute
main()
