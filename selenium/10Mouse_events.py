#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://login.51job.com/login.php?")

#登陆前程无忧个人账户
driver.find_element_by_id("loginname").send_keys("xfyangle@163.com")
driver.find_element_by_id("password").send_keys("2008512lele")
driver.find_element_by_id("login_btn").submit()
time.sleep(3)

#定位到要右击的元素
qqq=driver.find_element_by_xpath('//*[@id="rsm_div_info"]/div[1]/div[1]/a')

#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(qqq).perform()


'''
#你也可以使用三行的写法，但我觉得上面两行写法更容易理解
chain = ActionChains(driver)
implement = driver.find_element_by_xpath('//*[@id="rsm_div_info"]/div[1]/div[1]/a')
chain.context_click(implement).perform()
'''

# 鼠标双击
#定位到要双击的元素
qqq2 =driver.find_element_by_xpath('//*[@id="rsm_div_info"]/div[1]/div[1]/a')
#对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(qqq2).perform()

# 鼠标拖拽
#定位元素的原位置
element = driver.find_element_by_name("source")
#定位元素要移动到的目标位置
target = driver.find_element_by_name("target")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()


time.sleep(3) #休眠3秒
driver.close()