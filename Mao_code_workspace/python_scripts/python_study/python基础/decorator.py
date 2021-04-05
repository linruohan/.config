#coding=utf-8

import time,datetime,functools

'''请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：'''
def metric(func):
    @functools.wraps(func)
    def  wrapper(*args,**kw):
        t1=datetime.datetime.now()
        result=func(*args,**kw)
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
if f!=33:
    print("failed x+y  _____:testing!")
elif s!=7986:
    print(s)
    print("failed x y z_____:testing!")
print(datetime.datetime.now())
