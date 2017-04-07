#-*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

#向 cookie 的 name 和 value 添加会话信息。
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})

#遍历 cookies 中的 name 和 value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

# 下面可以通过两种方式删除 cookie# 删除一个特定的 cookie
driver.delete_cookie("CookieName")

# 删除所有 cookie
driver.delete_all_cookies()
time.sleep(2)

driver.close()