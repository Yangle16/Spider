#-*- coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()


# 有些弹出对话框窗，我们可以通过判断是否为当前窗口的方式进行操作。

#获得当前窗口
nowhandle=driver.current_window_handle

#打开弹窗
driver.find_element_by_name("xxx").click()

#获得所有窗口
allhandles=driver.window_handles
for handle in allhandles:
    if handle!=nowhandle: #比较当前窗口是不是原先的窗口
        driver.switch_to_window(handle) #获得当前窗口的句柄
        driver.find_element_by_class_name("xxxx").click() #在当前窗口操作

#回到原先的窗口
driver.switch_to_window(nowhandle)


# 这里只是操作窗口的代码片段， 提供一个思路， 能否完成我们想要的结果， 还需要我们
# 通过实例去验证。