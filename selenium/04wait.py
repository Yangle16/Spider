#-*- coding:utf-8 -*-
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

time.sleep(0.3) #休眠0.3秒

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

browser.implicitly_wait(30) #智能等待30秒,这是随机的（最大30s,视响应时间而定）

time.sleep(3) # 休眠3秒
browser.quit()