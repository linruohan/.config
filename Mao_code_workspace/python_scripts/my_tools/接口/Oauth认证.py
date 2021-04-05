# coding=utf-8

import requests

url = 'https://api.github.com'


def build_url(end):
    return '/'.join([url, end])


def oauth_auth():
    headers = {'Authorization': 'token 000694c88c67a496d4df80d0d1daf1b4a0ee69c7'}
    #     获取user/emails的信息
    response = requests.get(build_url('user/emails'), headers=headers)
    print(response.status_code)
    print(response.text)
    print(response.request.headers)


if __name__ == '__main__':
    oauth_auth()
