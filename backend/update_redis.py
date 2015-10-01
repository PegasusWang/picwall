#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
update redis query string of all leancloud class, run every 24 hours.
hset class_name:width page_num query_json_string.
"""

import _env
import lean_classname
import time
from config import redis_config
from config.img_config import Img
from redis import Redis
from lib.leancloud_api import LeanCloudApi
from tornado.escape import json_encode

r = Redis(redis_config.HOST, redis_config.PORT)
page_num = Img.PAGE_NUM # number of pages you want to cache query sting in redis
width = Img.WIDTH


def update_redis_by_class(class_name):
    """update redis query string of each leancloud class"""
    l = LeanCloudApi(class_name)
    for page in range(1, page_num+1):
        time.sleep(0.3)
        obj_list = l.get_skip_obj_list(page-1, limit_num=Img.LIMIT_NUM)
        if not obj_list:
            return

        result = []
        for i in obj_list:
            img_ID = i.get('ID')
            print(img_ID)
            img_url = i.get('File').url
            img_url = img_url + '?imageMogr2/thumbnail/%sx' % width

            ori_width = i.get('width')
            ori_height = i.get('height')
            height = width*ori_height/ori_width

            each_res = {'id': img_ID, 'image': img_url, 'width': width, 'height': height}
            result.append(each_res)

        res = {'total': page_num, 'result': result}

        try:
            key = class_name + ':' + str(width)
            r.hset(key, page, json_encode(res))
            print 'set redis class', class_name, page
        except:
            print 'redis hset fail', class_name, page


def update_redis_class_list(class_type):
    classname_li = class_type + '_CLASS_NAME'
    try:
        class_name_list = getattr(lean_classname, classname_li)
    except AttributeError:
        return
    for class_name in class_name_list.keys():
        print 'update redis:', class_name
        update_redis_by_class(class_name)


def update_redis_class_list_picwall(class_type):
    classname_li = class_type + '_CLASS_NAME_PICWALL'
    try:
        class_name_list = getattr(lean_classname, classname_li)
    except AttributeError:
        return
    for class_name in class_name_list.keys():
        print 'update redis class', class_name
        update_redis_by_class(class_name)


def main():
    class_type_list = ['GIRLS', 'BOYS', 'GIFS', 'ANIMALS']
    for each in class_type_list:
        print 'update_redis list', each, '**************'
        # update_redis_class_list(each)
        update_redis_class_list_picwall(each)
        time.sleep(1)

if __name__ == '__main__':
    main()
    print time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time()))
