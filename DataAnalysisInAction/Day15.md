# 【第三期】21 天打卡行动

#21 天打卡# Day15
专栏：数据分析实战 45 讲
时间：2020-02-27
学习：25
学习要点和总结：

一、[25 丨 KNN（下）：如何对手写数字进行识别？](https://time.geekbang.org/column/article/81018)

1. 在 Python 的 sklearn 工具包中有 KNN 算法。KNN 既可以做分类器，也可以做回归。a. 分类：from sklearn.neighbors import KNeighborsClassifier；b. 回归：from sklearn.neighbors import KNeighborsRegressor。总结：Classifier 对应的是分类，Regressor 对应的是回归。
2. 构造函数：构造函数 KNeighborsClassifier(n_neighbors=5, weights=‘uniform’, algorithm=‘auto’, leaf_size=30)
3. n_neighbors：即 KNN 中的 K 值，代表的是邻居的数量。K 值如果比较小，会造成过拟合。如果 K 值比较大，无法将未知物体分类出来。一般我们使用默认值 5。
4. weights：是用来确定邻居的权重，有三种方式：weights=uniform，代表所有邻居的权重相同；weights=distance，代表权重是距离的倒数，即与距离成反比；自定义函数，你可以自定义不同距离所对应的权重。
5. algorithm：用来规定计算邻居的方法，它有四种方式：(1). algorithm=auto，根据数据的情况自动选择适合的算法，默认情况选择 auto；(2). algorithm=kd_tree，也叫作 KD 树，是多维空间的数据结构，方便对关键数据进行检索，不过 KD 树适用于维度少的情况，一般维数不超过 20，如果维数大于 20 之后，效率反而会下降；(3). algorithm=ball_tree，也叫作球树，它和 KD 树一样都是多维空间的数据结果，不同于 KD 树，球树更适用于维度大的情况；(4). algorithm=brute，也叫作暴力搜索，它和 KD 树不同的地方是在于采用的是线性扫描，而不是通过构造树结构进行快速检索。当训练集大的时候，效率很低。
6. 在 5 基础上，输入训练集对它进行训练，这里我们使用 fit() 函数，传入训练集中的样本特征矩阵和分类标识，会自动得到训练好的 KNN 分类器。
7. 在 6 基础上，使用 predict() 函数来对结果进行预测，这里传入测试集的特征矩阵，可以得到测试集的预测分类结果
8. 完整的手写数字数据集 MNIST 里面包括了 60000 个训练样本，以及 10000 个测试样本。sklearn 自带的手写数字数据集做 KNN 分类，一个简版的 MNIST 数据集，它只包括了 1797 幅数字图像，每幅图像大小是 8\*8 像素。
