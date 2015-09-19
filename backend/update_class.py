#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from update_leancloud import *
from update_redis import *


def main():
    try:
        class_name = sys.argv[1]
    except:
        class_name = ''

    if class_name:
        print 'update leancloud class', class_name
        l = leancloud_api.LeanCloudApi(class_name)
        l.solve_nums_class_obj(update_obj_list, NUM)
        print 'update redis class', class_name
        update_redis_by_class(class_name)


if __name__ == '__main__':
    main()
