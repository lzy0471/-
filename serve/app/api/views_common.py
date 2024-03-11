# -*- coding: utf-8 -*-
import tornado.web
class CommonHandler(tornado.web.RequestHandler):
    @property
    def md(self):
        return self.application.md
