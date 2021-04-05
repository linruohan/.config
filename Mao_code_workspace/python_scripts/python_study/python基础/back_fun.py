#coding=utf-8

def count():
    fs=[]
    def f(j):
        def g():
            return j*j
        return g
    for i in range(1,4):
        fs.append(f(i))
    return fs


m,n,s=count()
print(m())
print(n())
print(s())
