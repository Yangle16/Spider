#-*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)

# id = cp 元素的文本信息
data = driver.find_element_by_id("cp").text
print data  # 打印信息

time.sleep(3)
driver.quit()