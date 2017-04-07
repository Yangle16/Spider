#-*- coding:utf-8 -*-
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

print "浏览器最大化"

browser.maximize_window() #将浏览器最大化显示
time.sleep(2)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(5)

#参数数字为像素点
print "定制浏览器窗口大小"
browser.set_window_size(1080, 720)


time.sleep(3)
browser.quit()