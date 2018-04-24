#!/usr/bin/env python
import socket
from kombu import Connection

def main():
  host = "host"
  port = 5672
  user = "username"
  password = "password"
  vhost = "/"

  url = 'amqp://{0}:{1}@{2}:{3}/{4}'.format(user, password, host, port, vhost)
  with Connection(url) as e:
    try:
      e.connect()
    except socket.error as c:
      print c              
    except IOError:
      raise ValueError("Received IOError, Authen fail")
    else:
      print "OK"

if __name__ == "__main__":
  main()
