from flask import Blueprint, request
import json
from app.user.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from exts import db
import redis

r = redis.Redis(host='localhost', port=6379, db=6, decode_responses=True)

# 创建一个蓝图
user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_data()
    dic = json.loads(data)
    username = dic.get("username")
    password = dic.get("password")

    user = User.query.filter(User.name == username).first()
    if not user:
        create = User(name=username, password=generate_password_hash(password))
        db.session.add(create)
        db.session.commit()
        return {"message": "success"}
    return {"message": "user is exist"}


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_data()
    dic = json.loads(data)
    username = dic.get("username")
    password = dic.get("password")

    user = User.query.filter_by(name=username).first()
    if not user:
        return {"message": "user is not register"}
    if not check_password_hash(user.password, password=password):
        return {"message": "password is error"}
    r.set(username, user.password, ex=60)
    return {"message": "success"}
