from redistimeseries.client import Client


class User(object):
    def __init__(self, time, last, id = None):
        RedisObject.__init__(self, id)
        self.first = first
        self.last = last

    def setitem(self):
        payload = {'first':self.first,'last':self.last}
        self.client.hmset(self.id, payload)
        
        
        
class Data(object):
    def __init__(self, timestamp, temperature, humidity):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        
    def setitem(self):
        client = Client(host='redistimeseries', port=6379, db=0, decode_responses=True)
        client.add('temperature', timestamp, temperature)
        client.add('humidity', timestamp, humidity)
        
    