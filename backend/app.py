import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化数据库
db = SQLAlchemy()

# 初始化JWT
jwt = JWTManager()

# 初始化迁移
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # 配置
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+pymysql://root:password@localhost:3306/saning_school')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-jwt-secret-key')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 令牌过期时间：1小时
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 2592000  # 刷新令牌过期时间：30天
    
    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    # 优化CORS配置
    cors_config = {
        "origins": [
            "http://localhost:5173",  # 开发环境
            "http://127.0.0.1:5173",  # 开发环境
            "https://*.github.io"      # GitHub Pages 环境
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
    CORS(app, **cors_config)
    
    # 添加安全响应头
    @app.after_request
    def set_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
    
    # 注册蓝图
    from routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    # 生产环境禁用debug
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(debug=debug)