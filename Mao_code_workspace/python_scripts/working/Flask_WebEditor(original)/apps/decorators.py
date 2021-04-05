# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'
from flask import session ,redirect,url_for
from functools import wraps


def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if 'user_id' in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('cms.login'))
    return inner