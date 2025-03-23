#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.medication import Medication


@app_views.route('/medication', methods=['GET'], strict_slashes=False)
def get_medication():
    """Retrieves the list of all Medication objects"""
    all_medication = storage.all(Medication).values()
    return jsonify([medication.to_dict() for medication in all_medication])

@app_views.route('/medication/<medication_id>', methods=['GET'], strict_slashes=False)
def get_medication_by_id(medication_id):
    """Retrieves a Medication object by its ID"""
    medication = storage.get(Medication, medication_id)
    if not medication:
        abort(404)
    return jsonify(medication.to_dict())

#@app_views.route('/medication/<medication_id>', methods=['DELETE'], strict_slashes=False)
def delete_medication(medication_id):
    """Deletes a Medication object by its ID"""
    return jsonify({"error": "Medication deletion is not allowed"}), 403

#@app_views.route('/medication', methods=['POST'], strict_slashes=False)
#def create_medication():
    """Creates a Medication object"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if "name" not in data:
        abort(400, description="Missing name")
    medication = Medication(**data)
    storage.new(medication)
    storage.save()
    return jsonify(medication.to_dict()), 201

#@app_views.route('/medication/<medication_id>', methods=['PUT'], strict_slashes=False)
#def update_medication(medication_id):
    """Updates a Medication object by its ID"""
    medication = storage.get(Medication, medication_id)
    if not medication:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(medication, key, value)
    storage.save()
    return jsonify(medication.to_dict()), 200
