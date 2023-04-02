from amqp_helper import Rabbitmq

import json



# Get GDAC alert
# gdac.alert
def alertCallback(ch, method, properties, body):
    data = json.loads(body)
    print("Received message:", body)
    pass

def main():
    rabbitmq = Rabbitmq()
    rabbitmq.subscribe('gdacalert',alertCallback)

    

# Send localised alerts
# [AMQP] {country}.{city}.alert

# Get all user latest location - send request
# [GET] /location/latest

# Create disaster  - send request
# [POST] /disaster/new

if __name__ == "__main__":
    main()

