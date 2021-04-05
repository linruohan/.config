#coding=utf-8
from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1]))
print(reduce(fn, [1, 3]))
print(reduce(fn, [1, 3, 5]))
print(reduce(fn, [1, 3, 5, 7]))
print(reduce(fn, [1, 3, 5, 7,9]))

l=[1,2,3,44,55,1,32]
print(sum(l))
