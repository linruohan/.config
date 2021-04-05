# encoding=utf-8
import io
import sys
import time

from lxml import etree
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class FindXpath(object):
    def __init__(self, driver):
        self.driver = driver

    def save_file(self):
        attribs = []
        contents = []
        xpaths = []
        driver = self.driver
        title = driver.title
        # html=driver.page_source.encode('gbk', 'ignore')
        html = driver.page_source.replace(
            u'\xa9', u'').encode('utf-8', 'ignore')
        page = etree.HTML(html)
        ids = page.xpath(
            u"//*[@id='menu_130402081930284387431bd38d30c4ac']/p/a")
        # for x in ids:
        #     print (x.attrib)
        # print(x.text)
        print('*' * 100)
        htree = etree.ElementTree(page)
        # # 依次打印出hdoc每个元素的文本内容和xpath路径
        for t in page.iter():
            attr = t.attrib
            text = t.text
            xpath = htree.getpath(t)
            attribs.append(t.attrib)
            contents.append(t.text)
            xpaths.append(htree.getpath(t))
            # print(t.attrib)
            # with open('ld_xpath.html','a') as f:
            #     s=str(htree.getpath(t)+'\n\r'+str(t.text))
            #     f.write(s)
        # print(len(attribs))
        # print(len(contents))
        # print(len(xpaths))
        print(attribs[0], contents[0], xpaths[0])


if __name__ == '__main__':
    url = 'http://193.169.100.249:8086/itmsld/home/admin/'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id('password').send_keys('admin')
    driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div[4]/input[1]').click()
    time.sleep(5)

    f = FindXpath(driver)
    f.save_file()
    driver.quit()
