#-*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)

#通过 submit() 来操作
driver.find_element_by_id("su").submit()

time.sleep(3)
driver.quit()

"""
send_keys("xx") 用于在一个输入框里输入 xx 内容。
click() 用于点击一个按钮。
clear() 用于清除输入框的内容， 比如百度输入框里默认有个“请输入关键
字” 的信息，再比如我们的登陆框一般默认会有“账号”“密码” 这样的默认信息。
clear 可以帮助我们清除这些信息
"""