from flask import Flask
from flask_mail import Mail

from config import Config

mail = Mail()

def create_app():
    """
    Factory function to create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(Config)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Add more blueprints if needed

    return app