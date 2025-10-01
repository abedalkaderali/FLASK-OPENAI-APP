from flask import Blueprint, jsonify

root_bp = Blueprint('root', __name__)

@root_bp.route('/', methods=['GET'])
def hello_world():
    return jsonify({"response": "Hello, World!"})

