#!/usr/bin/python

import json
from prettytable import PrettyTable # pip install prettytable

connections_data = '/tmp/linkedin-connections.json'

connections = json.loads(open(connections_data).read())

pt = PrettyTable(field_names=['Name', 'Location'])

pt.align = 'l'

[ pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name']))
  for c in connections['values']
      if c.has_key('location')]

print pt
