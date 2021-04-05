# -*- coding:utf-8 -*-
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
#
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml
#
# 参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。


from xml.parsers.expat import ParserCreate
from urllib import request
from collections import OrderedDict

weather_dict=OrderedDict({})
which_day=0


class WeatherSaxHandler(object):
    def start_element(self,name,attrs):
        global weather_dict,which_day
        #判断并获取xml文档中的地理位置信息
        if name=='yweather:location':
            #将本行的‘city’属性值赋予字典weather——dict中的’‘city’
            weather_dict['city']=attrs['city']
            weather_dict['country']=attrs['country']
            # 执行结束后此时，weather_dict={'city':'Beijing','country'='China'}
        # 同理获取天气预测信息
        if name=='yweather:forecast':
            which_day+=1
            #第一天天气。气温：
            if which_day==1:
                weather={
                'text',attrs['text'],
                'low',int(attrs['low']),
                'high',int(attrs['high']),
                }
                weather_dict['today']=weather
         # 此时weather_dict出现二维字典
         # weather_dict={'city': 'Beijing', 'country': 'China', 'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33}}
            elif which_day==2:
                weather={
                'text',attrs['text'],
                'low',int(attrs['low']),
                'high',int(attrs['high']),
                }
                weather_dict['tomorrow']=weather
            else:
                weather={
                'text',attrs['text'],
                'low',int(attrs['low']),
                'high',int(attrs['high']),
                }
                weather_dict[attrs['day']]=weather
        # weather_dict={'city': 'Beijing',
        #   'country': 'China',
        #   'today': {'text': 'Partly Cloudy', 'low': 20, 'high': 33},
        #   'tomorrow': {'text': 'Sunny', 'low': 21, 'high': 34}}

        # end_element函数
    def end_element(self, name):
        pass
    def char_data(self,text):
        pass


def parse_weather(xml):
    handler=WeatherSaxHandler()
    parser=ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return weather_dict



data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL) as f:
    data = f.read().decode('utf-8')
    print(data1)

weather = parse_weather(data1)
print('Weather:', str(weather))
print('weather["city"]', str(weather['city']))
print('weather["country"]:', str(weather['country']))
print('Weather:', str(weather))
# assert weather['city'] == 'Beijing'
# assert weather['city'] == 'Beijing', weather['city']
# assert weather['country'] == 'China', weather['country']
# assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
# assert weather['today']['low'] == 20, weather['today']['low']
# assert weather['today']['high'] == 33, weather['today']['high']
# assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
# assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
# assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
