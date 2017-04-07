#-*- coding:utf-8 -*-

# 隐式等待
# 隐式等待比较简单，就是简单地设置一个等待时间，单位为秒。

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")

# 当然如果不设置，默认等待时间为0