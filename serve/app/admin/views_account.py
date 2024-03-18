# -*- coding: utf-8 -*-
import datetime

import tornado.gen
import tornado.concurrent
from app.admin.views_admin import AdminHandler
from app.common.forms import AccountAddForm
from werkzeug.security import generate_password_hash

#添加账号视图
class AccountAddhandler(AdminHandler):
    #GET请求
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_reponse()
    #GET响应
    @tornado.concurrent.run_on_executor
    def get_reponse(self):
        self.html('admin/account_add.html')
    #post请求
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        yield self.post_response()
    #post响应
    @tornado.concurrent.run_on_executor
    def post_response(self):
        res = dict(code=0,msg='失败')
        form = AccountAddForm(self.form_params)
        if form.validate():
            #验证通过
            #保存数据
            db = self.md.face_project
            co = db.account
            co.insert_one(
                dict(
                    name=form.data['name'],
                    pwd=generate_password_hash(form.data['pwd']),
                    createdAt=datetime.datetime.now(),
                    updatedAt=datetime.datetime.now()
                )
            )
            #定义成功的接口格式
            res['code'] = 1
            res['msg'] = '成功'
        else:
            res['data'] = form.errors
            #定义失败的接口格式
        self.write(res)