from flask import Flask, send_from_directory
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    from routes.calculate import calculate_bp
    app.register_blueprint(calculate_bp)

    @app.route('/reports/<filename>')
    def download_report(filename):
        return send_from_directory("reports", filename)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)