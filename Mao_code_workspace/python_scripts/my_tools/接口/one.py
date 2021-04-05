import requests
import json
from requests import exceptions

''''
1、github中获取用户信息
2、github中添加邮箱
3、github中删除邮箱

requests 不带参数 请求接口
'''
URL = 'https://api.github.com'
def build(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_get():
    response=requests.get(build('users/linruohan'))
    print(better_output(response.text))

def request_post():
    response=requests.post(build('user/emails'),auth=('mjt1220@126.com','Mm1214875764'),json=['1214875764@qq.com'])
    print(better_output(response.text))
    print(response.request.headers)
    print(response.request.body)

def request_delete():
    response=requests.delete(build('user/emails'),auth=('mjt1220@126.com','Mm1214875764'),json=['1214875764@qq.com'])
    print(response.request.headers)
    print(response.request.body)


def time_out_requests():
    try:
        response=requests.get(build('user/emails'),auth=('mjt1220@126.com','Mm1214875764'),timeout=10.1)
    except exceptions.Timeout as e:
        print(str(e))
    else:
        print(response.text)

if __name__ == '__main__':
    # request_post()
    # request_delete()
    time_out_requests()
