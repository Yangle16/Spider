#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html' )
dr.get(file_path)

# 选择所有的 checkbox 并全部勾上
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()

time.sleep(2)

# 打印当前页面上有多少个checkbox
print len(dr.find_elements_by_css_selector('input[type=checkbox]'))
print len(checkboxes)

time.sleep(2)
# 把页面上最后1个checkbox 的勾给去掉
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
print '去掉了最后一个'

time.sleep(2)
dr.quit()