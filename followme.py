

#coding=utf-8
from selenium import webdriver
import os
import time
# set little time stop and big time stop for viewing changes
little_time_stop = 1
big_time_stop = 2
# 默认广告条数
ads_num_require = 8
# 请求连接
req_url = "http://www.followme.com/"
# 打开浏览器

driver = webdriver.Chrome()
# 开始请求
driver.get(req_url)

driver.get("https://www.followme.com/")
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='PTA'])[1]/following::button[1]").click()
time.sleep(5)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='验证码登录'])[1]/following::button[1]").click()
time.sleep(5)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[1]").click()
time.sleep(5)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[1]").clear()
time.sleep(5)
