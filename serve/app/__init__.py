# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

from tornado.options import options,define
from app.configs import configs, mongodb_configs
from app.urls import urls
from pymongo import  MongoClient   #mongodb的客户端连接


define('port',type=int,default=50000,help='运行端口') #配置服务器启动端口
class CustomApplication(tornado.web.Application):#自定义应用

    def __init__(self,urls,configs):
        settings = configs
        handlers = urls
        self.md = MongoClient(host=mongodb_configs['db_host'], port=mongodb_configs['db_port'])
        super(CustomApplication, self).__init__(handlers=handlers,**settings)

def create_server():  #创建服务
    tornado.options.parse_command_line()
    #创建http服务 #xheader=true       获取用户真实IP地址
    http_server = tornado.httpserver.HTTPServer(
        CustomApplication(urls,configs),
        xheaders=True
    )
    #监听端口
    http_server.listen(options.port)
    #启动输入输出事件循环
    tornado.ioloop.IOLoop.instance().start()


