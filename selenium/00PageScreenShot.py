#-*- coding:utf-8 -*-

""""
截取整个网页图像
"""

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.implicitly_wait(5)
driver.get('http://www.youth.cn/')
driver.get_screenshot_as_file('youth.png')