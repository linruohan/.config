# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
# =======================================================\
#   功能:
# =======================================================
import random
import requests

# 发送请求时的头文件
def get_requests(url, flag='t'):
    # 发送请求时的头文件
    headers = [
        {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"},
        {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"},
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
    ]
    result = requests.get(url, headers=random.choice(headers))
    if flag == 't':
        return result.text
    elif flag == 'c':
        return result.content
    elif flag == 'j':
        return result.json()
    else:
        return result
if __name__ == '__main__':
    pass
