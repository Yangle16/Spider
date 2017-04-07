#-*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn")
time.sleep(3)

driver.maximize_window() # 浏览器全屏显示

#通过用户名密码登陆
driver.find_element_by_id("username").send_keys("xfyangle@163.com")
driver.find_element_by_id("password").send_keys("2008512lele")

#勾选保存密码
driver.find_element_by_class_name("auto-login").click()
time.sleep(3)

#点击登陆按钮
driver.find_element_by_class_name("logging").click()

#截取页面，仅当前屏幕（截屏，不是整个网页快照）
driver.get_screenshot_as_file("mycsdn.png")

#获取 cookie 信息并打印
cookie= driver.get_cookies()
print cookie

#网页源码
page = driver.page_source
print page

time.sleep(3)
driver.find_element_by_link_text("博客").click()

time.sleep(10)
driver.close()