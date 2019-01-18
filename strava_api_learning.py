from oauth2_learning import token

print(token)

# attempt to integrate w/ strava
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = token['access_token']

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 2069849358 # Long | The identifier of the activity.

try: 
    # Get Activity
    api_response = api_instance.get_activity_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)