import requests, json, re
import pymongo, time, random

sleeptime = [1, 2, 3, 4, 5]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["fm5"]["accounts"]

s = requests.Session()


# 根据用户ID，获取用户账户列表
def account(uid):
    url = 'https://www.followme.com/api/v2/trade/other/user/accounts?userId=' + str(uid)
    print('crawl from userid：' + url)
    html = s.get(url)
    alist = json.loads(html.content)['data']['accounts']

    for aid in alist:
        account_detail(uid, aid)
        time.sleep(random.choice(sleeptime))


# https://www.followme.com/api/v2/trade/accounts/157448_5/statistics
def account_detail(uid, aid):
    url = 'https://www.followme.com/api/v2/trade/accounts/' + str(uid) + '_' + str(aid['AccountIndex']) + '/statistics'
    print('crawl account detail：' + url)
    html = s.get(url)
    adetail = json.loads(html.content)['data']
    try:
        accd = {
            'url': 'https://www.followme.com/user/' + str(aid['UserId']) + '/trade-account/analyze?activeType=1&index=' + str(aid['AccountIndex']),
            'id': aid['Id'],
            'BrokerName': aid['BrokerName'],
            'MT4Account': aid['MT4Account'],
            'UserType': aid['UserType'],
            'AccountType': aid['AccountType'],
            'UserId': aid['UserId'],
            'AccountIndex': aid['AccountIndex'],
            'StrategyDescription': aid['StrategyDescription'],
            'ROI': aid['ROI'],
            'Weeks': aid['Weeks'],
            'MoneyCloseAll': adetail['MoneyCloseAll'],
            'AddTime': time.time(),
            }

        if db.count({'id': aid['Id']}) == 0 and accd['BrokerName'] != '模拟账户':
            x = db.insert_one(accd)
            print('saved：' + str(x.inserted_id))
        else:
            print('exist:' + str(aid['Id']))
    except:
        pass


ids = list()


def new(uid):
    try:
        url = "https://www.followme.com/api/v3/social/user/attentions?userId=" + str(uid) + "&pageIndex=1&pageSize=32"
        time.sleep(random.choice(sleeptime))
        html = s.get(url).content

        ul = re.findall(r",\"UserId\":\"(.*?)\"", str(html))
        for u in ul:
            if ids.count(u) == 0 and db.count({'UserId': int(u)}) == 0:
                account(u)
                ids.append(u)
                new(u)
            else:
                print("user exist：" + u)
    except:
        new(random.choice(ids))


if __name__ == '__main__':
    # 入口
    new(188703)
