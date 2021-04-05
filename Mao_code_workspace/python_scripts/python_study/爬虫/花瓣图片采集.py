#coding=utf-8
import urllib.request as  urllib
import re,os
import requests,time
import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
class UtilsRequest():
    #联网超时时间
    time_out = 30
    #联网失败重试次数
    request_nums = 5;

    def __init__(self):
        super().__init__();

    def requestpageText(self,url):
        request_count = self.request_nums
        try:
            request_count-=1
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

            Page = requests.session().get(url, headers=head, timeout=self.time_out)
            Page.encoding = "utf-8"
            print("获取网页数据成功")
            return Page.text
        except Exception as e:
            print("联网失败了...重试中", e)
            time.sleep(5)
            print("暂停结束")
            if request_count >=0 :
                    self.requestpageText(url)

    def downfile(self,file, url):
        print("开始下载：", file, url)
        try:
            r = requests.get(url, stream=True)
            with open(file, 'wb') as fd:
                for chunk in r.iter_content():
                    fd.write(chunk)
        except Exception as e:
            print("下载失败了", e)

class Huaban:
    file_save_path = os.path.dirname(__file__)+"pic/"
    text_keyword = "航空";
    page_nums = 0;
    down_photo_num=0#下载的图片数量
    ru = ""

    def __init__(self):
        super().__init__();
        self.ru = UtilsRequest()

    def gethuaban(self):
        urlhuaban = "http://huaban.com/search/?q=%s&per_page=20&wfl=1&page=%d"
        urlhuaban = urlhuaban % (self.text_keyword,self.page_nums);
        file_save_path = self.file_save_path+self.text_keyword+"/";

        print("*******************************************************************")
        print("请求网址：", urlhuaban)

        self.page_nums += 1
        if not os.path.exists(file_save_path):
            os.makedirs(file_save_path)

        text = self.ru.requestpageText(urlhuaban)
        pattern = re.compile('{"pin_id":(\d*?),.*?"key":"(.*?)",.*?"like_count":(\d*?),.*?"repin_count":(\d*?),.*?}',
                             re.S)
        items = re.findall(pattern, text)
        if(len(items)==0):
            print("*******************************************************************")
            print("共下载图片%d张"%self.down_photo_num)
            print("下载资源结束~~~~~~~~~~~~~或未找到资源")
            return;

        print(items)
        for item in items:
            max_pin_id = item[0]
            x_key = item[1]
            x_like_count = int(item[2])
            x_repin_count = int(item[3])
            if (x_repin_count > 10 and x_like_count > 10) or x_repin_count > 10 or x_like_count > 1:
                print("开始下载第{0}张图片".format(self.down_photo_num))

                url_image = "http://hbimg.b0.upaiyun.com/"
                url_item = url_image + x_key
                filename = file_save_path + str(max_pin_id) + ".jpg"
                if os.path.isfile(filename):
                    print("文件存在：", filename)
                    continue

                self.ru.downfile(filename, url_item)
                self.down_photo_num += 1
        self.gethuaban()

h = Huaban()
h.gethuaban()
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read().decode('utf-8')
#     return html
#
# def getImg(html):
#     reg = r'src="(.*?)"'
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre,html)
#     x = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg' % x)
#         x+=1
#     return imglist
#
# html = getHtml('https://huaban.com/pins/1095596742/')
#
# print (getImg(html))
