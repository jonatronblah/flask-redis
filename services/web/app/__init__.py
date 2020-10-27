from flask import Flask, Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)




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



