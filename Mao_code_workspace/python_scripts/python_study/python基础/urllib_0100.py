# -*- coding: utf-8 -*-
# 利用urllib读取JSON，然后将JSON解析为Python对象：

from urllib import request
import json
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def fetch_data(url):
    with request.urlopen(url) as f:
        try:
            return json.loads(f.read().decode("utf-8"))
        except ValueError:
            print("ValueError:", url)


# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
