# -*- coding: utf-8 -*-
# 版本二可以提取出带名字的Email地址：
#
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
import re
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def name_of_email(addr):
    pre=r'^\<([\w|\d]*\s?[\w|\d]*)\>\s+|([\w|\d]*\.?[\w|\d]*)@([\w|\d]*)(.com|.cn|.net|.org)$'
    res=re.match(pre,addr).group(1)
    if res:
        print(u'邮箱格式正确')
        return re.match(pre,addr).group(1)
    else:
        return re.match(pre,addr).group(2)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
