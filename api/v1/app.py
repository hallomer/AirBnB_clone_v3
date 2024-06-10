#!/usr/bin/python3
"""Initializes a Flask web application."""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage."""
    storage.close()


@app.errorhandler(404)
def not_fonud(error):
    """"Returns a JSON-formatted 404 status code response."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
