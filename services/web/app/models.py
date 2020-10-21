from .dao import RedisObject
import json
import redis

class User(RedisObject):
    def __init__(self, first, last, id = None):
        RedisObject.__init__(self, id)
        self.first = first
        self.last = last

    def setitem(self):
        payload = dict({'first':self.first,'last':self.last})
        self.client.hset(self.id, mapping=payload)
        
    def getitem(self):
        self.client.hgetall(self.id)