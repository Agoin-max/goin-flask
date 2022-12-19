import os

# 项目基础配置
ENV = "development"  # 开发模式
DEBUG = True

# mysql配置
SQLALCHEMY_DATABASE_URI = "mysql://root:12345678@127.0.0.1:3306/flask"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
