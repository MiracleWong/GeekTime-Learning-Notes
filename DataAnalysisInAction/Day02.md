# 【第三期】21 天打卡行动

#21 天打卡# Day02
专栏：数据分析实战 45 讲
时间：2020-02-14
学习：03、04、06
学习要点和总结：

1. NumPy 所提供的数据结构是 Python 数据分析的基础。
2. 提升效率：避免采用隐式拷贝，而是采用就地操作的方式。举例 y \*= 2
3. Nupmy 入门：ndarray 和 ufunc
4. arange() 类似内置函数 range()，通过指定初始值、终值、步长来创建等差数列的一维数组，默认是不包括终值的。linspace 是 linear space 的缩写，代表线性等分向量的含义。linspace() 通过指定初始值、终值、元素个数来创建等差数列的一维数组，默认是包括终值的。
5. 最大值函数 amax()，最小值函数 amin()，amin() 用于计算数组中的元素沿指定轴的最小值，amax()同理
6. 统计最大值与最小值之差 ptp()、统计数组的百分位数 percentile()、统计数组中的中位数 median()、平均数 mean()、统计数组中的加权平均值 average()、统计数组中的标准差 std()、方差 var()
7. 对于 axis 轴的可视化理解：https://zhuanlan.zhihu.com/p/30960190
8. sort(a, axis=-1, kind=‘quicksort’, order=None)，默认情况下使用的是快速排序；在 kind 里，可以指定 quicksort、mergesort、heapsort 分别表示快速排序、合并排序、堆排序。同样 axis 默认是 -1，即沿着数组的最后一个轴进行排序，也可以取不同的 axis 轴，或者 axis=None 代表采用扁平化的方式作为一个向量进行排序。
9. 商业智能的英文是 Business Intelligence，缩写是 BI；数据仓库的英文是 Data Warehouse，缩写是 DW；数据挖掘的英文是 Data Mining，缩写是 DM。
10. 元数据（MetaData）：描述其它数据的数据，也称为“中介数据”。数据元（Data Element）：就是最小数据单元。
11. Knowledge Discovery in Database，简称 KDD：分类、聚类、预测和关联分析
12. 数据预处理的步骤：数据清洗，数据集成，以及数据变换