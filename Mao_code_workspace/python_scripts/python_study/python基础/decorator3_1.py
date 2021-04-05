import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s begining====== call %s()" % (text, func.__name__))
            ret = func(*args, **kw)
            print("%s ending======== call %s()" % (text, func.__name__))
            return ret
        return wrapper
    if isinstance(text, str):
        return decorator
    else:
        f = text
        text = '-'
        return decorator(f)

@log
def f1():
    print("12345!")
@log('excute')
def f2():
    print("shang shan da laohu!")
f1()
f2()
