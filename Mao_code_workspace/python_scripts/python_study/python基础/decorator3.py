#coding=utf-8

import time,datetime,functools
'''能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
'''





def log(arg):
    if not isinstance(arg, str):
        @functools.wraps(arg)
        def wrappers(*args, **kw):
            print('%s()' % arg.__name__)
            return arg(*args, **kw)
        return wrappers
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrappers(*args, **kw):
                print('%s %s()' % (arg, func.__name__))
                return func(*args, **kw)
            return wrappers
        return decorator


@log
def f1():
    print('log')


@log('execute')
def f2():
    print('log  execute')

f1()
f2()
