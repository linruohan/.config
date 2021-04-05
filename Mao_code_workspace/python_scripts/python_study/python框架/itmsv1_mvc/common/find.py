# coding=utf-8
'''
本文件简易的封装定位单个元素和定位一组元素的方法
'''
class Find (object):
    """docstring for Find."""

    def __init__(self, driver):
        self.driver=driver
    @property
    def __str__(self):
        return self.__class__.__name__

    def findId(self, id):  return self.driver.find_element_by_id (id)

    def findName(self, name):  return self.driver.find_element_by_name (name)

    def findClassName(self, name):     return self.driver.find_element_by_class_name (name)

    def findTagName(self, name):    return self.driver.find_element_by_tag_name (name)

    def findLinkText(self, text):      return self.driver.find_element_by_link_text (text)

    def findPLinkText(self, text):    return self.driver.find_element_by_partial_link_text (text)

    def findXpath(self, xpath):    return self.driver.find_element_by_xpath (xpath)

    def findCss(self, css):    return self.driver.find_element_by_css_selector (css)

    '''定位一组元素封装'''

    def findsId(self, id):     return self.driver.find_elements_by_id (id)

    def findsName(self, name):     return self.driver.find_elements_by_name (name)

    def findsClassName(self, name):    return self.driver.find_elements_by_class_name (name)

    def findsTagName(self, name):    return self.driver.find_elements_by_tag_name (name)

    def findsLinkText(self, text):    return self.driver.find_elements_by_link_text (text)

    def findsPLinkText(self, text):    return self.driver.find_elements_by_partial_link_text (text)

    def findsXpath(self, xpath):    return self.driver.find_elements_by_xpath (xpath)

    def findsCss(self, css):    return self.driver.find_elements_by_css_selector (css)
