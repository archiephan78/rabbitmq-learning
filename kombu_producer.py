#!/usr/bin/env python
from kombu import Connection, Exchange, Producer, Queue


def main():
  rabbit_url = "amqp://admin:password@ip:5672//"
  conn = Connection(rabbit_url)
  channel =  conn.channel()
  exchange = Exchange("test", type="direct")
  producer = Producer(exchange=exchange, channel=channel, routing_key="vcc")
  queue = Queue(name="chungpht", exchange=exchange, routing_key="vcc")
  queue.maybe_bind(conn)
  queue.declare()
  producer.publish("Hello from other side")

if __name__ == "__main__":
  main()