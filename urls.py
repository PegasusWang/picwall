#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import base
from handlers import tem_test
from handlers import mako_test
from handlers import leancloud_handler
from handlers import admin
from handlers import site
from tornado.web import url
from lib.leancloud_api import LeanCloudApi

class_name = 'Girls'


url_patterns = [
    url(r'/?', mako_test.ResizeHandler),

    # admin
    url(r'/admin/(\w+)/?', admin.AdminHandler),
    url(r'/admin/(\w+\/?\w+)/data.json', admin.LeanClassHandler),

    # site boys
    url(r'/boys/?', site.SiteHandler, dict(class_name='Boys')),
    url(r'/boys/(\w+-\w+)/?', site.SiteTagHandler),

    # site girls
    url(r'/girls/?', site.SiteHandler, dict(class_name='Girls')),
    url(r'/girls/(\w+-\w+)/?', site.SiteTagHandler),

    # site gifs
    url(r'/gifs/?', site.SiteHandler, dict(class_name='Gifs')),
    url(r'/gifs/(\w+-\w+)/?', site.SiteTagHandler),

    # site animals
    url(r'/animals/?', site.SiteHandler, dict(class_name='Animals')),
    url(r'/animals/(\w+-\w+)/?', site.SiteTagHandler),



    # leancloud
    url(r'/(\w+\/?\w+)/(\w+)?/data.json', leancloud_handler.LeanClassHandler),
    url(r'/(\w+\/?\w+-\w+)/(\w+)?/data.json', leancloud_handler.LeanClassHandler),


    #url(r'/mako/?', mako_test.MakoHandler),
    #url(r'/resize/?', mako_test.ResizeHandler),
    #url(r'/tem/?', tem_test.TemHandler),



    url(r'(\/?\w*)/data/data1.json', leancloud_handler.LeanHandler,
        dict(class_name=class_name, leancloud_db=LeanCloudApi(class_name))),



    url(r'.*', base.PageNotFoundHandler),    # catch return 404 page
]
