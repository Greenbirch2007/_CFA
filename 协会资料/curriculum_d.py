

# -*- coding:UTF-8 -*-

from urllib import request

import requests
from lxml import etree
import os

def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre'
    }
    response = requests.get(url,headers=headers)
    html =response.text
    return html





"""
urlretrieve参数说明：
1.传入网址,网址的类型一定是字符串

2.传入的，本地的网页保存路径+文件名

3.一个函数的调用，我们可以随便定义这个函数，但是必须得有3个参数
    ①到目前为此传递的数据块数量
    ②是每个数据块的大小，单位是byte,字节
    ③远程文件的大小
"""

def callback(a1,a2,a3):

    """
        @a1:目前为此传递的数据块数量
        @a2:每个数据块的大小，单位是byte,字节
        @a3:远程文件的大小
    """
    download_pg = 100.0*a1*a2/a3
    if download_pg > 100:
        download_pg = 100
    
    print("%.2f%%" %download_pg,)



#解析pdf文件的下载地址 迭代器,可以遍历
def parse_one_page(html):
    selector=etree.HTML(html)
    title = selector.xpath('//*[@id="main"]/article/section/div/div/ul/li/a/text()')
    links = selector.xpath('//*[@id="main"]/article/section/div/div/ul/li/a/@href')
    for i1,i2 in zip(title,links) :
        try:
            l_path = os.getcwd()
            f_url = 'https://www.cfainstitute.org/'+i2
            f_title = "".join(i1.split())
            local = "{0}/{1}.pdf".format(l_path,i1)
            request.urlretrieve(f_url,str(local),callback)
        except:
            pass










if __name__ == "__main__":
    url = 'https://www.cfainstitute.org/en/programs/investment-foundations/curriculum/download'
    html = get_one_page(url)
    parse_one_page(html)
    print("下载完成")
