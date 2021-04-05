import asyncio,os,json,time
import logging,aiomysql
from aiohttp import web
from datetime import datetime

logging.basicConfig(level=logging.INFO)

async def execute(sql,args):
    log(sql)
    with(await __pool) as conn:
        try:
            cur=await conn.cursor()
            await cur.execute(sql.replace('?','%s'),args)
            affected=cur.rowcount
            await cur.close()
        except Exception as e:
            raise
        return affected
