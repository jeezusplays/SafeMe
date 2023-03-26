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

hostname = "localhost"  # default hostname
port = 5672  # default port
# Note: the default port for AMQP is 5672, but the default port for RabbitMQ is 15672
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname, port=port, heartbeat=3600, blocked_connection_timeout=3600,
    ))
# Note about AMQP connection: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
# If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls.
# If see: Stream connection lost: ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None)
# - Try: simply re-run the program or refresh the page.
# For rare cases, it's incompatibility between RabbitMQ and the machine running it, Use the Docker version of RabbitMQ instead: https://www.rabbitmq.com/download.html
channel = connection.channel()
# Set up the exchange if the exchange doesn't exist
# - use a 'topic' exchange to enable interaction
exchangename = "order_topic"
exchangetype = "topic"
channel.exchange_declare(exchange=exchangename,
                         exchange_type=exchangetype, durable=True)
# 'durable' makes the exchange survive broker restarts

# Here can be a place to set up all queues needed by the microservices, instead of setting up the queues using RabbitMQ UI.
# Set up amqp exchange with queues

############   GDAC Alert queue   #############
# declare GDAC Alert queue (gdac.alert)
queue_name = 'GDAC_Alert'
channel.queue_declare(queue=queue_name, durable=True)

############   Log queue   #############
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

############   Event Log queue   #############
# Log event - [AMQP] log.event
# declare Event Log queue
queue_name = 'Event_Log'
channel.queue_declare(queue=queue_name, durable=True)

# Localised alert - {country}.{city}.alert

############   Error queue   #############
# declare Error queue
queue_name = 'Error'
channel.queue_declare(queue=queue_name, durable=True)
# 'durable' makes the queue survive broker restarts

# bind Error queue
channel.queue_bind(exchange=exchangename,
                   queue=queue_name, routing_key='*.error')
# bind the queue to the exchange via the key
# any routing_key with two words and ending with '.error' will be matched

############   Activity_Log queue    #############
# declare Activity_Log queue
queue_name = 'Activity_Log'
channel.queue_declare(queue=queue_name, durable=True)
# 'durable' makes the queue survive broker restarts

# bind Activity_Log queue
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='#')
# bind the queue to the exchange via the key
# 'routing_key=#' => any routing_key would be matched

"""
This function in this module sets up a connection and a channel to a local AMQP broker,
and declares a 'topic' exchange to be used by the microservices in the solution.
"""


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
