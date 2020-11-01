from flask import request, jsonify
import time
from flask_restful import Resource

from redistimeseries.client import Client
from .. import api

from ..models import TsData

 


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(TodoItem, '/todos/<int:id>')



class TimeSeries(Resource):
    def put(self):
        temperature = request.form['temperature']
        radiation = request.form['radiation']
        timestamp = request.form['timestamp']
        
        datapoint = TsData(timestamp = timestamp, temperature = temperature, radiation = radiation)
        datapoint.setitem()
        
        return {'timestamp': timestamp, 'temperature': temperature, 'radiation': radiation}
        
    def get(self):
        client = Client(host='redistimeseries', port=6379, db=0, decode_responses=True)
        raddata = client.range('rad_avg_min', 0, -1)
        tempdata = client.range('temp_avg_min', 0, -1)
        
        radlist = []
        for i in raddata:
            radlist.append({'timestamp': str(i[0]), 'radiation':str(i[1])})
        
        templist = []
        for i in tempdata:
            templist.append({'timestamp': str(i[0]), 'temperature':str(i[1])})
        
        payload = {'tempdata':templist, 'raddata':radlist}
        
        
        return jsonify(payload)
        
    
        
        
api.add_resource(TimeSeries, '/timeseries')
        
       
       
        