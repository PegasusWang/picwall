#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import (
    base, admin, site, user, show,
    leancloud_handler,
)
from tornado.web import url


url_patterns = [
    # leancloud api
    url(r'/api/data.json', leancloud_handler.LeanClassHandler),

    url(r'/?', site.SiteHandler, dict(class_name='Girls')),
    url(r'/show/([\w_]+)/?', show.ShowHandler),

    url(r'/user/?', user.UserMainHandler),
    url(r'/user/login/?', user.UserLoginHandler),
    url(r'/user/logout/?', user.UserLogoutHandler),
    url(r'/user/register/?', user.UserRegisterHandler),

    # admin
    url(r'/admin/?', admin.AdminMainHandler),
    url(r'/admin/login/?', admin.AdminLoginHandler),
    url(r'/admin/img/solve', admin.ImgDelHandler),
    url(r'/admin/girls/?', admin.AdminSiteHandler, dict(class_name='Girls')),
    url(r'/admin/girls/(\w+-\w+)/?', admin.AdminSiteTagHandler),

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

    url(r'.*', base.PageNotFoundHandler),    # catch return 404 page
]
