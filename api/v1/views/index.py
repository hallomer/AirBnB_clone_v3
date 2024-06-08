#!/usr/bin/python3
"""Defines the index view."""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
