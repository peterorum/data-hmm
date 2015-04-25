#!/usr/bin/python


from linkedin import linkedin # pip install python-linkedin

import logging
logging.captureWarnings(True)

import json

CONSUMER_KEY = '75o845gcado4hw'
CONSUMER_SECRET = 'dqrhOX2MSdraWSfT'
USER_TOKEN = '65f2dbc1-2521-44b6-8053-e2c8aa4c5978'
USER_SECRET = '31901047-d3b4-44ed-a263-91875f260db9'

RETURN_URL = '' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, permissions=linkedin.PERMISSIONS.enums.values())

app = linkedin.LinkedInApplication(auth)

#app.get_profile()

connections = app.get_connections()

connections_data = '/tmp/linkedin-connections.json'

f = open(connections_data, 'w')
f.write(json.dumps(connections, indent=1))
f.close()

