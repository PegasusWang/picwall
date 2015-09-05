#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import base
from handlers import tem_test
from handlers import mako_test
from handlers import json_handler
from handlers import leancloud_handler

url_patterns = [
    #(r'/', test.MainHandler),
    (r'/mako', mako_test.MakoHandler),
    (r'/resize', mako_test.ResizeHandler),
    (r'/tem', tem_test.TemHandler),
    #(r'/data/data1.json', json_handler.JsonHander),
    (r'/data/data1.json', leancloud_handler.LeanHandler),
    ('.*', base.PageNotFoundHandler),
]
