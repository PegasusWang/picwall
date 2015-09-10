#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import base
from handlers import tem_test
from handlers import mako_test
from handlers import leancloud_handler
from tornado.web import url
from lib.leancloud_api import LeanCloudApi

class_name = 'Jgiri'
#class_name = 'Tychoon'
#class_name = 'Ganpukudou'
#class_name = 'Girls'
leancloud_db = LeanCloudApi(class_name)


url_patterns = [
    url(r'/', leancloud_handler.LeanHandler),
    url(r'/mako/?', mako_test.MakoHandler),
    url(r'/resize/?', mako_test.ResizeHandler),
    url(r'/tem/?', tem_test.TemHandler),
    url(r'.*/data/data1.json', leancloud_handler.LeanHandler,
        dict(class_name=class_name, leancloud_db=leancloud_db)),
    url(r'.*', base.PageNotFoundHandler),    # catch return 404 page
]
