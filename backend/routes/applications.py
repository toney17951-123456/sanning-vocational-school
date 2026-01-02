from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models.application import Application
from models.course import Course
from app import db
from . import main_bp

@main_bp.route('/applications', methods=['GET'])
@jwt_required()
def get_applications():
    applications = Application.query.all()
    return jsonify([{
        'id': app.id,
        'name': app.name,
        'phone': app.phone,
        'email': app.email,
        'course': app.course.name if app.course else None,
        'status': app.status,
        'payment_method': app.payment_method,
        'payment_status': app.payment_status,
        'created_at': app.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for app in applications]), 200

@main_bp.route('/applications/<int:app_id>', methods=['GET'])
@jwt_required()
def get_application(app_id):
    app = Application.query.get_or_404(app_id)
    return jsonify({
        'id': app.id,
        'name': app.name,
        'phone': app.phone,
        'email': app.email,
        'course': {
            'id': app.course.id,
            'name': app.course.name,
            'price': app.course.price
        } if app.course else None,
        'status': app.status,
        'payment_method': app.payment_method,
        'payment_status': app.payment_status,
        'created_at': app.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }), 200

@main_bp.route('/applications', methods=['POST'])
def create_application():
    data = request.get_json()
    
    # 检查课程是否存在
    course = Course.query.get(data['course_id'])
    if not course:
        return jsonify({'message': 'Course not found'}), 404
    
    application = Application(
        name=data['name'],
        phone=data['phone'],
        email=data.get('email'),
        course_id=data['course_id']
    )
    
    db.session.add(application)
    db.session.commit()
    
    return jsonify({'message': 'Application created successfully'}), 201

@main_bp.route('/applications/<int:app_id>', methods=['PUT'])
@jwt_required()
def update_application(app_id):
    application = Application.query.get_or_404(app_id)
    data = request.get_json()
    
    if 'status' in data:
        application.status = data['status']
    
    if 'payment_method' in data:
        application.payment_method = data['payment_method']
    
    if 'payment_status' in data:
        application.payment_status = data['payment_status']
    
    db.session.commit()
    
    return jsonify({'message': 'Application updated successfully'}), 200

@main_bp.route('/applications/<int:app_id>', methods=['DELETE'])
@jwt_required()
def delete_application(app_id):
    application = Application.query.get_or_404(app_id)
    db.session.delete(application)
    db.session.commit()
    
    return jsonify({'message': 'Application deleted successfully'}), 200