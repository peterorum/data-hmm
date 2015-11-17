#!/usr/local/bin/python3

import os
# import re
import sys
# import json
import pickle
import urllib
from pprint import pprint

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError

access_token = os.environ['instagram_access_token']
client_secret = os.environ['instagram_access_token']

api = InstagramAPI(access_token=access_token, client_secret=bytearray(client_secret, 'utf-8'))


def tag_search(tag):

    try:
        results = api.tag_search(q=tag)[0]

        if (len(results) > 0):
            tag1 = results[0]
            pprint(vars(tag1))

            photos = []

            recent_media, next = api.tag_recent_media(tag_name=tag1.name, count=100)

            # pprint(next)

            for media in recent_media:
                photos.append(media)

            while next:
                query = urllib.parse.urlparse(next).query
                max_tag_id = urllib.parse.parse_qs(query)['max_tag_id'][0]

                recent_media, next = api.tag_recent_media(tag_name=tag1.name, count=100, max_tag_id=max_tag_id)

                for media in recent_media:
                    photos.append(media)

            with open('data/tag-' + tag + '-media.data', 'wb') as out_file:
                pickle.dump(photos, out_file)

    except InstagramAPIError as e:
        print(e)

#---- main


def main():

    tags = [
        'qantasinstaper', 'qantasinstadrw', 'qantasinstabne', 'qantasinstasyd',
        'qantasinstacbr', 'qantasinstamel', 'qantasinstahba', 'qantasinstaadl', 'qantasinstaulu',
        'qantasinstawello', 'qantasinstactl', 'qantasinstasun',
        'qantasinstameet',
        'qantasinstameetper', 'qantasinstameetdrw', 'qantasinstameetbne', 'qantasinstameetsyd',
        'qantasinstameetcbr', 'qantasinstameetmel', 'qantasinstameethba', 'qantasinstameetadl', 'qantasinstameetulu',
        'qantasinstameetwello', 'qantasinstameetctl', 'qantasmeetinstasun'
    ]

    for tag in tags:
        tag_search(tag)

    print("Remaining API Calls = %s/%s" %
          (api.x_ratelimit_remaining, api.x_ratelimit))


#------------------ start

main()

sys.exit()
