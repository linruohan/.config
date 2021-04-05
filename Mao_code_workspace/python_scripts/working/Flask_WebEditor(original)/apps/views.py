from flask import Blueprint, views, redirect, render_template, request, session, url_for, g, jsonify
from .forms import LoginForm, ResetPwdForm
from .models import CMSUser
from .decorators import login_required
import config
from exts import db
from utils.restful import *

#bp = Blueprint('cms', __name__, url_prefix='/cms')
bp = Blueprint('cms', __name__)


@bp.route('/')
@login_required
def index():
    return render_template('index.html')


@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            # user = CMSUser.query.filter_by(email=email).first()
            # print(email, password, user, remember)
            # if user and user.check_password(password):#使用mysql数据库
            #     config.CMS_USER_ID = user.id
            if email==config.EMAIL and password==config.PASSWD:#使用config文件
                if remember:
                    # 设置过期时间为31天
                    session.permanent = True
                return render_template('index.html')
                # return redirect(url_for("cms.index"))
            else:
                return self.get(message='邮箱或密码错误')
        else:
            message = form.get_error()
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('index.html')

    def post(self):
        form = ResetPwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.add(user)
                db.session.commit()
                return success()
            else:
                return params_error(message="旧密码错误")
        else:
            return params_error(form.get_error())

bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
