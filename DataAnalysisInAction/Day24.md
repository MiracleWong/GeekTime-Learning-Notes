# 【第三期】21 天打卡行动

#21 天打卡# Day24
专栏：数据分析实战 45 讲
时间：2020-03-08
学习：35、36
学习要点和总结：

一、[35 丨 AdaBoost（下）：如何使用 AdaBoost 对房价进行预测？](https://time.geekbang.org/column/article/84086)

1. 什么是分类，什么是回归呢？都是对未知事物做预测。不同之处在于输出结果的类型，分类输出的是一个离散值，因为物体的分类数有限的，而回归输出的是连续值，也就是在一个区间范围内任何取值都有可能。
2. 用 AdaBoost 进行分类：from sklearn.ensemble import AdaBoostClassifier
3. 用 AdaBoost 进行回归：from sklearn.ensemble import AdaBoostRegressor
4. 创建 AdaBoost 分类的函数： AdaBoostClassifier(base_estimator=None, n_estimators=50, learning_rate=1.0, algorithm='SAMME.R', random_state=None)
5. 参数说明：a. base_estimator：代表的是弱分类器。b. n_estimators：算法的最大迭代次数，也是分类器的个数，每一次迭代都会引入一个新的弱分类器来增加原有的分类器的组合能力。默认是 50。c. learning_rate：代表学习率，取值在 0-1 之间，默认是 1.0。d. algorithm：采用的哪种 boosting 算法，一共有两种选择：SAMME 和 SAMME.R。默认是 SAMME.R。e. random_state：代表随机数种子的设置，默认是 None。
6. 创建 AdaBoost 回归的函数：AdaBoostRegressor(base_estimator=None, n_estimators=50, learning_rate=1.0, loss='linear', random_state=None)。参数说明：loss 代表损失函数的设置，一共有 3 种选择，分别为 linear、square 和 exponential，它们的含义分别是线性、平方和指数。默认是线性。一般采用线性就可以得到不错的效果。
7. 将 AdaBoost 分类器、弱分类器和决策树分类器做了对比，可以看出经过多个弱分类器组合形成的 AdaBoost 强分类器，准确率要明显高于决策树算法。所以 AdaBoost 的优势在于框架本身，它通过一种迭代机制让原本性能不强的分类器组合起来，形成一个强分类器。

二、[36 丨数据分析算法篇答疑](https://time.geekbang.org/column/article/84499)

1. 一、sklearn 自带的小数据集（packageddataset）：sklearn.datasets.load\_<name>

1)鸢尾花数据集：load_iris（）：用于分类任务的数据集 2)手写数字数据集：load_digits（）:用于分类任务或者降维任务的数据集 3)乳腺癌数据集 load_breast_cancer（）：简单经典的用于二分类任务的数据集 4)糖尿病数据集：load_diabetes（）：经典的用于回归认为的数据集，值得注意的是，这 10 个特征中的每个特征都已经被处理成 0 均值，方差归一化的特征值。 5)波士顿房价数据集：load_boston（）：经典的用于回归任务的数据集 6)体能训练数据集：load_linnerud（）：经典的用于多变量回归任务的数据集。

体能训练数据集中的特征名称 linnerud.feature_names 为['Chins', 'Situps', 'Jumps']
鸢尾花数据集的特征名称 iris.feature_names 为['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']

2. https://www.kaggle.com/learn/overview 页面里有分类好的比较简单的 kernel，可以 fork kernel 在 kaggle 上运行，也可以下载 ipynb 或者 rmd 文件在自己的电脑上运行。比较经典的 kaggle 竞赛有泰坦尼克预测，房价预测，数字识别等，刚起步时可以参考这些竞赛里的 kernel.
   另外，有一个开源组织 ApacheCN 有一些 kaggle 的培训，有很多相关的活动，也可以找同伴组队参加比赛。

3. Kaggle 的 Python 数据分析入门教程：https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners

另外入门级别的 kernels 就是 Titanic 和房价预测：
1、https://www.kaggle.com/c/titanic
2、https://www.kaggle.com/c/house-prices-advanced-regression-techniques

4. Kaggle 里很多数据集都不错，另外在专栏里也会讲到关于信用卡违约率分析和信用卡欺诈分析。下面整理了一些数据集，更多数据集，可以通过https://www.kaggle.com/datasets 查找

Titanic: Machine Learning from Disaster
Titanic 乘客生存预测
https://www.kaggle.com/c/titanic

House Prices-Advanced Regression Techniques
预测房价
https://www.kaggle.com/c/house-prices-advanced-regression-techniques

MNIST 手写数字识别
https://www.kaggle.com/scolianni/mnistasjpg

Passenger Satisfaction
乘客满意度，提供了美国航空公司 US Airline 乘客满意度数据
https://www.kaggle.com/johndddddd/customer-satisfaction

Bike Sharing Demand
自行车共享数据库，用于预测自行车的共享需求
https://www.kaggle.com/lakshmi25npathi/bike-sharing-dataset

San Francisco Building Permits
5 年时间，三藩市 20 万的建筑许可
https://www.kaggle.com/aparnashastry/building-permit-applications-data

San Francisco Crime Classification
12 年时间的三藩市的犯罪记录
https://www.kaggle.com/kaggle/san-francisco-crime-classification
