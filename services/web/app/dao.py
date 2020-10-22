from redis import Redis
import base64
import json

class RedisObject(object):
    def __init__(self, id = None):
        self.client = Redis(host='redis', port=6379, db=0, decode_responses=True)
        if id:
            self.id = id
        else:
            self.id = base64.urlsafe_b64encode(os.urandom(9)).decode('utf-8')
    
    def getitem(self):
        id = str(self.id)
        payload = self.client.hgetall(id)
        return payload
        
        

 