#!/usr/bin/env python
# -*- coding:utf-8 -*-

import _env
import traceback
from tornado.gen import coroutine
from base import BaseHandler
from tornado.web import addslash
from tornado.escape import json_decode
from tornado.httpclient import AsyncHTTPClient
from config.img_config import Img

KEY = 'MOBILE'
SCALE = Img.SCALE


class ShowHandler(BaseHandler):
    @property
    def _redis(self):
        return self.application._redis

    @addslash
    @coroutine
    def get(self, *args):
        img_id = args[-1]
        img_url = 'http://ac-0pdchyat.clouddn.com/' + img_id.replace('_', '.')
        scale_img_url = img_url + ('?imageMogr2/thumbnail/!%dp/interlace/1' % int(SCALE*100))
        is_gif = True if 'gif' in img_id.lower() else False
        tpl = "/site/show_gif.html" if is_gif else "/site/show.html"

        try:
            img_info = self._redis.hget(KEY, img_id)    # value is width_height
            scale_width = int(img_info.split('_')[0])
            scale_height = int(img_info.split('_')[1])
            print('from redis', img_id)
            self.render(tpl, scale_src=scale_img_url, src=img_url,
                        width=scale_width, height=scale_height)
        except:
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
                scale_width, scale_height = int(img_width*SCALE), int(img_height*SCALE)

            try:
                self._redis.hset(KEY, img_id,
                                 str(scale_width)+'_'+str(scale_height))
            except:
                traceback.print_exc()
                pass

            self.render(tpl, scale_src=scale_img_url, src=img_url,
                        width=scale_width, height=scale_height)


class MobileShowHandler(BaseHandler):
    @property
    def _redis(self):
        return self.application._redis

    @addslash
    @coroutine
    def get(self, *args):
        img_id = args[-1]
        img_url = 'http://ac-0pdchyat.clouddn.com/' + img_id.replace('_', '.')
        self.render("/mobile/site.html", src=img_url)
