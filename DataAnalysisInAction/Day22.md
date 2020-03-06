# 【第三期】21 天打卡行动

#21 天打卡# Day22
专栏：数据分析实战 45 讲
时间：2020-03-05
学习：33
学习要点和总结：

一、[33 丨 PageRank（下）：分析希拉里邮件中的人物关系](https://time.geekbang.org/column/article/83471)

1. 图论和网络建模的工具叫 NetworkX，它是用 Python 语言开发的工具，内置了常用的图与网络分析算法
2. 图可以分为无向图和有向图，在 NetworkX 中分别采用不同的函数进行创建。无向图指的是不用节点之间的边的方向，使用 nx.Graph() 进行创建；有向图指的是节点之间的边是有方向的，使用 nx.DiGraph() 来创建
3. 增加节点：可以使用 G.add_node('A') 添加一个节点，也可以使用 G.add_nodes_from(['B','C','D','E']) 添加节点集合。
4. 删除节点：可以使用 G.remove_node(node) 删除一个指定的节点，也可以使用 G.remove_nodes_from(['B','C','D','E']) 删除集合中的节点。
5. 查询节点：使用 G.nodes()得到图中所有的节点，也可以用 G.number_of_nodes() 得到图中节点的个数。
6. 增加边：使用 G.add_edge("A", "B") 添加指定的"从 A 到 B"的边，也可以使用 add_edges_from 函数从边集合中添加。
7. 做一个加权图，也就是说边是带有权重的，使用 add_weighted_edges_from 函数从带有权重的边的集合中添加。在这个函数的参数中接收的是 1 个或多个三元组[u,v,w]作为参数，u、v、w 分别代表起点、终点和权重。
8. 删除边：使用 remove_edge 函数和 remove_edges_from 函数删除指定边和从边集合中删除。
9. 查询边：使用 edges() 函数访问图中所有的边，使用 number_of_edges() 函数得到图中边的个数。
10. 整个数据集由三个文件组成：Aliases.csv，Emails.csv 和 Persons.csv，其中 Emails 文件记录了所有公开邮件的内容，发送者和接收者的信息。Persons 这个文件统计了邮件中所有人物的姓名及对应的 ID。因为姓名存在别名的情况，为了将邮件中的人物进行统一，我们还需要用 Aliases 文件来查询别名和人物的对应关系。
11. NetworkX 还有另外三种可视化布局，circular_layout（在一个圆环上均匀分布节点），random_layout（随机分布节点 ），shell_layout（节点都在同心圆上）。
