from flask import request
import json
from flask_restful import Resource
from .. import api

from ..models import User

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(TodoItem, '/todos/<int:id>')




class NameItem(Resource):
    def put(self, id):
        first = request.form['first']
        last = request.form['last']
        
        user = User(id = id, first = first, last = last)
        user.setitem()
        
        return {'id': id, 'first': first, 'last': last}
    
    def get(self, id):
        user = User(id)
        payload = user.getitem()
        return payload
        
api.add_resource(NameItem, '/users/<string:id>')
        
       
        
        