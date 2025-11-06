from flask import Flask
from app.routes import evaluation_routes, analysis_routes, recommendation_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(evaluation_routes.bp)
    # app.register_blueprint(analysis_routes.bp)
    # app.register_blueprint(recommendation_routes.bp)
    return app
