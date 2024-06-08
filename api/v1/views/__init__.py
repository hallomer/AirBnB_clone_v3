#!/usr/bin/python3
from flask import Blueprint
"""Initializes the blueprint for the views."""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
