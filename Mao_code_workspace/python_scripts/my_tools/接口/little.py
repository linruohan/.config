import urllib.request

#请求百度网页
# re = urllib.request.urlopen('http://www.baidu.com', data = None, timeout = 10)
# print(re.info())



import requests

#请求百度网页
response = requests.get("https://www.baidu.com", data=None,timeout=10)
print(response.headers)
