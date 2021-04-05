#coding=utf-8

import  requests
import  base64

url='https://api.github.com'

def build_url(end):
    return '/'.join([url,end])

def basic_auth():
    response=requests.get(build_url('user'),auth=('mjt1220@126.com','Mm1214875764'))
    print(response.status_code)
    print(response.text)
    print(response.request.headers)
    print(response.headers)
    # 账号和密码是base64加密的，不安全，使用下面语句即可解密
    print(base64.b64decode('bWp0MTIyMEAxMjYuY29tOk1tMTIxNDg3NTc2NA=='))






if __name__ == '__main__':
    basic_auth()