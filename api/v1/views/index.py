#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views
"""Defines the index view."""
@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status of the API"""
    status = {
	    "status": "OK"
    }    
    return jsonify(status)
