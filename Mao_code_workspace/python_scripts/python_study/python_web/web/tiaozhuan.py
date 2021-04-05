import web

render = web.template.render('E:\\atom\\Python\\web\\templates')
urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        return render.hello2()

class index:
    def GET(self):
        #实现URL跳转
        #就是在得到用户发送请求的时候，
        #我们有时候需要把页面给跳转其他页面。
        #例如访问127.0.0.1:8080/index，要求跳转到百度首页，我们这样来实现。
        query = web.input()
        return web.seeother("https://www.baidu.com")

class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        # get the request head
        return web.ctx.env


if __name__ == "__main__":
    app.run()
