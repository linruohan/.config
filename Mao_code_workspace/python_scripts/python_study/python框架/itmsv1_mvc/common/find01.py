#coding=utf-8
from selenium import webdriver
import time

'''
本文件简易的封装定位单个元素和定位一组元素的方法
'''
'''定位单个元素封装'''

def find(func):
    def wrapper(*arg, **kwargs):

        # --- 附加功能 ---
        print("loging i ...")

        return func(*arg, **kwargs)
    return wrapper

def findId(driver,id):  return driver.find_element_by_id(id)
def findName(driver,name):  return driver.find_element_by_name(name)
def findClassName(driver,name):     return driver.find_element_by_class_name(name)
def findTagName(driver,name):    return  driver.find_element_by_tag_name(name)
def findLinkText(driver,text):      return  driver.find_element_by_link_text(text)
def findPLinkText(driver,text):    return driver.find_element_by_partial_link_text(text)
def findXpath(driver,xpath):    return driver.find_element_by_xpath(xpath)
def findCss(driver,css):    return driver.find_element_by_css_selector(css)

'''定位一组元素封装'''
def findsId(driver,id):     return driver.find_elements_by_id(id)
def findsName(driver,name):     return driver.find_elements_by_name(name)
def findsClassName(driver,name):    return driver.find_elements_by_class_name(name)
def findsTagName(driver,name):    return driver.find_elements_by_tag_name(name)
def findsLinkText(driver,text):    return driver.find_elements_by_link_text(text)
def findsPLinkText(driver,text):    return driver.find_elements_by_partial_link_text(text)
def findsXpath(driver,xpath):    return driver.find_elements_by_xpath(xpath)
def findsCss(driver,css):    return driver.find_elements_by_css_selector(css)
