#coding=utf-8
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
'''
the first
'''
# def createcouter():
#     f=[0]
#     def counter():
#         f[0]=f[0]+1
#         return f[0]
#     return counter
#

'''
the second
'''
def createcouter():
    f=0
    def counter():
        # 使用 nonlocal 修改外层变量
        nonlocal f
        f+=1
        return f
    return counter




counterA=createcouter()
print(counterA(),counterA(),counterA(),counterA(),)
counterB=createcouter()
if [counterB(),counterB(),counterB(),counterB()]==[1,2,3,4]:
    print(u"测试通过！")
else:
    print(u"测试失败！")
