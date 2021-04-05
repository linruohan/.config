import web
import MySQLdb
import MySQLdb.cursors
render=web.template.render('E:\\atom\\Python\\web\\templates')
urls = (
    '/article', 'article',
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name='world'
        return render.hello2()
class article:
    def GET(self):
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='12345',db='test',port=3306, cursorclass=MySQLdb.cursors.DictCursor)
        cur = conn.cursor()
        cur.execute('select * from user')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print (r)
        return render.article(r)
class index:
    def GET(self):
        query = web.input()
        return query

class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        # get the request head
        return web.ctx.env


if __name__ == "__main__":
    app.run()
