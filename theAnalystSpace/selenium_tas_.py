
import time

from selenium.webdriver.support.select import Select
from lxml import etree
import pymysql

from selenium import webdriver



def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cfa',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    for i in range(2000 ,2500):  # 5707 从2000开始反下载
        sql = 'select oneUrl from tas_link where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['oneUrl']
        print(i)

        yield url

def call_page(url):

    driver.get(url)
    html = driver.page_source
    selector = etree.HTML(html)
    hits = selector.xpath('//*[@id="wrap"]/div/div/div/div/div/p/text()')
    print(hits)


    # 弄一个模拟登陆背
    try:
        if hits==['对不起，原附件链接已失效。']:
            driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div/div/div/p/a[1]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="attachment"]/table/tbody/tr[8]/td[2]/input').click()
        else:
            driver.find_element_by_xpath('//*[@id="attachment"]/table/tbody/tr[8]/td[2]/input').click()

    except:
        pass






if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:

        for url_str in Python_sel_Mysql():
            call_page(url_str)
            time.sleep(1)
    except:
        pass



