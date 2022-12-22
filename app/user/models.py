from datetime import datetime
from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    name = db.Column(db.String(32), nullable=False, unique=True, comment="用户名")
    password = db.Column(db.String(256), nullable=True, comment="密码")
    gender = db.Column(db.Integer, nullable=True, comment="性别")
    age = db.Column(db.Integer, nullable=True, comment="年龄")
    phone = db.Column(db.String(32), comment="电话号码")
    email = db.Column(db.String(20), unique=True, comment="邮箱")
    isActive = db.Column(db.Boolean, default=True, comment="是否活跃")
    isAdmin = db.Column(db.Integer, default=0)
    createTime = db.Column(db.DateTime, default=datetime.utcnow(), comment="创建时间")
    updateTime = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), comment="修改时间")
