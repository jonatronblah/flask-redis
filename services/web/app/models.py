from dao import RedisObject
import json
import redis

class User(RedisObject):
    def __init__(self, first, last, id = None):
        RedisObject.__init__(self, id)
        self.first = first
        self.last = last

    def setitem(self)
        payload = json.dumps({'first':self.first,'last':self.last})
        self.client.hset(self.id, mapping=payload)