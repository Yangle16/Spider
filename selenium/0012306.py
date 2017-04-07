#-*- coding:utf-8 -*-
import time
from selenium import webdriver

station = raw_input(u"请输入到达车站:")
train_code = raw_input(u"请输入车次:")

driver = webdriver.Chrome()

url = 'http://dynamic.12306.cn/mapping/kfxt/zwdcx/LCZWD/CCCX.jsp'

driver.get(url)
driver.implicitly_wait(2)

driver.maximize_window() # 浏览器全屏显示

#通填写车站和车次
driver.find_element_by_id("chezhanInId").send_keys(station.decode('utf-8'))
driver.find_element_by_id("chechiInId").send_keys(train_code)
time.sleep(3)

captch_code = driver.find_element_by_id("divCode")
print captch_code.text
code = captch_code.text

# 填写验证码
driver.find_element_by_id("yzm").send_keys(code)
time.sleep(2)

#点击查询按钮
driver.find_element_by_id("chaxunBtnId").click()
time.sleep(3)

text = driver.find_element_by_id("resultJsp")
print text.text

time.sleep(2)
driver.close()