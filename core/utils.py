from decimal import Decimal, ROUND_DOWN
from datetime import datetime

_dtwo = Decimal("0.01")
_deight = Decimal("0.00000001")


def decimal_two(value):
    if type(value) != Decimal:
        try:
            value = Decimal(str(value))
        except (Exception,):
            return None
    return value.quantize(_dtwo, rounding=ROUND_DOWN)


def decimal_eight(value):
    if type(value) != Decimal:
        try:
            value = Decimal(str(value))
        except (Exception,):
            return None
    return value.quantize(_deight, rounding=ROUND_DOWN)


def days_between_dates(date1, date2):
    year1, month1, day1 = date1.split("-")
    year2, month2, day2 = date2.split("-")
    cur_day = datetime(int(year1), int(month1), int(day1))
    next_day = datetime(int(year2), int(month2), int(day2))
    return abs(next_day - cur_day)


# datetime转日期字符串str
def datetime_to_str(dt, fmt="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(fmt)


# 日期字符串str转datetime
def str_to_datetime(time_str, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(time_str, fmt)


# 日期字符串str转date
def str_to_date(time_str, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.date(str_to_datetime(time_str, fmt))


# date转日期字符串str
def date_to_str(date):
    return date.strftime("%Y-%m-%d")
