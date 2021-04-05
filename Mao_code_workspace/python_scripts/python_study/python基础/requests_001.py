#coding=utf-8
import  requests
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

url='https://www.douban.com/'
r=requests.get(url)
# print('r.status_code==',r.status_code)
# print(r.text)
# print(r.encoding)
# print('r.content==',r.content.decode('utf-8'))


r1=requests.get(url,params={'q':'python','cat':'1001'})
# print('url==:',r1.url)


r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r3.json())

r4=requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r4.text)
