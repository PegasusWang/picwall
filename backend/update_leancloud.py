#!/usr/bin/env python
# -*- coding:utf-8 -*-


import _env
import lib.leancloud_api as leancloud_api
import requests
import time
import lean_classname
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
        if obj.get('height') and obj.get('width'):  # skip obj has width
            return
        img_url = obj.get('File').url
        img_info_url = img_url + '?imageInfo'
        r = fetch_data(img_info_url)

        if not r:
            return

        img_info = r.json()
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
        if i:
            add_img_info(i)

NUM = 100    # num of each class imgs will update


def update_leancloud_class_list(class_type):
    classname_li = class_type + '_CLASS_NAME'
    class_name_list = getattr(lean_classname, classname_li)
    for class_name in class_name_list:
        l = leancloud_api.LeanCloudApi(class_name)
        obj_list = l.get_recent_obj_list(NUM)
        update_obj_list(obj_list)


def update_leancloud_class_list_picwall(class_type):
    classname_li = class_type + '_CLASS_NAME_PICWALL'
    class_name_list = getattr(lean_classname, classname_li)
    for class_name in class_name_list:
        l = leancloud_api.LeanCloudApi(class_name)
        obj_list = l.get_recent_obj_list(NUM)
        update_obj_list(obj_list)


def main():
    class_type_list = ['GIRLS', 'BOYS', 'GIFS']
    for each in class_type_list:
        print each
        # update_leancloud_class_list(each)
        update_leancloud_class_list_picwall(each)


if __name__ == '__main__':
    main()
    print '**********finish********'
