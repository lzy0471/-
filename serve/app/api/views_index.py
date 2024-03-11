
from app.api.views_common import CommonHandler
class IndexHandler(CommonHandler):
    def get(self,*args,**kwargs):
        self.write("<h1 style='color:blue'>这是API接口！</h1>")
        self.write("<h1 style='color:red'>{}</h1>".format(str(self.md)))