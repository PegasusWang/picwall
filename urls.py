#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import base
from handlers import tem_test
from handlers import mako_test
from handlers import leancloud_handler
from tornado.web import url

class_name = 'Catsdogsblog'

url_patterns = [
    url(r'/mako/?', mako_test.MakoHandler),
    url(r'/resize/?', mako_test.ResizeHandler),
    url(r'/tem/?', tem_test.TemHandler),
    url(r'.*/data/data1.json', leancloud_handler.LeanHandler,
        dict(class_name=class_name)),
    url(r'.*', base.PageNotFoundHandler),    # catch return 404 page
]
