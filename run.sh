#!/bin/bash

PREFIX=$(cd "$(dirname "$0")"; pwd)
cd $PREFIX

rm ./_templates/*
./app.py
