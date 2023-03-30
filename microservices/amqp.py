# Set up amqp exchange with queues
# GDAC alert
# gdac.alert

# Log alert
# log.alert

# Localised alert
# {country}.{city}.alert

# Update user status
# [PUT] /disaster/update/user/{userID}

# Email user status
# [AMQP] {userID}.status

# Family member status
# [AMQP] {userID}.{familyID}.status

# Log event
# [AMQP] log.event

# Localised alert
# {country}.{city}.alert

import pika

HOST = "localhost"  # default hostname
PORT = 5672  # default port

def check_setup():
    # The shared connection and channel created when the module is imported may be expired,
    # timed out, disconnected by the broker or a client;
    # - re-establish the connection/channel is they have been closed
    global connection, channel, hostname, port, exchangename, exchangetype

    if not is_connection_open(connection):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=hostname, port=port, heartbeat=3600, blocked_connection_timeout=3600))
    if channel.is_closed:
        channel = connection.channel()
        channel.exchange_declare(
            exchange=exchangename, exchange_type=exchangetype, durable=True)

def is_connection_open(connection):
    # For a BlockingConnection in AMQP clients,
    # when an exception happens when an action is performed,
    # it likely indicates a broken connection.
    # So, the code below actively calls a method in the 'connection' to check if an exception happens
    try:
        connection.process_data_events()
        return True
    except pika.exceptions.AMQPError as e:
        print("AMQP Error:", e)
        print("...creating a new connection.")
        return False

def create_queues(queues:list(tuple)):
    # Connect to RabbitMQ server

    # Note: the default port for AMQP is 5672, but the default port for RabbitMQ is 15672
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=HOST, port=PORT, heartbeat=3600, blocked_connection_timeout=3600,
        ))

    channel = connection.channel()

    # Declare the exchange
    exchange_name = 'safeme'
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

    # Declare and bind the topic queues
    for queue,key in queues:
        channel.queue_declare(queue=queue, durable=True)
        channel.queue_bind(queue=queue, exchange=exchange_name, routing_key=key)
    # Close the connection
    connection.close()

if __name__ == '__main__':
    queues = [('gdacalert','gdac.alert'),('logalert','log.alert'),('logevent','log.event')]
    create_queues(queues)