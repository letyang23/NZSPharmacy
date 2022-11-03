from pytrends.request import TrendReq

pytrends = TrendReq(hl='zh-TW')

# search terms
all_keywords = ['大樹藥局', '故宮', '台灣同志遊行', '彭文正', '勇士', '唾液快 篩', '丁丁藥局', '啄木鳥 藥 局', '屈臣氏']
keywords = []
# time frame
timeframes = ['today 5-y', 'today 12-m', 'today 3-m', 'today 1-m']
cat = '0'
geo = 'TW'
gprop = ''


def check_trends():
    pytrends.build_payload(keywords, cat, timeframes[0], geo, gprop)
    data = pytrends.interest_over_time()
    mean = round(data.mean(), 2)
    avg = round(data[kw][-52:].mean(), 2)
    avg2 = round(data[kw][:52].mean(), 2)
    trend = round(((avg / mean[kw]) - 1) * 100, 2)
    trend2 = round(((avg / avg2) - 1) * 100, 2)

    print("过去五年" + kw + "的平均兴趣值为" + str(mean[kw]) + "。（注意：此兴趣值仅为与自身比较）")
    print("过去一年" + kw + "的兴趣值对比过去五年改变了" + str(trend) + "%。")
    # Stable Trend
    if mean[kw] > 75 and abs(trend) <= 5:
        print(kw + "的热度在过去五年非常稳定")
    elif mean[kw] > 75 and trend > 5:
        print(kw + "的热度在过去五年非常稳定并且持续增加")
    elif mean[kw] > 75 and trend < -5:
        print(kw + "的热度在过去五年非常稳定并且持续减少")
    # Relatively　Stable
    elif mean[kw] > 60 and abs(trend) <= 15:
        print(kw + "的热度在过去五年相对稳定。")
    elif mean[kw] > 60 and trend > 15:
        print(kw + "的热度在过去五年相对稳定并且持续上升。")
    elif mean[kw] > 60 and trend < 15:
        print(kw + "的热度在过去五年相对稳定并且持续下降。")

    print("============================================================")


for kw in all_keywords:
    keywords.append(kw)
    check_trends()
    keywords.pop()
