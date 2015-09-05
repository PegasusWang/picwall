#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.write('<a href="%s">link to story 1</a>' %
                   self.reverse_url('story', '1'))

class StoryHandler(BaseHandler):
    def initialize(self, name):
        print name
        self.name = name

    def get(self, story_id):
        self.write(story_id)
