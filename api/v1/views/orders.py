#!/usr/bin/python3
""" Order API """
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.order import Order


@app_views.route('/orders', methods=['GET'], strict_slashes=False)
def get_orders():
    """Retrieves the list of all Order objects"""
    orders = storage.all(Order).values()
    return jsonify([order.to_dict() for order in orders])

@app_views.route('/orders/<order_id>', methods=['GET'], strict_slashes=False)
def get_order(order_id):
    """Retrieves a Order object by its ID"""
    order = storage.get(Order, order_id)
    if not order:
        abort(404)
    return jsonify(order.to_dict())

@app_views.route('/orders', methods=['POST'], strict_slashes=False)
def create_order():
    """Creates a new Order object"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if "user_id" not in data:
        return jsonify({"error": "Missing user_id"}), 400
    if "medication_id" not in data:
        return jsonify({"error": "Missing medication_id"}), 400
    if "quantity" not in data:
        return jsonify({"error": "Missing quantity"}), 400
    order = Order(**data)
    storage.new(order)
    storage.save()
    return jsonify(order.to_dict()), 201

@app_views.route('/orders/<order_id>', methods=['PUT'], strict_slashes=False)
def update_order(order_id):
    """Updates a Order object by its ID"""
    order = storage.get(Order, order_id)
    if not order:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ["id", "user_id", "medication_id", "quantity", "created_at", "updated_at"]:
            setattr(order, key, value)
    storage.save()
    return jsonify(order.to_dict()), 200
