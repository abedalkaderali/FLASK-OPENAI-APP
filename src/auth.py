from functools import wraps
from flask import request, jsonify
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("X_API_KEY")
 
def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        # print("Received API key:", api_key) 
        if api_key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

