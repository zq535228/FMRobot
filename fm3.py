#coding=utf-8

import time
from selenium import webdriver
import requests
import json,re
import pprint
from selenium.webdriver.chrome.options import Options
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

chrome_options = Options()
# hide browser window
chrome_options.add_argument("--headless")       # define headless
prefs = {
    'profile.default_content_setting_values' : {
        'images' : 2
    }
}
chrome_options.add_experimental_option('prefs',prefs)
chrome_options.add_argument('lang=zh_CN.UTF-8')

# add the option when creating driver
driver = webdriver.Chrome(chrome_options=chrome_options)




def main():
    if islogin():
        '''
        urls = []
        urls.append('104252_4')
        urls.append('230764_2')
        urls.append('104252_4')
        urls.append('193166_4')
        urls.append('184338_2')
      
        for index in range(len(urls)):
            url = buildvisturl(urls[index])
            visit(url)
        '''
        getidfromnew()

    else:
        login()
        main()

def buildvisturl(id):
    url  = "https://www.followme.com/api/v2/trade/traders/"+id+"/followers?isFollowing=false&pageSize=1000&pageIndex=1&accountType=&pageField=PROFIT&pageSort=DESC&flag=1"

    return url

def getidfromnew():
    url = "https://www.followme.com/api/v3/social/newsBlogs?pageSize=100&pageIndex=1&LastBlogId=0"
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>','',html)
    #print(html)
    al = re.findall(r",\"UserId\":\"(.*?)\"", html)
    
    urls = set()
    for index in al:
        url = "https://www.followme.com/user/"+ index +"/zone"
        urls.add(url)
    i = 0
    for u in urls:
        i = i+1
        time.sleep(5)
        driver.get(u)
        driver.get_screenshot_as_file("./img/"+str(i)+".png")

def login():
    driver.get("https://auth.followme.com/login?source=iframe")
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='验证码登录'])[1]/following::button[1]").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[1]").clear()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[1]").send_keys("13604023002")
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[2]").clear()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='注册'])[1]/following::input[2]").send_keys("")
    driver.find_element_by_id("login-password").click()
    time.sleep(5)

def islogin():
    driver.get("https://www.followme.com/?t=my")
    html = driver.page_source
    if "与世界分享" in html:
        print('login in success')
        return True
    else:
        return False


def visit(url):
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>','',html)

    j1 = json.loads(html)['data']['items']

    for index in range(len(j1)):
        url = "https://www.followme.com/user/"+ str(j1[index]["CustomerUserId"])+"/zone"
        driver.get(url)
        time.sleep(5)


if __name__ == "__main__":
    main()
