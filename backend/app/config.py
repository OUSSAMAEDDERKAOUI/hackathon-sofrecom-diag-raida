import os
from typing import Dict, Any


class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = False
    TESTING = False
    
    # API Configuration
    API_VERSION = "v1"
    API_TITLE = "Diag-Raida API"
    
    # LLM Configuration (to be added later)
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    
    # Model paths
    MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'saved')
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENV = 'production'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True


# Configuration dictionary
config: Dict[str, Any] = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
