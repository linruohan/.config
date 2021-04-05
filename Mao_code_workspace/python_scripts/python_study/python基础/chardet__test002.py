import chardet

import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
data = '最新の主要ニュース'.encode('euc-jp')
s=data.decode((chardet.detect(data))['encoding'])
'''最新の主要ニュース'''
print(s)
