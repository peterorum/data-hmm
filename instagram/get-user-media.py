#!/usr/bin/python3

import os
#import re
import sys
#import json
import pickle
from pprint import pprint

from instagram.client import InstagramAPI

access_token = os.environ['instagram_access_token']
client_secret = os.environ['instagram_access_token']

api = InstagramAPI(access_token=access_token, client_secret=bytearray(client_secret, 'utf-8'))


def get_user_media(username):

    users = api.user_search(q=username)
    user = users[0]
    pprint(vars(user))

    return

    recent_media, next_url = api.user_recent_media(user_id=user.id, count=10)

    photos = []

    while True:
        for media in recent_media:
            photos.append(media)

        if next_url:
            recent_media, next_url = api.user_recent_media(with_next_url=next_url)
        else:
            break

    # pprint(photos)
    # pprint(len(photos))

    with open('data/' + username + '-media.data', 'wb') as out_file:
        pickle.dump(photos, out_file)


#---- main

def main():

    get_user_media('peterorum')

#------------------ start

main()

sys.exit()
