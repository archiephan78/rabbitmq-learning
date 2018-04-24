#!/usr/bin/env python
from kombu import Connection, Exchange, Consumer, Queue


rabbit_url = "amqp://chungpht:123456@10.5.9.177:5672//"
conn = Connection(rabbit_url)
exchange = Exchange("test", type="direct" )

queue = Queue(name="chungpht", exchange=exchange, routing_key="vcc")

def process_message(body, message):
    print("Ben kia bao tui la {}".format(body))
    message.ack()
with Consumer(conn, queues=queue, callbacks=[process_message], accept=["text/plain"]):  
    conn.drain_events(timeout=2)

