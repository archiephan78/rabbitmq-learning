#!/usr/bin/python

import pika 
import sys

credentials = pika.PlainCredentials('chungpht', '123456')
connection =  pika.BlockingConnection(pika.ConnectionParameters('10.5.9.177', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='test_queue', durable=True)

f = open('message.txt')
for message in f:
    channel.basic_publish(exchange='',
                        routing_key='test_queue',
                        body=message,
                        properties=pika.BasicProperties(
                         delivery_mode = 2, 
                      ))
    print(" [x] Sent %r" % message)
f.close()
connection.close()