#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Chapter 05
import pandas as pd
from pandas import Series, DataFrame

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=["a", "b", "c", "d"])
print(x1)
print(x2)


d = {"a": 1, "b": 2, "c": 3, "d": 4}
x3 = Series(d)
print(x3)


data = {
    "Chinese": [66, 95, 93, 90, 80],
    "English": [65, 85, 92, 88, 90],
    "Math": [30, 98, 96, 77, 90],
}
df1 = DataFrame(data)
df2 = DataFrame(
    data,
    index=["ZhangFei", "GuanYu", "ZhaoYun", "HuangZhong", "DianWei"],
    columns=["English", "Math", "Chinese"],
)
print(df1)
print(df2)

# 删除行或列
df3 = df2.drop(columns=["Chinese"])
print(df3)


df4 = df2.drop(index=["ZhangFei"])
print(df4)


# 重命名
df2.rename(columns={"Chinese": "YuWen", "English": "Yingyu"}, inplace=True)
print(df2)


df1 = DataFrame({"name": ["ZhangFei", "GuanYu", "a", "b", "c"], "data1": range(5)})
print(df1.describe())



from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({"name": ["ZhangFei", "GuanYu", "a", "b", "c"], "data1": range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print(pysqldf(sql))
