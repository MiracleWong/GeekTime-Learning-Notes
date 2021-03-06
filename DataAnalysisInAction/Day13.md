# 【第三期】21 天打卡行动

#21 天打卡# Day13
专栏：数据分析实战 45 讲
时间：2020-02-25
学习：23
学习要点和总结：

一、23 丨 SVM（下）：如何进行乳腺癌检测？

1. 在 Python 的 sklearn 工具包中有 SVM 算法，引入 svm，`from sklearn import svm`
2. 当用 SVM 做回归的时候，我们可以使用 SVR 或 LinearSVR。SVR 的英文是 Support Vector Regression。当做分类器的时候，我们使用的是 SVC 或者 LinearSVC。SVC 的英文是 Support Vector Classification。
3. LinearSVC 是个线性分类器，用于处理线性可分的数据，只能使用线性核函数
4. SVC 的构造函数：model = svm.SVC(kernel=‘rbf’, C=1.0, gamma=‘auto’)，这里有三个重要的参数 kernel、C 和 gamma。
5. kernel 代表核函数的选择，它有四种选择，只不过默认是 rbf，即高斯核函数。(1)：linear：线性核函数；(2). poly：多项式核函数；(3). rbf：高斯核函数（默认）；(4). sigmoid：sigmoid 核函数
6. 4 种核函数的优点和缺点：a. 线性核函数，是在数据线性可分的情况下使用的，运算速度快，效果好。不足在于它不能处理线性不可分的数据。2. 多项式核函数可以将数据从低维空间映射到高维空间，但参数比较多，计算量大。3. 高斯核函数同样可以将样本映射到高维空间，但相比于多项式核函数来说所需的参数比较少，通常性能不错，所以是默认使用的核函数。4. 当选用 sigmoid 核函数时，SVM 实现的是多层神经网络。
7. 参数 C 代表目标函数的惩罚系数，惩罚系数指的是分错样本时的惩罚程度，默认情况下为 1.0。当 C 越大的时候，分类器的准确性越高，但同样容错率会越低，泛化能力会变差。相反，C 越小，泛化能力越强，但是准确性会降低。
8. 参数 gamma 代表核函数的系数，默认为样本特征数的倒数，即 gamma = 1 / n_features。
9. 乳腺癌诊断分类的 SVM 实战，整个执行的流程，包括数据加载、数据探索、数据清洗、特征选择、SVM 训练和结果评估等环节。
