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