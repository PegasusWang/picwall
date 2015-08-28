# coding=utf-8
__author__ = 'JIE'

import tornado.ioloop
from tornado.escape import json_encode
import tornado.web
import tornado.wsgi
import os
from lib import leancloud_api
import requests


class TestHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.render("index.html")
        self.render("t.html")


class LeanHandler(tornado.web.RequestHandler):
    def get(self):
        page = int(self.get_argument('page'))
        l = leancloud_api.LeanCloudApi('Girls')
        obj_list = l.get_skip_obj_list(page-1)

        result = []
        for i in obj_list:
            img_url = i.get('File').url
            img_info_url = img_url + '?imageInfo'
            try:
                img_info = requests.get(img_info_url).json()
            except:
                img_info = """{
                "format":       "jpeg",
                "width":        640,
                "height":       427,
                "colorModel":   "ycbcr"
                }"""
            #width = img_info.get('width')
            #height = img_info.get('height')
            width = 192
            height = 288
            each_res = {'image': img_url, 'width': width, 'height': height}
            result.append(each_res)

        res = {'total': 20, 'result': result}
        self.write(json_encode(res))


class MyHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        l = leancloud_api.LeanCloudApi('Aewae')
        d = l.get_obj_by_ID(100)
#        s = """{"total": 20, "result": [{"width": 540, "image": "http://ac-0pdchyat.clouddn.com/9d82a80a1fc876c2.jpg", "height": 810}, {"width": 533, "image": "http://ac-0pdchyat.clouddn.com/2b03d871b325b62.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/481bb15c2aadf4a.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/c6b8408d80b66a61.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/6aaf69d02d93bdd9.jpg", "height": 792}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/c3f2ed087f8ca062.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/2df28ec3da44bd1.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/eb94f64e82281d51.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/2412eb0893913284.jpg", "height": 810}, {"width": 300, "image": "http://ac-0pdchyat.clouddn.com/73d76469e9e9e06d.jpg", "height": 450}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/a6f9f5bb15e738b3.jpg", "height": 361}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/276ea122655840eb.jpg", "height": 720}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/e9c99f09861a21f8.jpg", "height": 809}, {"width": 538, "image": "http://ac-0pdchyat.clouddn.com/59775cc48dae277b.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/ea6c75baf6b447b4.jpg", "height": 540}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/f1aed681def2d168.jpg", "height": 405}, {"width": 500, "image": "http://ac-0pdchyat.clouddn.com/adb4334f6b111a68.jpg", "height": 750}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/62767ce688852ba4.jpg", "height": 810}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/52fec7a33edbb28f.jpg", "height": 360}, {"width": 540, "image": "http://ac-0pdchyat.clouddn.com/5fd5a07431a0cf2b.jpg", "height": 721}]}"""
        s = """{"total": 20, "result": [{"width": 192, "image": "http://ac-0pdchyat.clouddn.com/9d82a80a1fc876c2.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/2b03d871b325b62.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/481bb15c2aadf4a.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/c6b8408d80b66a61.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/6aaf69d02d93bdd9.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/c3f2ed087f8ca062.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/2df28ec3da44bd1.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/eb94f64e82281d51.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/2412eb0893913284.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/73d76469e9e9e06d.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/a6f9f5bb15e738b3.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/276ea122655840eb.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/e9c99f09861a21f8.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/59775cc48dae277b.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/ea6c75baf6b447b4.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/f1aed681def2d168.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/adb4334f6b111a68.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/62767ce688852ba4.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/52fec7a33edbb28f.jpg", "height": 288}, {"width": 192, "image": "http://ac-0pdchyat.clouddn.com/5fd5a07431a0cf2b.jpg", "height": 288}]}"""
        self.write(s)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "gzip": True,
    "debug": True,
}

app = tornado.wsgi.WSGIApplication([
    ("/", TestHander),
    ("/data/data1.json", MyHander),
    ("/res", LeanHandler),
], **settings)




# if __name__ == "__main__":
#     app.listen(8888)
#     print 'server start'
#     tornado.ioloop.IOLoop.current().start()
