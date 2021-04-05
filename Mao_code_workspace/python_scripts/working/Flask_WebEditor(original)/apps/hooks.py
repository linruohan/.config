# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

from flask import  session,g
from .models import CMSUser
from .views import bp
import config


@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        print(f'user:{user}')
        if user:
            g.cms_user = user
