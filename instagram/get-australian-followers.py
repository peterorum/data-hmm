#!/usr/bin/python3

#import os
#import re
import sys
#import json
import pickle
from pprint import pprint

#---- main


def main():

    with open('data/erickimphoto-followers.data', 'rb') as in_file:
        followers = pickle.load(in_file)

    pprint(vars(followers[0]))

#------------------ start
main()

sys.exit()
