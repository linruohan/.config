from pypinyin import pinyin, lazy_pinyin
import pypinyin

pinyin(u'中心')
# [[u'zh\u014dng'], [u'x\u012bn']]

# 启用多音字模式
pinyin(u'中心', heteronym=True)  
# [[u'zh\u014dng', u'zh\xf2ng'], [u'x\u012bn']]

# 设置拼音风格
pinyin(u'中心', style=pypinyin.INITIALS)  
# [['zh'], ['x']]

pinyin('中心', style=pypinyin.TONE2, heteronym=True)
# [['zho1ng', 'zho4ng'], ['xi1n']]

# 不考虑多音字的情况
lazy_pinyin(u'中心')  
# ['zhong', 'xin']