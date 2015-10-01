#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
import leancloud
import _leancloud_init
from base import BaseHandler
from tornado.web import authenticated, addslash
from leancloud import User
from lib.leancloud_api import LeanCloudApi
from _tag_to_class import tag_to_class


class AdminBaseHandler(BaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user_id')

    def get_login_url(self):
        return '/admin/login/'


class AdminMainHandler(AdminBaseHandler):
    @authenticated
    def get(self):
        if not self.current_user:
            self.redirect('/admin/login/')
        self.render('/admin/admin.html', user=self.current_user,
                    class_name='Girls')


class AdminSiteHandler(AdminBaseHandler):
    def initialize(self, class_name):
        super(AdminSiteHandler, self).initialize()
        self._class_name = class_name

    @authenticated
    @addslash
    def get(self):
        self.render("/admin/adminsite.html", class_name=self._class_name)


class AdminSiteTagHandler(AdminBaseHandler):
    @authenticated
    @addslash
    def get(self, class_name):
        self.render("/admin/adminsite.html",
                    class_name=tag_to_class[class_name])


class ImgDelHandler(AdminBaseHandler):
    @authenticated
    def post(self):
        class_name = self.get_body_argument('class_name')
        img_ID = self.get_body_argument('img_id')
        l = LeanCloudApi(class_name)
        try:
            # l.del_by_ID(int(img_ID))
            l.set_by_ID(int(img_ID))    # set img ID to 0
            d = {'msg': 'success', 'img_id': img_ID}
            self.write(d)
        except:
            import traceback
            traceback.print_exc()
            d = {'msg': 'success', 'img_id': img_ID}
            self.write(d)


class AdminLoginHandler(AdminBaseHandler):
    def get(self):
        self.render('/admin/login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if "admin" == username:
            try:
                user = User()
                user.login(username, password)
            except leancloud.errors.LeanCloudError as e:
                print(e.code, e.error)
                self.redirect('/admin/login/')

            self.set_secure_cookie("user_id", user.id)
            self.set_secure_cookie("username", username)
            self.redirect('/admin/')
        else:
            self.redirect('/admin/login/')


class AdminLogoutHandler(AdminBaseHandler):
    def get(self):
        self.clear_cookie("user_id")
        self.clear_cookie("username")
        self.redirect(self.get_argument("next", "/"))
