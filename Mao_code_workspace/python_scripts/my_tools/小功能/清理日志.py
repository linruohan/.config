import os
import time
import datetime

def strToTimestamp(time_st, format='%Y%m%d%H%M%S'):
    # 20181128113859
    # 这个函数是格式化好的时间，转时间戳的
    t = time.strptime(time_st, format)  # 把格式化好的时间转成时间元组
    res = time.mktime(t)  # 时间元组转成时间戳
    return res


def timestampToStr(time_strmp, format='%Y%m%d%H%M%S'):
    # 时间戳转格式化好的时间
    cur_time = time.localtime(time_strmp)  # 时间戳转成时间元组
    res = time.strftime(format, cur_time)  # 再把时间元组转成格式化好的时间
    return res


def clean_log(path):
    if os.path.exists(path) and os.path.isdir(path):
        today = time.strftime('%Y-%m-%d')  # 20170102
        cur_timestamp = strToTimestamp(today, '%Y-%m-%d')
        yesterday = cur_timestamp - 86400
        before_yesterday = yesterday - 86400
        file_name_list = [today, timestampToStr(
            yesterday, '%Y-%m-%d'), timestampToStr(before_yesterday, '%Y-%m-%d')]
        for file in os.listdir(path):
            file_name_sp = file.split('.')
            if len(file_name_sp) > 2:
                file_date = file_name_sp[1]  # 取文件名里面的日期
                if file_date not in file_name_list:
                    abs_path = os.path.join(path, file)
                    print('删除的文件是%s,' % abs_path)
                    os.remove(abs_path)
                else:
                    print('没有删除的文件是%s' % file)
    else:
        print('路径不存在/不是目录')


clean_log(r'C:/Users/dmj/Desktop/logs')
# 通过datetime实现


def clean_log(path):
    if os.path.exists(path) and os.path.isdir(path):
        today = datetime.date.today().strftime('%y-%m-%d')  # 2017-01-02
        yesterday = (datetime.date.today() +
                     datetime.timedelta(-1)).strftime('%Y-%m-%d')
        before_yesterday = (datetime.date.today() +
                            datetime.timedelta(-2)).strftime('%Y-%m-%d')
        file_name_list = [today, yesterday, before_yesterday]
        for file in os.listdir(path):
            file_name_sp = file.split('.')
            if len(file_name_sp) > 2:
                file_date = file_name_sp[1]  # 取文件名里面的日期
                # print type(file_date)
                # print type(file_name_list[0])
                if file_date not in file_name_list:
                    abs_path = os.path.join(path, file)
                    print('删除的文件是%s,' % abs_path)
                    os.remove(abs_path)
                else:
                    print('没有删除的文件是%s' % file)
    else:
        print('路径不存在/不是目录')


clean_log(r'C:/Users/dmj/Desktop/logs')
