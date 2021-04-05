#coding=utf-8


import web

urls=("/.*","hello")
app=web.application(urls,globals())

class hello:
    def GET(self):
        return "hello,xiaohan"

if __name__ == '__main__':
    app.run()
