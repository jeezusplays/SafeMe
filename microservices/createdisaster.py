from invokes import invoke_http
from pprint import pprint
from amqp_helper import Rabbitmq
from math import radians, sin, cos, sqrt, atan2
from time import sleep
from datetime import datetime

import json

# Get GDAC alert
# gdac.alert
def createDisasterWithUsers(alerts):
    usersLoc = getUsersLastLoc()
    for alert in alerts:
        
        if len(alert.get('country','')) > 0 and bool(alert.get('isToday',False)):
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

                    if result.get("code",400) in range(200,300):
                        print(f'Added affected user {result["data"]}')

                    affectedUser = result["data"]
                    affectedUsersID = affectedUser["affectedUsersID"]

                    msgs.append(json.dumps({
                        "affectedUsersID":affectedUsersID,
                        "alert":alert
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
    
def getUsersLastLoc():
    try:
        result = invoke_http("http://127.0.0.1:5001/location/latest", method="GET")
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
            result = invoke_http(f"http://127.0.0.1:5001/user/{ids}",method="GET")
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
    
    try:
        result = invoke_http('http://127.0.0.1:5002/affecteduser', method='POST', json=affectedUser)
        print(result)
        if result.get("code",400) in range(200,300):
            return result
        else:
            return Exception('error adding affected user createdisaster.py')
    except Exception as e:
        print(e)

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


    try:
        result = invoke_http("http://127.0.0.1:5002/disaster/new", method="POST", json=data)

        if result.get("code",400) in range(200,300):
            return result
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
    rabbitmq.subscribe('gdacalert',alertCallback)
    sleep(20)
    rabbitmq.unsubscribe()

# Send localised alerts
# [AMQP] user.{userID}.alert

# Get all user latest location - send request
# [GET] /location/latest

# Create disaster - send request
# [POST] /disaster/new


# Execute this program if it is run as a main script
if __name__ == "__main__":
    main()


