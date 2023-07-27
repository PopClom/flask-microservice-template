from flask import Blueprint, jsonify, request
from bootstrap import get_user_service

user_controller = Blueprint('user_controller', __name__)


@user_controller.route('/users', methods=['GET'])
def get_users():
    user_service = get_user_service()
    users = user_service.get_all_users()

    users_data = [user.to_dict() for user in users]
    return jsonify(users_data)


@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_service = get_user_service()
    user = user_service.get_user_by_id(user_id)

    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'message': 'User not found'}), 404


@user_controller.route('/users', methods=['POST'])
def create_user():
    user_service = get_user_service()
    data = request.get_json()
    user = user_service.create_user(data)

    if user:
        return jsonify(user.to_dict()), 201
    else:
        return jsonify({'message': 'Failed to create user'}), 400


@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_service = get_user_service()
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data)

    if updated_user:
        return jsonify(updated_user.to_dict())
    else:
        return jsonify({'message': 'User not found'}), 404


@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service = get_user_service()
    user_service.delete_user(user_id)
    return jsonify({'message': 'User deleted'}), 200
