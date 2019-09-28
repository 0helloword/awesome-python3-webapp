#导入logging模块，通过logging.basicConfig函数对日志的输出等级做相关配置
import logging;logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):#首页返回显示AWesome
    #要加上content_type='text/html'，否则打开localhost:9000变成下载一个显示AWesome的文件
    return web.Response(body='<h1>AWesome</h1>'.encode('utf-8'),content_type='text/html')

#@符号属于函数式编程的装饰器。放在函数定义的上面。主要作用是在不改变原来函数代码的前提下，给函数增加新的功能。
#asyncio模块是对异步IO的支持，init()从普通generator变成了coroutine类型。通过装饰，将同步流程转为异步流程。
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)#增加路由
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()#要运行协程函数，就需要用到event_loop。需要生成一个event_loop，然后把函数注册到该事件循环上。
loop.run_until_complete(init(loop))#run_until_complete方法将协程包装成为了一个任务（task）对象
loop.run_forever()