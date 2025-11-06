from flask import Flask, jsonify
from app.config import config
from app.routes import analysis_routes, evaluation_routes, recommendation_routes
import os


def create_app(config_name=None):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config['FLASK_APP'] = 'app.main:create_app'  # Add this line to specify the application factory
    
    # Load configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(config.get(config_name, config['default']))
    
    # Register blueprints
    app.register_blueprint(analysis_routes.bp)
    app.register_blueprint(evaluation_routes.bp)
    app.register_blueprint(recommendation_routes.bp)
    
    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'Diag-Raida API',
            'version': app.config['API_VERSION']
        }), 200
    
    # Root endpoint
    @app.route('/', methods=['GET'])
    def root():
        return jsonify({
            'message': 'Welcome to Diag-Raida API',
            'version': app.config['API_VERSION'],
            'endpoints': {
                'health': '/health',
                'analysis': '/api/analysis',
                'evaluation': '/api/evaluation',
                'recommendation': '/api/recommendation'
            }
        }), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app


# This allows running the app directly with: python -m app.main
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
