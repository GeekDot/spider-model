#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
# 【解析器】
#
# bs4 模块需要安装
# sudo pip3 install bs4
#
# 对外提供一个方法：
#
# 1. parser(url)
# BeautifulSoup DOM 树处理，接收两个参数 URL 和 html 内容
#
# 对内提供两个方法：
#
# 1. _get_urls(url, soup)
# 获取网页中的 URL，接收两个参数 URL 和 DOM 树
#
# 2. _get_data(url, soup)
# 获取网页中的数据，接收两个参数 URL 和 DOM 树
#


import re
from bs4 import BeautifulSoup


class Parser(object):

    def _get_urls(self, url, soup):
        
        urls = set()

        links = soup.find_all('a', href=re.compile(r'/peida/archive/*'))
        
        for link in links:

            new_url = link['href']
            urls.add(new_url)

        return urls

    def _get_data(self, url, soup):

        res_data = {}
        res_data['url'] = url
        title_node = soup.find('div', class_='post').find('a')
        res_data['title'] = title_node.get_text()

        return res_data

    def parser(self, url, html):
        
        # 判断 url 是否为空，或网页数据是否为空，为空则返回 None
        if url is None or html is None:
            return

        # 格式化 html 为 BeautifulSoup DOM 树
        soup = BeautifulSoup(html, 'html.parser')

        # 获取网页中的 URL
        urls = self._get_urls(url, soup)
        # 获取网页中的数据
        data = self._get_data(url, soup)
        
        return urls, data
