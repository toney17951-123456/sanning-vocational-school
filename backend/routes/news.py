from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models.news import News
from app import db
from . import main_bp

@main_bp.route('/news', methods=['GET'])
def get_news():
    news = News.query.filter_by(is_published=True).order_by(News.created_at.desc()).all()
    return jsonify([{
        'id': news_item.id,
        'title': news_item.title,
        'content': news_item.content[:100] + '...' if len(news_item.content) > 100 else news_item.content,
        'author': news_item.author,
        'cover_image': news_item.cover_image,
        'created_at': news_item.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for news_item in news]), 200

@main_bp.route('/news/<int:news_id>', methods=['GET'])
def get_news_item(news_id):
    news_item = News.query.get_or_404(news_id)
    if not news_item.is_published:
        return jsonify({'message': 'News not found'}), 404
    
    return jsonify({
        'id': news_item.id,
        'title': news_item.title,
        'content': news_item.content,
        'author': news_item.author,
        'cover_image': news_item.cover_image,
        'created_at': news_item.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }), 200

@main_bp.route('/news/admin', methods=['GET'])
@jwt_required()
def get_all_news():
    news = News.query.order_by(News.created_at.desc()).all()
    return jsonify([{
        'id': news_item.id,
        'title': news_item.title,
        'author': news_item.author,
        'is_published': news_item.is_published,
        'created_at': news_item.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for news_item in news]), 200

@main_bp.route('/news', methods=['POST'])
@jwt_required()
def create_news():
    data = request.get_json()
    
    news_item = News(
        title=data['title'],
        content=data['content'],
        author=data.get('author'),
        cover_image=data.get('cover_image'),
        is_published=data.get('is_published', True)
    )
    
    db.session.add(news_item)
    db.session.commit()
    
    return jsonify({'message': 'News created successfully'}), 201

@main_bp.route('/news/<int:news_id>', methods=['PUT'])
@jwt_required()
def update_news(news_id):
    news_item = News.query.get_or_404(news_id)
    data = request.get_json()
    
    news_item.title = data.get('title', news_item.title)
    news_item.content = data.get('content', news_item.content)
    news_item.author = data.get('author', news_item.author)
    news_item.cover_image = data.get('cover_image', news_item.cover_image)
    if 'is_published' in data:
        news_item.is_published = data['is_published']
    
    db.session.commit()
    
    return jsonify({'message': 'News updated successfully'}), 200

@main_bp.route('/news/<int:news_id>', methods=['DELETE'])
@jwt_required()
def delete_news(news_id):
    news_item = News.query.get_or_404(news_id)
    db.session.delete(news_item)
    db.session.commit()
    
    return jsonify({'message': 'News deleted successfully'}), 200