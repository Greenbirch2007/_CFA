# -*- coding:UTF-8 -*-

from urllib import request



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

url = "https://www.cfainstitute.org/-/media/documents/support/programs/investment-foundations/4-microeconomics.ashx?la=en&hash=563FFB49A6951B1A5E984C30E757F116DF3B01B7"
local = "/home/greenb/CFA_J/dd.pdf"
request.urlretrieve(url,str(local),callback)