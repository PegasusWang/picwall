#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handlers import (
    base, admin, site, user, show,
    leancloud_handler, mobile,
)
from tornado.web import url


url_patterns = [
    # leancloud api
    url(r'/api/data.json', leancloud_handler.LeanClassHandler),

    url(r'/?', site.SiteHandler, dict(class_name='Girls')),
    url(r'/show/([\w_]+)/?', show.ShowHandler),
    url(r'/mobile/show/([\w_]+)/?', show.MobileShowHandler),

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
    url(r'/admin/boys/?', admin.AdminSiteHandler, dict(class_name='Boys')),
    url(r'/admin/boys/(\w+-\w+)/?', admin.AdminSiteTagHandler),
    url(r'/admin/gifs/?', admin.AdminSiteHandler, dict(class_name='Gifs')),
    url(r'/admin/gifs/(\w+-\w+)/?', admin.AdminSiteTagHandler),
    url(r'/admin/animals/?', admin.AdminSiteHandler, dict(class_name='Animals')),
    url(r'/admin/animals/(\w+-\w+)/?', admin.AdminSiteTagHandler),
    url(r'/admin/nature/?', admin.AdminSiteHandler, dict(class_name='Nature')),

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

    # site nature
    url(r'/nature/?', site.SiteHandler, dict(class_name='Nature')),


    # for mobile
    url(r'/mobile/?', mobile.SiteHandler, dict(class_name='Girls')),

    url(r'/mobile/boys/?', mobile.SiteHandler, dict(class_name='Boys')),
    url(r'/mobile/boys/(\w+-\w+)/?', mobile.SiteTagHandler),

    # site girls
    url(r'/mobile/girls/?', mobile.SiteHandler, dict(class_name='Girls')),
    url(r'/mobile/girls/(\w+-\w+)/?', mobile.SiteTagHandler),

    # site gifs
    url(r'/mobile/gifs/?', mobile.SiteHandler, dict(class_name='Gifs')),
    url(r'/mobile/gifs/(\w+-\w+)/?', mobile.SiteTagHandler),

    # site animals
    url(r'/mobile/animals/?', mobile.SiteHandler, dict(class_name='Animals')),
    url(r'/mobile/animals/(\w+-\w+)/?', mobile.SiteTagHandler),

    # site nature
    url(r'/mobile/nature/?', mobile.SiteHandler, dict(class_name='Nature')),

    url(r'.*', base.PageNotFoundHandler),    # catch return 404 page
]
