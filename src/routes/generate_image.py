from flask import Blueprint, request, jsonify
from src.openai_client import generate_image_response

generate_image_bp = Blueprint('generate_image', __name__)

@generate_image_bp.route('/generateImage', methods=['POST'])
def generate_image():
    api_key = request.headers.get('x-api-key')
    response_type = request.headers.get('response-type')
    
    if not api_key:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({"error": "Content is required"}), 400

    try:
        response = generate_image_response(content, response_type, api_key)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
