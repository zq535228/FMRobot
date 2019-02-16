# coding=utf-8
import time
from selenium import webdriver
import json, re
from selenium.webdriver.chrome.options import Options
import io
import sys

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
    getidfromnew()


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
        if index < 10:
            totalprofittop10 += '@' + j1[index]['NickName'] + '#' + str(j1[index]['AccountIndex']) + '\n'

    url = "https://www.followme.cn/api/v2/trade/rank/followers?pageSize=100&pageIndex=1&time=7&pageSort=asc"
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>', '', html)
    j1 = json.loads(html)['data']['items']

    totalloss = 0
    totallosstop10 = ""
    for index in range(len(j1)):
        totalloss += j1[index]['FollowMoney']
        if index < 10:
            totallosstop10 += '@' + j1[index]['NickName'] + '#' + str(j1[index]['AccountIndex']) + '\n'

    outstr = '又到周末了，发布一下上周的跟随统计。上周跟随者们的盈亏合计约：' + str(round((totalloss + totalprofit) * 6.9, 2)) + '人民币。详情请看图片：\n\n'
    outstr += '渔哥爬取了FM的±TOP' + str(len(j1)) + '名跟随者数据，简单汇总分析后，结果如下：\n\n'
    outstr += '上周盈利TOP10：\n' + totalprofittop10 + '\n'
    outstr += '上周亏损TOP10：\n' + totallosstop10 + '\n'
    outstr += '上周跟随总盈利值：' + str(round(totalprofit, 2)) + '美元\n'
    outstr += '上周跟随总亏损值：' + str(round(totalloss, 2)) + '美元\n'
    outstr += '上周跟随盈亏合计：' + str(round(totalprofit + totalloss, 2)) + '美元\n'
    outstr += '上周跟随盈亏合计：' + str(round((totalloss + totalprofit) * 6.9, 2)) + '人民币\n\n'

    outstr += '统计by NinjaLoveFish ' + time.strftime("%Y-%m-%d", time.localtime())
    print(outstr)


if __name__ == "__main__":
    main()

# https://www.followme.cn/api/v2/trade/rank/followers?pageSize=100&pageIndex=1&time=7&pageSort=desc
