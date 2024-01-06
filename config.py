import os

class Config:
    """
    Common configuration settings for the Flask application.

    Attributes:
        SECRET_KEY (str): A secret key used for session security.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Enable or disable modification tracking.
    
    Run the following commands in the terminal to set the environment variable:
        For development: export FLASK_ENV=development
        For testing: export FLASK_ENV=testing
        For production: export FLASK_ENV=production
    """
    SECRET_KEY = 'your_secret_key_here'  # Change this to a strong, random value
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Development configuration settings.

    Attributes:
        DEBUG (bool): Enable or disable debugging mode.
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy in development.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    """
    Testing configuration settings.

    Attributes:
        TESTING (bool): Enable or disable testing mode.
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy in testing.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    """
    Production configuration settings.

    Attributes:
        DEBUG (bool): Disable debugging mode in production.
        SQLALCHEMY_DATABASE_URI (str): Database URI for SQLAlchemy in production.
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
