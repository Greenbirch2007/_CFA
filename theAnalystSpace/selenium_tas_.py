

import time

from selenium.webdriver.support.select import Select

import pymysql

from selenium import webdriver



def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cfa',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    for i in range(500,700):
        sql = 'select oneUrl from tas_link where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['oneUrl']

        yield url

def call_page(url):

    driver.get(url)
    # 弄一个模拟登陆背
    driver.find_element_by_xpath('//*[@id="attachment"]/table/tbody/tr[8]/td[2]/input').click()
    time.sleep(1)






if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
    
        for url_str in Python_sel_Mysql():
            call_page(url_str)
    except:
        pass



