#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler


class TemHandler(RequestHandler):
    def get(self):
        self.render("tem.html")
