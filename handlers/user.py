#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
import leancloud
import _leancloud_init
from base import BaseHandler
from tornado.web import authenticated
from leancloud import User


class UserBaseHandler(BaseHandler):
    def get_current_user(self):
        # Do not use get_secure_cookie('use_id', 0)
        return self.get_secure_cookie('user_id')


class UserMainHandler(UserBaseHandler):
    @authenticated
    def get(self):
        self.render('/user/index.html', user=self.current_user)


class UserRegisterHandler(UserBaseHandler):
    def get(self):
        self.render('/user/register.html')

    def post(self):
        email = self.get_argument('email')
        username = self.get_argument('username')
        password = self.get_argument('password')

        user = User()
        user.set("email", email)
        user.set("username", username)
        user.set("password", password)
        user.sign_up()

        self.set_secure_cookie("username", username)
        self.set_secure_cookie("user_id", user.id)

        self.redirect('/')
        # self.redirect(self.get_argument('next', '/'))


class UserLoginHandler(UserBaseHandler):
    def get(self):
        self.render('/user/login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        try:
            user = User()
            user.login(username, password)
        except leancloud.errors.LeanCloudError as e:
            print(e.code, e.error)

        self.set_secure_cookie("user_id", user.id)
        self.set_secure_cookie("username", username)
        #self.redirect('/')
        self.redirect('/user/')


class UserLogoutHandler(UserBaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.clear_cookie("user_id")
        self.redirect(self.get_argument("next", "/"))
