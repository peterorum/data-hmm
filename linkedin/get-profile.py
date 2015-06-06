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

profile = app.get_profile()

profile_file = '/tmp/linkedin-profile.json'

f = open(profile_file, 'w')
f.write(json.dumps(profile, indent=1))
f.close()
