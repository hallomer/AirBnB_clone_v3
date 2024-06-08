#!/usr/bin/python3
from flask import json, Response
from api.v1.views import app_views
"""Defines the index view."""
@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status of the API"""
    response_data = {
        "status": "OK"
    }
    response_json = json.dumps(response_data, indent=2, sort_keys=True)
    return Response(response_json, content_type="application/json")
