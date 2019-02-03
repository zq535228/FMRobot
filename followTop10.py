# coding=utf-8

import time
from selenium import webdriver
import requests
import json, re
import pprint
from selenium.webdriver.chrome.options import Options
import io
import sys
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

chrome_options = Options()
prefs = {'profile.default_content_setting_values': {'images': 2}}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('lang=zh_CN.UTF-8')
# hide browser window
chrome_options.add_argument("--headless")  # define headless

# add the option when creating driver
driver = webdriver.Chrome(chrome_options=chrome_options)


def main():
    # 判断是否已经登录
    if islogin():
        getidfromnew()
    else:
        # 如果没有登录那么一直进行登录。
        login()
        main()


# 创建url
def buildvisturl(id):
    url = "https://www.followme.com/api/v2/trade/traders/" + id + "/followers?isFollowing=false&pageSize=1000&pageIndex=1&accountType=&pageField=PROFIT&pageSort=DESC&flag=1"
    return url


# 进行最新微博的刷新
def getidfromnew():
    # 选择1周内，盈利金额最多的那些人，列表出来。
    url = "https://www.followme.cn/api/v2/trade/rank/followers?pageSize=100&pageIndex=1&time=7&pageSort=desc"
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>', '', html)
    j1 = json.loads(html)['data']['items']

    totalprofit = 0
    totalprofittop10 = ""
    for index in range(len(j1)):
        totalprofit += j1[index]['FollowMoney']
        if index <= 10:
            totalprofittop10 += '@' + j1[index]['NickName'] + '\n'

    url = "https://www.followme.cn/api/v2/trade/rank/followers?pageSize=100&pageIndex=1&time=7&pageSort=asc"
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>', '', html)
    j1 = json.loads(html)['data']['items']

    totalloss = 0
    totallosstop10 = ""
    for index in range(len(j1)):
        totalloss += j1[index]['FollowMoney']
        if index <= 10:
            totallosstop10 += '@' + j1[index]['NickName'] + '\n'

    outstr = '渔哥爬取了FM的TOP' + str(len(j1)) + '名跟随者数据，简单汇总分析后，结果如下：\n\n'
    outstr += '上周盈利TOP10：\n' + totalprofittop10 + '\n'
    outstr += '上周亏损TOP10：\n' + totallosstop10 + '\n'
    outstr += '上周跟随盈利值：' + str(round(totalprofit, 2)) + '美元\n'
    outstr += '上周跟随亏损值：' + str(round(totalloss, 2)) + '美元\n'
    outstr += '上周跟随盈亏净值：' + str(round(totalprofit + totalloss, 2)) + '美元\n'
    outstr += '上周跟随盈亏净值：' + str(round((totalloss + totalprofit) * 6.9, 2)) + '人民币\n\n'

    outstr += '统计by NinjaLoveFish ' + time.strftime("%Y-%m-%d", time.localtime())
    print(outstr)


def login():
    driver.get("https://auth.followme.com/login?source=iframe")
    try:
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='SMS Login'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[1]/following::input[1]").send_keys("13604023002")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Login'])[1]/following::input[2]").send_keys("z123456")
        driver.find_element_by_id("login-password").click()
    except:
        pass

    time.sleep(5)


def islogin():
    driver.get("https://www.followme.com/?t=my")
    html = driver.page_source
    if "What's happening?" in html:
        print('login in success')
        return True
    else:
        return False


def visit(url):
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>', '', html)

    j1 = json.loads(html)['data']['items']

    for index in range(len(j1)):
        url = "https://www.followme.com/user/" + str(j1[index]["CustomerUserId"]) + "/zone"
        driver.get(url)
        time.sleep(5)


if __name__ == "__main__":
    main()

# https://www.followme.cn/api/v2/trade/rank/followers?pageSize=100&pageIndex=1&time=7&pageSort=desc
