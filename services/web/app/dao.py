from redis import Redis
import base64

class RedisObject(object):
    def __init__(self, id = None):
        self.client = Redis(host='redis', port=6379, db=0)
        if id:
            self.id = id
        else:
            self.id = base64.urlsafe_b64encode(os.urandom(9)).decode('utf-8')
        
        

 