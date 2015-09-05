#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler


class MakoHandler(BaseHandler):

    def get(self):
        self.render("mako.html")


class ResizeHandler(BaseHandler):
    def get(self):
        self.render("resize.html")
