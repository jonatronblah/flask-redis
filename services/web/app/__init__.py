from flask import Flask, Blueprint
from flask_restful import Api
from redistimeseries.client import Client
import random
import time

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

client = Client(host='redistimeseries', port=6379, db=0, decode_responses=True)

client.create('temperature')
client.create('radiation')

client.create('temp_avg_min')
client.create('rad_avg_min')

client.createrule('temperature', 'temp_avg_min', 'avg', 60)
client.createrule('radiation', 'rad_avg_min', 'avg', 60)

t = int(time.time())

for i in range(1000):
    client.add('temperature', t, random.randint(1,100))
    client.add('radiation', t, random.randint(1,100))
    t += 1


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    
    from .main import main as main_blueprint
    from .api import api as api_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(api_bp)
    
    from .main.dash_app import create_dashboard
    app = create_dashboard(app)
    
    
    return app



