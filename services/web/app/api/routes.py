from flask_restful import Resource
from .. import api

from .dao import NameRedis

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(TodoItem, '/todos/<int:id>')

class NameItem(Resource):
    def put(self):
        json_data = request.get_json(force=True)
        id = json_data['id']
        first = json_data['first']
        last = json_data['last']
        return jsonify(id=id, first=first, last=last)
        
        