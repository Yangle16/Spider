#-*- coding:utf-8 -*-
from selenium import webdriver
import time

#访问百度
driver=webdriver.Chrome()
driver.get("https://mm.taobao.com/self/album_photo.htm?spm=719.6642053.0.0.6SuWMd&user_id=45834230&album_id=300874026&album_flag=0")

# #搜索
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# time.sleep(3)

#将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=10000"
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,10000)")
time.sleep(2)

# #将滚动条移动到页面的顶部
# js="var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
time.sleep(5)

driver.quit()