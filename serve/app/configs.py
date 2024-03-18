# -*- coding: utf-8 -*-
import os
root_path = os.path.dirname(__file__)

#公共配置
configs = dict(
    xsrf_cookies=True,
    cookie_secret='e7d864e84e7142a49bcb555a0b491951',
    static_path=os.path.join(root_path, 'static'),
    template_path=os.path.join(root_path, 'templates'),
    debug=True  #开启调试模式，False是关闭
)

#mongodb配置
#mongodb_configs = dict(
 #   db_host='127.0.0.1',
  #  db_port=27017
#)
mongodb_configs = {
    'db_host': '127.0.0.1',
    'db_port': 27017
}
