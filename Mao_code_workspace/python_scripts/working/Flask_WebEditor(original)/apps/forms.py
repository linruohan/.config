# *_*coding:utf-8 *_* 
__Author__ = 'xiaohan'

from flask_wtf import Form

from wtforms import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo


class BaseForm(Form):
    def get_error(self):
        return self.errors.popitem()[1][0]


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='邮箱格式不正确'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(3, 20, message='密码格式不正确')])
    remember = IntegerField()


class ResetPwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(3, 20, message='旧密码格式不正确')])
    newpwd = StringField(validators=[Length(3, 20, message='新密码格式不正确')])
    new2pwd = StringField(validators=[EqualTo('newpwd', message='重复新密码不相等')])
