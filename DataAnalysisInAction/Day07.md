# 【第三期】21 天打卡行动

#21 天打卡# Day07
专栏：数据分析实战 45 讲
时间：2020-02-19
学习：15、16
学习要点和总结：

一、15 丨一次学会 Python 数据可视化的 10 种技能

1. 按照数据之间的关系，可视化图示有四种关系：1. 比较：比较数据间各类别的关系，或者是它们随着时间的变化趋势，比如折线图；2. 联系：查看两个或两个以上变量之间的关系，比如散点图；3. 构成：每个部分占整体的百分比，或者是随着时间的百分比变化，比如饼图；4. 分布：关注单个变量，或者多个变量的分布情况，比如直方图。
2. 按照变量多少的关系，可视化图示分为：单变量分析和多变量分析。1. 单变量分析指的是一次只关注一个变量；2. 多变量分析可以让你在一张图上可以查看两个以上变量的关系。
3. 工具包：1. Matplotlib：Python 2D绘图基础库，也是其他绘图库的基础；2. Seaborn：基于Matplotlib的高级可视化效果库。
4. 可视化视图包括了散点图、折线图、直方图、条形图、箱线图、饼图、热力图、蜘蛛图、二元变量分布和成对关系。
5. 散点图的英文叫做 scatter plot，它将两个变量的值显示在二维坐标中，非常适合展示两个变量之间的关系。1. Matplotlib：plt.scatter(x, y, marker=None)；2. Seaborn：sns.jointplot(x, y, data=None, kind=‘scatter’)
6. 折线图：折线图可以用来表示数据随着时间变化的趋势。1. Matplotlib：plt.plot() ；2. Seaborn：sns.lineplot (x, y, data=None) 
7. 直方图：把横坐标等分成一定数量的数据段，然后用矩形条显示y轴的数量。1. Matplotlib：plt.hist(x, bins=10)；2. Seaborn：sns.distplot(x, bins=10, kde=True) 。
8. 条形图：用于查看类别的特征。长条形的长度表示类别的频数，宽度表示类别。1. Matplotlib：plt.bar(x, height) ；2. Seaborn：sns.barplot(x=None, y=None, data=None) 。
9. 箱线图：又称盒式图，由五个数值点组成：最大值 (max)、最小值 (min)、中位数 (median) 和上下四分位数 (Q3, Q1)。用于分析出数据的差异性、离散程度和异常值等。1. Matplotlib：plt.boxplot(x, labels=None)；2. Seaborn：sns.boxplot(x=None, y=None, data=None) 
10. 饼图：饼图是常用的统计学模块，可以显示每个部分大小与总和之间的比例。1. Matplotlib：plt.pie(x, labels=None)
11. 热力图：热力图，英文叫 heat map，是一种矩阵表示方法，其中矩阵中的元素值用颜色来代表，不同的颜色代表不同大小的值。热力图是一种非常直观的多元变量分析方法。1. Seaborn：sns.heatmap(data) 
12. 蜘蛛图: 蜘蛛图是一种显示一对多关系的方法。在蜘蛛图中，一个变量相对于另一个变量的显著性是清晰可见的。也称作为雷达图。1. 需要使用 Matplotlib 来进行画图，进行连线和填充。
13. 二元变量分布：两个变量之间的关系。1. Seaborn：sns.jointplot(x, y, data=None, kind)，用 kind 表示不同的视图类型：“kind=‘scatter’”代表散点图，“kind=‘kde’”代表核密度图，“kind=‘hex’ ”代表 Hexbin 图，它代表的是直方图的二维模拟。
14. 成对关系：探索数据集中的多个成对双变量的分布。1. sns.pairplot() 


二、16 丨数据分析基础篇答疑

1. 问题：如何理解 NumPy 中 axis 的使用？回答：如果排序的时候，没有指定 axis，默认 axis=-1，代表就是按照数组最后一个轴来排序。如果 axis=None，代表以扁平化的方式作为一个向量进行排序。
2. 问题：S32 代表什么意思？回答：i 代表整数，f 代表单精度浮点数，d 代表双精度浮点数，S 代表字符串，S32 代表的是 32 个字符的字符串，b 代表布尔值，U 代表 Unicode。
3. Python3 默认 str 是 Unicode 类型，所以要转成 bytestring，会在原来的 str 前加上 b。
4. ceil 是 numpy 中的一个函数，代表向上取整。比如 np.ceil(2.4)=3。
5. 选择 leetcode 或者 pythontip 进行训练；提交人数和 Accepted 比例越高，说明越简单。
6. Scrapy 本身包括了爬取、处理、存储等工具。在 scrapy 中，有一些组件是提供给你的，需要你针对具体任务进行编写。比如在 item.py 对抓取的内容进行定义，在 spider.py 中编写爬虫，在 pipeline.py 中对抓取的内容进行存储，可以保存为 csv 等格式。
7. Puppeteer 是个很好的选择，可以控制 Headless Chrome，与 Selenium 相比，Puppeteer 直接调用 Chrome 的 API 接口，不需要打开浏览器，直接在 V8 引擎中处理，同时这个组件是由 Google 的 Chrome 团队维护的，所以兼容性会很好。
