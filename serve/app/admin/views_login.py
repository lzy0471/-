# -*- coding: utf-8 -*-
import tornado.gen
import tornado.concurrent
from app.admin.views_admin import AdminHandler
#登录视图
class LoginHandler(AdminHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        self.html('admin/login.html')
