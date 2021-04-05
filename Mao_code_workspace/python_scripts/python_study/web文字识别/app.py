#coding=utf-8

from tornado import web,ioloop,httpserver
from wordid import get_word_by_image
settings={
    # 模板的路径：
    'template_path':'templates',
    # 静态资源的路径
    'static_path': 'static',

         }
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('index.html')
    def post(self,*args,**kwargs):
        file=self.request.files.get('file')[0]
        res=get_word_by_image(file['body'])
        # print(res)
        self.render('results.html',content=res['words_result'])

application = web.Application([
                (r"/", MainPageHandler),
        ],**settings)
if __name__ == '__main__':
    http_server=httpserver.HTTPServer(application)
    http_server.listen(81)
    ioloop.IOLoop.current().start()