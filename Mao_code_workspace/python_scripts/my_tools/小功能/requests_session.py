# -*- coding:UTF-8 -*-
import json

import requests

url = 'http://193.169.100.249:8086/itmsld/login'


def get_session_content():
    MAX_RETRIES = 20

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
    session.mount('https://', adapter)
    session.mount('http://', adapter)

    r = session.get(url)
    print(r.content)


def get_request_content():
    headers = {'authorization': 'your Client-ID'}
    req = requests.get(url, headers=headers)
    print(req.content)
    # req = requests.get(url=target, headers=headers, verify=False)
    html = json.loads(req.text)
    next_page = html['next_page']
    print('下一页地址:', next_page)
    for each in html['photos']:
        print('图片ID:', each['id'])
