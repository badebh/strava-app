# This accomplishes the fetching of access and refresh token from Strava.
# Borrowed from examples included with requests_oauthlib on github.
from credentials import api_cred
from requests_oauthlib import OAuth2Session

client_id = api_cred.client_id
client_secret = api_cred.client_secret

auth_base_url = 'https://www.strava.com/oauth/authorize'
scope = 'read_all,profile:read_all,activity:read_all'
redirect_uri = 'https://localhost/'
token_url = 'https://www.strava.com/oauth/token'

strava = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

auth_url, state = strava.authorization_url(auth_base_url)
print('Please go here and authorize:', auth_url)

# How do I eliminate the need for copy and paste? There's another real
# world example posted on github, i'll dive in to that
redirect_response = input('Paste the full redirect url here:')

# includes access_token, refresh_token
token = strava.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

