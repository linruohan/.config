#coding=utf-8
import sys,io,time
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')



def f(func):
    def s(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return s


@f
def now():
    time1=time.strftime(' %Y-%m-%d  %H:%M:%S ',time.localtime(time.time()))
    print(u"打印日志：》》》》》"+time1)


now()
