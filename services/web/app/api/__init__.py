from flask import Blueprint



api = Blueprint('resource', __name__)



from . import routes

