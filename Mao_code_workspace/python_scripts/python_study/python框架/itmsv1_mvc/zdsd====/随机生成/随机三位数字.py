# coding=utf-8
from random import sample
import sys,io,random
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def sj_3():
    s = random.randint(100,999)
    return str(s)
print(sj_3())
