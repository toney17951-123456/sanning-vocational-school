from app import db

class Application(db.Model):
    __tablename__ = 'applications'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, paid, completed, cancelled
    payment_method = db.Column(db.String(20), nullable=True)  # wechat, alipay
    payment_status = db.Column(db.String(20), default='unpaid')  # unpaid, paid, failed
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # 关联课程
    course = db.relationship('Course', backref='applications', lazy=True)