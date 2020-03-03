# 【第三期】21 天打卡行动

#21 天打卡# Day19
专栏：数据分析实战 45 讲
时间：2020-03-02
学习：29
学习要点和总结：

一、[29 丨 EM 聚类（下）：用 EM 算法对王者荣耀英雄进行划分](https://time.geekbang.org/column/article/82333)

1. 引入工具包：from sklearn.mixture import GaussianMixture
2. 创建聚类：gmm = GaussianMixture(n_components=1, covariance_type=‘full’, max_iter=100) 来创建 GMM 聚类
3. 参数说明：a. n_components：即高斯混合模型的个数，也就是我们要聚类的个数，默认值为 1；b. covariance_type：代表协方差类型。四种类型：covariance_type=full，代表完全协方差，也就是元素都不为 0；covariance_type=tied，代表相同的完全协方差；covariance_type=diag，代表对角协方差，也就是对角不为 0，其余为 0；covariance_type=spherical，代表球面协方差，非对角为 0，对角完全相同，呈现球面的特性。c. max_iter：代表最大迭代次数，默认值为 100。
4. EM整个流程中可以看出，我们需要经过数据加载、数据探索、数据可视化、特征选择、GMM 聚类和结果分析等环节。
