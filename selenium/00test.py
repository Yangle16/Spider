#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

driver.maximize_window() #将浏览器最大化显示
time.sleep(2)

elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

print driver.page_source

