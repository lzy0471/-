import tornado.web
class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("<h1 style='color:#8b8b8b'>这是后台管理系统！</h1>")