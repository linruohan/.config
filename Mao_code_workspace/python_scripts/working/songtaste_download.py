import requests
import os

def DownloadFile(self):
    for i in self.map3_names:
        try:
            mp3_url = self.url_list.get(i)
            mp3_name = i + '.mp3'
            if mp3_url is None or self.save_path is None or mp3_name is None:
                print('参数错误')
                return None
            # 文件夹不存在，则创建文件夹
            folder = os.path.exists(self.save_path)
            if not folder:
                os.makedirs(self.save_path)
            # 读取MP3资源
            res = requests.get(mp3_url,stream=True)
            # 获取文件地址
            file_path = os.path.join(self.save_path, mp3_name)
            print('开始写入文件：', file_path)
            # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
            with open(file_path, 'wb') as fd:
                for chunk in res.iter_content():
                    fd.write(chunk)
            print(mp3_name+' 成功下载！')
        except BaseException as e:
            print(e)
            print("程序错误")
            
def dowload_single_mp3():
    url='http://www.songtaste.co/attachment/music/202101/31/28NqJMGeFtry4cWlTnL7.mp3'
    res=requests.get(url,stream=True)
    with open("1.mp3",'wb') as f:
        for chunk in res.iter_content():
            f.write(chunk)
        print(' 成功下载！')
    
def get_cookie():
    url='http://www.songtaste.co/api/ulog/login?username=mjt1220&userpass=m1214875764&random=0.7914986310765486&callback=jQuery19101968524053537135_1613306913564&_=1613306913566'
    res=requests.get(url)
    ck=res.cookies
    print(ck)
    print(ck.keys)
    for k,v in ck.items():
        
        print(f"{k}={v}")
    
    
    
if __name__ == "__main__":
    
    get_cookie()