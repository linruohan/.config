#coding=utf-8

import time,datetime,functools
'''请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。'''
def metric(func):
    @functools.wraps(func)
    def  wrapper(*args,**kw):
        print("begin call")
        t1=datetime.datetime.now()
        result=func(*args,**kw)
        print('call %s():' %func.__name__)
        print("end call")
        t2=datetime.datetime.now()
        print("%s excutedd in %s ms" %(func.__name__,t2-t1))
        return result
    return wrapper

#测试
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y


@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

f=fast(11,22)
print(f)
s=slow(11,22,33)
print(s)
