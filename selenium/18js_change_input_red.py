#-*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://login.51job.com/login.php?")

#给用户名的输入框标红
js="var q=document.getElementById(\"loginname\");q.style.border=\"1px solidred\";"

#调用 js
driver.execute_script(js)
time.sleep(3)

driver.find_element_by_id("loginname").send_keys("xfyangle@163.com")
driver.find_element_by_id("password").send_keys("2008512lele")
driver.find_element_by_id("login_btn").submit()

time.sleep(3)
driver.quit()

"""
js 解释：
q=document.getElementById(\"user_name\")
元素 q 的 id 为 user_name
q.style.border=\"1px solid red\"
元素 q 的样式，边框为1个像素红色
"""