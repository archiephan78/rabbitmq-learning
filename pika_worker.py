#!/usr/bin/python

import pika
import time

credentials = pika.PlainCredentials('chungpht', '123456')
connection =  pika.BlockingConnection(pika.ConnectionParameters('10.5.9.177', 5672, '/', credentials))
channel = connection.channel()

channel.queue_declare(queue='test_queue', durable=True)
print('Waiting for messages: ')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='test_queue')

channel.start_consuming()