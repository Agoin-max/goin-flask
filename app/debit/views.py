from datetime import datetime

from flask import Blueprint, request
import json
from app.debit.models import Currency, DebitCurrency, DebitUser, DebitOrder
from exts import db
from core.utils import decimal_eight, decimal_two, days_between_dates, str_to_date, date_to_str
import arrow

# 创建一个蓝图
loan_bp = Blueprint("loan", __name__)


@loan_bp.route("/currency/create", methods=["POST"])
def create_currency():
    data = request.get_data()
    dic = json.loads(data)
    currency_name = dic.get("currency_name")

    cur = Currency.query.filter_by(currency_name=currency_name.upper()).first()
    if not cur:
        db.session.add(Currency(currency_name=currency_name.upper()))
        db.session.commit()
        return {"message": "success"}
    else:
        return {"message": "fail"}


@loan_bp.route("/debit/currency/create", methods=["POST"])
def create_debit_currency():
    data = request.get_data()
    dic = json.loads(data)
    currency_id = dic.get("currency_id")
    max_amount = decimal_eight(dic.get("max_amount"))
    min_amount = decimal_eight(dic.get("min_amount"))
    rate = decimal_two(dic.get("rate"))
    overdue_rate = decimal_two(dic.get("overdue_rate"))

    deb = DebitCurrency.query.filter_by(currency_id=currency_id).first()
    if deb:
        return {"message": "fail"}

    dic_debit_currency = {"currency_id": currency_id, "max_amount": max_amount,
                          "min_amount": min_amount, "rate": rate, "overdue_rate": overdue_rate}
    db.session.add(DebitCurrency(**dic_debit_currency))
    db.session.commit()
    return {"message": "success"}


@loan_bp.route("/opened/debit", methods=["POST"])
def opened_debit():
    data = request.get_data()
    dic = json.loads(data)
    user_id = dic.get("user_id")
    currency_id = dic.get("currency_id")

    # 逻辑 -> 实名认证给多少额度
    deb = DebitUser(**{"user_id": user_id, "currency_id": currency_id, "amount": 1000, "borrowing_times": 0, "used": 0})
    db.session.add(deb)
    db.session.commit()

    return {"message": "success"}


@loan_bp.route("/orders", methods=["POST"])
def generate_orders():
    """借款订单"""
    data = request.get_data()
    dic = json.loads(data)
    user_id = dic.get("user_id")
    currency_id = dic.get("currency_id")
    amount = dic.get("amount")
    rate = dic.get("rate")
    start_time = dic.get("start_time")
    end_time = dic.get("end_time")

    # 校验借款资格 DebitUser 产品的逻辑 pass

    # 生成借款订单
    days = days_between_dates(start_time, end_time)
    print(days.days)

    start_utc_time = arrow.get(start_time).to("UTC").strftime("%Y-%m-%d")
    end_utc_time = arrow.get(end_time).to("UTC").strftime("%Y-%m-%d")

    deb = DebitOrder(**{"user_id": user_id, "currency_id": currency_id, "amount": amount, "rate": rate,
                        "startTime": start_utc_time, "endTime": end_utc_time, "days": days.days,
                        "status": 1})
    db.session.add(deb)
    db.session.commit()

    return {"message": "success"}


@loan_bp.route("/repayment/info", methods=["POST"])
def repayment():
    """还款"""
    data = request.get_data()
    dic = json.loads(data)
    order_id = dic.get("id")

    deb = DebitOrder.query.filter_by(id=order_id).first()
    end_time = arrow.get(datetime.now()).to("UTC").strftime("%Y-%m-%d")
    print(end_time)

    # 提前还款情况|准时还款
    if deb.endTime >= str_to_date(end_time, fmt="%Y-%m-%d"):
        days = days_between_dates(date_to_str(deb.startTime), end_time)
        # 提前还款利息
        prepayment_interest = decimal_two(deb.rate * deb.amount / 365 * days.days)
    # 逾期
    else:
        pass

    return {"message": "success"}
