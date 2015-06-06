#!/usr/bin/python

from linkedin import linkedin # pip install python-linkedin

import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

import json

CONSUMER_KEY = '75o845gcado4hw'
CONSUMER_SECRET = 'dqrhOX2MSdraWSfT'
USER_TOKEN = '65f2dbc1-2521-44b6-8053-e2c8aa4c5978'
USER_SECRET = '31901047-d3b4-44ed-a263-91875f260db9'

RETURN_URL = '' # Not required for developer authentication

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, permissions=linkedin.PERMISSIONS.enums.values())

app = linkedin.LinkedInApplication(auth)

my_positions = app.get_profile(selectors=['positions'])

print json.dumps(my_positions, indent=1)

# Display positions for someone in your network...

# Get an id for a connection. We'll just pick the first one.
connections_data = '/tmp/linkedin-connections.json'
connections = json.loads(open(connections_data).read())

connection_id = connections['values'][0]['id']

connection_positions = app.get_profile(member_id=connection_id,
                                       selectors=['positions'])

print json.dumps(connection_positions, indent=1)