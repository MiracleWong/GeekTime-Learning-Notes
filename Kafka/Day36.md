# 21 天打卡行动

#21 天打卡# Day36
专栏：kafka 核心技术与实战
时间：2020-04-03
学习：17
学习要点和总结：

一、[16 | 揭开神秘的"位移主题"面纱](https://time.geekbang.org/column/article/105473?utm_term=pc_interstitial_208)

1. Rebalance 就是让一个 Consumer Group 下所有的 Consumer 实例就如何消费订阅主题的所有分区达成共识的过程。在 Rebalance 过程中，所有 Consumer 实例共同参与，在协调者组件的帮助下，完成订阅主题分区的分配。但是，在整个过程中，所有实例都不能消费任何消息，因此它对 Consumer 的 TPS 影响很大。
2. Rebalance 的弊端：(1). Rebalance 影响 Consumer 端 TPS。(2). Rebalance 很慢。Rebalance 效率不高。(3). 当前 Kafka 的设计机制决定了每次 Rebalance 时，Group 下的所有成员都要参与进来，而且通常不会考虑局部性原理，但局部性原理对提升系统性能是特别重要的。
3. 社区于 0.11.0.0 版本推出了 StickyAssignor，即有粘性的分区分配策略。所谓的有粘性，是指每次 Rebalance 时，该策略会尽可能地保留之前的分配方案，尽量实现分区分配的最小变动。
4. Rebalance 发生的时机有三个：(1). 组成员数量发生变化；(2). 订阅主题数量发生变化；(3). 订阅主题的分区数发生变化。
5. 在真实的业务场景中，很多 Rebalance 都是计划外的或者说是不必要的。两种：(1). 第一类非必要 Rebalance 是因为未能及时发送心跳，导致 Consumer 被“踢出”Group 而引发的。(2). 第二类非必要 Rebalance 是 Consumer 消费时间过长导致的。
6. 用于减少 Rebalance 的 4 个参数：session.timeout.ms；heartbeat.interval.ms；max.poll.interval.ms；GC 参数。
7. Consumer 端有个参数，叫 session.timeout.ms，该参数的默认值是 10 秒，session.timeout.ms 决定了 Consumer 存活性的时间间隔
8. Consumer 还提供了一个允许你控制发送心跳请求频率的参数，就是 heartbeat.interval.ms。
9. Consumer 端还有一个参数，用于控制 Consumer 实际消费能力对 Rebalance 的影响，即 max.poll.interval.ms 参数。它限定了 Consumer 端应用程序两次调用 poll 方法的最大时间间隔。它的默认值是 5 分钟。
10. 最佳实践 1：(1). 设置 session.timeout.ms = 6s。(2). 设置 heartbeat.interval.ms = 2s。(3). 要保证 Consumer 实例在被判定为“dead”之前，能够发送至少 3 轮的心跳请求，即 session.timeout.ms >= 3 \* heartbeat.interval.ms。
