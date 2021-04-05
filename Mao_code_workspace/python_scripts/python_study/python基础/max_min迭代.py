#coding=utf-8
from collections import Iterable
def findmax_min(L):
    if len(L)==0:
        return None
    else:
        if isinstance(L,Iterable):
            for i in range(0,len(L)):
                for j in range(i,len(L)):
                    if L[i]>L[j]:
                        L[i],L[j]=L[j],L[i]
            print(L[0],L[-1])
            return L[0],L[-1]
        else:
            print(u'error,您输入的是非可迭代数据')

L=[-200,99,102,1,2,5,388,22,789,0,-150]
findmax_min(L)
L1=[]
findmax_min(L1)
