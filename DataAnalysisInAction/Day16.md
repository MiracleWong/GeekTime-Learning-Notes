# 【第三期】21 天打卡行动

#21 天打卡# Day16
专栏：数据分析实战 45 讲
时间：2020-02-28
学习：26
学习要点和总结：

一、[26 丨 K-Means（上）：如何给 20 支亚洲球队做聚类？](https://time.geekbang.org/column/article/81390)

1. K-Means 是一种非监督学习，解决的是聚类问题。K 代表的是 K 类，Means 代表的是中心，算法的本质是确定 K 类的中心点，当你找到了这些中心点，也就完成了聚类。
2. K-Means 有自我纠正机制，在不断的迭代过程中，会纠正中心点。中心点在整个迭代过程中，并不是唯一的，只是你需要一个初始值，一般算法会随机设置初始的中心点。
3. n_neighbors：即 KNN 中的 K 值，代表的是邻居的数量。K 值如果比较小，会造成过拟合。如果 K 值比较大，无法将未知物体分类出来。一般我们使用默认值 5。
4. K-Means 的工作原理：1. 选取 K 个点作为初始的类中心点，这些点一般都是从数据集中随机抽取的；2. 将每个点分配到最近的类中心点，这样就形成了 K 个类，然后重新计算每个类的中心点；3. 重复第二步，直到类不发生变化，或者你也可以设置最大迭代次数，这样即使类中心点发生变化，但是只要达到最大迭代次数就会结束。
5. 距离计算方式：1.欧氏距离；2.曼哈顿距离；3.切比雪夫距离；4.余弦距离
6. sklearn 可以实现分类、聚类、回归、降维、模型选择和预处理等功能
7. K-Means 只是 sklearn.cluster 中的一个聚类库。sklearn.cluster 一共提供了 9 种聚类方法，比如 Mean-shift，DBSCAN，Spectral clustering（谱聚类）等
8. K-Means 创建：KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')
9. K-Means 参数说明：1. n_clusters: 即 K 值，一般需要多试一些 K 值来保证更好的聚类效果。2. max_iter： 最大迭代次数；3. n_init：初始化中心点的运算次数，默认是 10。4. init： 即初始值选择的方式，默认是采用优化过的 k-means++ 方式，你也可以自己指定中心点，或者采用 random 完全随机的方式。5. algorithm：k-means 的实现算法，有“auto” “full”“elkan”三种。一般来说建议直接用默认的"auto"。
10. K-Means 和 KNN 的异同：1. 这两个算法解决数据挖掘的两类问题。K-Means 是聚类算法，KNN 是分类算法。2. 这两个算法分别是两种不同的学习方式。K-Means 是非监督学习，也就是不需要事先给出分类标签，而 KNN 是有监督学习，需要我们给出训练数据的分类标识。3. K 值的含义不同。K-Means 中的 K 值代表 K 类。KNN 中的 K 值代表 K 个最接近的邻居。
