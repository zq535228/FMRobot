# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pprint

import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

chrome_options = Options()
_prefs = {'profile.default_content_setting_values': {'images': 2}}
chrome_options.add_experimental_option('prefs', _prefs)
chrome_options.add_argument('lang=zh_CN.UTF-8')
# hide browser window
# chrome_options.add_argument("--headless")  # define headless

# add the option when creating driver
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 30)


def findtext(css):
    return browser.find_element_by_css_selector(css).text


def pagedetail():
    try:
        browser.get('https://www.followme.com/user/136561/trade-account/analyze?index=6&activeType=1&bindFrom=&brokerId=7&hash=511836397')
        roi = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-data-list > div:nth-child(1) > div.data.high')))

        detail = {
            'url': browser.current_url,
            'user': findtext('#app-header-head-content-box > div.head-content-container > div.head-user-introduction > div.nickname > span'),
            'account': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-info > div:nth-child(1) > span:nth-child(3)'),
            'broker': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-info > div:nth-child(1) > span:nth-child(4)'),
            'equity': findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(5) > div.tab-value'),
            'balance': findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div.detail_numtable > div:nth-child(1) > div.tab-value'),
            'roi': findtext("#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-data-list > div:nth-child(1) > div.data.high"),
            'Profits': findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(1) > div.tab-value'),
            'pips': findtext('#trade-analyze > div > div:nth-child(1) > div > div.detail_numtable > div:nth-child(2) > div.tab-value'),
            'desc': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-rate-list > div.rate-item.right > div:nth-child(2) > div.rate-desc'),
            'DD': findtext('#app > div.content-wrap > div.container > div > div.ac-rate-wrapper > div.ac-data-list > div:nth-child(3) > div.data'),

            }

        print(detail)
    except TimeoutException:
        pagedetail()


def main():
    pagedetail()
    browser.close()


if __name__ == '__main__':
    main()
