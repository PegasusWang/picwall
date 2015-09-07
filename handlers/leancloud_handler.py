#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
import requests
from config import redis_config
from base import BaseHandler
from lib.leancloud_api import LeanCloudApi
from redis import Redis
from tornado.escape import json_encode

# todo: 在Application __init__里边初始化redis客户端，和leancloud_api
r = Redis(host=redis_config.HOST, port=redis_config.PORT, db=0)


class LeanHandler(BaseHandler):
    def initialize(self, class_name):
        print 'initialize'
        self._leancloud_api = LeanCloudApi(class_name)
        self._class_name = class_name

    def get(self, width=280):
        page = int(self.get_argument('page'))
        res = r.hget(self._class_name, page)
        if res:
            print 'get from redis'
            self.write_json(res)
        else:
            l = self._leancloud_api

            obj_list = l.get_skip_obj_list(page-1)

            result = []
            for i in obj_list:

                img_url = i.get('File').url
                img_url = img_url + '?imageMogr2/thumbnail/%sx' % width
                ori_width = i.get('width')
                ori_height = i.get('height')
                height = width*ori_height/ori_width

                each_res = {'image': img_url, 'width': width, 'height': height}

                result.append(each_res)

            res = {'total': 20, 'result': result}
            r.hset(self._class_name, page, json_encode(res))
            self.write_json(res)


'''
class LeanHandler(BaseHandler):
    def initialize(self):
        #self._leancloud_api = LeanCloudApi('Girls')
        #self._leancloud_api = LeanCloudApi('Happylim')
        self._leancloud_api = LeanCloudApi('Blendy99')

    def get(self):
        page = int(self.get_argument('page'))
        print page
        l = self._leancloud_api
        obj_list = l.get_skip_obj_list(page-1)

        result = []
        for i in obj_list:
            img_url = i.get('File').url
            img_info_url = img_url + '?imageInfo'
            try:
                #img_info = requests.get(img_info_url).json()
                r = requests.get(img_info_url,
                                        headers={'Connection':'close'})
                print '******'
                img_info = r.json()
                r.connection.close()
                print 'close'
            except:
                img_info = """{
                "format":       "jpeg",
                "width":        640,
                "height":       427,
                "colorModel":   "ycbcr"
                }"""
            ori_width = img_info.get('width')
            ori_height = img_info.get('height')

            width = 480
            height = width*ori_height/ori_width
            img_url = img_url + '?imageMogr2/thumbnail/480x'
            each_res = {'image': img_url, 'width': width, 'height': height}
            result.append(each_res)

        res = {'total': 20, 'result': result}
        self.write_json(res)
'''


'''
 I have experience using tornadoredis, an async redis client, and I
haven't had any problems with it. Works great so far. Here's an
example usage for a WebSocket server:

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
import tornadoredis

class Application(tornado.web.Application):
    def __init__(self):
        self.trdb = tornadoredis.Client()
        self.trdb.connect()
        handlers = [
            (r"/", MyHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)


class MyHandler(tornado.websocket.WebSocketHandler):
    ...
    @tornado.web.anyschronous
    @tornado.gen.engine
    def on_message(self, message):
        yeild tornado.gen.Task(self.application.trdb.lpush, 'messages', message)


That stripped down example will return right away, will not wait for
the lpush to complete.

Hope that helps.
Nick

'''
