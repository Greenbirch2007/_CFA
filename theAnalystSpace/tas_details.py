#! -*- coding:utf-8 -*-


import datetime
import re
import time

import pymysql
import requests
import wget
from lxml import etree
from requests.exceptions import RequestException
import os
import xlrd
import sys
import requests
import re
import pymysql
from multiprocessing import Pool
from requests.exceptions import RequestException






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
    req= requests.get(url)
      #  requests 中文编码的终极办法！
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return  (encode_content)


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

# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):
    big_list = []
    last_list = []
    selector = etree.HTML(html)
    name_cn = selector.xpath('//*[@id="attachment"]/table/tbody/tr[7]/td[2]/text()')
    oneUrl = selector.xpath('//*[@id="attachment"]/table/tbody/tr[8]/td[2]/input/@onclick')

    print(name_cn,oneUrl)




url = 'http://forum.theanalystspace.com/attachment.php?aid=MjA1Nzh8M2QwZDUxYzd8MTYwMjM4NTAxOXw2MTg2U1R6S0t6UFdCajk2VDFxZGJOZTRYQWlENnZaZjM2TTdCeXpQeUJkcWpMMA%3D%3D'


if __name__ == '__main__':


    # 默认访问本目录
    excelFile = 'tas_link.xlsx'
    full_items = read_xlrd(excelFile=excelFile)
    for i in full_items:
        url1= i[0]
        f_url =i[0]+'&down=1'
        html = call_page(url1)
        patt = re.compile('<td height="30" colspan="2" align="left" class="wz">附件名称："(.*?)"</td>', re.S)
        items = re.findall(patt, html)
        title=items[0]
        file_name = wget.download(f_url, out=title)
        print(file_name)
        time.sleep(6)
        # 直接在这里下载





