#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from lib.leancloud_api import LeanCloudApi
from base import BaseHandler
import requests


class LeanHandler(BaseHandler):
    def initialize(self):
        self._leancloud_api = LeanCloudApi('Girls')

    def get(self):
        print 'hehe'
        page = int(self.get_argument('page'))
        print page
        l = self._leancloud_api
        obj_list = l.get_skip_obj_list(page-1)

        result = []
        for i in obj_list:
            img_url = i.get('File').url
            img_info_url = img_url + '?imageInfo'
            try:
                img_info = requests.get(img_info_url).json()
            except:
                img_info = """{
                "format":       "jpeg",
                "width":        640,
                "height":       427,
                "colorModel":   "ycbcr"
                }"""
            #width = img_info.get('width')
            #height = img_info.get('height')
            width = 192
            height = 288
            each_res = {'image': img_url, 'width': width, 'height': height}
            result.append(each_res)

        res = {'total': 20, 'result': result}
        self.write_json(res)
