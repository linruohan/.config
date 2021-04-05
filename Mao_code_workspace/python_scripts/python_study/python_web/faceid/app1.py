# -*- coding:utf-8 -*-
from tornado import web,ioloop,httpserver
class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.render("index.html")
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('welcome,007')
        self.render('index.html')
class LoginHandler(web.RequestHandler):
    def get(self):
        # self.write("请登录")
        self.render("login.html")

    def post(self, *args, **kwargs):
        v = self.get_argument('username')
        print(v)
        self.redirect('/index.html')

settings = {
    'template_path': 'templates',
    'static_path': 'static',
    'static_url_prefix': '/ppp/',
}

# application对象中封装了：路由信息，配置信息
application = web.Application([
    (r"/", MainPageHandler),
    (r"/login", LoginHandler),
    (r"/register", MainHandler),
],**settings)

# application.add_handlers('buy.oldboy.com',[
#     (r"/login.html", LoginHandler),
#     (r"/index.html", MainHandler),
# ])


if __name__ == "__main__":
    # 创建socket对象
    # sock = socket.socket()
    # inputs = [socket,]
    application.listen(8888)

    # 开启 r,w,e = select.select(inputs,)
    ioloop.IOLoop.instance().start()
