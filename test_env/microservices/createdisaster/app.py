from invokes import invoke_http
from pprint import pprint
from amqp_helper import Rabbitmq
from math import radians, sin, cos, sqrt, atan2
from time import sleep
from datetime import datetime
from os import environ

import json
import servicehelper

USER_HOST_PORT = environ.get("USER_HOST_PORT")
DISASTER_HOST_PORT = environ.get("DISASTER_HOST_PORT")

# Get GDAC alert
# gdac.alert

# Send localised alerts
# [AMQP] user.{userID}.alert
def createDisasterWithUsers(alerts):
    usersLoc = getUsersLastLoc()
    for alert in alerts:
        
        if len(alert.get('country','')) > 0 and bool(alert.get('isToday',False)):
            print(alert['country'])
            print(alert['location'])
            try:
                routing_keys = []
                family_routing_keys = []

                disaster = createDisaster(alert)
                affected_userIds = affectedUsers(usersLoc,alert)
                users = getUsersById(affected_userIds)
                
                
                msgs = []

                for user in users:
                    disasterId = disaster.get('disasterID',0)
                    result = addAffectedUser(user,disasterId)
                    print(result)
                    if result.get("code",400) in range(200,300):
                        print(f'Added affected user {result["data"]}')

                    affectedUser = result["data"]
                    affectedUsersID = affectedUser["affectedUsersID"]

                    msgs.append(json.dumps({
                        "affectedUsersID":affectedUsersID,
                        "alert":alert,
                        "userID":user["userID"]
                    }))
                    routing_keys.append(f'user.{user["userID"]}.alert')
                    family_routing_keys.append(f'family.{user["familyID"]}.alert')
                
                rabbitmq.publish_fanout_message_multi(msgs,routing_keys)
                rabbitmq.publish_fanout_message_multi(msgs,family_routing_keys)

            except Exception as e:
                print(e)
                raise e
    pass

def alertCallback(ch, method, properties, body):
    data = json.loads(body)
    # pprint(data)
    createDisasterWithUsers(data)

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

# Get all user latest location - send request
# [GET] /location/latest 
def getUsersLastLoc():
    try:
        result = invoke_http(f"http://user:{USER_HOST_PORT}/location/latest", method="GET")
        print(result)
        code = result.get("code",400)
        if code in range(200,300):
            return result['data']
        elif code == 404:
            return []
        else:
            return []
    except Exception as e:
        print(e)
        raise e

def getUsersById(userIds):
    users = []
    for ids in userIds:
        try:
            result = invoke_http(f"http://user:{USER_HOST_PORT}/user/{ids}",method="GET")
            print(result)
            if result.get("code",400) in range(200,300):
                users.append(result['data'])
            else:
                raise Exception('Error getting users by user id createdisaster.py')
        except Exception as e:
            print(e)
            raise e
    return users

def addAffectedUser(user, disasterId):
    affectedUser = {
        "disasterID":disasterId,
        "userID":user["userID"],
        "userName":user["userName"],
        "status": "Pending",
        "contact":user["contact"]
    }

    print(f"Adding affected user {affectedUser}")
    
    try:
        result = invoke_http(f'http://disaster:{DISASTER_HOST_PORT}/affecteduser', method='POST', json=affectedUser)
        print(result)
        if result.get("code",400) in range(200,300):
            return result
        else:
            return Exception('error adding affected user createdisaster.py')
    except Exception as e:
        print(e)

# Create disaster - send request
# [POST] /disaster/new
def createDisaster(alert:dict):
    data = {
        'disasterName': alert['name'],
        'country': alert['country'],
        'city':alert['country'],
        'lat':alert['location']['coordinates'][0],
        'long':alert['location']['coordinates'][1],
        'disasterSeverityLevel': alert['alertlevel'].lower(),
        'disasterTimestamp': alert['to']
    }

    print(data)

    try:
        result = invoke_http(f"http://disaster:{DISASTER_HOST_PORT}/disaster/new", method="POST", json=data)

        if result.get("code",400) in range(200,300):
            return result['data']
        else:
           print(result)
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
    global rabbitmq
    rabbitmq = Rabbitmq()
    rabbitmq._setup()
    print("Subscribing to gdacalert now")
    rabbitmq.subscribe('gdacalert',alertCallback)
    

# Execute this program if it is run as a main script
if __name__ == "__main__":
    print("getdisaster container is running...")
    while not servicehelper.isServiceReady("disaster") or\
        not servicehelper.isServiceReady("user"):
        sleep(1)
    main()
    servicehelper.serviceIsReady("createdisaster")
    


