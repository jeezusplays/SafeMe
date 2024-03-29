from os import environ
from invokes import invoke_http
from time import sleep

import requests


KONG_ADMIN_PORT = environ.get("KONG_ADMIN_PORT")
USER_HOST_PORT = environ.get("USER_HOST_PORT")
DISASTER_HOST_PORT = environ.get("DISASTER_HOST_PORT")
VOLUNTEEREVENT_HOST_PORT = environ.get("VOLUNTEEREVENT_HOST_PORT")
UPDATEUSERSTATUS_HOST_PORT = environ.get("UPDATEUSERSTATUS_HOST_PORT")
SIGNUPVOLUNTEER_HOST_PORT = environ.get("SIGNUPVOLUNTEER_HOST_PORT")

KONG_ADMIN_URL = f'http://kong:{KONG_ADMIN_PORT}'
print(KONG_ADMIN_URL)

# Function to create a service and a route to that service on Kong


def create_service_and_route(service_name, service_url, consumer_route):
    # First create the service
    response = requests.post(KONG_ADMIN_URL + '/services/', json={
        'name': service_name,
        'url': service_url
    })

    if response.status_code != 201:
        print('Error creating service:', response.json())
        return

    service_id = response.json()['id']
    print('Service created with ID:', service_id)

    # Now create the route to the service
    response = requests.post(KONG_ADMIN_URL + '/routes/', json={
        'name': service_name + '_route',
        'paths': [consumer_route],
        'methods': ['GET', 'POST', 'PUT', 'DELETE','OPTIONS'],
        'service': {'id': service_id}
    })

    if response.status_code != 201:
        print('Error creating route:', response.json())
        # Clean up by deleting the service if the route creation failed
        requests.delete(KONG_ADMIN_URL + '/services/' + service_id)
        return

    route_id = response.json()['id']
    print('Route created with ID:', route_id)
    allowCors(route_id)


def check_connection():
    r = invoke_http(f"{KONG_ADMIN_URL}/services")
    code = r.get("code", 200)
    while not code in range(200, 300):
        r = invoke_http(f"{KONG_ADMIN_URL}/services")
        code = r.get("code", 200)
        print("Kong connection not ready")
        sleep(1)
    print("Kong connection ready")


def allowCors(route_id):
    plugin_config = {
        "origins": ["*"],
        "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        "headers": ["Content-Type", "Authorization"],
        "exposed_headers": [],
        "max_age": 3600
    }

    # Send a request to Kong to add the plugin to all routes
    response = requests.post(
        f"{KONG_ADMIN_URL}/routes/{route_id}/plugins",
        json={
            "name": "cors",
            "config": plugin_config
        }
    )

    # Check if the request was successful
    if response.status_code == 201:
        print("CORS plugin added to all routes in Kong.")
    else:
        print("Failed to add CORS plugin to all routes in Kong.")
        print(response.text)

if __name__ == '__main__':
    print("Kong sert up container is running ...")
    # Now create a dummy service and route
    check_connection()

    print("Setting routes")

    create_service_and_route('user',
                             f'http://user:{USER_HOST_PORT}',
                             '/api/user')
    create_service_and_route('disaster',
                             f'http://disaster:{DISASTER_HOST_PORT}',
                             '/api/disaster')
    create_service_and_route('volunteerevent',
                             f'http://volunteerevent:{VOLUNTEEREVENT_HOST_PORT}',
                             '/api/volunteerevent')
    create_service_and_route('updateuserstatus',
                             f'http://updateuserstatus:{UPDATEUSERSTATUS_HOST_PORT}',
                             '/api')
    create_service_and_route('signupvolunteer',
                             f'http://signupvolunteer:{SIGNUPVOLUNTEER_HOST_PORT}',
                             '/api/signupvolunteer')
    print("Done")
