#!/usr/bin/python3
"""Defines the index view."""
from flask import json, Response
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status of the API"""
    response_data = {
        "status": "OK"
    }
    response_json = json.dumps(response_data, indent=2, sort_keys=True) + '\n'
    return Response(response_json, content_type="application/json")
