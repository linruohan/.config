#!/usr/bin/python
# encoding: utf-8
import sys

import requests
from lxml import etree
import time, datetime
import re
from switch import *
from PIL import Image
import sys
import pyocr
import pyocr.builders
import pytesseract

image_path = 'dufu.jpg'

im = Image.open (image_path)
imgry = im.convert ('L')
threshold = 140
table = []
for i in range (256):
    if i < threshold:
        table.append (0)
    else:
        table.append (1)
out = imgry.point (table, '1')
# out.show ()
# 读取出字符串

text=pytesseract.image_to_string(Image.open('baojia.jpg'),lang='chi_sim')
print(text)