from flask import Flask, Blueprint
from flask_restful import Api
from redistimeseries.client import Client

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

client = Client(host='redistimeseries', port=6379, db=0, decode_responses=True)

client.create('temperature')


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    
    from .main import main as main_blueprint
    from .api import api as api_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(api_bp)
    
    return app



