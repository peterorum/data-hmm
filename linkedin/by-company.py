#!/usr/bin/python

import os
import csv

from collections import Counter
from operator import itemgetter
from prettytable import PrettyTable

# XXX: Place your "Outlook CSV" formatted file of connections from
# http://www.linkedin.com/people/export-settings at the following
# location: resources/ch03-linkedin/my_connections.csv

CSV_FILE = os.path.join("private", 'linkedin-connections.csv')

# Define a set of transforms that converts the first item
# to the second item. Here, we're simply handling some
# commonly known abbreviations, stripping off common suffixes,
# etc.

transforms = [(', Inc.', ''), (', Inc', ''), (', LLC', ''), (', LLP', ''),
                (' LLC', ''), (' Inc.', ''), (' Inc', ''), (' AU', ''), (' Australia', ''),
                (' Pty Ltd', ''), (' Ltd', '')]

csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')

contacts = [row for row in csvReader]

companies = [c['Company'].strip() for c in contacts if c['Company'].strip() != '']

for i, _ in enumerate(companies):
    for transform in transforms:
        companies[i] = companies[i].replace(*transform)

pt = PrettyTable(field_names=['Company', 'Freq'])
pt.align = 'l'

c = Counter(companies)

[pt.add_row([company, freq])
 for (company, freq) in sorted(c.items(), key=itemgetter(1), reverse=True)
     if freq > 1]

print pt