import orm
from models import User,Blog,Comment
import asyncio

async def destory_pool():
    global __pool
    if __pool is not None :
        __pool.close()
        await __pool.wait_closed()
async def test(loop,**kw):

    await orm.create_pool(loop=loop,user='www-data',password='www-data',db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))
    await u.save()
    await destory_pool()


if __name__ == '__main__':

    data=dict(name='1234', email='22512341@qq.com', passwd='12345', image='about:blank')
    loop=asyncio.get_event_loop()
    loop.run_until_complete(test(loop,**data))
    loop.close()
    if loop.is_closed():
        sys.exit(0)
