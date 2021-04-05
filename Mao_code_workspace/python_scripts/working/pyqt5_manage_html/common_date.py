# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

from datetime import datetime


def get_remain_date(end_date="2020-12-20 11:30", date_stamp_str='%Y-%m-%d %H:%M'):
    if "%S" in date_stamp_str:
        now_str = str(datetime.now()).split('.')[0]
    else:
        now_str = ":".join(str(datetime.now()).split('.')[0].split(":")[:-1])
    now = datetime.strptime(now_str, date_stamp_str)
    end_date = datetime.strptime(end_date, date_stamp_str)
    return str(end_date - now)


if __name__ == '__main__':
    str=get_remain_date()
    print(str)
