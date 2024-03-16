# -*- coding:utf-8 -*-
import tornado.concurrent
import tornado.gen

from app.api.views_common import CommonHandler

#菜单接口
class GridHandler(CommonHandler):
    @tornado.gen.coroutine
    def get(self):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        grid = {
            'style': 'width:50%',
            'logo': self.site_url + 'static/images/background.png',  # 这里缺少了逗号
            'name': '导航栏',
            'data': [
                {
                    'name': '人脸检测',
                    'image': self.site_url + 'static/images/g1-1.png',  # 这里也缺少了逗号
                    'url': '/pages/match/match?cate=1'
                },
                {
                    'name': '人脸勾勒',
                    'image': self.site_url + 'static/images/g1-2.png',  # 这里也缺少了逗号
                    'url': '/pages/match/match?cate=2'
                },
                {
                    'name': '人脸截取',
                    'image': self.site_url + 'static/images/g1-3.png',  # 这里也缺少了逗号
                    'url': '/pages/match/match?cate=3'
                },
                {
                    'name': '人脸化妆',
                    'image': self.site_url + 'static/images/g1-4.png',  # 这里也缺少了逗号
                    'url': '/pages/match/match?cate=4'
                },
                {
                    'name': '人脸特征',
                    'image': self.site_url + 'static/images/g1-5.png',  # 这里也缺少了逗号
                    'url': '/pages/match/match?cate=5'
                },
                {
                    'name': '关于作者',
                    'image': self.site_url + 'static/images/g1-6.png',  # 这里也缺少了逗号
                    'url': '/pages/about/about'
                },
            ]
        }
        # 此处可以添加处理grid的代码，例如返回grid或对其进行进一步的操作
        self.write(grid) # 假设你想返回这个字典
