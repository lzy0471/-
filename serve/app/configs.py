# -*- coding: utf-8 -*-
import os
root_path = os.path.dirname(__file__)

#公共配置
configs = dict(
    static_path=os.path.join(root_path, 'static'),
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
