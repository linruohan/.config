# coding=utf-8
import requests,urllib.parse
import threading

# 设置最大线程锁 10
# thread_lock=threading.BoundedSemaphore(value=2)

def get_page(url):
    page=requests.get(url)
    page=page.content
    page=page.decode('utf-8')
    return page

def pages_from_duitang(key):
    pages=[]
    url='https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000'
    key=urllib.parse.quote(key)#将中文转成URL编码
    for i in range(0,3600,100):
        u=url.format(key,i)
        print(u)
        page=get_page(u)
        pages.append(page)
    return pages


def findallpage(page,startpart,endpart):
    all_str=[]
    end=0
    while page.find(startpart,end)!=-1:
        start=page.find(startpart,end)+len(startpart)
        end=page.find(endpart,start)
        string=page[start:end]
        all_str.append(string)
    return all_str


def pic_urls_frompages(pages):
    pic_urls=[]
    for page in pages:
        urls=findallpage(page,'path":"','"')
        pic_urls.extend(urls)#讲一个列表元素添加到另一个列表后面
    return pic_urls

def download(url,n):
    r=requests.get(url)#下载
    path='D:/图片/'+str(n)+'.jpg'
    with open(path,'wb') as f:
        f.write(r.content)
    # 下载完了解锁
    # thread_lock.release()

def main(key):
    pages=pages_from_duitang(key)
    pic_urls=pic_urls_frompages(pages)
    n=0
    for url in pic_urls:
        n+=1
        print('正在下载第{}张图片'.format(n))
        # thread_lock.accquire()# 上锁
        # t=threading.Thread(target=download,args=(url,n))
        # t.start()
        download(url,n)


main('美女')
