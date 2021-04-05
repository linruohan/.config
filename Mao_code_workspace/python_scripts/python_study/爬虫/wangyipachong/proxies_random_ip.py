from bs4 import BeautifulSoup
import requests
import random
class Proxies:
    def __init__(self):
        self.ip=self.get_random_ip(self.get_ip_list())
    def get_ip_list(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        # IP地址取自国内髙匿代理IP网站：http://www.xicidaili.com/nn/
        url = 'http://www.xicidaili.com/nn/'
        # 仅仅爬取首页IP地址就足够一般使用
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[1].text + ':' + tds[2].text)
        # print(ip_list)
        # print(len(ip_list))
        return ip_list

    def get_random_ip(self,ip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}
        # print(proxies)
        return proxies

if __name__ == '__main__':
    s=Proxies()
    print(s.ip)
    # web_data = requests.get (url, headers=headers, proxies=proxies)