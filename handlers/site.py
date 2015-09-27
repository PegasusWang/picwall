#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler
from tornado.web import addslash
from tag_to_class import tag_to_class


class SiteHandler(BaseHandler):
    def initialize(self, class_name):
        super(SiteHandler, self).initialize()
        self._class_name = class_name

    @addslash
    def get(self):
        self.render("/site/site.html", class_name=self._class_name)


class SiteTagHandler(BaseHandler):
    @addslash
    def get(self, class_name):
        self.render("/site/site.html",
                    class_name=tag_to_class[class_name])
