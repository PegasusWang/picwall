#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup

domain = 'http://jinritu.com'


def get_all_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    all_a = soup.find_all('a')
    res = []
    for i in all_a:
        res.append(domain+i.get('href'))
    res = [i for i in res if '#' not in i]
    return res


def get_time():
    time_stamp = time.time()
    t = time.localtime(time_stamp)
    return time.strftime('%Y-%m-%dT%H:%M:%S:%SZ', t)


def generate_xml(filename, url_list):
    with open(filename, "w") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n""")
        for i in url_list:
            f.write('<url>\n')
            f.write('\t<loc>%s</loc>\n' % i)
            f.write('\t<lastmod>%s</lastmod>\n' % get_time())
            f.write('</url>\n')
        f.write("""</urlset>""")


def main():
    urls = get_all_url(domain)
    generate_xml('sitemap.xml', urls)


if __name__ == '__main__':
    main()
    print('gen done')
