# _*_coding:utf-8_*_

import urllib2
import http.cookiejar
from bs4 import BeautifulSoup
import re
import time
import threading

start = start_time = time.ctime()
s = []
max_length = 30
condition = threading.Condition()


class Producer(threading.Thread):
    def run(self):
        for i in range(20):
            condition.acquire()
            if len(s) == max_length:
                print( 's is full')
                condition.wait()
            request_url = 'https://site.douban.com/widget/public_album/86320/?start=%s' % (i*30) #推荐相册的url

            headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                }

            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(http.cookiejar.CookieJar()))
            response = urllib2.Request(request_url, headers=headers)
            html = opener.open(response)
            soup = BeautifulSoup(html)
            img_urls = soup.find_all('a', {'class': 'album_photo'})

            for item in img_urls:
                p = re.compile(r'src="(.*?)"')
                img_url = p.search(str(item.find('img'))).group(1)  #图片的url
                s.append(img_url)
                print( 'producer somthing')
            condition.notify()


class Consumer(threading.Thread):
    def run(self):
        count = 0
        while True:
            if condition.acquire():
                if not s:
                    print( 's is empty wait')
                    condition.wait()
                img_url = s.pop(0)
                print( 'consumer something')
                with open('E:\\douban\\%s.jpg' %count, 'wb') as fp:
                    try:
                        response_img = urllib2.urlopen(img_url).read() #下载图片
                        fp.write(response_img)
                    except Exception:
                        print( 'error')
                count += 1
                condition.notify()
                condition.release()

t1 = Producer()
c1 = Consumer()
t1.start()
c1.start()