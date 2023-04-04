import requests

KONG_ADMIN_URL = 'http://localhost:8001'

# Function to create a service and a route to that service on Kong
def create_service_and_route(service_name, service_url,consumer_route):
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
        'methods': ['GET','POST','PUT','DELETE'],
        'service': {'id': service_id}
    })

    if response.status_code != 201:
        print('Error creating route:', response.json())
        # Clean up by deleting the service if the route creation failed
        requests.delete(KONG_ADMIN_URL + '/services/' + service_id)
        return

    route_id = response.json()['id']
    print('Route created with ID:', route_id)


if __name__ == '__main__':
    # Now create a dummy service and route
    create_service_and_route('user_service4',
                             'http://host.docker.internal:5001',
                             '/api')