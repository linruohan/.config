#coding=utf-8
import re
'''
re.search()---完整搜索可能位置，返回match对象----------
'''
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))
'''
re.match()---从头匹配，返回match对象----------
'''
match1=re.match(r'[1-9]\d{5}','100801 BIT 100081')
if match1:
    print(match1.group(0))
'''
re.findall()--所有子串-----------
'''
ls=re.findall(r'[1-9]\d{5}','100801 BIT 100081')
print(ls)
'''
re.split()-------分割，返回列表类型------
'''
s=re.split(r'[1-9]\d{5}','100801 BIT 100081')
print (s)
s=re.split(r'[1-9]\d{5}','100801 BIT 100081',maxsplit=1)
print (s)
'''
re.finditer()------迭代类型，每个迭代类型是match对象-------
'''
for m in re.finditer(r'[1-9]\d{5}','100801 BIT 100081'):
    if m:
        print(m.group(0))
'''
re.sub()------返回替换后字符串-------
'''
s=re.sub(r'[1-9]\d{5}',':zipcode','100801 BIT 100081')
print(s)
