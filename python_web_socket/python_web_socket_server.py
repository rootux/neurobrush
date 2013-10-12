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
    
    def __init__(self):
      self.val1 = 50
      self.val2 = 50
      self.val3 = 50
      self.val4 = 50
      self.val5 = 50

      self.dir1 = 0
      self.dir2 = 0
      self.dir3 = 0
      self.dir4 = 0
      self.dir5 = 0

    def onMessage(self, msg, binary):
      self.dir1 += random.randint(-1, 1)
      self.dir2 += random.randint(-1, 1)
      self.dir3 += random.randint(-1, 1)
      self.dir4 += random.randint(-1, 1)
      self.dir5 += random.randint(-1, 1)

      if self.dir1 > 3: 
        self.dir1 = 3

      if self.dir2 > 3: 
        self.dir2 = 3

      if self.dir3 > 3: 
        self.dir3 = 3

      if self.dir4 > 3: 
        self.dir4 = 3

      if self.dir5 > 3: 
        self.dir5 = 3
      if self.dir1 < -3: 
        self.dir1 = -3

      if self.dir2 < -3: 
        self.dir2 = -3

      if self.dir3 < -3: 
        self.dir3 = -3

      if self.dir4 < -3: 
        self.dir4 = -3

      if self.dir5 < -3: 
        self.dir5 = -3

      self.val1 += self.dir1
      self.val2 += self.dir2
      self.val3 += self.dir3
      self.val4 += self.dir4
      self.val5 += self.dir5

      if self.val1 > 100:
        self.val1 = 100

      if self.val2 > 100: 
        self.val2 = 100

      if self.val3 > 100: 
        self.val3 = 100

      if self.val4 > 100: 
        self.val4 = 100

      if self.val5 > 100: 
        self.val5 = 100
      if self.val1 < 0: 
        self.val1 = 0

      if self.val2 < 0: 
        self.val2 = 0

      if self.val3 < 0: 
        self.val3 = 0

      if self.val4 < 0: 
        self.val4 = 0

      if self.val5 < 0: 
        self.val5 = 0


      data = {'WirelessSignalStatus': self.val1}, \
                {'ExcitementShortTerm' : self.val2}, \
                {'ExcitementLongTerm' : self.val3}, \
                {'EngagementBoredom' : self.val4}, \
                {'FrustrationScore' : self.val5}, \
                {'Upperface' : 'LeftWink'}, \
                {'Lowerface' : 'Smile'}, \
                {'LowerfaceValue' : self.val1}, \
                {'UpperfaceValue' : self.val2}

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
                                    debugCodePaths = debug)

   factory.protocol = EchoServerProtocol
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8080, web)

   reactor.run()
