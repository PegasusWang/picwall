#!/usr/bin/env python
# -*- coding:utf-8 -*-

import traceback
from tornado.gen import coroutine
from base import BaseHandler
from tornado.web import addslash,  asynchronous
from tornado.escape import json_decode
from tornado.httpclient import AsyncHTTPClient
from _tag_to_class import tag_to_class


KEY = 'IMGINFO'

'''
class ShowHandler(BaseHandler):
    @addslash
    def get(self):

        self.render("/site/show.html")
'''


class ShowHandler(BaseHandler):
    @property
    def _redis(self):
        return self.application._redis

    @addslash
    @coroutine
    def get(self, *args):
        class_name = args[0]
        img_id = args[1]
        img_url = 'http://ac-0pdchyat.clouddn.com/' + img_id.replace('_', '.')
        scale_img_url = img_url + '?imageMogr2/thumbnail/!80p/interlace/1'    # 80%
        is_gif = True if 'gif' in img_id.lower() else False
        tpl = "/site/show_gif.html" if is_gif else "/site/show.html"

        try:
            img_info = self._redis.hget(KEY, img_id)    # value is width_height
            scale_width = int(img_info.split('_')[0])
            scale_height = int(img_info.split('_')[1])
            self.render(tpl, scale_src=scale_img_url, src=img_url,
                        width=scale_width, height=scale_height)
        except:
            pass
            img_info_url = img_url + '?imageInfo'
            http_client = AsyncHTTPClient()
            response = yield http_client.fetch(img_info_url)
            json_str = response.body

            img_info = json_decode(json_str)
            img_width = img_info.get('width', None)
            img_height = img_info.get('height', None)
            if is_gif:
                scale_width, scale_height = int(img_width), int(img_height)
                scale_img_url = img_url
            else:
                scale_width, scale_height = int(img_width*0.8), int(img_height*0.8)

            try:
                self._redis.hset(KEY, img_id,
                    str(scale_width)+'_'+str(scale_height))
            except:
                traceback.print_exc()
                pass

            self.render(tpl, scale_src=scale_img_url, src=img_url,
                        width=scale_width, height=scale_height)
