#-*- coding:utf-8 -*-

# 需要的工具和组件有：
# 浏览器驱动ChromeDriver http://chromedriver.storage.googleapis.com/index.html?path=2.20/
# Python 3.5
# Splinter 执行：pip install splinter安装Splinter即可

#12306秒抢Python代码

from splinter.browser import Browser

x = Browser(driver_name="chrome")
url = "https://kyfw.12306.cn/otn/leftTicket/init"
x.visit(url)
#填写登陆账户、密码
x.find_by_text(u"登录").click()
x.fill("loginUserDTO.user_name","your login name")
x.fill("userDTO.password","your password")
#填写出发点目的地
x.cookies.add({"_jc_save_fromStation":"%u4E0A%u6D77%2CSHH"})
x.cookies.add({"_jc_save_fromDate":"2016-01-20"})
x.cookies.add({u'_jc_save_toStation':'%u6C38%u5DDE%2CAOQ'})
#加载查询
x.reload()
x.find_by_text(u"查询").click()
#预定
x.find_by_text(u"预订")[1].click()
#选择乘客
x.find_by_text(u"数据分析")[1].click()