from flask import Blueprint

# 创建主蓝图
main_bp = Blueprint('main', __name__)

# 导入路由
from . import auth, users, teachers, courses, news, applications