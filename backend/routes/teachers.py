from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models.teacher import Teacher
from models.course import Course
from app import db
from . import main_bp

@main_bp.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = Teacher.query.all()
    return jsonify([{
        'id': teacher.id,
        'name': teacher.name,
        'title': teacher.title,
        'bio': teacher.bio,
        'avatar': teacher.avatar,
        'courses_count': len(teacher.courses)
    } for teacher in teachers]), 200

@main_bp.route('/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return jsonify({
        'id': teacher.id,
        'name': teacher.name,
        'title': teacher.title,
        'bio': teacher.bio,
        'avatar': teacher.avatar,
        'courses': [{ 
            'id': course.id, 
            'name': course.name 
        } for course in teacher.courses]
    }), 200

@main_bp.route('/teachers', methods=['POST'])
@jwt_required()
def create_teacher():
    data = request.get_json()
    
    teacher = Teacher(
        name=data['name'],
        title=data.get('title'),
        bio=data.get('bio'),
        avatar=data.get('avatar')
    )
    
    db.session.add(teacher)
    db.session.commit()
    
    return jsonify({'message': 'Teacher created successfully'}), 201

@main_bp.route('/teachers/<int:teacher_id>', methods=['PUT'])
@jwt_required()
def update_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    data = request.get_json()
    
    teacher.name = data.get('name', teacher.name)
    teacher.title = data.get('title', teacher.title)
    teacher.bio = data.get('bio', teacher.bio)
    teacher.avatar = data.get('avatar', teacher.avatar)
    
    db.session.commit()
    
    return jsonify({'message': 'Teacher updated successfully'}), 200

@main_bp.route('/teachers/<int:teacher_id>', methods=['DELETE'])
@jwt_required()
def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    db.session.delete(teacher)
    db.session.commit()
    
    return jsonify({'message': 'Teacher deleted successfully'}), 200