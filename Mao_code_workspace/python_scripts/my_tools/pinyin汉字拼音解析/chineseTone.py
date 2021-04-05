#coding=utf-8
from ChineseTone import *
s='了解了'
s.encode('utf-8','ignore')
# print( PinyinHelper.convertToPinyinFromSentence(s))
# # 输出：[u'li\u01ceo', u'ji\u011b', u'le']
#
# print( '/'.join(PinyinHelper.convertToPinyinFromSentence(s)))
# # 输出：liǎo/jiě/le
#
# print (PinyinHelper.convertToPinyinFromSentence(s, pinyinFormat=PinyinFormat.WITH_TONE_MARK))
# # 输出：[u'li\u01ceo', u'ji\u011b', u'le']
#
# print (PinyinHelper.convertToPinyinFromSentence(s, pinyinFormat=PinyinFormat.WITH_TONE_NUMBER))
# # 输出：[u'lia3o', u'jie3', u'le']
#
# print (PinyinHelper.convertToPinyinFromSentence(s, pinyinFormat=PinyinFormat.WITHOUT_TONE))
# # 输出：[u'liao', u'jie', u'le']
# print (PinyinHelper.convertToPinyinFromSentence('了解了，Mike', pinyinFormat=PinyinFormat.WITHOUT_TONE))
# 输出：[u'liao', u'jie', u'le', u'\uff0c', u'M', u'i', u'k', u'e']
import jieba



def cut(s):
    return jieba.cut(s, cut_all=False)
for word in cut('我来到北京清华大学,mike'):
    print (word)

## 未指定分词函数
print (PinyinHelper.convertToPinyinFromSentence('提出了解决方案', pinyinFormat=PinyinFormat.WITHOUT_TONE))
# 输出：[u'ti', u'chu', u'liao', u'jie', u'jue', u'fang', u'an']

## 指定分词函数
print (PinyinHelper.convertToPinyinFromSentence('提出了解决方案', pinyinFormat=PinyinFormat.WITHOUT_TONE, segment=cut))
# 输出：[u'ti', u'chu', u'le', u'jie', u'jue', u'fang', u'an']