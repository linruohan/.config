#coding=utf-8
def triangles(n):
    L=[1]
    s=0
    while s<n:
        yield L
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        s=s+1


results=[]
for t in triangles(10):
    print(t)
    results.append(t)

num = len(results)
def print_backspace(n):
    str = ''
    for i in range(n):
        print(' '), #打印不换行
for l in results:
    print_backspace(2 * (num - 1))
    num = num - 1
    for n in l:
        print('%8d' % n), #调整数据输出格式，不然因为数字位数不一样，显示会有差距
    print('\n')
