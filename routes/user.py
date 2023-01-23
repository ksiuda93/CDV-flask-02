from . import Blueprint, jsonify, request
from models.User import User, UserSchema

user_bp = Blueprint('user', __name__)
users = []


@user_bp.get('/user/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    if user is not None:
        return jsonify(UserSchema().dump(user))
    else:
        return jsonify(
            {
                "ERROR": "User does not exist!"
            }
        ), 404


@user_bp.get('/users')
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


#int, float, any, uuid
@user_bp.delete('/user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify(
            {
                "ERROR": "User does not exist!"
            }
        ), 404
    if user.delete_user():
        return jsonify({
            "INFO": f"User {user_id} deleted!"
        })
    else:
        return jsonify(
            {
                "ERROR": "User issue!"
            }
        ), 404