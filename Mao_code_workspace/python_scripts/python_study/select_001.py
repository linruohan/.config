import asyncio,os,json,time
import logging,aiomysql
from aiohttp import web
from datetime import datetime

logging.basicConfig(level=logging.INFO)

async def select(sql,args,size=None):
    log(sql,args)
    global __pool
    with (await __pool) as conn:
        cur=await conn.cursor(aiomysql.DictCursor)
        await cru.execute(sql.replace('?','%s'),args or ())
        if size:
            rs=await cur.fetchmany(size)
        else:
            rs=await cur.fetchall()
        await cur.close()
        logging.info('rows returned :%s' %len(rs))
        return rs
