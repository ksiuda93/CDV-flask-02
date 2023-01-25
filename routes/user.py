from . import Blueprint, jsonify, request
from models.User import User, UserSchema
from flask_jwt import jwt_required, current_identity

user_bp = Blueprint('user', __name__)
users = []


@user_bp.get('/user')
@jwt_required()
def get_user():
    return jsonify(UserSchema().dump(current_identity))

@user_bp.get('/users')
@jwt_required()
def get_all_user():
    return jsonify(UserSchema(many=True).dump(User.query.all()))


@user_bp.post('/user')
def add_user():
    user = User(**request.get_json())
    if user.add_user():
        return jsonify(request.get_json()), 201
    else:
        return jsonify(
            {
                "ERROR": "User issue!"
            }
        ), 404


@user_bp.delete('/user')
@jwt_required()
def delete_user():
    if current_identity.delete_user():
        return jsonify({
            "INFO": f"User {current_identity.id} deleted!"
        })
    else:
        return jsonify(
            {
                "ERROR": "User issue!"
            }
        ), 404