import requests, json, re
import pymongo, time, random, threading

s = requests.Session()


def start():
    try:
        url = "https://www.followme.cn/jyds/api/sign_up_list"
        print('crawl from userid：' + url)
        html = s.get(url)
        alist = json.loads(html.content)['data']

        i = 0
        for aid in alist:
            print(aid)
            i=i+1

        print(i)
    except:
        print("except!")


if __name__ == '__main__':
    start()