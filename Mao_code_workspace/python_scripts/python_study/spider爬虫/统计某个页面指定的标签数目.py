# coding=utf-8

#统计某个页面指定的标签（<a .../>.<script .../>数目
#用到re正则、字典

import re
from urllib.request import urlopen

def ParserWebHtml():
    url = "http://www.baidu.com";
    pageDoc = urlopen(url).read().decode("gbk");

    #正则处理，生成结果列表
    pattern = re.compile(r"<[a-zA-Z]* "); #匹配诸如"<a ","<div "，”<script "类型
    list = pattern.findall(pageDoc);

    #解析同时统计
    calc = {    "div" : 0,
                "script" : 0,
                "a" : 0
            }
    for listItem in list:
        tag = listItem[1 : len(listItem) - 1];
        if tag in calc.keys():
            calc[tag] += 1;
        elif tag is not "":
            calc[tag] = 1;
    #输出
    for tagName,count in calc.items():
        print ("标签：",tagName,"\t出现次数：" , count);

if __name__ == '__main__':
    ParserWebHtml();
