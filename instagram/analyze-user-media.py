#!/usr/bin/python3

# import os
# import re
import sys
# import json
import pickle
from pprint import pprint

#---- main


def main():

    with open('data/peterorum-media.data', 'rb') as in_file:
        photos = pickle.load(in_file)

    photo = photos[0]
    pprint(vars(photo))

    # to get location
    # use id to get meida info
    # look for location
    #image_id = '976907440786573124_25025320'
    #image_info = api.media(image_id)
    #lat = image_info.location.point.latitude
    #lon = image_info.location.point.longitude
    #print (lat,lon)

#------------------ main
main()

sys.exit()
