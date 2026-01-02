from app import db

class Teacher(db.Model):
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    avatar = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # 关联课程
    courses = db.relationship('Course', backref='teacher', lazy=True)