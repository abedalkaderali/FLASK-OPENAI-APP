from flask import Blueprint, jsonify

from src.auth import authenticate

root_bp = Blueprint('root', __name__)

@root_bp.route('/', methods=['GET'])
@authenticate
def hello_world():

    return ({"response": "Hello, World!"})

