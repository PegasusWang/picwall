#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler
from tornado.web import addslash

tag_to_class = {
    # girls
    'girls-sexy': 'Sexy',
    'girls-cute': 'Cute',
    'girls-beauty': 'Beauty',
    'girls-japan': 'Japan',
    'girls-korean': 'Korean',
    'girls-china': 'China',
    'girls-leg': 'Leg',
    'girls-cos': 'Cos',
    'girls-gif': 'GirlsGif',

    # boys
    'boys-korean': 'Boys',

    # gif
    'gifs-funny': 'GifsFunny',
    'gifs-kuso': 'GifKuso',
    'gifs-other': 'GifsOther',
    'gifs-lol': 'GifsLol',

    # animails
    'animals-catdog': 'AnimalsCatdog',
}


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
