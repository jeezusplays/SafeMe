from pika.exchange_type import ExchangeType
from os import environ
from typing import List, Tuple
from time import sleep

import pika
import json
import threading


HOST = "rabbitmq"  # default hostname
PORT = environ.get("RABBITMQ_PORT")  # default port
print(f'Listening to port: {str(PORT)}')
EXCHANGE = 'safeme'


class Rabbitmq():

    def __init__(self, host=None, port=None, exchange=None) -> None:
        # host
        if host is None:
            self.host = HOST
        else:
            self.host = host

        # port
        if port is None:
            self.port = PORT
        else:
            self.port = port
        
        # exchange
        if exchange is None:
            self.exchange = EXCHANGE
        else:
            self.exchange = exchange

        self.connection = None
        self.channel = None
        self.consumers = []
        
        
    def _connect(self):
        print(f"connectiong to {HOST}:{PORT}")
        # Connect to RabbitMQ server
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, heartbeat=3600, blocked_connection_timeout=3600,))
        channel = connection.channel()

        self.connection = connection
        self.channel = channel

        # Declare the exchange
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=ExchangeType.topic)
        return self.connection, self.channel
    
    def _close(self):
        
        self.connection.close()
        self.channel = None

    def _has_queue(self,queue_name):
            
            if self.channel is None:
                self._connect()

            try:
                queues = self.channel.queue_declare(queue_name, passive=True, arguments={'x-expires': 60000})
            except Exception as e:
                print(e)
                return False

            # Close the connection
            self._close()

            return True

    def add_queue(self, queues:List[Tuple]):
        self._connect()

        # Declare and bind the topic queues
        for queue,key in queues:
            self.channel.queue_declare(queue=queue, durable=True)
            self.channel.queue_bind(queue=queue, exchange=self.exchange, routing_key=key)

        self._close()

    def _subscribe(self,queue, callback=None):
        while True:
            try:
                if self.channel is None or self.connection is None:
                    self._connect()

                if callback is None:
                    callback = lambda ch, method, properties, body: print(f"Received message: {json.loads(body)}")

                def start_consuming():
                    self.channel.start_consuming()

                
                # Register a consumer
                queues = self.channel.queue_declare(queue, passive=True, arguments={'x-expires': 60000})
                self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

                consumer_thread = threading.Thread(target=start_consuming)
                consumer_thread.start()
                break
            except Exception as e:
                print(e)
    
            sleep(1)
        
                
            
            
            
    def subscribe(self,queue,callback=None):

        self.consumers.append({
            'exchange': Rabbitmq(),
            'queue': queue,
            'callback': callback
            })
        self.consumers[-1]['exchange']._subscribe(queue,callback)

    def checkConsuming(self):
        while True:
            for consumer_tag in self.channel.consumer_tags:
                print(f"Consumer tag: {consumer_tag}")
                
    def _unsubscribe(self):
        if self.channel is None:
            self._connect()
        self.channel.stop_consuming()

    def unsubscribe(self):
        for consumer in self.consumers:
            rabbit = consumer['exchange']
            rabbit._unsubscribe()
        self.consumers.clear()

    def publish_message(self,msg,key):
        self._connect()
        self.channel.basic_publish(exchange=self.exchange, routing_key=key, body=msg)
        self._close()

    def publish_fanout_message(self,msg,keys):
        self._connect()
        for key in keys:
            self.channel.basic_publish(exchange=self.exchange, routing_key=key, body=msg)
        self._close()
    
    def publish_fanout_message_multi(self,msgs,keys):
        self._connect()
        for msg,key in zip(msgs,keys):
            self.channel.basic_publish(exchange=self.exchange, routing_key=key, body=msg)
        self._close()

    def _is_connection_open(self):
        # For a BlockingConnection in AMQP clients,
        # when an exception happens when an action is performed,
        # it likely indicates a broken connection.
        # So, the code below actively calls a method in the 'connection' to check if an exception happens

        try:
            self.connection.process_data_events()
            return True
        except Exception as e:
            print("AMQP Error:", e)
            print("...creating a new connection.")
            return False

    def _setup(self):
    # The shared connection and channel created when the module is imported may be expired,
    # timed out, disconnected by the broker or a client;
    # - re-establish the connection/channel is they have been closed
    
        while self.connection is None or self.channel is None:
            try:
                self._connect()
            except Exception as e:
                print(e)
            sleep(1)
            

if __name__ == '__main__':
    pass
    # broker = Rabbitmq()
    # queues = [('gdacalert','gdac.alert'),('logalert','log.alert'),('logevent','log.event')]
    # broker.add_queue(queues)
