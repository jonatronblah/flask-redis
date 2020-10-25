from redistimeseries.client import Client


        
        
        
class TsData(object):
    def __init__(self, timestamp, temperature, radiation):
        self.timestamp = timestamp
        self.temperature = temperature
        self.radiation = radiation
        
    def setitem(self):
        client = Client(host='redistimeseries', port=6379, db=0, decode_responses=True)
        client.add('temperature', self.timestamp, self.temperature)
        client.add('radiation', self.timestamp, self.radiation)
        
    