#!/usr/bin/env python
# -*- coding:utf-8 -*-


import _env
import lib.leancloud_api as leancloud_api
import requests
import time
import lean_classname
from config.img_config import Img
try:
    import simplejson as json
except ImportError:
    import json


def fetch_data(url, retries=5):
    try:
        data = requests.get(url, timeout=5)
    except:
        if retries > 0:
            print 'fetch...', retries, url
            time.sleep(3)
            return fetch_data(url, retries-1)
        else:
            print 'fetch failed', url
            data = None
            return data
    return data


def add_img_info(obj):
    if not obj:
        return
    if obj.get('height') and obj.get('width'):  # skip obj has width
        print 'skip', obj.get('ID')
        return
    if not obj.get('File'):
        obj.destroy()
        return
    img_url = obj.get('File').url

    img_info_url = img_url + '?imageInfo'
    r = fetch_data(img_info_url)

    if not r:
        return

    img_info = r.json()
    if not img_info:
        print img_info
        print 'can not get img_info', obj.get('ID')
    width = img_info.get('width', None)
    height = img_info.get('height', None)

    try:
        obj.set('height', height)
        obj.set('width', width)
        print 'saving info', obj.get('ID')
        obj.save()
    except:
        time.sleep(1)
        obj.set('height', height)
        obj.set('width', width)
        print 'saving info', obj.get('ID')
        obj.save()


def update_obj_list(res_list):
    for i in res_list:
        add_img_info(i)

NUM = Img.UPDATE_NUM    # num of each class imgs will update
print 'update nums', NUM


def update_leancloud_class_list(class_type, num=NUM):
    classname_li = class_type + '_CLASS_NAME'
    try:
        class_name_list = getattr(lean_classname, classname_li)
    except AttributeError:
        return
    for class_name in class_name_list.keys():
        l = leancloud_api.LeanCloudApi(class_name)
        l.solve_nums_class_obj(update_obj_list, num)


def update_leancloud_class_list_picwall(class_type, num=NUM):
    classname_li = class_type + '_CLASS_NAME_PICWALL'
    try:
        class_name_list = getattr(lean_classname, classname_li)
    except AttributeError:
        return
    for class_name in class_name_list.keys():
        print 'update leancloud class', class_name, '***********'
        l = leancloud_api.LeanCloudApi(class_name)
        l.solve_nums_class_obj(update_obj_list, num)


def main():
    class_type_list = ['GIRLS', 'BOYS', 'GIFS', 'ANIMALS']
    for each in class_type_list:
        print 'update_leancloud list', each, '****************'
        # update_leancloud_class_list(each)
        update_leancloud_class_list_picwall(each)
        time.sleep(1)


if __name__ == '__main__':
    main()
    print time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time()))
