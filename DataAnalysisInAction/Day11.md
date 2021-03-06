# 【第三期】21 天打卡行动

#21 天打卡# Day11
专栏：数据分析实战 45 讲
时间：2020-02-22
学习：21
学习要点和总结：

一、21 丨朴素贝叶斯分类（下）：如何对文档进行分类？

1. 朴素贝叶斯分类最适合的场景就是文本分类、情感分析和垃圾邮件识别。其中情感分析和垃圾邮件识别都是通过文本来进行判断。文本分类，这也是朴素贝叶斯最擅长的地方。朴素贝叶斯也常用于自然语言处理 NLP 的工具。
2. sklearn 的全称叫 Scikit-learn，它给我们提供了 3 个朴素贝叶斯分类算法，分别是高斯朴素贝叶斯（GaussianNB）、多项式朴素贝叶斯（MultinomialNB）和伯努利朴素贝叶斯（BernoulliNB）。
3. (1). 高斯朴素贝叶斯：特征变量是连续变量，符合高斯分布，比如说人的身高，物体的长度。(2). 多项式朴素贝叶斯：特征变量是离散变量，符合多项分布，在文档分类中特征变量体现在一个单词出现的次数，或者是单词的 TF-IDF 值等。(3). 伯努利朴素贝叶斯：特征变量是布尔变量，符合 0/1 分布，在文档分类中特征是单词是否出现。
4. TF-IDF 是一个统计方法，用来评估某个词语对于一个文件集或文档库中的其中一份文件的重要程度。TF-IDF 实际上是两个词组 Term Frequency 和 Inverse Document Frequency 的总称，两者缩写为 TF 和 IDF，分别代表了词频和逆向文档频率。
5. 词频 TF 计算了一个单词在文档中出现的次数，它认为一个单词的重要性和它在文档中出现的次数呈正比。逆向文档频率 IDF，是指一个单词在文档中的区分度。它认为一个单词出现在的文档数越少，就越能通过这个单词把该文档和其他文档区分开。IDF 越大就代表该单词的区分度越大。所以 TF-IDF 实际上是词频 TF 和逆向文档频率 IDF 的乘积。
6. sklearn 中我们直接使用 TfidfVectorizer 类，它可以帮我们计算单词 TF-IDF 向量的值。在这个类中，取 sklearn 计算的对数 log 时，底数是 e，不是 10。
7. 停用词就是在分类中没有用的词，这些词一般词频 TF 高，但是 IDF 很低，起不到分类的作用。
8. 对文档进行分类：1. 基于分词的数据准备，包括分词、单词权重计算、去掉停用词；2. 应用朴素贝叶斯分类进行分类，首先通过训练集得到朴素贝叶斯分类器，然后将分类器应用于测试集，并与实际结果做对比，最终得到测试集的分类准确率。
9. (1).对文档进行分词： 英文文档中，最常用的是 NTLK 包。NTLK 包中包含了英文的停用词 stop words、分词和标注方法。在中文文档中，最常用的是 jieba 包。jieba 包中包含了中文的停用词 stop words 和分词方法。(2).加载停用词表；(3).计算单词的权重：sklearn 里的 TfidfVectorizer 类；(4).生成朴素贝叶斯分类器：将特征训练集的特征空间 train_features，以及训练集对应的分类 train_labels 传递给贝叶斯分类器 clf，它会自动生成一个符合特征空间和对应分类的分类器。当 alpha=1 时，使用的是 Laplace 平滑。当 0< alpha <1 时，使用的是 Lidstone 平滑。(5). 使用生成的分类器做预测：a.得到测试集的特征矩阵；b. 训练好的分类器对新数据做预测。(6). 计算准确率： 调用 sklearn 中的 metrics 包，在 metrics 中提供了 accuracy_score 函数
