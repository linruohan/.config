import asyncio
import os
import json
import time
import logging
import aiomysql
from aiohttp import web
from datetime import datetime

logging.basicConfig(level=logging.INFO)


async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost')
        port=kw.get('port', 3306)
        user=kw['user']
        password=kw['password']
        db=kw['db']
        charset=kw.get('charset', 'utf8')
        autocommit=kw.get('autocommit', True)
        maxsize=kw.get('maxsize', 10)
        minsize=kw.get('minsize', 1)
        loop=loop
    )
