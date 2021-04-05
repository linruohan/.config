#coding=utf-8

from selenium import webdriver
import os
import urllib
import requests
import re,sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import csv

file_url=os.path.dirname(__file__)+'//info.csv'
data=csv.reader(open(file_url,'r',encoding='utf-8'))
for user in data:
    print (user[0]+':'+user[1]+'age='+user[2]+':'+user[3])#第一列数据
