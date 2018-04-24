#!/usr/bin/python

import pika
import sys 

credentials = pika.PlainCredentials('chungpht', '123456')
connection =  pika.BlockingConnection(pika.ConnectionParameters('10.5.9.177', 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='many-rev',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or " Halo!"
channel.basic_publish(exchange='many-rev',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
