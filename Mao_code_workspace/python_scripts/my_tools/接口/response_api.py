# coding=utf-8

import requests

r = requests.get('https://api.github.com')

print(r.status_code)
print(r.reason)
print(r.headers)
print(r.url)
print(r.history)
print(r.elapsed)
print(r.request)



print(r.encoding)
print(r.raw)
print(r.content)
print(r.text)
print(r.json())