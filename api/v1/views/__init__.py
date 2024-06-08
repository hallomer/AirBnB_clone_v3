#!/usr/bin/python3
from flask import Blueprint
from api.v1.views.index import * 
"""Initializes the blueprint for the views."""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
