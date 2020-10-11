#! -*- coding:utf-8 -*-


import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException
import os
import xlrd
import sys


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # # if 去掉表头
    # if rowNum > 0:

    return dataFile


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def RemoveDot(item):
    f_l = []
    for it in item:
        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l


def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cfa',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into tas_link (oneUrl) values (%s)', content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass


def page_parse_(html):
    big_list = []
    element = etree.HTML(html)

    links = element.xpath('//a/@href')

    for item in links:
        if 'thread-' in item and len(item)<=28 and '-1-' in item :
            big_list.append("http://forum.theanalystspace.com/"+item)

    return big_list




if __name__ == '__main__':
    for num in range(2,32):
        url ='http://forum.theanalystspace.com/forum-42-{0}.html'.format(num)
        html = call_page(url)
        content = page_parse_(html)
        for item in content:
            html = call_page(item)
            try:

                patt = re.compile('"attachment.php\?aid=(.*?)"', re.S)
                items = re.findall(patt,html)
                for it in items:
                    d_url ='http://forum.theanalystspace.com/attachment.php?aid='+it
                    f_url =[(d_url)]
                    print(f_url)
                    insertDB(f_url)
                    time.sleep(1)
            except:
                pass



#
# create table tas_link (id int not null primary key auto_increment,
#  oneUrl text
# ) engine=InnoDB  charset=utf8;