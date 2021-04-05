# coding=utf-8

import requests
from  requests.auth import AuthBase

url = 'https://api.github.com'


def build_url(end):
    return '/'.join([url, end])


def GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # 给Request添加headers
        r.headers['Authorazation'] = ' '.join(['token', self.token])


def oauth_auth_advance():
    auth = GithubAuth('000694c88c67a496d4df80d0d1daf1b4a0ee69c7')  # 我们想要替换一个别的token，这样就非常方便
    headers = {'Authorization': 'token 000694c88c67a496d4df80d0d1daf1b4a0ee69c7'}
    #     获取user/emails的信息
    response = requests.get(build_url('user/emails'), auth=auth)
    print(response.status_code)
    print(response.text)
    print(response.request.headers)


if __name__ == '__main__':
    oauth_auth_advance()
