from .main_routes import main_bp
from .auth_routes import auth_bp
from .file_routes import file_bp


# Register Blueprints
def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(file_bp)
