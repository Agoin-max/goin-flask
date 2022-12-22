from datetime import datetime, date
from exts import db


class BaseModel(db.Model):
    # 基类模型
    __abstract__ = True

    createTime = db.Column(db.DateTime, default=datetime.utcnow(), comment="创建时间")
    updateTime = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), comment="修改时间")


class Currency(BaseModel):
    __tablename__ = 'currency'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    currency_name = db.Column(db.String(32), nullable=False, index=True, comment="币种名称")
    icon = db.Column(db.String(50), nullable=True, comment="币种图标")
    isActive = db.Column(db.Boolean, default=True, comment="是否启用")

    def __repr__(self):
        return "<Currency %r>" % self.currency_name


class DebitCurrency(BaseModel):
    __tablename__ = 'debit_currency'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    max_amount = db.Column(db.DECIMAL(25, 8), nullable=False, comment="最多可借额度")
    min_amount = db.Column(db.DECIMAL(25, 8), nullable=False, comment="最少可借额度")
    rate = db.Column(db.DECIMAL(5, 2), nullable=False, comment="利率")
    overdue_rate = db.Column(db.DECIMAL(5, 2), nullable=False, comment="逾期利率")
    isActive = db.Column(db.Boolean, default=True, comment="是否启用")

    currency_id = db.Column(db.Integer, db.ForeignKey("currency.id"), nullable=False, index=True, comment="币种ID")
    currency = db.relationship("Currency", backref="debit_currency", uselist=False)

    def __repr__(self):
        return "<DebitCurrency %r>" % self.currency.currency_name


class DebitUser(BaseModel):
    __tablename__ = 'debit_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    amount = db.Column(db.DECIMAL(25, 8), default=0, comment="可用额度")
    borrowing_times = db.Column(db.Integer, comment="借款次数")
    used = db.Column(db.DECIMAL(25, 8), default=0, comment="已使用")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True, comment="用户ID")
    user = db.relationship("User", backref="debit_user", uselist=False)

    currency_id = db.Column(db.Integer, db.ForeignKey("currency.id"), nullable=False, index=True, comment="币种ID")
    currency = db.relationship("Currency", backref="debit_user", uselist=False)

    def __repr__(self):
        return "<DebitUser %r>" % self.user.name


class DebitOrder(BaseModel):
    __tablename__ = 'debit_order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="主键")
    amount = db.Column(db.DECIMAL(10, 2), default=0, comment="金额")
    fee = db.Column(db.DECIMAL(10, 2), default=0, comment="手续费")
    liquidated_damages = db.Column(db.DECIMAL(10, 2), default=0, comment="违约金")
    prepayment_interest = db.Column(db.DECIMAL(10, 2), default=0, comment="提前还款利息")
    rate = db.Column(db.DECIMAL(5, 2), nullable=False, comment="利率")
    days = db.Column(db.Integer, nullable=False, comment="借款天数")
    status = db.Column(db.Integer, comment="状态 1进行中 2完成")
    startTime = db.Column(db.Date, default=datetime.utcnow(), comment="开始时间")
    endTime = db.Column(db.Date, default=datetime.utcnow(), comment="结束时间")
    repaymentTime = db.Column(db.Date, default=datetime.utcnow(), comment="还款时间")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True, comment="用户ID")
    user = db.relationship("User", backref="debit_order", uselist=False)

    currency_id = db.Column(db.Integer, db.ForeignKey("currency.id"), nullable=False, index=True, comment="币种ID")
    currency = db.relationship("Currency", backref="debit_order", uselist=False)
