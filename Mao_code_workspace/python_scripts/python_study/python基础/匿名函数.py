#coding=utf-8

def is_odd(n):
    return n%2==0
f=lambda x:x%2==0
print(f(3))
lo=list(filter(is_odd,range(1,21)))
print(lo)

lj=list(filter(lambda x:x%2,range(1,20)))
print(lj)
