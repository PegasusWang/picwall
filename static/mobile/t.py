#!/usr/bin/env python
# -*- coding:utf-8 -*-

#from codecs import open as open

with open('backup_default.htm') as f:
    for each in f:
        print each.decode('gb2312').encode('utf-8'),
