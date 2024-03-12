# -*- coding: utf-8 -*-
import tornado.web
from concurrent.futures import ThreadPoolExecutor
class CommonHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(1000)  #定义线程池
    @property
    def md(self):
        return self.application.md
