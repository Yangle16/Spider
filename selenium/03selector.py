#-*- coding:utf-8 -*-
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
# <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">
# 各种选择器
browser.find_element_by_id("kw").send_keys("python")
browser.find_element_by_class_name("s_ipt").send_keys("python")
browser.find_element_by_name("wd").send_keys("python")
# browser.find_element_by_tag_name("input").send_keys("python")
browser.find_element_by_css_selector("#kw").send_keys("python")
browser.find_element_by_xpath("//input[@id='kw']").send_keys("python")


# Xpath选择器
# xpath:attributer（属性）
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
#input 标签下 id =kw 的元素

# xpath:idRelative（id 相关性）
browser.find_element_by_xpath("//div[@id='fm']/form/span/input").send_keys("selenium")
#在/form/span/input 层级标签下有个 div 标签的 id=fm 的元素
browser.find_element_by_xpath("//tr[@id='check']/td[2]").click()
# id 为'check' 的 tr ，定位它里面的第2个 td

# xpath:position（位置）
browser.find_element_by_xpath("//input").send_keys("selenium")
browser.find_element_by_xpath("//tr[7]/td[2]").click()
#第7个 tr 里面的第2个 td

# xpath: href（水平参考）
browser.find_element_by_xpath("//a[contains(text(),' 网页')]").click()
#在 a 标签下有个文本（text）包含（contains）'网页' 的元素

# xpath:link
browser.find_element_by_xpath("//a[@href='http://www.baidu.com/']").click()
#有个叫 a 的标签，他有个链接 href='http://www.baidu.com/的元素



# Link定位 文字连接定位
browser.find_element_by_link_text("贴吧").click()

# Partial link text定位 部分连接定位
browser.find_element_by_partial_link_text("贴").click()
#通过find_element_by_partial_link_text() 函数，我只用了“贴” 字，脚本一样找到了"贴吧" 的链接

browser.find_element_by_id("su").click()
print browser.title
print browser.current_url

time.sleep(3)
browser.quit()