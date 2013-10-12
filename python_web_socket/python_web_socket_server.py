#!/usr/bin/env python2.7

import sys
import json
import random

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.websocket import WebSocketServerFactory, \
                               WebSocketServerProtocol, \
                               listenWS


class EchoServerProtocol(WebSocketServerProtocol):

   def onConnect(self, connectionRequest):
      headers = {'Access-Control-Allow-Origin': '*'}
      return (None, headers)

   def onMessage(self, msg, binary):
      rand1 = random.randint(1, 100)
      rand2 = random.randint(1, 100)
      rand3 = random.randint(1, 100)
      rand4 = random.randint(1, 100)
      rand5 = random.randint(1, 100)

      data =    {'WirelessSignalStatus': rand1}, \
                {'ExcitementShortTerm' : rand2}, \
                {'ExcitementLongTerm' : rand3}, \
                {'EngagementBoredom' : rand4}, \
                {'FrustrationScore' : rand5}, \
                {'Upperface' : 'LeftWink'}, \
                {'Lowerface' : 'Smile'}, \
                {'LowerfaceValue' : rand1}, \
                {'UpperfaceValue' : rand2}

      json_data = json.dumps(data)
      self.sendMessage(msg, binary)
      self.sendMessage(json_data, binary)


if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WebSocketServerFactory("ws://localhost:9000",
                                    debug = debug,
                                    debugCodePaths = debug, 
                                    )

   factory.protocol = EchoServerProtocol
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8080, web)

   reactor.run()
