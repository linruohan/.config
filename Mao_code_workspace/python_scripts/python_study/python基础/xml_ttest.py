from xml.parsers.expat import ParserCreate
from urllib import request
from matplotlib import pyplot as plt
import collections
import re
from datetime import datetime

class DefaultSaxHandler():
    #初始化
    def __init__(self):
        self._temp={}
        self.forecast=collections.OrderedDict()#按序存入
        # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
    # 举个例子，当SAX解析器读到一个节点时：

    '''<a href="/">python</a>'''
    #start_element事件，在读取<a href="/">时；

    # char_data事件，在读取python时；

    def start_element(self,name,attrs):
        #如果标签名字tagname='yweather:forecast'
        # 获取一系列值赋给self，存入self_temp临时字典中
        if name=='yweather:forecast':
            self._date=self._handle_attr(attrs,'date')
            self._day=self._handle_attr(attrs,'day')
            self._high=self._handle_attr(attrs,'high')
            self._low=self._handle_attr(attrs,'low')
            self._text=self._handle_attr(attrs,'text')
            self._temp={
            'day':self._day,
            'high':self._high,
            'low':self._low,
            'text':self._text
            }
            self.forecast['%s'%self._date]=self._temp
            # 将self._temp存入self.forecast
            # list={'2017 12 28 16:37:45:555',
            #   {'day':self._day,
                # 'high':self._high,
                # 'low':self._low,
                # 'text':self._text
            #   }
            #
            # }
            # 将self._temp清空，下一次重新使用
            self._temp={}

    # end_element事件，在读取</a>时。
    # attrs是list，attrname是key值，list[key]=attrs[attrname]
    #输入list和key值，返回list[key]的value，供给start_element赋值
    def _handle_attr(self,attrs,attrname):
        for key in attrs.keys():
            if key==attrname:
                return attrs[attrname]
        return "NO DATA!"

#原始URL
headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
url='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
reg=request.Request(url, headers=headers)
# reg.add_header('User-Agent','User-Agent:Mozilla/5.0')

with request.urlopen(reg) as file_object:
    xml_str=file_object.read()
    #得到xml格式的字符串
handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.Parse(xml_str)
#得到处理后的xml字符串
highs,lows,texts,dates,days=[],[],[],[],[]
for key1,value1 in handler.forecast.items():
    dates.append(key1)#存入日期
    highs.append((int(value1['high'])-32)/1.8)
    lows.append((int(value1['low'])-32)/1.8)
    texts.append(value1['text'])
    days.append(value1['day'])

# 处理日期
'''==========================================='''
temp_dates=[]
for date in dates:
    m=re.match(r'^(\w+)\s(\w+)\s(\d+)',date)
    print(date)
    #判断月份
    if m.group(2)=='Nov':
        mouth='November'
    if m.group(2)=='Dec':
        mouth='December'

    temp_date=m.group(1)+'-'+mouth+'-'+m.group(3)
    temp_dates.append(temp_date)

new_dates=[]
for date in temp_dates:
    new_date=datetime.strptime(date,'%d-%B-%Y')
    new_dates.append(new_date)
'''==========================================='''
for i in range(len(dates)):
    print('date=:',dates[i])
    print('high=:%.2f'%highs[i])
    print('lows=:%.2f'%lows[i])
    print('texts=:',texts[i])
    print('days=:',days[i])

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(new_dates,lows,c='blue')  #注意y轴数值是否是数字类型，若不是，则可能出现间隔不均匀的情况
plt.plot(new_dates,highs,c='red')  #注意y轴数值是否是数字类型，若不是，则可能出现间隔不均匀的情况
plt.title('Weather Forecast-BeiJing',fontsize=18)
plt.xlabel('DATE',fontsize=16)
plt.ylabel('Temperature(C)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.axis([new_dates[0],new_dates[-1],min(lows)-2,max(highs)+2])
fig.autofmt_xdate()
fig.savefig('weather.svg')
plt.show()
