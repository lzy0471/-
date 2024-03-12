# -*- coding: utf-8 -*-
from app.admin.views_index import IndexHandler as admin_index
from app.api.views_index import IndexHandler as api_index
from app.api.views_user import UserHandler as api_user

# 相同视图名称可以用不同的别名区分命名
# API接口
api_urls = [
    (r'/', api_index),
    (r'/user/', api_user),
]

# 后台系统
admin_urls = [
    (r'/admin/', admin_index)
]

# urls汇总
urls = api_urls + admin_urls
