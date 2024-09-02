import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
CSRF_ENABLED = True


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
    UPLOAD_FOLDER = 'static/images/uploads'

class DevelopmentConfig(Config):
    """Development configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO') == 'true'

class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test_secret_key'
    WTF_CSRF_ENABLED = False  # CSRF disabled for testing
    RECAPTCHA_PUBLIC_KEY = 'test_recaptcha_public_key'
    RECAPTCHA_PRIVATE_KEY = 'test_recaptcha_private_key'
    UPLOAD_FOLDER = 'static/images/uploads'


class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# Dictionary to easily switch between configurations
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
