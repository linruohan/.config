# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
import re

def to_timestamp(dt_str, tz_str):
    # 获取时区间隔小时数字int
    tz_num = int(re.match(r'(\w+)([-|\+]\d+):(\d+)',tz_str).group(2))
    # 处理时间转换成datetime类型
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    # 将本地时间切换为目标小时的时区UTC时间  datetime
    utc_dt = dt.replace(tzinfo = timezone(timedelta(hours=tz_num)))
    # 将datetime时间转换成timestamp时间类型
    ts = utc_dt.timestamp()
    return ts
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
