#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config import redis_config
from redis import StrictRedis
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen
from tornado.options import options

from settings import settings
from urls import url_patterns


class PicWall(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        self._redis = StrictRedis(redis_config.HOST, redis_config.PORT)


def main():
    app = PicWall()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
