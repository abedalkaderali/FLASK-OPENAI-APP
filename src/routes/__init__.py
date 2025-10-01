from flask import Blueprint

routes_bp = Blueprint('routes', __name__)

from .root import root_bp
from .chat import chat_bp
from .generate_image import generate_image_bp

def register_routes(app):
    app.register_blueprint(root_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(generate_image_bp)
