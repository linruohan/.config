# -*- coding: utf-8 -*-
# !/usr/bin/python
# filename: todo.py
# codedtime: 2014-8-28 20:50:44

import sqlite3
import bottle
from bottle import error


@bottle.route('/help')
def help():
    return bottle.static_file('help.html', root='.')  # 静态文件


@bottle.route('/json:json#[0-9]+#')
def show_json(json):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT task FROM todo WHERE  id LIKE ?', (json))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}


'''Web程序难免会遇到访问失败的错误，
那么怎样去捕获这些错误，
Bottle可以用路由机制来捕捉错误，
如下捕获403、404：'''


@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


bottle.debug(True)
bottle.run(host='127.0.0.1', port=8080, reloader=True)
