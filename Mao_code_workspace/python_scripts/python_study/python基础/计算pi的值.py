#coding=utf-8


import itertools
n=8

iter=itertools.cycle((4,-4))

list1=[i for i in range(2*n) if i%2]
s1=map(lambda x:next(iter)/x,list1)
print(list1)
print(sum(s1))

list=[i for i in itertools.takewhile(lambda x:x<=2*n-1,itertools.count(1,2))]
s=map(lambda x:next(iter)/x,list)
print(list)
print(sum(s))

# print(sum(4/n*(-1)**i for i,n in enumerate(itertools.takewhile(lambda x: x<=2*n-1,itertools.count(1,2)))))
def pi(n):
    #计算pi的前N项和

    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    list=[i for i in range(2*n) if i%2]
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    L = [2 * i + 1 for i in range(n)]
    ns = itertools.cycle((4,-4))
    return sum(next(ns)/x for x in L)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...



# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
