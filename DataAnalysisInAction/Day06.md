# 【第三期】21 天打卡行动

#21 天打卡# Day06
专栏：数据分析实战 45 讲
时间：2020-02-18
学习：13、14
学习要点和总结：

一、13 | 数据变换：考试成绩要求正态分布合理么？

1. 数据变换是数据准备的重要环节，它通过数据平滑、数据聚集、数据概化和规范化等方式将数据转换成适用于数据挖掘的形式。
2. 常见的变换方法：1. 数据平滑：去除数据中的噪声，将连续数据离散化。2. 数据聚集：对数据进行汇总。3. 数据概化：将数据由较低的概念抽象成为较高的概念，减少数据复杂度。4. 数据规范化：使属性数据按比例缩放。5. 属性构造：构造出新的属性并添加到属性集中。
3. 数据平滑：可以采用分箱、聚类和回归。
4. 数据规范化的方法：1. Min-max 规范化：新数值 =（原数值 - 极小值）/（极大值 - 极小值），将原始数据变换到[0,1]的空间中。2. Z-Score 规范化：新数值 =（原数值 - 均值）/ 标准差，易于比较，但是没有实际意义。3. 小数定标规范化：通过移动小数点的位置来进行规范化，位数取决于属性 A 的取值中的最大绝对值。
5. SciKit-Learn 是 Python 的重要机器学习库，封装了大量的机器学习算法，比如分类、聚类、回归、降维等。此外，它还包括了数据变换模块。
6. SciKit-Learn 库使用：1. Min-max 规范化：preprocessing.MinMaxScaler()；2. Z-Score 规范化：preprocessing.scale()；
7. NumPy使用：3. 小数定标规范化：j = np.ceil(np.log10(np.max(abs(x))))；scaled_x = x/(10**j)

二、14丨数据可视化：掌握数据领域的万金油技能

1. 可视化视图超过 20 种，分别包括：文本表、热力图、地图、符号地图、饼图、水平条、堆叠条、并排条、树状图、圆视图、并排圆、线、双线、面积图、双组合、散点图、直方图、盒须图、甘特图、靶心图、气泡图等
2. 数据可视化工具：商业智能分析（Tableau 和 PowerBI、FineBI）、可视化大屏类（DataV 和 FineReport）、前端可视化组件（Echarts、D3、Three.js 和 AntV）
3. Python 里包括了众多可视化库，比如 Matplotlib、Seaborn、Bokeh、Plotly、Pyecharts、Mapbox 和 Geoplotlib。
4. Matplotlib 是 Python 的可视化基础库，Seaborn 是一个基于 Matplotlib 的高级可视化效果库，针对 Matplotlib 做了更高级的封装，
5. R 自带的绘图包 Graphics 以及工具包 ggplot2、ggmap、timevis 和 plotly 等。
6. 如何开始数据可视化的学习：1. 重点推荐 Tableau 2. 使用微图、DataV；3. Python 可视化
7. 课后学员推荐：[Python编程实践：数据可视化](https://mp.weixin.qq.com/s/dmJGMvFAroxJkTk5NwynSw)