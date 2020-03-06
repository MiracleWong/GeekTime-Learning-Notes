# 【第三期】21 天打卡行动

#21 天打卡# Day21
专栏：数据分析实战 45 讲
时间：2020-03-04
学习：31
学习要点和总结：

一、[31 丨关联规则挖掘（下）：导演如何选择演员？](https://time.geekbang.org/column/article/82943)

1. https://pypi.org/ 上搜索相关的包
2. pip install efficient-apriori 安装
3. itemsets, rules = apriori(data, min_support, min_confidence)
4. 参数说明：data 是数据集，它是一个 list 数组类型。min_support 参数为最小支持度，在 efficient-apriori 工具包中用 0 到 1 的数值代表百分比，比如 0.5 代表最小支持度为 50%。min_confidence 是最小置信度，数值也代表百分比。
5. efficient-apriori 这个工具包，它会把每一条数据中的项（item）放到一个集合（篮子）里来处理，不考虑项（item）之间的先后顺序。
6. FP-growth 的算法包：import fptools as fp

二、[32 丨 PageRank（上）：搞懂 Google 的 PageRank 算法](https://time.geekbang.org/column/article/83034)

1. PageRank 模型：一个网页的影响力 = 所有入链集合的页面的加权影响力之和
2. 出链会给被链接的页面赋予影响力，当我们统计了一个网页链出去的数量，也就是统计了这个网页的跳转概率。
3. 等级泄露（Rank Leak）：如果一个网页没有出链，就像是一个黑洞一样，吸收了其他网页的影响力而不释放，最终会导致其他网页的 PR 值为 0。
4. 等级沉没（Rank Sink）：如果一个网页只有出链，没有入链（如下图所示），计算的过程迭代下来，会导致这个网页的 PR 值为 0（也就是不存在公式中的 V）
5. PageRank 的随机浏览模型：阻尼因子 d，这个因子代表了用户按照跳转链接来上网的概率，通常可以取一个固定值 0.85，而 1-d=0.15 则代表了用户不是通过跳转链接的方式来访问网页的
