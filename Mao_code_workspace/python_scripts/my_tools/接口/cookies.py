#coding=utf-8



import requests
from  requests.auth import AuthBase

url = 'https://api.github.com'


def build_url(end):
    return '/'.join([url, end])


cookies = dict(c='xxxx')
requests.get(url, cookies=cookies)

r = requests.get(url)
r.cookies['cookiename']







if __name__ == '__main__':
    main()