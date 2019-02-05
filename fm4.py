# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sys, io, re, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
chrome_options = Options()
_prefs = {'profile.default_content_setting_values': {'images': 2}}
chrome_options.add_experimental_option('prefs', _prefs)
chrome_options.add_argument('lang=zh_CN.UTF-8')
# hide browser window
# chrome_options.add_argument("--headless")  # define headless

# add the option when creating driver
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 60)


def findtext(css):
    return browser.find_element_by_css_selector(css).text


def followdetail(url):
    try:
        browser.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.table-more > span')))

        browser.find_element_by_css_selector('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.table-more > span').click()

        profit = findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(6) > div.tab-value')

        p = float(re.sub(r'\$', '', profit))

        detail = {
            'url': browser.current_url,
            'user': findtext('#app-header-head-content-box > div.head-content-container > div.head-user-introduction > div.nickname > span'),
            'Type': 2,  # 跟随账户
            'account': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-info > div > span:nth-child(3)'),
            'broker': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-info > div > span:nth-child(4)'),
            'roi': findtext("#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(1) > div.tab-value"),
            'Profits': p,
            'pips': findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(4) > div.tab-value'),

            }

        print(detail)

    except TimeoutException:
        print('time out')
        # followdetail(url)


def tradedetail(url):
    try:
        browser.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.table-more > span')))

        browser.find_element_by_css_selector('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.table-more > span').click()

        equity = findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(5) > div.tab-value')
        deposit = findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.detail_numtable > div:nth-child(9) > div.tab-value')
        withdraw = findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.detail_numtable > div:nth-child(5) > div.tab-value')
        balance = findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.detail_numtable > div:nth-child(1) > div.tab-value')
        profit = findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(1) > div.tab-value')

        d = float(re.sub(r'\$', '', deposit))
        e = float(re.sub(r'\$', '', equity))
        w = float(re.sub(r'\$', '', withdraw))
        b = float(re.sub(r'\$', '', balance))
        p = float(re.sub(r'\$', '', profit))

        detail = {
            'url': browser.current_url,
            'user': findtext('#app-header-head-content-box > div.head-content-container > div.head-user-introduction > div.nickname > span'),
            'Type': 1,  # 交易账户
            'account': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-info > div:nth-child(1) > span:nth-child(3)'),
            'broker': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-info > div:nth-child(1) > span:nth-child(4)'),
            'balance': b,
            'equity': e,
            'deposit': d,
            'withdraw': w,
            'roi': findtext("#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-data-list > div:nth-child(1) > div.data.high"),
            'Profits': p,
            'pips': findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(2) > div.tab-value'),
            'desc': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-rate-list > div.rate-item.right > div:nth-child(2) > div.rate-desc'),
            'DD': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-data-list > div:nth-child(3) > div.data'),
            'period': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-data-list > div:nth-child(4) > div.data')

            }

        print(detail)

    except TimeoutException:
        print('time out')
        # tradedetail(url)


def userAccount(uid):
    browser.get('https://www.followme.com/api/v2/trade/other/user/accounts?userId=' + uid)
    html = browser.page_source
    html = re.sub(r'<.*?>', '', html)

    alist = json.loads(html)['data']['accounts']

    for a in alist:

        if a['AccountType'] == 3:
            pass

        if a['UserType'] == 1:
            url = 'https://www.followme.com/user/' + str(uid) + '/trade-account/exhibition?index=' + str(a['AccountIndex'])
            tradedetail(url)

        if a['UserType'] == 2:
            url = 'https://www.followme.com/user/' + str(uid) + '/trade-account/exhibition?index=' + str(a['AccountIndex'])
            followdetail(url)


def main():
    ids = {
        '157448',
        '232319'
        }
    for id in ids:
        userAccount(id)


if __name__ == '__main__':
    main()

# 这里可以获取到该用户的账户列表，然后可以进行进一步的分析。
# https://www.followme.com/api/v2/trade/other/user/accounts?userId=157448

#
# https://www.followme.com/user/{userid}/trade-account/exhibition?index=5
