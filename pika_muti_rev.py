#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('chungpht', '123456')
connection =  pika.BlockingConnection(pika.ConnectionParameters('10.5.9.177', 5672, '/', credentials))

channel = connection.channel()

channel.exchange_declare(exchange='many-rev',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='many-rev',
                   queue=queue_name)

print(' [*] Waiting for logs:')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()