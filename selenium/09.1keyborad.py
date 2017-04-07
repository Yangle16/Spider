#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
import os,time

driver = webdriver.Chrome()
url = 'https://login.51job.com/login.php?'
driver.get(url)
time.sleep(3)

driver.maximize_window() # 浏览器全屏显示
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("xfyangle@163.com")

#tab 的定位相相于清除了密码框的默认提示信息，等同上面的 clear()
driver.find_element_by_id("loginname").send_keys(Keys.TAB)

time.sleep(3)
driver.find_element_by_id("password").send_keys("2008512lele")

#通过定位密码框， enter（回车）来代替登陆按钮
driver.find_element_by_id("password").send_keys(Keys.ENTER)


'''
#也可定位登陆按钮，通过 enter（回车）代替 click()
driver.find_element_by_id("login_btn").send_keys(Keys.ENTER)
'''

time.sleep(3)
driver.quit()

""""
要想调用键盘按键操作需要引入 keys 包：
from selenium.webdriver.common.keys import Keys
通过 send_keys()调用按键：
send_keys(Keys.TAB) # TAB
send_keys(Keys.ENTER) # 回车
注意： 这个操作和页面元素的遍历顺序有关， 假如当前定位在账号输入框， 按键
盘的 tab 键后遍历的不是密码框，那就不法输入密码。 假如输入密码后，还有
需要填写验证码，那么回车也起不到登陆的效果。
"""