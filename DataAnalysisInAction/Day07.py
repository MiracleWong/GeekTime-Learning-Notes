#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Chapter 15


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# # 1. 散点图
# # 数据准备
# N = 1000
# x = np.random.randn(N)
# y = np.random.randn(N)
# # 用Matplotlib画散点图
# plt.scatter(x, y, marker="x")
# plt.show()
# # 用Seaborn画散点图
# df = pd.DataFrame({"x": x, "y": y})
# sns.jointplot(x="x", y="y", data=df, kind="scatter")
# plt.show()


# # 2. 折线图

# # 数据准备
# x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
# # 使用Matplotlib画折线图
# plt.plot(x, y)
# plt.show()
# # 使用Seaborn画折线图
# df = pd.DataFrame({"x": x, "y": y})
# sns.lineplot(x="x", y="y", data=df)
# plt.show()


# # 3. 直方图

# # 数据准备
# a = np.random.randn(100)
# s = pd.Series(a)
# # 用Matplotlib画直方图
# plt.hist(s)
# plt.show()
# # 用Seaborn画直方图，kde代表显示核密度估计
# sns.distplot(s, kde=False)
# plt.show()
# sns.distplot(s, kde=True)
# plt.show()


# # 4. 条形图📊

# # 数据准备
# x = ["Cat1", "Cat2", "Cat3", "Cat4", "Cat5"]
# y = [5, 4, 8, 12, 7]
# # 用Matplotlib画条形图
# plt.bar(x, y)
# plt.show()
# # 用Seaborn画条形图
# sns.barplot(x, y)
# plt.show()


# # 5. 箱线图

# # 数据准备
# # 生成0-1之间的10*4维度数据
# data = np.random.normal(size=(10, 4))
# lables = ["A", "B", "C", "D"]
# # 用Matplotlib画箱线图
# plt.boxplot(data, labels=lables)
# plt.show()
# # 用Seaborn画箱线图
# df = pd.DataFrame(data, columns=lables)
# sns.boxplot(data=df)
# plt.show()

# # 6. 饼图

# # 数据准备
# nums = [25, 37, 33, 37, 6]
# labels = ["High-school", "Bachelor", "Master", "Ph.d", "Others"]
# # 用Matplotlib画饼图
# plt.pie(x=nums, labels=labels)
# plt.show()

# # 7. 热力图

# # 数据准备
# flights = sns.load_dataset("flights")
# data = flights.pivot("year", "month", "passengers")
# # 用Seaborn画热力图
# sns.heatmap(data)
# plt.show()


# # 8. 蜘蛛图

# from matplotlib.font_manager import FontProperties

# # 数据准备
# labels = np.array([u"推进", "KDA", u"生存", u"团战", u"发育", u"输出"])
# stats = [83, 61, 95, 67, 76, 88]
# # 画图数据准备，角度、状态值
# angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
# stats = np.concatenate((stats, [stats[0]]))
# angles = np.concatenate((angles, [angles[0]]))
# # 用Matplotlib画蜘蛛图
# fig = plt.figure()
# ax = fig.add_subplot(111, polar=True)
# ax.plot(angles, stats, "o-", linewidth=2)
# ax.fill(angles, stats, alpha=0.25)
# # 设置中文字体
# # font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

# # 设置MacOS X 上的中文字体
# font = FontProperties(fname=r"/System/Library/Fonts/STHeiti Light.ttc", size=14)
# ax.set_thetagrids(angles * 180 / np.pi, labels, FontProperties=font)
# plt.show()


# # 二元变量分析

# # 数据准备
# tips = sns.load_dataset("tips")
# print(tips.head(10))
# # 用Seaborn画二元变量分布图（散点图，核密度图，Hexbin图）
# sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
# sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
# sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
# plt.show()


# # 成对关系

# # 数据准备
# iris = sns.load_dataset("iris")
# # 用Seaborn画成对关系
# sns.pairplot(iris)
# plt.show()


# # Chapter 16
# import numpy as np
# a = np.array([[4, 3, 2], [2, 4, 1]])
# print(np.sort(a))
# print(np.sort(a, axis=None))
# print(np.sort(a, axis=0))
# print(np.sort(a, axis=1))


# persontype = np.dtype({
#     'names':['name', 'age', 'chinese', 'math', 'english'],
#     'formats':['U32','i', 'i', 'i', 'f']})
# peoples = np.array([("张飞", 32, 75, 100, 90), ("关羽", 24, 85, 96, 88.5), ("赵云", 28, 85, 92, 96.5), ("黄忠", 29, 65, 85, 100)], dtype=persontype)
# print(peoples)


# student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
# print(a)
# print(a['name'])
