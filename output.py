#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
# 【输出器】
#
# 对外提供两个方法：
#
# 1. add_data(data) 
# 存储网页数据，接收一个参数 data
# 
# 2. output()
# 将数据输出到 html 文件中
#


class Output(object):

    def __init__(self):
        
        self.datas = []

    def add_data(self, data):

        if data is None:
            return 

        self.datas.append(data)

    def output(self):

        head = '''

            <html>
            <meta charset="UTF-8">
            <body>
            <table>
            
        '''

        foot = '''
                
            </table>
            </body>
            </html>

        '''

        with open('CSDN.html', 'w') as f:

            f.write(head)

            for data in self.datas:
                
                f.write('<tr><td><a href =%s>%s</a></td>' % (data['url'], data['url']))
                f.write('<td>%s</td></tr>' % data['title'])
                
            f.write(foot)
