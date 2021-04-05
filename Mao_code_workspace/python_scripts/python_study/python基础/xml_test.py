from urllib import request

from bs4 import BeautifulSoup
from datetime import datetime,timedelta

def get_url(city):

    str0 = 'http://sugg.us.search.yahoo.net/gossip-gl-location/?appid=weather&output=xml&command='+str(city)
    with request.urlopen(str0) as f:
        data = f.read().decode('utf-8')
    s = BeautifulSoup(data, 'lxml').find("s")["d"]
    woeid = s[s.index('woeid')+6:s.index('woeid')+13]
    q = 'select+*+from+weather.forecast+where+woeid%3D'+woeid+'+and+u%3D%22c%22&diagnostics=true'
    url = 'https://query.yahooapis.com/v1/public/yql?q='+q
    return url
def get_weather(data):

    weather = {}

    soup = BeautifulSoup(data,'lxml')
    weather['city'] = soup.find("yweather:location")["city"]
    weather['country'] = soup.find("yweather:location")["country"]
    todayDate = soup.find("yweather:condition")["date"].split(',')[0]
    today = soup.find("yweather:forecast",day=todayDate)
    weather['today'] = {'text':today['text'],'low':today['low'],'high':today['high']}

    currentDay = datetime.today()
    tommorrow = currentDay + timedelta(days=1)
    tommorrowStr = datetime.strftime(tommorrow,'%d %b %Y')
    tommorrowData = soup.find("yweather:forecast",date=tommorrowStr)

    weather['tommorrow'] = {'text':tommorrowData['text'],'low':tommorrowData['low'],'high':tommorrowData['high']}

    return weather
if __name__ == '__main__':
    url = get_url('beijing')
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
    print(get_weather(data))
