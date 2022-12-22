from flask import Flask
import settings
from app.admin.views import admin_bp
from app.user.views import user_bp
from app.debit.views import loan_bp
from exts import migrate
# models
from app.user.models import User
from app.blog.models import *
from app.debit.models import *


def create_app():
    # 创建flask app并指定相关目录
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    # 导入配置文件
    app.config.from_object(settings)
    # 添加数据库扩展
    db.init_app(app)
    # 数据库迁移
    migrate.init_app(app, db)
    # 注册蓝图
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(loan_bp, url_prefix="/loan")

    return app
