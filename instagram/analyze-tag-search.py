#!/usr/local/bin/python3

# import os
# import re
import sys
# import json
import pickle
from pprint import pprint

#---- main


def main():

    tags = ['qantasinstaper', 'qantasinstadrw', 'qantasinstabne', 'qantasinstasyd',
            'qantasinstacbr', 'qantasinstamel', 'qantasinstahba', 'qantasinstaadl', 'qantasinstaulu']

    for tag in tags:

        with open('data/tag-' + tag + '-media.data', 'rb') as in_file:
            photos = pickle.load(in_file)

            likes = 0
            photographers = set()

            for photo in photos:
                likes += photo.like_count
                photographers.add(photo.user.username)

                #pprint(tag + ', ' + photo.user.username)

            pprint("{},{},{},{}".format(tag, len(photos), likes, len(photographers)))


#------------------ main
main()

sys.exit()
