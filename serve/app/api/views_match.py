# -*- coding: utf-8 -*-
from app.api.views_common import CommonHandler
import tornado.gen
import tornado.concurrent
class MatchHandler(CommonHandler):
#人脸识别视图
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
       yield self.get_response()
    @tornado.concurrent.run_on_executor
    def get_response(self):
        cate = self.get_argument('cate',1)
        print("Received cate:", cate)
        data = {
        1:{
            'cate':1,
            'name':'人脸检测示例',
            'unknown_image':[self.site_url+'static/images/exp/g.png'],
            'known_image':[self.site_url+'static/images/exp/g_box.png']
        },
        2: {
            'cate': 2,
            'name': '人脸勾勒示例',
            'unknown_image': [self.site_url + 'static/images/exp/g.png'],
            'known_image': [self.site_url + 'static/images/exp/g_sence.png']
        },
        3: {
            'cate': 3,
            'name': '人脸截取示例',
            'unknown_image': [self.site_url + 'static/images/exp/g.png'],
            'known_image': [
                self.site_url + 'static/images/exp/g1.png',
                self.site_url + 'static/images/exp/g2.png',
                self.site_url + 'static/images/exp/g3.png',
                self.site_url + 'static/images/exp/g4.png'
                            ]
        } ,
        4: {
            'cate': 4,
            'name': '人脸化妆示例',
            'unknown_image': [self.site_url + 'static/images/exp/g.png'],
            'known_image': [self.site_url + 'static/images/exp/g_makeup.png']
        },
        5: {
            'cate': 5,
            'name': '人脸特征示例',
            'unknown_image': [self.site_url + 'static/images/exp/face_68.jpg'],
            'known_image': [self.site_url + 'static/images/exp/face_68_feature.png']
        }
    }
        self.write(data[int(cate)])