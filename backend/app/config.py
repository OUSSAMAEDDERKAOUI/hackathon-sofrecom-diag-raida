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
    
    # OpenRouter LLM Configuration
    OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    OPENROUTER_APP_NAME = "Diag-Raida"
    OPENROUTER_SITE_URL = os.environ.get('OPENROUTER_SITE_URL', 'http://localhost:5000')
    
    # Free models available on OpenRouter
    LLM_MODEL = os.environ.get('LLM_MODEL', 'meta-llama/llama-3.2-3b-instruct:free')
    # Alternative free models:
    # - 'google/gemma-2-9b-it:free'
    # - 'mistralai/mistral-7b-instruct:free'
    # - 'microsoft/phi-3-mini-128k-instruct:free'
    # - 'qwen/qwen-2-7b-instruct:free'
    
    LLM_TIMEOUT = 30  # seconds
    LLM_MAX_TOKENS = 500
    LLM_TEMPERATURE = 0.7
    LLM_FALLBACK_ENABLED = True  # Use fallback if LLM fails
    
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
