#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
# 【调度器】
#
# 调度器又称为引擎，是爬虫逻辑实现的模块。
#
# 爬虫逻辑可分解为如下几个部分：
#
# 1. 查询管理器中是否有待爬取的 URL
# 2. 调度器从管理器中获取一个待爬取 URL
# 3. 将获取到的 URL 交给下载器处理
# 4. 将下载器获取到的网页数据交给解析器处理
# 5. 将解析器处理后的 URL 集合交给管理器
# 6. 将解析器处理后的数据交给输出器
# 7. 重复上述步骤
# 


import manager, download, parser, output


class Spider(object):

    def __init__(self):

        # 实例化 管理器、下载器、解析器、输出器
        self.manager  = manager.Manager()
        self.download = download.Download()
        self.parser   = parser.Parser()
        self.output   = output.Output()

    def spider(self, url):

        # 爬虫计数器
        count = 0

        # 将第一个 URL 放入管理器中
        self.manager.add_url(url)

        # 判断管理器中 URL 的数量是否为 0
        while self.manager.num_url():
                
            try:

                # 从管理器中获取一个 URL
                url = self.manager.get_url()

                # 将获取到的 URL 交给下载器处理
                html = self.download.download(url)

                # 将 URL 和 下载器处理后的网页数据交给解析器处理
                urls, data = self.parser.parser(url, html)

                # 将解析器处理后的数据和新的 URL 分别交给管理器和输出器
                self.manager.add_urls(urls)
                self.output.add_data(data)

                # 最多爬取 100 次
                if count == 100:
                    break

                count += 1

                print('爬虫运行状态 ==> %d : %s' % (count, url))
                                
            except:

                print('爬虫爬取失败')

        # 当爬虫爬取完所有数据后，输出器将数据输出到文件
        self.output.output()

if __name__ == '__main__':
    
    # URL 入口（爬虫爬取的第一个 URL）
    url = 'http://www.cnblogs.com/peida/archive/2012/12/05/2803591.html'
    
    # 实例化调度器并启动爬虫
    run = Spider()
    run.spider(url)
