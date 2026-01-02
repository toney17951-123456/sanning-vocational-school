from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models.course import Course
from models.teacher import Teacher
from app import db
from . import main_bp

@main_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{
        'id': course.id,
        'name': course.name,
        'description': course.description,
        'price': course.price,
        'duration': course.duration,
        'teacher_name': course.teacher.name if course.teacher else None
    } for course in courses]), 200

@main_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify({
        'id': course.id,
        'name': course.name,
        'description': course.description,
        'price': course.price,
        'duration': course.duration,
        'teacher': {
            'id': course.teacher.id,
            'name': course.teacher.name,
            'title': course.teacher.title
        } if course.teacher else None
    }), 200

@main_bp.route('/courses', methods=['POST'])
@jwt_required()
def create_course():
    data = request.get_json()
    
    # 检查教师是否存在
    teacher = Teacher.query.get(data['teacher_id'])
    if not teacher:
        return jsonify({'message': 'Teacher not found'}), 404
    
    course = Course(
        name=data['name'],
        description=data.get('description'),
        price=data.get('price', 0.0),
        duration=data.get('duration'),
        teacher_id=data['teacher_id']
    )
    
    db.session.add(course)
    db.session.commit()
    
    return jsonify({'message': 'Course created successfully'}), 201

@main_bp.route('/courses/<int:course_id>', methods=['PUT'])
@jwt_required()
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()
    
    if 'teacher_id' in data:
        teacher = Teacher.query.get(data['teacher_id'])
        if not teacher:
            return jsonify({'message': 'Teacher not found'}), 404
        course.teacher_id = data['teacher_id']
    
    course.name = data.get('name', course.name)
    course.description = data.get('description', course.description)
    course.price = data.get('price', course.price)
    course.duration = data.get('duration', course.duration)
    
    db.session.commit()
    
    return jsonify({'message': 'Course updated successfully'}), 200

@main_bp.route('/courses/<int:course_id>', methods=['DELETE'])
@jwt_required()
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    
    return jsonify({'message': 'Course deleted successfully'}), 200