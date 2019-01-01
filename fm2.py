import os

import re
import requests

import traceback
from datetime import datetime
from datetime import timedelta
import sys

import pprint
import json


headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'ContentType': 'text/html; charset=utf-8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection' : 'keep-alive',
        }
cookie = {'Cookie':'acw_tc=3b2e041815450315157961708e74559a8469923a93e9f1ee244439924a; USER_TOKEN=1184zHkUL6yX5vkRx3O1_IKh-ZZRVqaHjLbqF9kctw6g5U04ccffB3gu4j5aFpPUYpsDoXHLCsiZpxHeO-jywg; _ga=GA1.2.1546177824.1545040088; lang=zh-CN; _gid=GA1.2.682410759.1545653079; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22226162%22%2C%22%24device_id%22%3A%22167bb8fef9657e-0b745719e6caf2-b781636-1881600-167bb8fef971dd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_campaign%22%3A%22wechat%22%2C%22%24latest_utm_content%22%3A%22jyds%22%2C%22_latest_vcode%22%3A%22239523%22%7D%2C%22first_id%22%3A%22167bb8fef9657e-0b745719e6caf2-b781636-1881600-167bb8fef971dd%22%7D; xfmversion=2.9; Hm_lvt_6fcd62ad8d4fa46fe6c001c4876b8e3d=1546236377,1546257000,1546259022,1546311553; _gat_gtag_UA_81113615_1=1; Hm_lpvt_6fcd62ad8d4fa46fe6c001c4876b8e3d=1546313425'}
sess = requests.Session()

'''
session = requests.session()
url = "https://www.followme.com/?t=my"

html = session.get(url,cookies=cookie,headers=headers).text

if '与世界分享' in html:
    print('login')
else:
    print("not login")

url  = "https://www.followme.com/api/v2/trade/traders/230764_2/followers?isFollowing=false&pageSize=20&pageIndex=1&accountType=&pageField=PROFIT&pageSort=DESC&flag=1"

html = session.get(url,cookies=cookie,headers=headers).text

j = json.loads(html)['item']
pprint.pprint(j)
'''


from selenium import webdriver
driver = webdriver.Chrome()
cookieDict = {}
cookie = 'acw_tc=3b2e041815450315157961708e74559a8469923a93e9f1ee244439924a; USER_TOKEN=1184zHkUL6yX5vkRx3O1_IKh-ZZRVqaHjLbqF9kctw6g5U04ccffB3gu4j5aFpPUYpsDoXHLCsiZpxHeO-jywg; _ga=GA1.2.1546177824.1545040088; lang=zh-CN; _gid=GA1.2.682410759.1545653079; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22226162%22%2C%22%24device_id%22%3A%22167bb8fef9657e-0b745719e6caf2-b781636-1881600-167bb8fef971dd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_campaign%22%3A%22wechat%22%2C%22%24latest_utm_content%22%3A%22jyds%22%2C%22_latest_vcode%22%3A%22239523%22%7D%2C%22first_id%22%3A%22167bb8fef9657e-0b745719e6caf2-b781636-1881600-167bb8fef971dd%22%7D; xfmversion=2.9; Hm_lvt_6fcd62ad8d4fa46fe6c001c4876b8e3d=1546236377,1546257000,1546259022,1546311553; _gat_gtag_UA_81113615_1=1; Hm_lpvt_6fcd62ad8d4fa46fe6c001c4876b8e3d=1546313425'

cookies = cookie.split("; ")
for co in cookies:
    co = co.strip()
    p = co.split('=')
    value = co.replace(p[0]+'=', '').replace('"', '')
    
    cc = {'name':p[0],'value':value}
    
    driver.add_cookie(cc)




#driver.get("https://www.followme.com/")