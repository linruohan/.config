import re,os
import urllib.request
import urllib.error
import time


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        try:
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
            "'发出请求'"
            request = urllib.request.Request(url=url, headers=header)
            "'获取结果'"
            response = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        if response.getcode() != 200:
            return None
        html = response.read()
        response.close()
        return html


class Image(object):
    def ImageGet(self, imageurl, image_path):
        x = 0
        for li in imageurl:
            urllib.request.urlretrieve(li, image_path % x)
            x = x + 1
            print('第%s张'%x+' '+li)
            "'休眠5s以免给服务器造成严重负担'"
            time.sleep(2)
# "'起始URL'"
# # url = "https://www.douban.com"
# url = "https://www.douban.com/people/viva-l/photos"
# "'保存目录'"
# image_path = os.path.dirname(__file__)+"/douban/Image%s.jpg"
# "'定义实体类'"
# downloader = HtmlDownloader()
# html = downloader.download(url)
# "'SaveFile(html, html_path)'"
# html = html.decode('utf-8')
# "'正则表达式'"
# reg1 = r'="(https://img[\S]*?[jpg|png])"'
# "'提取图片的URL'"
# dbdata = re.findall(reg1, html)
# imgsave = Image()
# #
# "'下载保存图片'"
# imgsave.ImageGet(dbdata, image_path)


import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
for i in range(1,51):
    url = "https://ypy.douban.com/package?page="+str(i)
    r = requests.get(url, headers = headers)
    bsObj = BeautifulSoup(r.text, "html.parser") #urllib.request不需要加`.text`
    imagesSet = bsObj.findAll("a", {"class": "lnk-pic-card"})
    for image in imagesSet:
        photoUrl = "https://ypy.douban.com"+image["href"]
        r1 = requests.get(photoUrl, headers = headers)
        bsObj1 = BeautifulSoup(r1.text, "html.parser")
        images = bsObj1.findAll("div", {"class": "pic-wrapper"})
        for image1 in images:
            photoName = image1.img.attrs["data-src"][28:]+".jpg" #创造独一无二的文件名
            urlretrieve(image1.img.attrs["data-src"], photoName) #Python自带的保存多媒体文件的方法
    print(i) #打印下载的页数信息

