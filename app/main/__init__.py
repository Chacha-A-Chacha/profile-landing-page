import os
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
    # app.config.from_object(Config)
    env = os.environ.get('FLASK_ENV', 'development')
    
    if env == 'development':
        app.config.from_object('config.DevelopmentConfig')
    elif env == 'testing':
        app.config.from_object('config.TestingConfig')
    elif env == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        raise ValueError(f"Unsupported environment: {env}")

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Add more blueprints if needed

    return app
