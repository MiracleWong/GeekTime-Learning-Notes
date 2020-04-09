# 21 天打卡行动

#21 天打卡# Day33
专栏：kafka 核心技术与实战
时间：2020-03-26
学习：15
学习要点和总结：

一、[15 | 消费者组到底是什么？](https://time.geekbang.org/column/article/105112)

1. Consumer Group 是 Kafka 提供的可扩展且具有容错性的消费者机制。
2. Consumer Group 的特性：（1）Consumer Group 下可以有一个或多个 Consumer 实例。这里的实例可以是一个单独的进程，也可以是同一进程下的线程。在实际场景中，使用进程更为常见一些。（2）Group ID 是一个字符串，在一个 Kafka 集群中，它标识唯一的一个 Consumer Group。（3）Consumer Group 下所有实例订阅的主题的单个分区，只能分配给组内的某个 Consumer 实例消费。这个分区当然也可以被其他的 Group 消费。
3. Kafka 仅仅使用 Consumer Group 这一种机制，却同时实现了传统消息引擎系统的两大模型：如果所有实例都属于同一个 Group，那么它实现的就是消息队列模型；如果所有实例分别属于不同的 Group，那么它实现的就是发布 / 订阅模型。
4. 理想情况下，Consumer 实例的数量应该等于该 Group 订阅主题的分区总数。
5. Kafka 社区重新设计了 Consumer Group 的位移管理方式，采用了将位移保存在 Kafka 内部主题的方法。这个内部主题就是让人既爱又恨的 \_\_consumer_offsets。
6. Rebalance 本质上是一种协议，规定了一个 Consumer Group 下的所有 Consumer 如何达成一致，来分配订阅 Topic 的每个分区。
7. Rebalance 的触发条件有 3 个：组成员数发生变更。订阅主题数发生变更。订阅主题的分区数发生变更。
8. Rebalance 的缺点：(1) Rebalance 过程对 Consumer Group 消费过程有极大的影响；(2) 分配方案的变动太大 (3)Rebalance 太慢
