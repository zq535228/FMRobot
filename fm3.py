#coding=utf-8

import time
from selenium import webdriver
import requests
import json,re
import pprint
from selenium.webdriver.chrome.options import Options
import io
import sys
import random

res = []
res.append("看起来很高大尚哦！")
res.append("支持你！")
res.append("很棒")
res.append("good")
res.append("格雷厄姆")
res.append("可以接受多少亏损，菜可以博取多大的利润，这个是成正比的")
res.append("耗时越短，收益率越高")
res.append("注意风险")
res.append("不要亏钱，时刻要防范风险")
res.append("历史最大净值回撤、收益率都很重要")
res.append("交易员优秀，耗时越短，收益率越高")
res.append("风险的态度不能太随意")
res.append("截断亏损，让获利奔跑")
res.append("人们都是风险规避的，有效的方式就是设置止损")
res.append("为了能在晚上安然入睡，所以。。。")
res.append("最好选择那些将“不要亏钱”作为首要定律的交易员。")
res.append("风险始终是存在的")
res.append("系统性风险、策略性风险、人为主观性风险")
res.append("作为一名投资者首先你自己应该明白一点任何投资都是有风险的")
res.append("投资毕竟不是赌博")
res.append("做投资是一个非常需要耐心的事情")
res.append("非常清晰和明白短期爆发式的增长绝对不能持续")
res.append("交易之路上面我的交易回撤会控制在30%之内")
res.append("斯坦利·克罗操盘术")
res.append("K线、趋势、均线、形态、波浪,主流的技术工具，你用那种方式？")
res.append("顺势的仓位，很可能有巨大的利润，因此不要轻易放弃")
res.append("保持你的仓位不动，一直到你在客观分析以后发现，趋势已经发生了反转才平仓，并且速度要快。")
res.append("值得认真的思考")
res.append("授人以鱼不如授人以渔")
res.append("只有在市场表现很剧烈的趋势特性，或是你的分析显示市场正在酝酿形成趋势，才能入市。")
res.append("必须要找到每个市场中持续进行的大趋势，并且顺着这个主控全局的趋势交易，否则就不要入市")
res.append("交易的本质是什么？")
res.append("加入市场走势非常不利，也就是没有站到你的一边，那怎么办？赶快跑！")
res.append("自己去寻找得到的来的经验更加深刻")
res.append("黄金分割和时间周期的你懂吗 ？")
res.append("理论能够判断的准确略在止盈止损比超过1：1的情况下达到50%以上,那么就按这个办法来一样能赚钱.")
res.append("再没有自己完整的交易系统前不要做长线只做短线")
res.append("挑选流动性强交易活跃的品种，这种品种的分钟K线走势大部分时间都要流畅的。")
res.append("做短线，不是让你盲目下单，而是验证自己的方法是否正确。")
res.append("同样的入场方法，你做日线可能要一个月才能入场两三次。但换成分K线，你可能一天就要进10多次.")
res.append("我就见过一个50多的大爷，天天中长线，还在讲江恩的时间周期，说这个地方该掉头做空了，结果亏的一塌糊涂。为什么？")
res.append("做短线，不是让你重仓交易。")
res.append("如果没有过人的天赋，相信自己不是天才对你更重要！")
res.append("告诉你这个市场不是那么美丽，反而残酷")
res.append("市场的复杂多变，国内外汇交易市场的混乱。")
res.append("不要用指标，只看K线。")
res.append("无论是MACD,KDJ,RSI还是什么顾比均线、布林带，这些指标只会让你眼花缭乱，反而忽略了市场波动的本质。")
res.append("前两天和一个已经做家庭妇男的朋友聊天，这是他关于指标的感慨:我已经放弃指标了！so。。。")
res.append("不要叛变到基本面分析，不过基本面在外汇领域挺难的额，起码语言就对我们不利。")
res.append("日本蜡烛图，道氏理论这些基本理论的书你必须看。")
res.append("不要一开始以为自己获得了制胜法宝，以为交易市场比提款机还方便，相信我即便你做了交易后的几年都很可能不会有你想的美好。")
res.append("只看一个品种，一直盯着，不做别的")
res.append("每天都用复盘软件再重新模拟一遍今天的行情是个好习惯。")
res.append("对于小散户而言，基本面分析很难")
res.append("我研究过几乎所有的技术指标，但是发现这些指标不适合用于短时交易")
res.append("在技术面，有两种基本的策略，趋势和反转")
res.append("我开始的时候着迷于趋势，但一段时间后发现，短时交易很难很难抓趋势")
res.append("趋势本身就是个很难精确表达的概念，当然可能有更精确的定义，如一段时间内多方向上连续超过多少点，而同时空方向上少于多少点，就可以定义为方向为多，但没时间和精力去验证。")
res.append("趋势和反转这两种策略我都尝试过，对我个人而言，趋势策略是完全失败的，而反转策略其实非常不错。")
res.append("策略最大的问题是支撑和阻力的确定问题")
res.append("外汇交易中的时间，也就是周期性。")
res.append("聊时间的话必须把空间放在一起来谈，外汇交易里有空间其实就是价格。")
res.append("地球上的生物是生活在时间和空间里，我们人生命时间不过百年，人的活动空间不过在地球上（去外太空还在探索中）；")
res.append("人生百年，二十弱冠，三十而立，四十不惑，五十知天命，六十花甲，七十古稀，八十耄耋。")
res.append("我们活动的空间是有限的，我们生命时间也是有限的。")
res.append("时间还分成很多小周期")
res.append("有其他问题也可以提出来，有时间我会写出来。")
res.append("好比做生意，赔了，我们能够接受，经历过了，成长，东山再起。但是被骗，是坚决无法接受的。")
res.append("澳大利亚ASIC监管,怎么样")
res.append("美国NFA监管，中国好像不能投吧，有吗")
res.append("以技术分析为主，基本面和市场情绪分析为辅助，注重风险控制 ")
res.append("趋势线、通道")
res.append("斐波那契回调、顶底背离")
res.append("布林带、MACD、支撑与阻力")
res.append("K线组合形态")
res.append("反转形态（M头、头肩顶底等）")
res.append("波浪理论")
res.append("止损位置和利润空间，注重资金管理，都非常重要")
res.append("留得青山在不愁没柴烧")
res.append("千万不要死扛")
res.append("用闲钱做，不要影响了家庭和生活。")
res.append("行情机会有的是，发现情况不对，直接抛掉，找机会再来")
res.append("考虑盈亏比，注重资金管理")
res.append("汇市有风险，入市需谨慎！")
res.append("我们政府也不允许我们去境外平台做交易")
res.append("外汇平台的监管实际上是没卵用的，作为参考可以，但不是唯一标准")
res.append("外汇平台监管只用于参考，加入监管，至少能证明其实力，监管也要钱才能加入的...")
res.append("ICMarkets用的人比较多")
res.append("有些交易商，杠杆会在数据行情来临之前，自动变成200，会搞死人的")
res.append("不赞我也不关注我真的让我觉得很伤心")
res.append("少听业务员吹牛逼，你的还算靠谱。")
res.append("最近市面上骗子越来越多了")
res.append("什么EA交易，保本，月化...还有资金盘越来越多了，建议各位远离。")
res.append("外汇市场能让人一夜暴富，也能一夜爆负，如果不心存敬畏的话，狂妄就是崩溃的边缘。这是社区多少账户显示的真理。")
res.append("没毛病")
res.append("时光荏苒，辉煌继续")
res.append("越努力越有趣")
res.append("讲的很好")
res.append("先要存活下来，才有活路，所以交易从来不是随心所欲的一件事情。你说呢？")
res.append("交易计划，必须忠诚于它以及必须严格遵守它。你有吗？")
res.append("连续几笔的损失，是再正常不过的事情。")
res.append("这个纯干货")
res.append("年化多少，才算合理？")




sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

chrome_options = Options()
# hide browser window
#chrome_options.add_argument("--headless")       # define headless
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
    #判断是否已经登录
    if islogin():
        getidfromnew()
    else:
        #如果没有登录那么一直进行登录。
        login()
        main()
#创建url
def buildvisturl(id):
    url  = "https://www.followme.com/api/v2/trade/traders/"+id+"/followers?isFollowing=false&pageSize=1000&pageIndex=1&accountType=&pageField=PROFIT&pageSort=DESC&flag=1"

    return url

#进行最新微博的刷新
def getidfromnew():
    url = "https://www.followme.com/api/v3/social/newsBlogs?pageSize=100&pageIndex=1&LastBlogId=0"
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>','',html)

    al = re.findall(r",\"UserId\":\"(.*?)\"", html)
    
    urls = set()
    for index in al:
        url = "https://www.followme.com/user/"+ index
        urls.add(url)
    
    print(urls)
    
    i = 0
    for u in urls:
        i = i+1
        driver.get(u)
        time.sleep(5)
        html = driver.page_source

        #微博点赞
        try:
            driver.find_element_by_xpath("//*[contains(@class,'fm-fmt-nums')]").click()
            time.sleep(1)   
            driver.find_element_by_xpath("//*[contains(@class,'cmt-foot-count')]").click()
            time.sleep(1)   
            driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[1]/a[1]/i").click()
            time.sleep(3)

            #跟帖回复
            driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[1]/div/textarea").click()
            driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[1]/div/textarea").clear()
            tmpre = random.choice(res)
            driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[1]/div/textarea").send_keys(tmpre)
            driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[2]/div[2]/a").click()
            time.sleep(3)   
        except:
            pass

        urls = driver.current_url.split('/')
        driver.get_screenshot_as_file("./img/"+urls[4]+".png")

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
    html = re.sub(r'<.*?>','',html)

    j1 = json.loads(html)['data']['items']

    for index in range(len(j1)):
        url = "https://www.followme.com/user/"+ str(j1[index]["CustomerUserId"])+"/zone"
        driver.get(url)
        time.sleep(5)


if __name__ == "__main__":
    main()
