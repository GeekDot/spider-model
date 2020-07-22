#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
# 【下载器】
#
# requests 模块需要安装
# sudo pip3 install requests
#
# 对外提供一个方法：
#
# download(url)
# 下载网页中的内容，接收一个参数 URL
#


import requests


class Download(object):
    
    def download(self, url):
        
    	# 判断 URL 是否为空，为空直接返回 None
        if url is None:
            return None

        # 请求 URL
        response = requests.get(url = url)

    	# 判断 URL 地址是否访问成功，若失败直接返回 None
        if response.status_code != 200:
            return None

        return response.text
