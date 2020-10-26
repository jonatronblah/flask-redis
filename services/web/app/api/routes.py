from flask import request
import json
import time
from flask_restful import Resource
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
        
    
        
        
api.add_resource(TimeSeries, '/timeseries')
        
       
        
        