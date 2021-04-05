# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
from jinja2 import Environment, FileSystemLoader
from config import configs
from handlers import cookie2user, COOKIE_NAME
import orm
from coroweb import add_routes, add_static

# 初始化jinja2模板
def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        if cookie_str:
            user = yield from cookie2user(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        return (yield from handler(request))
    return auth

# 一轮过后，如何将函数返回值转化为web.response对象呢？
# 这里引入aiohttp框架的web.Application()中的middleware参数。
# middleware是一种拦截器，一个URL在被某个函数处理前，可以经过一系列的middleware的处理。一个middleware可以改变URL的输入、输出，甚至可以决定不继续处理而直接返回。middleware的用处就在于把通用的功能从每个URL处理函数中拿出来，集中放到一个地方。
# 在我看来，middleware的感觉有点像装饰器，这与上面编写的RequestHandler有点类似。
# 有官方文档可以知道，当创建web.appliction的时候，可以设置middleware参数，而middleware的设置是通过创建一些middleware factory(协程函数)。这些middleware factory接受一个app实例，一个handler两个参数，并返回一个新的handler。
# 例如，一个记录URL日志的logger可以作为middle factory简单定义如下:
@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # yield from asyncio.sleep(0.3)
        return (yield from handler(request))
    return logger

# 集中处理request数据格（POST：’application/json’、’application/x-www-form-urlencoded’、’multipart/form-data’）
@asyncio.coroutine
def data_factory(app, handler):
    @asyncio.coroutine
    def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = yield from request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = yield from request.post()
                logging.info('request form: %s' % str(request.__data__))
        return (yield from handler(request))
    return parse_data

# 生成标准HTTP response的函数工厂，利用handler的性质，接收request，返回浏览器可识别的Response对象
@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and t >= 100 and t < 600:
            return web.Response(t)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response

# Blog的创建日期显示的是一个浮点数，因为它是由这段模板渲染出来的：
# <p class="uk-article-meta">发表于{{ blog.created_at }}</p>
# 解决方法是通过jinja2的filter（过滤器），把一个浮点数转换成日期字符串。我们来编写一个datetime的filter，在模板里用法如下：
# <p class="uk-article-meta">发表于{{ blog.created_at|datetime }}</p>
# filter（过滤器）需要在初始化jinja2时设置。相关代码如下：
def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)
'''
*******************************
*******  开始测试  ************
*******************************
'''
#编写web框架测试
@asyncio.coroutine
def init(loop):
    # 首先先连接数据库
    yield from orm.create_pool(loop=loop, **configs.db)
    # 连接数据库之后会根据aiohttp来构造一个app类
    #把app类与线程绑定并为app类添加middlewares
    app = web.Application(loop=loop, middlewares=[
        logger_factory, auth_factory,response_factory
    ])
    # 注册模板
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    # 注册url处理函数
    add_routes(app, 'handlers')
    # 添加静态文件
    add_static(app)
    # 这样，app类就拥有了我们想要的功能接下来就是把app类返回用来处理传进来的url
    srv = yield from loop.create_server(app.make_handler(), '193.169.100.238', 9000)
    logging.info('server started at http://193.169.100.238:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
