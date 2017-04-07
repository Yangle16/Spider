#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import os
import selenium.webdriver.support.ui as ui

if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY' ]

dr = webdriver.Chrome()
file_path = ' file:///' + os.path.abspath('modal.html')
dr.get(file_path)

# 打开对话框
dr.find_element_by_id('show_modal' ).click()
sleep(3)
# 点击对话框中的链接

# 由于对话框中的元素被蒙板所遮挡，直接点击会报 Element is not clickable 的错误
# 所以使用 js 来模拟 click
link = dr.find_element_by_id('myModal' ).find_element_by_id('click' )
dr.execute_script('$(arguments[0]).click()' , link)
sleep(4)

# 关闭对话框
buttons = dr.find_element_by_class_name('modal-footer' ).find_elements_by_tag_name('button' )
buttons[0].click()
dr.quit()