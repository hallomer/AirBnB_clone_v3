#!/usr/bin/python3
"""Defines the index view."""
from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"amenities": Amenity,
           "cities": City,
           "places": Place,
           "reviews": Review,
           "states": State,
           "users": User
           }


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Retrieves the number of each objects by type"""
    return jsonify({key: storage.count(value)
                    for key, value in classes.items()})
