# -*- coding: utf-8 -*-
import tornado.web
from concurrent.futures import ThreadPoolExecutor
from app.common.ip2Addr import ip2addr


class CommonHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(1000)  # 定义线程池

    @property
    def md(self):
        return self.application.md

    # 公共参数
    def common_params(self):
        data = dict(
            ip=self.request.remote_ip,
            addr=ip2addr(self.request.remote_ip)['region'].decode('utf-8'),
            headers=dict(self.request.headers)
        )
        return data
