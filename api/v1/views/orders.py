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
        
    for required_key in ["user_id", "medication_id", "quantity"]:
        if required_key not in data:
            return jsonify({"error": f"Missing {required_key}"}), 400
    user = storage.get(User, data["user_id"])
    if not user:
        return jsonify({"error": "User not found"}), 404
    medication = storage.get(Medication, data["medication_id"])
    if not medication:
        return jsonify({"error": "Medication not found"}), 404
    try:
        quantity = int(data["quantity"])
        if quantity <= 0:
            return jsonify({"error": "Quantity must be a positive integer"}), 400
    except:
        return jsonify({"error": "Invalid quantity"}), 400
    total_price = quantity * medication.price
    order = Order(
        user_id=user.id,
        medication_id=medication.id,
        quantity=quantity,
        total_price=total_price,
        status="pending"
    )
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
    if "status" in data:
        order.status = data["status"]
        storage.save()
        return jsonify(order.to_dict()), 200
    else:
        return jsonify({"error": "Missing status"}), 400
