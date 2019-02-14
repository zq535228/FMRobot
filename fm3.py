# coding=utf-8

import time
from selenium import webdriver
import json, re
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
res.append("不要以为自己获得了制胜法宝，以为交易市场比提款机还方便，相信我即便你做了交易后的几年都很可能不会有你想的美好。")
res.append("只看一个品种，一直盯着，不做别的")
res.append("每天都用复盘软件再重新模拟一遍今天的行情是个好习惯。")
res.append("对于小散户而言，基本面分析很难")
res.append("我研究过几乎所有的技术指标，但是发现这些指标不适合用于短时交易")
res.append("在技术面，有两种基本的策略，趋势和反转")
res.append("我开始的时候着迷于趋势，但一段时间后发现，短时交易很难很难抓趋势")
res.append("趋势是个很难精确表达的概念，当然可能有更精确的定义，如一段时间内多方向上连续超过多少点，而同时空方向上少于多少点，就可以定义为方向为多，但没时间和精力去验证。")
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
res.append("我曾经把1000美金0.01的仓做爆，就是不设损像他们那样，套住了就扛着，就不信他不会拐弯，跟行情死磕，最后是我输了，它赢了")
res.append("来点赞，加油")
res.append("控制好仓位，顺势交易，设止盈止损。如果真能严格遵守这些交易纪律还是能把赔的钱赚回来的。")
res.append("慢慢来迟早会赚回来的")
res.append("愿楼主早日能大彻大悟，在外汇的道路上越走越顺")
res.append("被强平仓很正常，同样的错误再范三次就不就不应该了。")
res.append("爆仓确实很正常。加油！")
res.append("有希望就要追")
res.append("坚持不住吧")
res.append("贪，重仓，急躁，没耐性，不按规则出牌，这些都是导致爆仓的重要原因。")
res.append("其实我想说的是，刚进入这个市场的新手朋友可能会觉得外汇很简单！但是外汇赚钱的是极少数的，大部分都是亏钱的，如果真要进入这个行业，首先两条原则 一是兼职就好，不要影响工作。二是资金量一定要小，亏了不影响生活。")
res.append("刚进入这个行业的新手很多都是抱着赚大钱，一夜暴富的想法来的，但是很残酷，往往抱有这种想法的交易者，最容易在外汇交易市场里折戟！")
res.append("开始进入市场就要抱着缴学费的心态来交易，所以资金量自然不会大，用最少的学费学到更多的东西，当你有一天觉得自己有把握能够持续稳定盈利之后，再增加资金也不迟。")
res.append("如果你真有悟性，真能持续盈利，哪怕是100块钱，也能赚得满盆钵。")
res.append("认识并承认自己身上的不足，不要固执。")
res.append("对别人的任何建议和想法都不盲目的拒绝，用批判接受的态度去接纳不同的意见，有时候你觉得不可能的事情也许就是可能的。")
res.append("只要是交易了五年以上的老手写的关于交易的文章我都会认真拜读。")
res.append("真正的交易光靠学是学不来的，而是要靠自己亲身体验才能悟得更多真谛。")
res.append("学习当然也很重要，至少可能让你少走很多弯路。")
res.append("市场是一只猛虎，不要只看到它温顺的一面，要看到它凶猛的一面，它温顺的时候你可以随意的拔几根毛，但它凶猛起来却能要你的命。交易就是先保命，再拔毛。")
res.append("只有当你在这个市场浸淫越久，你会越感觉对市场的无知，才会感觉技术已经是个无足轻重的东西了。")
res.append("这个市场很简单，但这个简单分为两个简单，一是对市场的无知而觉得简单，另一个是已经理解了市场的本质而觉得简单。")
res.append("在这个市场，没有人能够随随便便成功，即便是暂时的成功也不一定能持续的成功")
res.append("关键在于你是否能够看到别人没有看到的一些本质的东西，而你看到的一些本质的东西当别人也看到了之后")
res.append("你是否还能看到更深层次的东西。")
res.append("想要在这个市场里生存，并长久的持续下去，唯有不断的努力，不断的学习，不断的进步，任何时候都能先人一步，你才会持续成功。")
res.append("希望不要寄托在别人身上，而是要自己不断的努力才行。")
res.append("这几年我最大的收获就是明白了自己在哪些地方不足，明白了市场是怎样的一头怪兽，以至于说自己到底在这个市场能不能成功，那就要看自己的信念是否足够强，自己的努力是否足够多。在任何时候，任何行业，付出跟回报永远成正比，这个市场也一样。")
res.append("其实前面也有朋友问我如何坚持下来的。就两个字 信念。")
res.append("我这个人最大的缺点是不够坚持。")
res.append("最大的优点是比较爱学习。")
res.append("还有个毛病是打工又不喜欢受人管束，但自己做生意又做得不好。")
res.append("回想以前做过的很多事情，只要多坚持一下，结果也就不一样了。")
res.append("我发现我以前很多事情半途而废就是因为信念不足，而导致自己坚持不够。")
res.append("我有个朋友，到今年认识刚好十年。我跟他认识也是因为工作原因。而他现在还在做我和他认识时一起做的工作，只不过现在他是手底下有几十名员工的老板。他十年就只做了一件事，而我好高骛远东奔西跑，结果一事无成。")
res.append("我相信在外汇市场，别人能够赚钱，我为什么不能？")
res.append("虽然一而再再而三的失败，但我的信念没有一丝动摇。")
res.append("虽然中途可能因为工作原因很长时间没有操作，但心里时时刻刻都是惦记着的。")
res.append("但是最后对新手朋友说一句，做这个兼职就好。")
res.append("除非你有能力，有自信自己能够靠交易获得持续稳定的收入，还有就是要坚持学习，不断的拓展自己的思维，交易是灵活的，没有一成不变的东西。")
res.append("要像一颗大树一样，根基牢牢扎在地上，树枝迎风摇摆。")
res.append("现在想想时间确实很快！外汇投机之旅更是异常的艰辛，个中滋味也只有自己能体会！！！")
res.append("我才打造出自己的交易体统！ 我花费八年打造的交易系统却用的是八年前入门学的东西！")
res.append("我所苦苦追寻的交易技术从起点又回到了起点！今天，又是一个新的起点！")
res.append("大家都早日翻倍！")
res.append("不由想起中学时候的一位老师，想对她说声谢谢。离开论坛有大半年了，并不是忘记了，而确实工作太忙了。每天忙到晚上十一二点，回家几乎都是疲惫入睡，第二天又早起，一方面是家庭的责任，一方面是朋友的信任")
res.append("现在以事业家庭为重！但外汇是不放弃，也不沉迷！权当乐趣，生活佐料！")
res.append("但凡有一点点赌性，而自律和执行稍差的话，一旦进入市场，赌性就会被市场的波动无限放大，最终结局就逃不过爆仓！")
res.append("时间太快，人生太短。")
res.append("通过最近两年的努力，工作也还算略有小成。")
res.append("本来是想通过改变自己来提升交易方面的能力，然而自己的改变给我的工作带来了很大的帮助，抽了快二十年的烟也戒掉了快一年了，人也变帅了不少，这可能也是从外汇交易中获得的一点补偿吧，但不管怎样，总比一无所获强，对吧。")
res.append("虽然工作很辛苦，但是从没有想过放弃外汇交易，工作之余也会抽点时间陪一下外汇交易这个老朋友，所以我并没有离开。")
res.append("有句话叫 暂时的放弃是为了永久的陪伴。说的没错。")
res.append("做好交易是我一直以来的信仰和希望，谢谢还有朋友一直鼓励我。")
res.append("都说十年磨一剑，今年正好十年，我觉得我对交易的解读又更深了一点。")
res.append("眨眼之间。回来看看有多少朋友还在。")
res.append("南阎浮提众生，其性刚强，难调难服。")
res.append("资本市场要是有人能听劝就好了，因为每个人都有自己的特质，每个人都有理由相信自己没准也是个传奇")
res.append("是啊，交易者是孤独的，不和市场大多数人不一样，如何挣市场的钱？")
res.append("天天盯盘，半夜还要起来，熬的性生活都不想有了，忍心吗")
res.append("我的任务就是让你玩爽 一直在")

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
    # 判断是否已经登录
    if islogin():
        getidfromnew()
    else:
        # 如果没有登录那么一直进行登录。
        login()
        main()


# 创建url
def buildvisturl(id):
    url = "https://www.followme.com/api/v2/trade/traders/" + id + "/followers?isFollowing=false&pageSize=1000&pageIndex=1&accountType=&pageField=PROFIT&pageSort=DESC&flag=1"
    return url


# 进行最新微博的刷新
def getidfromnew():
    url = "https://www.followme.com/api/v3/social/newsBlogs?pageSize=100&pageIndex=1&LastBlogId=0"
    driver.get(url)
    html = driver.page_source
    html = re.sub(r'<.*?>', '', html)

    al = re.findall(r",\"UserId\":\"(.*?)\"", html)

    urls = set()
    for index in al:
        url = "https://www.followme.com/user/" + index
        urls.add(url)

    print(urls)

    i = 0
    for u in urls:
        i = i + 1
        driver.get(u)
        time.sleep(5)
        html = driver.page_source

        # 微博点赞
        try:
            driver.find_element_by_xpath("//*[contains(@class,'fm-fmt-nums')]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[contains(@class,'cmt-foot-count')]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[1]/a[1]/i").click()
            time.sleep(3)

            # 跟帖回复,20%概率。
            r = [1, 2, 3, 4, 5]
            if 1 == random.choice(r):
                driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[1]/div/textarea").click()
                driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[1]/div/textarea").clear()
                tmpre = random.choice(res)
                driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[1]/div/textarea").send_keys(tmpre)
                driver.find_element_by_xpath("//*[@id=\"fm-new-details-comment\"]/div[2]/div/div[2]/div[2]/a").click()
                time.sleep(3)
        except:
            pass

        urls = driver.current_url.split('/')
        driver.get_screenshot_as_file("./img/" + urls[4] + ".png")


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
    html = re.sub(r'<.*?>', '', html)

    j1 = json.loads(html)['data']['items']

    for index in range(len(j1)):
        url = "https://www.followme.com/user/" + str(j1[index]["CustomerUserId"]) + "/zone"
        driver.get(url)
        time.sleep(5)


if __name__ == "__main__":
    main()
