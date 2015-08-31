#!/usr/bin/env python
# -*- coding:utf-8 -*-

import _env
import tornado.web
import mako.lookup
import mako.template
from mako import exceptions
from os.path import join


TEMPLATE_PATH = [join(_env.PREFIX, 'templates')]

MAKO_LOOK_UP = mako.lookup.TemplateLookup(
    directories=TEMPLATE_PATH,
    input_encoding='utf-8',
    output_encoding='utf-8',
    filesystem_checks=False,
    encoding_errors='replace',
    module_directory=join(_env.PREFIX, '_templates'),
)


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, lookup=MAKO_LOOK_UP):
        '''Set template lookup object, Defalut is MAKO_LOOK_UP'''
        self._lookup = lookup

    def render_string(self, filename, **kwargs):
        '''Override render_string to use mako template.
        Like tornado render_string method, this method
        also pass request handler environment to template engine.
        '''
        try:
            template = self._lookup.get_template(filename)
            env_kwargs = dict(
                handler=self,
                request=self.request,
                current_user=self.current_user,
                locale=self.locale,
                _=self.locale.translate,
                static_url=self.static_url,
                xsrf_form_html=self.xsrf_form_html,
                reverse_url=self.application.reverse_url,
            )
            env_kwargs.update(kwargs)
            return template.render(**env_kwargs)
        except:
            # exception handler
            print exceptions.html_error_template().render()
            # pass

    def render(self, filename, **kwargs):
        self.finish(self.render_string(filename, **kwargs))

    def write_json(self, data_dict):
        """Write json data to client, self.write default call json_encode."""
        self.set_header('Content-Type', 'application/json')
        self.write(data_dict)
