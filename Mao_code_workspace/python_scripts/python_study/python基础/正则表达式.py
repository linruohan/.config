# -*- coding: utf-8 -*-
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#
# someone@gmail.com
# bill.gates@microsoft.com
import re
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def is_valid_email(addr):
    pre=r'^[0-9a-zA-Z_\.]+@[0-9a-zA-Z_-]+(.[0-9a-zA-Z_-])+$'
    res=re.match(pre,addr)
    if res:
        print(u'邮箱格式正确')
        return True
    else:
        print(u'邮箱格式错误!')
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
