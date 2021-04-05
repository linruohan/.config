# -*- coding: utf-8 -*-
# !/usr/bin/python
# filename: GETPOST_test.py
# codedtime: 2014-9-20 19:07:04


import bottle


def check_login(username, password):
    if username == '123' and password == '123':
        return True
    else:
        return False


@bottle.route('/login')
def login():
    if bottle.request.GET.get('do_submit', '').strip():  # 点击登录按钮
        # 第一种方式(latin1编码)
        ##    username = bottle.request.GET.get('username','').strip() # 用户名
        ##    password = bottle.request.GET.get('password','').strip() # 密码

        # 第二种方式(获取username\password)(latin1编码)
        getValue = bottle.request.query_string
        ##    username = bottle.request.query['username'] # An utf8 string provisionally decoded as ISO-8859-1 by the server
        ##    password = bottle.request.query['password'] # 注：ISO-8859-1(即aka latin1编码)
        # 第三种方式(获取UTF-8编码)
        username = bottle.request.query.username  # The same string correctly re-encoded as utf8 by bottle
        password = bottle.request.query.password  # The same string correctly re-encoded as utf8 by bottle

        print('getValue= ' + getValue,
              '\r\nusername= ' + username,
              '\r\npassword= ' + password)  # test

        if check_login(username, password):
            return "<p> Your login information was correct.</p>"
        else:
            return "<p>Login failed. </p>"
    else:
        return ''' <form action="/login" method="get">
           Username: <input name="username" type="text" />
           Password: <input name="password" type="password" />
           <input value="Login" name="do_submit" type="submit">
          </form>
        '''


bottle.run(host='localhost', port=8083)
