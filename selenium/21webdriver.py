#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.youdao.com")

driver.find_element_by_name("q").send_keys("hello")
driver.find_element_by_name("q").send_keys("key.ENTER")

driver.close()