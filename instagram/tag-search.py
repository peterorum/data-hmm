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


def tag_search(tag):

    try:
        results = api.tag_search(q=tag)[0]
        tag1 = results[0]
        pprint(vars(tag1))

        recent_media = api.tag_recent_media(tag_name=tag1.name, count=10)[0]

        photos = []

        for media in recent_media:
            photos.append(media)

        # pprint(photos)
        # pprint(len(photos))

        with open('data/tag-' + tag + '-media.data', 'wb') as out_file:
            pickle.dump(photos, out_file)

    except InstagramAPIError as e:
        print(e)

    print("tag_search: Remaining API Calls = %s/%s" %
          (api.x_ratelimit_remaining, api.x_ratelimit))

#---- main


def main():

    tag_search('streetphotography')

#------------------ start

main()

sys.exit()
