#  coding=utf-8
import json
from time import sleep

import pandas as pd
import requests


def get_bus_data(city, linename):
    """获取公交线路详细信息"""
    key = 'cd1b11521a7cc599f64c37515708b9eb'
    url = f'https://restapi.amap.com/v3/bus/linename?s=rsv3&extensions=all&key=%s&output=json&city=%s&offset=1&keywords=%s&platform=JS' % (
        key, city, linename)
    html = requests.get(url).text
    rt = json.loads(html)
    print(rt)
    try:
        if rt['buslines'] and len(rt['buslines']):
            busdict = {}
            busdict['name'] = rt['buslines'][0]['name']
            busdict['polyline'] = rt['buslines'][0]['polyline']
            busdict['distance'] = rt['buslines'][0]['distance']
            busdict['total_price'] = rt['buslines'][0]['total_price']
            busdict['timedesc'] = rt['buslines'][0]['timedesc']

            station_name, station_corrds = [], []
            for i in rt['buslines'][0]['busstops']:
                station_name.append(i['name'])
                station_corrds.append(i['location'])
            busdict['station_name'] = station_name
            busdict['station_corrds'] = station_corrds
            df = pd.DataFrame([busdict])
    except:
        sleep(2)
        get_bus_data(city, linename)
    return df


if __name__ == '__main__':
    CITY = '西安'
    LINENAME = '800路'
    df = get_bus_data(CITY, LINENAME)
    print(df)
