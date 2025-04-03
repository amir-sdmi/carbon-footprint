from flask import Flask
from flask_cors import CORS

# Initialize Flask app
def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for frontend-backend communication

    # Register routes
    from routes.calculate import calculate_bp
    app.register_blueprint(calculate_bp)

    return app

# Run the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
