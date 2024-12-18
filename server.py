from flask import Flask
from app.routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__)
    # Load config, init DB if needed
    app.register_blueprint(admin_bp)
    # Register other blueprints
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
