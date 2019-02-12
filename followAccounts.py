import requests, json, re
import pymongo, time, random, threading

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_accounts = myclient["fm5"]["accounts"]
db_userids = myclient['fm5']['userids']

s = requests.Session()


# 根据用户ID，获取用户账户列表
# https://www.followme.com/api/v2/trade/other/user/accounts?userId={}
def account(uid):
    try:
        url = 'https://www.followme.com/api/v2/trade/other/user/accounts?userId=' + str(uid)
        print('crawl from userid：' + url)
        html = s.get(url)
        alist = json.loads(html.content)['data']['accounts']

        for aid in alist:
            account_detail(uid, aid)
    except:
        if 'get account card info failed' in s.get(url):
            return
        else:
            account(uid)


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

        if db_accounts.count({'id': aid['Id']}) == 0 and accd['BrokerName'] != '模拟账户':
            x = db_accounts.insert_one(accd)
            print('saved：' + str(x.inserted_id))
            print('.' * 10)
        else:
            print('acc exist or demo account:' + str(aid['Id']))
    except:
        if '{}' in s.get(url):
            return
        account_detail(uid, aid)


def new(uid):
    try:
        url = "https://www.followme.com/api/v3/social/user/attentions?userId=" + str(uid) + "&pageIndex=1&pageSize=32"
        html = s.get(url).content

        ul = re.findall(r",\"UserId\":\"(.*?)\"", str(html))
        for u in ul:
            if db_userids.count({'UserId': int(u)}) == 0:
                account(u)
                db_userids.insert_one({'UserId': int(u)})
                new(u)
            else:
                print("user exist：" + u)
    except:
        new(random.choice(db_userids.find()))


if __name__ == '__main__':
    # 入口
    # new(222799)
    t1 = threading.Thread(target=new, args=("212509",))
    t1.start()
    t2 = threading.Thread(target=new, args=("222799",))
    t2.start()

