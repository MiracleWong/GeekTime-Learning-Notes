#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Chapter 13

from sklearn import preprocessing
import numpy as np

# 初始化数据
x = np.array([[0.0, -3.0, 1.0], [3.0, 1.0, 2.0], [0.0, 1.0, -1.0]])
# 将数据进行[0,1]规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)

# 将数据进行Z-Score规范化
scaled_x = preprocessing.scale(x)
print(scaled_x)

# 小数定标规范化
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x / (10 ** j)
print(scaled_x)


## 课后练习
# 初始化数据，每一行表示一个样本，每一列表示一个特征
y = np.array([[5000.0], [16000.0], [58000.0]])
# 将数据进行 [0,1] 规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_y = min_max_scaler.fit_transform(y)
print(minmax_y)
