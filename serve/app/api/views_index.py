import time
import tornado.gen
import tornado.concurrent
from app.api.views_common import CommonHandler

class IndexHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self,*args,**kwargs):
        yield self.get_response()
    @tornado.concurrent.run_on_executor()   #让阻塞的代码在线程池里面运行
    def get_response(self):
        time.sleep(3)  # 休息3秒（响应3秒）
        self.write("<h1 style='color:blue'>这是API接口！</h1>")
        self.write("<h1 style='color:red'>{}</h1>".format(str(self.md)))