from datetime import datetime
from exts import db


class BaseModel(db.Model):
    # 基类模型
    __abstract__ = True

    createTime = db.Column(db.DateTime, default=datetime.utcnow(), comment="创建时间")
    updateTime = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), comment="修改时间")


class Category(BaseModel):
    """
        分类模型
    """
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    name = db.Column(db.String(128), nullable=False)
    icon = db.Column(db.String(128), nullable=True)

    post = db.relationship("Post", backref="category", lazy=True)

    def __repr__(self):
        return "<Category %r>" % self.name


# 多对多关系
tags = db.Table("tags",
                db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
                db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
                )


class Post(BaseModel):
    """
        文章模型
    """
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    title = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.String(128), nullable=True)
    content = db.Column(db.Text, nullable=True)
    # 一对多
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    # 多对多
    tags = db.relationship("Tag", secondary=tags, lazy="subquery", backref=db.backref("post", lazy=True))

    def __repr__(self):
        return "<Post %r>" % self.title


class Tag(BaseModel):
    """
        文章标签
    """
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    name = db.Column(db.String(128), nullable=False, unique=True)

    def __repr__(self):
        return "<Tag %r>" % self.name
