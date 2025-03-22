#!/usr/bin/python3
""" API entry point """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = os.getenv('PILLPOCKET_API_HOST', '0.0.0.0')
    port = os.getenv('PILLPOCKET_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)



# export PILLPOCKET_API_HOST=0.0.0.0
# export PILLPOCKET_API_PORT=5001