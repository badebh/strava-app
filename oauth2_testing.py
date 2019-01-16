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

## attempt to integrate w/ strava
#import time
#import swagger_client
#from swagger_client.rest import ApiException
#from pprint import pprint

## Configure OAuth2 access token for authorization: strava_oauth
#swagger_client.configuration.access_token = token['access_token']

## create an instance of the API class
#api_instance = swagger_client.ActivitiesApi()
#id = 2069849358 # Long | The identifier of the activity.

#try: 
#    # Get Activity
#    api_response = api_instance.get_activity_by_id(id)
#    pprint(api_response)
#except ApiException as e:
#    print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)