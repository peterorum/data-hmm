#!/usr/bin/python3

import os

lasttweet = ''
filename = 'last-tweet.txt'

tweet = 'helo2'

if os.path.isfile(filename):
    f = open(filename, 'r')
    lasttweet = f.read()
    f.close()

if lasttweet != tweet:
    f = open(filename, 'w')
    f.write(tweet)
    f.close()
