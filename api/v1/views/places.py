#!/usr/bin/python3
"""Handles all default RESTful API actions for Place objects."""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places(city_id):
    """Retrieves the list of all Place objects of a City."""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify([place.to_dict() for place in city.places])


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Retrieves a Place object."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """Creates a Place."""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.is_json:
        abort(400, 'Not a JSON')
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)
    if 'name' not in data:
        abort(400, 'Missing name')
    new_place = Place(city_id=city_id, **data)
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """Updates a Place object."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.is_json:
        abort(400, 'Not a JSON')
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200

@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search_places():
    """Retrieves all Place objects based on search criteria."""
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()

    if not data or not len(data) or ('states' not in data and 'cities' not in data and 'amenities' not in data):
        places = list(storage.all(Place).values())
    else:
        places = set()
        state_ids = data.get('states', [])
        city_ids = data.get('cities', [])
        amenity_ids = data.get('amenities', [])

        if state_ids:
            for state_id in state_ids:
                state = storage.get(State, state_id)
                if state:
                    for city in state.cities:
                        places.update(city.places)

        if city_ids:
            for city_id in city_ids:
                city = storage.get(City, city_id)
                if city:
                    places.update(city.places)

        if not state_ids and not city_ids:
            places = set(storage.all(Place).values())

        if amenity_ids:
            amenity_objs = [storage.get(Amenity, amenity_id) for amenity_id in amenity_ids]
            places = {place for place in places if all(amenity in place.amenities for amenity in amenity_objs)}

    result = [place.to_dict() for place in places]
    return jsonify(result)
