#coding =utf-8
'''
把test——case的目录添加到path下，这里用的是相对路径

'''
import sys
sys.path.append("D:\\Python\\testsuit\\test_case")
from test_case import baidu
from test_case import youdao

#用例列表
def caselist():
    alltestnames=[
    baidu.Baidu,
    youdao.Youdao,
    ]
    print("success read case list!!")
    return alltestnames
caselist()
