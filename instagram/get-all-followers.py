#!/usr/local/bin/python3

import os
# import re
import sys
# import json
import pickle
from pprint import pprint

from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError

access_token = os.environ['instagram_access_token']
client_secret = os.environ['instagram_access_token']

api = InstagramAPI(access_token=access_token, client_secret=bytearray(client_secret, 'utf-8'))

#---- main


def main():

    tags = ['qantasinstaper', 'qantasinstadrw', 'qantasinstabne', 'qantasinstasyd',
            'qantasinstacbr', 'qantasinstamel', 'qantasinstahba', 'qantasinstaadl', 'qantasinstaulu']

    photographers = set()

    for tag in tags:
        with open('data/tag-' + tag + '-media.data', 'rb') as in_file:
            photos = pickle.load(in_file)

            for photo in photos:
                photographers.add(photo.user.id)

    for photographer in photographers:
        user = api.user(user_id=photographer)
        # pprint(vars(user))
        pprint("{},{}".format(user.username, user.counts['followed_by']))

#------------------ main
main()

print("Remaining API Calls = %s/%s" %
      (api.x_ratelimit_remaining, api.x_ratelimit))


sys.exit()
