from enum import Enum, unique
from xml.parsers.expat import ParserCreate

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

class WeatherSaxHandler(object):
    def __init__(self):
        self.weather = {}
        self.today = ""
        self.tomorrow = ""
        self.params = "low|high|text"
    def start_element(self,name,attrs):

    # print("sax:start_element:%s,attrs:%s"%(name,str(attrs)))
    # print(attrs)
        if name == "yweather:location":
            for key in attrs:
                value = attrs[key]
                if len(value) ==0:
                    print(key)
                else:
                    self.weather[key] = value
        elif name == "yweather:condition":
            self.today = attrs["date"]
            self.today = self.today[0:self.today.find(",")]

            if Weekday[self.today]==Weekday.Sat:
                self.tomorrow = "Sun"
            else:
                index = Weekday[self.today].value + 1
                self.tomorrow = Weekday(index).name
        elif name == "yweather:forecast":
            if len(self.today)>0:
                if attrs["day"] == self.today:
                    self.weather["today"] = {}
                    for key in attrs:
                        value = attrs[key]
                        if self.params.find(key) >= 0:
                            self.weather["today"][key] = value
            if len(self.tomorrow)>0:
                if attrs["day"] == self.tomorrow:
                    self.weather["tomorrow"] = {}
                    for key in attrs:
                        value = attrs[key]
                        if self.params.find(key) >= 0:
                            self.weather["tomorrow"][key] = value


    def end_element(self,name):
        # print("sax:end_element:%s"%name)
        pass
    def char_data(self,text):
        # print("sax:char_data:%s"%text)
        pass

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return handler.weather

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

weather = parse_weather(data)

print('Weather:', str(weather))
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == "20", weather['today']['low']
assert weather['today']['high'] == "33", weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == "21", weather['tomorrow']['low']
assert weather['tomorrow']['high'] == "34", weather['tomorrow']['high']

# 判断条件改过了。。。
