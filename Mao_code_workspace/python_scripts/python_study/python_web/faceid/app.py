#coding=utf-8
from tornado import web,ioloop,httpserver

settings={
    # 模板的路径：
    'template_path':'templates',
    # 静态资源的路径
    'static_path': 'static',

         }
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('welcome,007')
        self.render('index.html')
    def post(self,*args,**kwargs):
        self.write('welcome,007')
        self.render('index.html')

class RegisterHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('register.html')
    def post(self,*args,**kwargs):
        # 接收参数
        username=self.get_argument('username')
        password=self.get_argument('password')
        img=self.get_argument('face')
        # 保存数据到数据库
        print(img)
        print(username,password)

class LoginHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('welcome,1')
        self.render('login.html')
    def post(self,*args,**kwargs):
        self.write('welcome,1')
class L1Handler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('welcome,1')
        self.render('shexiang.html')
class L2Handler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('welcome,1')
        # self.render('video.html')
        self.render('001.html')
application = web.Application([
                (r"/", MainPageHandler),
                (r"/register", RegisterHandler),
                (r"/login", LoginHandler),
                (r"/1", L1Handler),
                (r"/2", L2Handler),
        ],**settings)
if __name__ == '__main__':
    http_server=httpserver.HTTPServer(application)
    http_server.listen(8000)
    ioloop.IOLoop.current().start()
