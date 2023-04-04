# Kong API gateway

import requests

# Define the Kong API Gateway URL and Admin API endpoint
KONG_URL = 'http://localhost:8001'

def addAPI(json):
    # Create the API using the Kong Admin API
    response = requests.post(KONG_URL, json=json)

    # Check if the API was successfully created
    if response.status_code == 201:
        print('API created successfully.')
    else:
        print('API creation failed with status code:', response.status_code)

# Get user
# [GET] /user/{userID}
getUserAPI = {
    'name': 'get-user',
    'upstream_url': 'http://my-service:8080',
    'uris': ['/user/{userID}'],
    'methods':['GET']
}
addAPI(getUserAPI)

# Update user
# [POST] /user/update
updateUserAPI = {
    'name': 'update-user',
    'upstream_url': 'http://my-service:8080',
    'uris': ['/user/update'],
    'methods': ['POST']
}
addAPI(updateUserAPI)

# Add location
# [POST] /user/location
addLocationAPI = {
    'name': 'add-location',
    'upstream_url': 'http://my-service:8080',
    'uris': ['/user/location'],
    'methods': ['POST']
}
addAPI(addLocationAPI)

# Get all user latest location
# [GET] /user/location/latest
getLocationAPI = {
    'name': 'get-latest-location',
    'upstream_url': 'http://my-service:8080',
    'uris': ['/user/location/latest/{userID}'],
    'methods': ['GET']
}
addAPI(getLocationAPI)

# Get user status 
# [GET] disaster/affectedusers/{disasterID}
getAffectedUsersAPI = {
    'name': 'get-affected-users',
    'upstream_url': 'http://my-service:8080',
    'uris': ['/disaster/affectedusers/{disasterID}'],
    'methods': ['GET']
}
addAPI(getAffectedUsersAPI)

# Receive alerts & Send status
# [WebSocket] /get/alerts

# Send status - POST request to Update user status microservice
# [POST] /user/status

# Get alerts
# [AMQP] {country}.{city}.alert

# Get family status
# [WebSocket] /{familyID}/users/status

# Get member status
# [AMQP] *.{familyID}.status
