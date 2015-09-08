#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
update redis query string of all leancloud class when class save new img.
hset class_name:width page_num query_json_string.
"""

import _env
import lean_classname
from config import redis_config
from redis import Redis
from lib.leancloud_api import LeanCloudApi
from tornado.escape import json_encode

r = Redis(redis_config.HOST, redis_config.PORT)
page_num = 50
width = 280


def update_redis_by_class(class_name):
    """update redis query string of each leancloud class"""
    l = LeanCloudApi(class_name)
    for page in range(1, page_num):
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
            key = class_name + ':' + str(width)
            r.hset(key, page, json_encode(res))
        except:
            print 'redis hset fail'


def update_redis_class_list(class_type):
    classname_li = class_type + '_CLASS_NAME'
    class_name_list = getattr(lean_classname, classname_li)
    for class_name in class_name_list:
        print 'update redis:', class_name
        update_redis_by_class(class_name)


def main():
    class_type_list = ['GIRLS', 'BOYS', 'GIFS']
    for each in class_type_list:
        print each
        update_redis_class_list(each)

if __name__ == '__main__':
    main()
