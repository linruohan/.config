# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    # print('user==',user)
    # print('password==',password)
    # print('usget_md5(password)er==',get_md5(password))
    # print('get_md5(password+user.salt)==',get_md5(password+user.salt))
    '''
    user.password=User(username,password)为真值
    get_md5(password+user.salt)为计算后得出的加密值
    两者相互比较得出是否正确，返回true和false
    '''
    return user.password == get_md5(password+user.salt)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
