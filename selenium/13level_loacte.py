#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('level_locate.html' )
dr.get(file_path)

#点击 Link1链接（弹出下拉列表）
dr.find_element_by_link_text('Link1' ).click()

#找到 id 为 dropdown1的父元素
WebDriverWait(dr, 10).until(lambda the_driver:the_driver.find_element_by_id('dropdown1').is_displayed())

#在父亲元件下找到 link 为 Action 的子元素
menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action' )

#鼠标定位到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()

time.sleep(2)
dr.quit()


""""
WebDriverWait(dr, 10)
10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束。 dr 就不解释了， 前
面操作 webdriver.firefox()的句柄

is_displayed()
该元素是否用户可以见

class ActionChains(driver)
driver: 执行用户操作实例 webdriver
生成用户的行为。 所有的行动都存储在 actionchains 对象。 通过 perform()存储的行为。

move_to_element(menu)
移动鼠标到一个元素中， menu 上面已经定义了他所指向的哪一个元素

to_element：元件移动到
perform()
执行所有存储的行为
"""