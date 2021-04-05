import re

'''電話號碼'''
# 800-555-1212
# 800 555 1212
# 800.555.1212
# (800) 555-1212
# 1-800-555-1212
# 800-555-1212-1234
# 800-555-1212x1234
# 800-555-1212 ext. 1234
# work 1-(800) 555.1212 #1234


phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
S = phonePattern.search('800-555-1212').groups()
S1 = phonePattern.search('800-555-1212-1234')
print(S)
print(S1)
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
phonePattern.search('800-555-1212-1234').groups()
phonePattern.search('800 555 1212 1234')
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
# \D匹配任意字符，除了数字位，+ 表示“1个或者多个”，
# +的含义是“1或者多个”吗? 好的，*的含义是“0或者多个”。
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')

phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
phonePattern.search('work 1-(800) 555.1212 #1234').groups()

('800', '555', '1212', '1234')
phonePattern.search('800-555-1212')

('800', '555', '1212', '')
