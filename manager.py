#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
# 【管理器】
#
# 对外提供四个方法：
#
# 1. add_url(url)
# 添加一个 URL，接收一个参数 URL
# 
# 2. add_urls(url)
# 批量添加 URL，接收一个参数 URL
#
# 3. num_url()
# 管理器中URL 的数量
# 
# 4. get_url()
# 从管理器中获取一个 URL
#


class Manager(object):

    def __init__(self):

        # 待爬取的 URL 集合
        self.new_urls = set()
        # 已爬取的 URL 集合
        self.old_urls = set()

    # 添加一个 URL
    def add_url(self, url):

        # 判断 url 是否为空，为空则返回 None
        if url is None:
            return

        # 判断 url 是否存在于【待爬取的 URL 集合】和【已爬取的 URL 集合】，如若都不在将新 url 添加到【待爬取的 URL 集合】中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加 URL
    def add_urls(self, urls):
 
        if urls is None or len(urls) == 0:
            return
 
        for url in urls:
            # 将 URL 集合交给 add_url() 函数处理
            self.add_url(url)

    # 返回管理器中 URL 的数量
    def num_url(self):

        return len(self.new_urls) != 0

    # 从管理器中获取一个 URL
    def get_url(self):

        url = self.new_urls.pop()
        self.old_urls.add(url)

        return url
