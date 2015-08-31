#!/bin/bash

PREFIX=$(cd "$(dirname "$0")"; pwd)
cd $PREFIX

./app.py
