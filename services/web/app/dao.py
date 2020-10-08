from redis import Redis

class RedisObject(Object):
    def __init__(self, id = None):
        self.client = Redis()
        if id:
            self.id = id
        else:
            self.id = base64.urlsafe_b64encode(os.urandom(9)).decode('utf-8')
        
        

 