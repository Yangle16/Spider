#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#进入设置下拉菜单
WebDriverWait(driver, 10).until(lambda the_driver:the_driver.find_element_by_link_text("设置").is_displayed())

menu = driver.find_element_by_link_text("设置").find_element_by_link_text("搜索设置")

#鼠标定位到子元素上
webdriver.ActionChains(driver).move_to_element(menu).perform()



#设置每页搜索结果为100条
m = driver.find_element_by_name("NR")
m.find_element_by_xpath("//option[@value='100']").click()
time.sleep(2)

#保存设置的信息
driver.find_element_by_xpath("//input[@value=' 保存设置']").click()
time.sleep(2)
driver.switch_to_alert().accept()

#跳转到百度首页后，进行搜索表（一页应该显示100条结果）
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()

"""
当我们在保存百度的设置时会会弹出一个确定按钮； 我们并没按照常规的方法去定
位弹窗上的“确定” 按钮，而是使用：
driver.switch_to_alert().accept()
完成了操作，这是因为弹窗比较是一个具有唯一性的警告信息，所以可以用这种简便
的方法处理。
– switch_to_alert()
焦点集中到页面上的一个警告（提示）
– accept()
接受警告提示
"""