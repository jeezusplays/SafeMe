import pika
import json

HOST = ''
PORT = ''
QUEUE = ''


# Connect to RabbitMQ server
CONNECTION = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT))


# Get GDAC alert
# gdac.alert
def alertCallback(ch, method, properties, body):
    data = json.loads(body)
    print("Received message:", body)
    pass

def subscribeAlert():
    channel = CONNECTION.channel()

    # Declare a queue named 'hello'
    channel.queue_declare(queue='hello')    

    # Register the callback function to consume messages from the 'hello' queue
    channel.basic_consume(queue='hello', on_message_callback=alertCallback, auto_ack=True)

    # Start consuming messages from the 'hello' queue
    channel.start_consuming()
    pass

    

# Send localised alerts
# [AMQP] {country}.{city}.alert

# Get all user latest location - send request
# [GET] /location/latest

# Create disaster  - send request
# [POST] /disaster/new


