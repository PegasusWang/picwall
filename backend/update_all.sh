#!/bin/bash

PREFIX=$(cd "$(dirname "$0")"; pwd)
cd $PREFIX

python update_leancloud.py
python update_redis.py
