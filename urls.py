#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import tem_test
from handlers import mako_test
from handlers import json_handler

url_patterns = [
    #(r'/', test.MainHandler),
    (r'/mako', mako_test.MakoHandler),
    (r'/tem', tem_test.TemHandler),
    (r'/data/data1.json', json_handler.JsonHander),
]
