from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User
from app import db
from . import main_bp

@main_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    
    return jsonify({'message': 'Invalid username or password'}), 401

@main_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'Protected route'}), 200