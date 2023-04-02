from invokes import invoke_http
from pprint import pprint
from amqp_helper import Rabbitmq
from math import radians, sin, cos, sqrt, atan2

import json

# Get GDAC alert
# gdac.alert
def createDisasterWithUsers(alerts):
    usersLoc = getUsersLastLoc()
    for alert in alerts:
        try:
            affected_userIds = affectedUsers(usersLoc,alert)
            disaster = createDisaster(alert)
            affected_users = getUsersById(affected_userIds)
            disasterId = disaster.get('disasterID',0)
            result = addAffectedUsers(affected_users,disasterId)
            if result.get("code",400) != 200:
                raise Exception('error createDisaster')
        except Exception as e:
            print(e)
            raise e
    pass

def alertCallback(ch, method, properties, body):
    data = json.loads(body)
    pprint(data)
    createDisasterWithUsers(data)
    ########################### TODO SEND NOTIFICATION TO AMQP ###############################


def distanceFrom(lat1,lon1,lat2,lon2)->float:
    '''
    Return distance from 2 points in km
    '''
    R = 6371  # radius of the earth in km

    # convert latitudes and longitudes from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # calculate the difference between the latitudes and longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # apply the Haversine formula to calculate the distance
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    return distance
    
def getUsersLastLoc():
    try:
        result = invoke_http("http://0.0.0.0:5001/location/latest", method="GET")
        if result.get("code",400) == 200:
            return result
        else:
            return None
    except Exception as e:
        print(e)
        raise e

def getUsersById(userIds):
    users = []
    for ids in userIds:
        try:
            result = invoke_http(f"http://0.0.0.0:5002/user/{ids}",method="GET")
            if result.get("code",400) == 200:
                users.append(result)
            else:
                raise Exception('Error getting users by user id createdisaster.py')
        except Exception as e:
            print(e)
            raise e
    return users

def addAffectedUsers(user, disasterId):
    affectedUser = {
        "disasterID":disasterId,
        "userID":user["userID"],
        "userName":user["userName"],
        "status": "Pending",
        "contact":user["contact"]
    }
    
    try:
        result = invoke_http('http://0.0.0.0:5002/affecteduser', method='POST', json=affectedUser)
        if result.get("code",400) == 200:
            return result
        else:
            return Exception('error adding affected user createdisaster.py')
    except Exception as e:
        print(e)

def createDisaster(alert):
    data = alert
    try:
        result = invoke_http("http://localhost:5002/disaster/new", method="POST", json=data)

        if result.get("code",400) == 200:
            return result
        else:
           raise SystemError('Unable to create disaster')
        
    except Exception as e:
        raise e
    
def affectedUsers(usersLoc,alert:dict):
    location = alert.get('location',{'coordinates':[0,0],'type':'point'})
    coordinates = location.get('coordinates')

    userIds = []

    for user in usersLoc:
        userID = user['userID']
        country = user['country']
        city = user['city']
        lat = user['lat']
        long = user['long']
        timestamp = user['timestamp']

        if distanceFrom(lat,long,coordinates[0],coordinates[1]) <= 4:
            userIds.append(userID)
        
    return userIds

def main():
    rabbitmq = Rabbitmq()
    rabbitmq.subscribe('gdacalert',alertCallback)

# Send localised alerts
# [AMQP] {country}.{city}.alert

# Get all user latest location - send request
# [GET] /location/latest

# Create disaster - send request
# [POST] /disaster/new


# Execute this program if it is run as a main script
if __name__ == "__main__":
    main()


