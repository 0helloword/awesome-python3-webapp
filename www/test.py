#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio, logging
import aiomysql
from aiohttp import web

def create_pool(loop,**kw):
    print('create databases connection pool...')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user='wwwdata',
        password='wwwdata',
        db='awesome',
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop                               
                                    )
    
# def select(sql,args,size=None):
    sql='select * from users'
    args=''
    size=1
#     global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
#     with (yield from __pool) as conn:#异步打开__pool，并赋值给conn
#         cur=yield from conn.cursor(aiomysql.DictCursor)#建立一个dict类型的游标
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs
#         if size:
#             rs=yield from cur.fetchmany(size)
#         else:
#             rs=yield from cur.fetchall()
#         cur.close()
#         logging.info('rows returned:%s' %len(rs))
#         print( rs)






loop = asyncio.get_event_loop()#要运行协程函数，就需要用到event_loop。需要生成一个event_loop，然后把函数注册到该事件循环上。
loop.run_until_complete(create_pool(loop))





