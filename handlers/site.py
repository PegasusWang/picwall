#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler

tag_to_class = {
    'sexy': 'Sexy',
    'cute': 'Cute',
    'beauty': 'Beauty',
    'japan': 'Japan',
    'korean': 'Korean',
    'china': 'China',
    'leg': 'Leg',
}


class SiteHandler(BaseHandler):
    def initialize(self, class_name):
        super(SiteHandler, self).initialize()
        self._class_name = class_name

    def get(self):
        self.render("/site/site.html", class_name=self._class_name)


class SiteTagHandler(BaseHandler):
    def get(self, class_name):
        self.render("/site/site.html",
                    class_name=tag_to_class[class_name])
