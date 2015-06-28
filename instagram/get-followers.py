#!/usr/bin/python3

import os
#import re
import sys
#import json
import pickle
from pprint import pprint

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError

access_token = os.environ['instagram_access_token']
client_secret = os.environ['instagram_access_token']

api = InstagramAPI(access_token=access_token, client_secret=bytearray(client_secret, 'utf-8'))


def get_user_followers(username):

    try:
        users = api.user_search(q=username)
        # pprint(users)
        user = users[0]
        pprint(vars(user))

        users, next_url = api.user_followed_by(user_id=user.id)

        # pprint(users)

        followers = []

        while True:
            for follower in users:
                followers.append(follower)

            pprint(len(followers))

            if next_url:
                users, next_url = api.user_followed_by(with_next_url=next_url)
            else:
                break

        # pprint(followers)

        with open('data/' + username + '-followers.data', 'wb') as out_file:
            pickle.dump(followers, out_file)

    except InstagramAPIError as e:
        print(e)


#---- main

def main():

    get_user_followers('erickimphoto')

    print("remaining api calls = %s/%s" % (api.x_ratelimit_remaining, api.x_ratelimit))

#------------------ start

main()

sys.exit()
