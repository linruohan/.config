import json  # 需要这三个库
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

class Weather:

    def __init__(self, city):
        self.city = city
        if u'市' not in city:
            self.city = city + u'市'
        url = self.get_download_url()
        self.get_weather(url)

    def get_download_url(self):
        api_key = 'd522aa97197fd864d36b418f39ebb323'
        url = f'https://api.weather.com/v3/location/search?apiKey={api_key}&format=json&language=zh-CN&locationType=locale&query=%s' % quote(
            self.city)
        res = requests.get(url).text
        # print(res)
        # print(type(res))
        res = json.loads(res)
        for i in range(len(res['location']['city'])):
            if self.city in res['location']['city'][i]:
                index = i
                print('现在查询的是:', res['location']['displayName'][i])
        place_id = res['location']['placeId'][index]
        download_url = f'https://weather.com/zh-CN/weather/hourbyhour/l/{place_id}'
        print(download_url)
        return download_url

    def get_weather(self, Download_addres):
        # 文件下载地址
        # 西安
        # Download_addres = 'https://weather.com/zh-CN/weather/hourbyhour/l/469847d38b26dbfd9519a7467fbcc689c42cceb1bd104a74d6637ce8359a0fba'
        # 把下载地址发送给requests模块
        html_text = requests.get(Download_addres).text
        bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
        body = bs.body  # 获取body部分
        trs = tr = body.find('table', class_='twc-table').find_all('tr')  # .find定  # 找到id=7d的div
        # print(trs)
        head = trs[0]
        time = head.find('th', id="time").text  # 时间
        description = head.find('th', id="description").text  # 说明
        temp = head.find('th', id="temp").text  # 温度
        feels = head.find('th', id="feels").text  # 体感
        precip = head.find('th', id="precip").text  # 降雨概率
        humidity = head.find('th', id="humidity").text  # 湿度
        wind = head.find('th', id="wind").text  # 风力

        head_str = '\t'.join([time, description, temp, feels, precip, humidity, wind])
        print(head_str)
        for i in trs[1:]:
            record = []
            date = i.find('div', class_="hourly-date").text.replace(' ', '')
            time = i.find('span', class_="dsx-date").text.replace(' ', '')
            description = i.find('td', headers="description").text.replace(' ', '')
            temp = i.find('td', headers="temp").text.replace(' ', '')
            feels = i.find('td', headers="feels").text.replace(' ', '')
            precip = i.find('td', headers="precip").text.replace(' ', '')
            humidity = i.find('td', headers="humidity").text.replace(' ', '')
            wind = i.find('td', headers="wind").text.replace(' ', '')
            record = [date + time, description, temp, feels, precip, humidity, wind]
            print('\t'.join(record))

if __name__ == '__main__':
    Weather(u'兰州')
