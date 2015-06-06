#!/usr/bin/python

import nltk

ceo_bigrams = nltk.bigrams("Chief Executive Officer".split(), pad_right=True,
                                                              pad_left=True)

cto_bigrams = nltk.bigrams("Chief Technology Officer".split(), pad_right=True,
                                                               pad_left=True)

print list(ceo_bigrams)
print list(cto_bigrams)

ceo_bigrams = nltk.bigrams("Chief Executive Officer".split(), pad_right=True,
                                                              pad_left=True)

cto_bigrams = nltk.bigrams("Chief Technology Officer".split(), pad_right=True,
                                                               pad_left=True)

print len(set(ceo_bigrams).intersection(set(cto_bigrams)))