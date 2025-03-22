#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.medication import Medication
from models.order import Order


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the status of the API.
    """
    return jsonify({'status': 'OK'})

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def stats():
    """
    Returns the stats of the API.
    """
    return jsonify({
        'users': storage.count(User),
        'medications': storage.count(Medication),
        'orders': storage.count(Order)
    })
