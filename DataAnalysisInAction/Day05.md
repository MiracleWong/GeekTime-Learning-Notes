# 【第三期】21 天打卡行动

#21 天打卡# Day05
专栏：数据分析实战 45 讲
时间：2020-02-17
学习：10、11、12
学习要点和总结：

一、10丨Python爬虫：如何自动化下载王祖贤海报？

1. Requests 是 Python HTTP 的客户端库，编写爬虫的时候都会用到，编写起来也很简单。它有两种访问方式：Get 和 Post。这两者最直观的区别就是：Get 把参数包含在 url 中，而 Post 通过 request body 来传递参数
2. XPath 是 XML 的路径语言，实际上是通过元素和属性进行导航，帮我们定位位置。
3. Chrome 插件：XPath Helper、JSON-gandle
4. 解析库 lxml，只需要调用 HTML 解析命令即可，然后再对 HTML 进行 XPath 函数的调用。
5. json：json.dumps() 将 Python 对象转换成 JSON 对象; json.loads() 将 JSON 对象转换成 Python 对象。
6. 在Chrome 使用开发者工具，查看 XHR 数据
7. Selenium 是 Web 应用的测试工具，可以直接运行在浏览器中，它的原理是模拟用户在进行操作

二、11 | 数据科学家80%时间都花费在了这些清洗任务上？

1. 好的数据分析师必定是一名数据清洗高手，要知道在整个数据分析过程中，不论是在时间还是功夫上，数据清洗大概都占到了 80%。
2. 数据清洗规则（完全合一）：1. 完整性；2. 全面性；3. 合法性；4. 唯一性。
3. 缺失值，用平均值进行填充：df['Age'].fillna(df['Age'].mean(), inplace=True)
4. 空行，需要删除：df.dropna(how='all',inplace=True)
5. 列数据的单位不统一，统一单位：磅（lbs）→ 千克（kgs）
6. 非 ASCII 字符，删除或替换：df['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
7. 一列有多个参数：拆分成新列，删除旧的
8. 重复数据：df.drop_duplicates(['first_name','last_name'],inplace=True)
9. 养成数据审核的习惯：数据清洗是高质量数据的一道保障。


三、12 | 数据集成：这些大号一共20亿粉丝？

1. 数据集成的两种架构：ELT 和 ETL
2. ETL 是英文 Extract、Transform 和 Load 的缩写，顾名思义它包括了数据抽取、转换、加载三个过程。(1) 抽取是将数据从已有的数据源中提取出来。(2) 转换是对原始数据进行处理。(3) 加载数据
3. 典型的 ETL 工具有: 商业软件——Informatica PowerCenter、IBM InfoSphere DataStage、Oracle Data Integrator、Microsoft SQL Server Integration Services 等；开源软件——Kettle、Talend、Apatar、Scriptella、DataX、Sqoop 等。
4. 举例三个软件：开源的 ETL 软件：Kettle；阿里开源软件：DataX；Apache 开源软件: Sqoop
5. Kettle 采用可视化的方式进行操作，来对数据库间的数据进行迁移。它包括了两种脚本：Transformation 转换和 Job 作业。
6. Transformation（转换）：相当于一个容器，对数据操作进行了定义。数据操作就是数据从输入到输出的一个过程。你可以把转换理解成为是比作业粒度更小的容器。在通常的工作中，我们会把任务分解成为不同的作业，然后再把作业分解成多个转换。Job（作业）：相比于转换是个更大的容器，它负责将转换组织起来完成某项作业。
7. Transformation 可以分成三个步骤，它包括了输入、中间转换以及输出。在 Transformation 中包括两个主要概念：Step 和 Hop。Step 的意思就是步骤，Hop 就是跳跃线的意思。
8. Step（步骤）：Step 是转换的最小单元，每一个 Step 完成一个特定的功能。在上面这个转换中，就包括了表输入、值映射、去除重复记录、表输出这 4 个步骤；Hop（跳跃线）：用来在转换中连接 Step。它代表了数据的流向。
9. 完整的任务，实际上是将创建好的转换和作业串联起来。在这里 Job 包括两个概念：Job Entry、Hop。
10. Job Entry（工作实体）：Job Entry 是 Job 内部的执行单元，每一个 Job Entry 都是用来执行具体的任务，比如调用转换，发送邮件等。Hop：指连接 Job Entry 的线。并且它可以指定是否有条件地执行。