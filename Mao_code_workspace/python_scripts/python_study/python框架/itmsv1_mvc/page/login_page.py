#coding=utf-8
import time
from itmsv1_mvc.common.basePage import Page

class Login_page(Page):

	# //本例使用XPath方式来进行定位，使用ID、name等方式均可定位
    '''操作元素如下所示：'''
    Input_user='id=>username'#用户名
    Input_passwd='id=>password'#密码
    submit_button='xpath=>//input[@value="登 录"]'#登录
    reset_button='xpath=>//*[@id="loginForm"]/div[4]/input[2]'#重置
    success_name='xpath=>//*[@id="dropdown-toggle"]/span[1]'#登录成功之后显示昵称
    logout_link='xpath=>//*[@id="dropdown-menu"]/li[2]/a'#登出连接
    def type_user(self, username):
        self.type(self.Input_user, username)
    def type_passwd(self, password):
        self.type(self.Input_passwd, password)
    def click_submit_btn(self):
        self.click(self.submit_button)
    def enter_keys(self):
        self.enter_key(self.Input_passwd)

    # //第二部分：业务操作
	# //登录操作
    def login(self,username,password):
        self.clear_text(self.Input_user)
        self.clear_text(self.Input_passwd)
        self.type_user(username)
        self.type_passwd(password)
        self.click(self.submit_button)
        time.sleep(3)
    # //登出操作
    def logout(self):
        self.click(self.success_name)
        self.click(self.logout_link)
        time.sleep(3)

    # //获取登录成功之后的昵称
    def get_login_name(self):
        return self.get_text(self.success_name)
    def get_user_input(self):
        return self.get_text(self.Input_user)
    def get_passwd_input(self):
        return self.get_text(self.Input_passwd)

    def reset(self):
        self.click(self.reset_button)
