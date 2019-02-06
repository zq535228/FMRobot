import requests, json, re
import pymongo, time, random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_accounts = myclient["fm5"]["accounts"]


def main():
    ulist = db_accounts.find().sort('MoneyCloseAll', 1).limit(500)

    loss = 0;
    for u in ulist:
        loss += u['MoneyCloseAll']

    loss = round(loss * 6.9, 2)

    ulist = db_accounts.find().sort('MoneyCloseAll', -1).limit(500)

    win = 0;
    for u in ulist:
        win += u['MoneyCloseAll']

    win = round(win * 6.9, 2)

    count = db_accounts.estimated_document_count()

    # print("社区亏损TOP500，累计亏损金额合计：" + str(win))

    # print("社区TOP500盈亏平衡金额：" + str(round(win + loss, 2)))

    print('截止' + time.strftime("%Y-%m-%d", time.localtime()) + ' 渔哥爬取账户数量：' + str(count) + '个，分析后：')
    print("社区亏损TOP500累计亏损金额合计：" + str(loss) + '人民币')

    print('其中亏损TOP10的连接如下：')

    ulist = db_accounts.find().sort('MoneyCloseAll', 1).limit(10)

    for u in ulist:
        print(u['url'])


if __name__ == '__main__':
    main()
