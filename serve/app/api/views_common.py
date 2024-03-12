# -*- coding: utf-8 -*-
from datetime import datetime
import json
import tornado.web
from concurrent.futures import ThreadPoolExecutor
from app.common.ip2Addr import ip2addr


class CommonHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(1000)  # 定义线程池
    #客户端向服务器端发送的数据进行处理
    #json转化为字典
    @property
    def params(self):
        data = self.request.body
        #包含字节类型，转化为python数据类型
        data = {
            k:v
            for k,v in json.load(data.decode('utf-8')).items()
            }
        return data
    @property
    def dt(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #返回一个时间
    def md(self):
        return self.application.md

    # 公共参数
    def common_params(self):
        data = dict(
            createAdt=self.dt,
            ip=self.request.remote_ip,
            addr=ip2addr(self.request.remote_ip)['region'].decode('utf-8'),
            headers=dict(self.request.headers)
        )
        return data
