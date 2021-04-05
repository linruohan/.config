import re, os
import urllib.request
import urllib.error
import time
from urllib.request import urlretrieve
import requests, re
from bs4 import BeautifulSoup
from proxies_random_ip import Proxies
Proxies=Proxies()
class Douban:
    def cbk(self, a, b, c):
        '''''回调函数
        @a:已经下载的数据块
        @b:数据块的大小
        @c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print ('%.2f%%' % per)

    def __init__(self, url):
        self.url = url
        self.upzhu = self.url.split ('/')[-2]
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    def get_xiangceSet_page_urls(self):
        '''相册列表分20页显示，每页18个相册，
        return：获取每页的url'''
        dic = {}
        r = requests.get (self.url, headers=self.headers, proxies=Proxies.ip)
        bsObj = BeautifulSoup (r.text, "html.parser")  # urllib.request不需要加`.text`
        divSet = bsObj.findAll ("span", {"class": "count"})
        divSet01 = bsObj.findAll ("span", {"class": "thispage"})
        # print(divSet)
        pagenum=int((divSet[0]).string.split('(共')[1].split('个')[0])
        # print('pagenum:',pagenum)
        if pagenum <= 18:
            xiangce_page_num = 1
        else:
            xiangce_page_num = int (divSet01[0].attrs["data-total-page"])
        xiangce_page_urls = [self.url + "?start=%s" % (str (n * 18)) for n in range (1, xiangce_page_num)]
        xiangce_page_urls.insert (0, self.url)
        print ('【%s】主页,总共有【%s】个相册需要爬取，共%s页>>>,urls为%s' % (self.upzhu, pagenum, xiangce_page_num, xiangce_page_urls))
        return xiangce_page_urls

    def get_xiangceSetname_nums_urls(self):
        '''获取每页的url，下载图片'''
        pageurls=self.get_xiangceSet_page_urls()
        n=0
        xiangceUrls,xiangcenames,numbers,nums1={},{},{},{}
        for url in pageurls:
            time.sleep(1)
            if url.split ('photos')[1] == '':
                page = 1
            else:
                page = int (int (url.split ('photos')[1].split ('=')[1]) / 18)+1
            # url='https://www.douban.com/people/maohuoer/photos?start=90'
            r = requests.get (url, headers=self.headers, proxies=Proxies.ip)
            bsObj = BeautifulSoup (r.text, "html.parser")  # urllib.request不需要加`.text`
            imagesSet = bsObj.findAll ("a", {"class": "album_photo"})
            # print(imagesSet)
            imagenameSet = bsObj.findAll ("div", {"class": "pl2"})
            numberSet = bsObj.findAll ("span", {"class": "pl"})

            xiangceUrls[n] = [i['href'] for i in imagesSet]#相册url集合
            xiangcenames[n] = [image.string for i in range (len (imagenameSet)) for image in imagenameSet[i] if
                          image.string != '\n']#相册名字集合
            numbers[n] = [(image.string) for i in range (len (numberSet)) for image in numberSet[i] if
                       image.string != '\n' and image.string != None and i < len (xiangcenames[n])]
            nums1[n] = [number.split ('\n')[1].split ('张')[0].strip () for number in numbers[n]]#每个相册图片数量集合
            # print ('在【%s】相册的第【%s】页，获取相册共%s个，相册名为%s,相册的图片数目为%s' % (self.upzhu,page, len (xiangceUrls[n]), xiangcenames[n], nums1[n]))
            n+=1
        urls,names,nums = [],[],[]
        for i in range (len (xiangceUrls)):
            urls += xiangceUrls[i]
            names+=xiangcenames[i]
            nums+=nums1[i]
        return (urls, names, nums)
    def get_single_xiangceSeturl_nums_by_name(self,name):
        urls, names, nums = s.get_xiangceSetname_nums_urls ()
        # print(names)
        if name in names:
            i=names.index(name)
            # print(i)
        url=urls[i]
        num=nums[i]
        # print(url,num)
        return url,num
    def get_page_urls_by_name(self, name):
        '''每个相册的图片总页数，获取所有页的url'''
        time.sleep(1)
        url,num=self.get_single_xiangceSeturl_nums_by_name(name)
        r = requests.get (url, headers=self.headers, proxies=Proxies.ip)
        bsObj = BeautifulSoup (r.text, "html.parser")  # urllib.request不需要加`.text`
        divSet = bsObj.findAll ("span", {"class": "thispage"})
        nums = int (divSet[0].attrs["data-total-page"])
        if int (nums) <= 18:
            pagenum = 1
        else:
            pagenum = int (divSet[0].attrs["data-total-page"])
        pageurl1s = [url + "?start=%s" % (str (n * 18)) for n in range (1, pagenum)]
        pageurl1s.insert (0, url)
        print ('【%s】相册,总共有【%s】张照片需要爬取，共%s页>>>,url为%s' % (name, num, pagenum, pageurl1s))
        return pageurl1s

    def imagesUrls(self,name):
        '''获取每页的url，下载图片'''
        pageurls=self.get_page_urls_by_name(name)
        t = 0
        picsrcs,picNames={},{}
        for url in pageurls:
            time.sleep(1)
            r1 = requests.get (url, headers=self.headers, proxies=Proxies.ip)
            bsObj1 = BeautifulSoup (r1.text, "html.parser")
            images = bsObj1.findAll ("a", {"class": "photolst_photo"})
            picsrcs[t] = [image.contents[1].attrs["src"] for image in images]
            picNames[t] = [src[46:57] + ".jpg" for src in picsrcs[t]]  # 创造独一无二的文件名
            # print(picNames[t],picsrcs[t])
            t+=1
        # print(picsrcs[0],picNames[0])
        # print(len(picsrcs),len(picNames))
        srcs, picnames = [], []
        for i in range (len (picNames)):
            srcs += picsrcs[i]
            picnames += picNames[i]
        # print(srcs[1],picnames[1])
        # return (srcs, picnames)

    def my_mkdir(self, path):
        # 引入模块
        import os
        # 去除首位空格
        path = path.strip ()
        # 去除尾部 \ 符号
        path = path.rstrip ("\\")
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists (path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs (path)
            # print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print (path + ' 目录已存在')
            return False

    def down(self,  imagename):
        srcs, picnames=self.imagesUrls(imagename)
        i=0
        for src in srcs:
            time.sleep(1)
            new_imagename = re.sub ('[\/:*?"<>|]', '-', imagename)
            path = os.path.dirname (__file__) + '/douban/' + self.upzhu + '/' + new_imagename + '/'
            self.my_mkdir (path)
            pathnew = path + picnames[i]
            if not os.path.exists(pathnew):
                urlretrieve (src, pathnew, self.cbk)
            i+=1
    def download(self, src, photoName,imagename):
        new_imagename = re.sub ('[\/:*?"<>|]', '-', imagename)
        path = os.path.dirname (__file__) + '/douban/' + self.upzhu + '/' + new_imagename + '/' + photoName
        r = requests.get (src, headers=self.headers ,proxies=Proxies.ip)  # 下载
        with open (path, 'wb') as f:
            f.write (r.content)

        # print('upzhu【%s】的【%s】相册，第【%s】页，已下载了【%s】张图片【%s】'%s(self.upzhu,self.imagenames[i]))  # 下载完了解锁  # thread_lock.release()

    #只下载第一页的相册，18个
    def download_firstpage(self):
        imagesUrls, imagenames, nums, numbers = self.get_xiangce_urls ()
        page_urls_dic = self.get_page_urls (imagesUrls)
        n = 1
        for xiangce in imagesUrls:
            imagename = imagenames[imagesUrls.index (xiangce)]
            # print('%s个相册：现在是【%s】相册》》》'%(len(imagesUrls),imagename))
            # print('imagename:>>>',imagename)
            page_urls = page_urls_dic[imagename]
            for url in page_urls:
                # print('%s页：现在是%s页》》》'%(len(page_urls),page_urls.index(url)))
                srcs, photoNames = self.images (url)
                for src in srcs:
                    photoName = photoNames[srcs.index (src)]
                    # print(src)
                    # print('%s张图片：现在是%s》》》'%(len(srcs),photoName))
                    # print('photoName:>>>',photoName)
                    self.down (src, imagename, photoName)

                    # s.download (src, photoName)
                    # print('已下载了%s张图片.>>>' % n)
                    n += 1
        print ('一共下载了%s张图片' % n)

    def download_allpages(self):
        xiangce_page_urls = self.get_xiangce_page_urls ()
        n = 1
        for url in xiangce_page_urls:
            imagesUrls, imagenames, nums = self.get_xiangces (url)
            page_urls_dic = self.get_page_urls (imagesUrls)

            for xiangce in imagesUrls:
                imagename = imagenames[imagesUrls.index (xiangce)]
                # print('%s个相册：现在是【%s】相册》》》'%(len(imagesUrls),imagename))
                # print('imagename:>>>',imagename)
                page_urls = page_urls_dic[imagename]
                for url in page_urls:
                    # print('%s页：现在是%s页》》》'%(len(page_urls),page_urls.index(url)))
                    srcs, photoNames = self.images (url)
                    for src in srcs:
                        photoName = photoNames[srcs.index (src)]
                        # print(src)
                        # print('%s张图片：现在是%s》》》'%(len(srcs),photoName))
                        # print('photoName:>>>',photoName)
                        self.down (src, imagename, photoName)
                        n += 1
        print ('一共下载了%s张图片'%n)

    def download_xiangce(self):
        n=0
        url0='https://www.douban.com/photos/album/1614039318/'

        upzhu = url0.split('/')[-3]
        print(upzhu)
        urls=self.get_page_urls2(url0)
        print(urls)
        for url in urls:
            srcs, photoNames = self.images (url)
            for src in srcs:
                photoName = photoNames[srcs.index (src)]
                print(src)
                # print('%s张图片：现在是%s》》》'%(len(srcs),photoName))
                # print('photoName:>>>',photoName)
                # self.down (src, upzhu, photoName)

                # s.download (src, photoName)
                # print('已下载了%s张图片.>>>' % n)
                n += 1


        print ('一共下载了%s张图片' % n)
if __name__ == '__main__':
    # url = 'https://www.douban.com/people/viva-l/photos'#荒木
    # url = 'https://www.douban.com/people/qsxiao/photos'#萧秋水
    # url = 'https://www.douban.com/people/kantingq/photos'#侃烃
    # url = 'https://www.douban.com/people/suqianxia/photos'#苏千雪
    # url = 'https://www.douban.com/people/Viki00ikiV/photos'#煮豆微撒以盐
    # url = 'https://www.douban.com/people/beiliya/photos'#沉歌
    url = 'https://www.douban.com/people/ffnowaygo/photos'#泡面
    # url = 'https://www.douban.com/people/hgtc/photos'#和光同晨
    # url='https://www.douban.com/people/maohuoer/photos'
    s = Douban (url)
    upzhu = s.upzhu
    # s.get_all_xiangceSet_urls()
    # s.get_single_xiangceSeturl_nums_by_name('早饭要积极')
    # s.get_page_urls_by_name('早饭要积极')
    name='早饭要积极'
    # s.imagesUrls(name)
    s.down(name)