#!/usr/bin/python3

#import os
#import re
import sys
#import json
import pickle
from pprint import pprint

#---- main

def main():

    with open('photos.data', 'rb') as in_file:
        photos = pickle.load(in_file)

    pprint(photos)
    pprint(photos[0].caption.text)

#------------------ main
main()

sys.exit()
