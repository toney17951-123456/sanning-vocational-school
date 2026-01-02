from flask.cli import FlaskGroup
from app import create_app, db
from models.user import User
from models.teacher import Teacher
from models.course import Course
from models.news import News
from models.application import Application

app = create_app()
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    """创建数据库表"""
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("数据库表创建成功！")

@cli.command("seed_db")
def seed_db():
    """填充初始数据"""
    # 创建管理员用户
    admin = User(username="admin", role="admin")
    admin.set_password("admin123")
    
    # 创建示例教师
    teacher1 = Teacher(
        name="张老师",
        title="高级讲师",
        bio="10年Web开发经验，擅长前端技术"
    )
    
    teacher2 = Teacher(
        name="李老师",
        title="资深讲师",
        bio="8年Python开发经验，专注于后端开发"
    )
    
    # 创建示例课程
    course1 = Course(
        name="Web前端开发",
        description="学习HTML、CSS、JavaScript、Vue.js等前端技术",
        price=3999.0,
        duration="3个月",
        teacher_id=1
    )
    
    course2 = Course(
        name="Python后端开发",
        description="学习Python、Flask、Django等后端技术",
        price=4999.0,
        duration="4个月",
        teacher_id=2
    )
    
    # 创建示例新闻
    news1 = News(
        title="三宁职校2025年春季招生开始",
        content="三宁职校2025年春季招生现已开始，欢迎广大学生报名咨询。",
        author="管理员"
    )
    
    # 添加到数据库
    db.session.add_all([admin, teacher1, teacher2, course1, course2, news1])
    db.session.commit()
    print("初始数据填充成功！")

if __name__ == "__main__":
    cli()