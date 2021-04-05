# coding=utf-8
import re
import urllib.request
import os
from selenium import webdriver  #########需要先安装selenium

user = 'mjt1220'  #########用户名
theurl = 'http://' + user + '.blog.163.com/blog'
thepath = 'D:\\wa'  #########选择一个路径，确保其中存在url_path.txt
url_path = thepath + '\\' + 'url_path.txt'  # 存储该用户所有页面链接
phantomjs_path = "C:\phantomjs.exe"  #########需要先下载phantomjs.exe
coding = 'gbk'  #########这个要去网页源代码里面查


def get_all_url():  # 获取该用户所有页面链接
    already = []
    all_url = ['http://jason0320.blog.163.com/blog/static/2703529720161017111442198']
    fp = open(url_path, 'r')
    lines = fp.readlines()
    for line in lines:
        line = line.strip('\n')
        if line == '':
            continue
        already.append(line)
        all_url.append(line)
    fp.close()
    driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_args=['--load-images=no'])  # 不加载图片，加快速度
    i = 0
    fp = open(url_path, 'w')
    already = list(set(already))
    for each in already:
        fp.write(each + '\n')
    while (i < len(all_url)):
        url = all_url[i]
        i = i + 1
        try:
            driver.get(url)
        except:
            print('连接失败')
            print(url)
            continue
        html = driver.page_source
        url_list = re.findall('.blog.163.com/blog/static/[0-9]*', html)
        for each in url_list:
            u = 'http://' + user + each
            if u not in all_url:
                all_url.append(u)  # 广度优先搜索
            if u not in already:
                fp.write(u + '\n')
                already.append(u)
        print(i)
    fp.close()


if __name__ == '__main__':
    get_all_url()
