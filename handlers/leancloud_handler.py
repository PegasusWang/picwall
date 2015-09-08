#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from tornado.web import RequestHandler
from lib.leancloud_api import LeanCloudApi
from tornado.escape import json_encode


class LeanHandler(RequestHandler):
    @property
    def _redis(self):
        return self.application._redis

    def initialize(self, class_name, leancloud_db):
        self._leancloud_api = leancloud_db
        self._class_name = class_name

    def get(self, width=280):
        try:
            page = int(self.get_argument('page'))
        except:
            page = 1
        try:
            res = self._redis.hget(self._class_name, page)
        except:
            res = ''
        if res:
            self.write(res)

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
                # TODO: 错误检查，没有高和宽度的设置默认值

            res = {'total': 20, 'result': result}
            try:
                key = self._class_name + ':' + str(width)
                self._redis.hset(key, page, json_encode(res))
            except:
                pass
            self.write(res)

"""
    @asynchronous
    @engine
    def get(self, width=280):
        try:
            page = int(self.get_argument('page'))
        except:
            page = 1
        try:
            #res = self._redis.hget(self._class_name, page)
            res = yield Task(self._redis.hget, self._class_name, page)
        except:
            res = ''
        if res:
            print 'get from redis'
            print 'len', len(res)
            self.write(res)
            self.finish()
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
            try:
                #self._redis.hset(self._class_name, page, json_encode(res))
                yield Task(self._redis.hset(self._class_name, page, json_encode(res)))
            except:
                pass
            self.write(res)
            self.finish()

"""

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
