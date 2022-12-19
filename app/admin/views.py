from flask import Blueprint

# 创建一个蓝图
admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
