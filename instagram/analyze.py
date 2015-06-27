#!/usr/bin/python

#import os
#import re
import sys
#import json
import pickle
from pprint import pprint

from instagram.client import InstagramAPI

#---- main

def main():

    with open('photos.txt', 'r') as in_file:
        photos = pickle.load(in_file)

    pprint(photos)
    pprint(photos[0].caption.text)

#------------------ main
main()

sys.exit()
