#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time

driver = webdriver.Chrome()
driver.get("http://pan.baidu.com/")
driver.implicitly_wait(30)

#登陆百度网盘
driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("xfyangle@163.com")
driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("2008512lele")
driver.find_element_by_id("TANGRAM__PSP_4__submit").submit()
time.sleep(3)

"""说明：百度网盘页面进行了加密，可以用开发者工具查看到页面代码，但源码加密不可见，所以以下无法找到对应标签"""

#进入网盘
# driver.find_element_by_xpath('//*[@id="h5Input0"]').click()
#找到 id 为 dropdown1的父元素
WebDriverWait(driver, 1000).until(lambda the_driver:the_driver.find_element_by_id('h5Input0').is_displayed())

#在父亲元件下找到 link 为 Action 的子元素
menu = driver.find_element_by_id('h5Input0').find_element_by_id('h5Input1')

#鼠标定位到子元素上
webdriver.ActionChains(driver).move_to_element(menu).perform()
time.sleep(3)

#上传文件
driver.find_element_by_id("h5Iuput1").send_keys('C:\Users\MyPC\Downloads\selenium.txt')

time.sleep(5)
driver.quit()