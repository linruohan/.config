import json
import requests
# import geoip2.database#https://dev.maxmind.com/geoip/geoip2/geolite2/
# '''GeoLite2数据库是免费的IP地理定位数据库与MaxMind的GeoIP2数据库相当，但不太准确。
# GeoLite2国家和城市数据库在每个月的第一个星期二更新。
# GeoLite2 ASN数据库每周二更新一次。'''
# reader = geoip2.database.Reader(
#     r'C:/Users/name/PycharmProjects/test/GeoLite2-City.mmdb')
# response = reader.city('103.235.46.39')
# print(response.country.iso_code)

# 根据ip地址查询出IP所在的地理位置


def get_ip_info(ip):
    r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
    if r.json()['code'] == 0:
        i = r.json()['data']
        print(str(i))
        print(u'国家: %s\n区域: %s\n省份: %s\n城市: %s\n运营商: %s\n' %
              (i['country'], i['area'], i['region'], i['city'], i['isp']))
    else:
        print("ERROR! ip: %s" % ip)


if __name__ == "__main__":
    ip = '106.33.128.216'
    get_ip_info(ip)
