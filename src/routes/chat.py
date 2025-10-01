from flask import Blueprint, request, jsonify
from src.openai_client import get_chat_completion
from src.auth import authenticate
import os
API_KEY = os.getenv("API_KEY")

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
@authenticate
def chat():
    data = request.get_json()
    user_message = data.get('content')

    if not user_message:
        return jsonify({"error": "Content is required"}), 400

    response = get_chat_completion(user_message, API_KEY)

    return jsonify({
        "response": response,
        "version": "0.1.0"
    })

