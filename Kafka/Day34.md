# 21 天打卡行动

#21 天打卡# Day34
专栏：kafka 核心技术与实战
时间：2020-03-27
学习：14
学习要点和总结：

一、[14 | 幂等生产者和事务生产者是一回事吗？](https://time.geekbang.org/column/article/103974)

1. 所谓的消息交付可靠性保障，是指 Kafka 对 Producer 和 Consumer 要处理的消息提供什么样的承诺。常见的承诺有以下三种：最多一次（at most once）：消息可能会丢失，但绝不会被重复发送。至少一次（at least once）：消息不会丢失，但有可能被重复发送。精确一次（exactly once）：消息不会丢失，也不会被重复发送。
2. Kafka 是怎么做到精确一次的呢？简单来说，这是通过两种机制：幂等性（Idempotence）和事务（Transaction）。
3. "幂等"这个词原是数学领域中的概念，指的是某些操作或函数能够被执行多次，但每次得到的结果都是不变的。
4. 幂等性有很多好处，其最大的优势在于我们可以安全地重试任何幂等性操作，反正它们也不会破坏我们的系统状态。
5. 在 Kafka 中，Producer 默认不是幂等性的，0.11.0.0 版本引入幂等性 Producer。仅需要设置一个参数即可，即 props.put("enable.idempotence", ture)，或 props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG， true)。
6. 幂等性 Producer 的作用范围：首先，它只能保证单分区上的幂等性，即一个幂等性 Producer 能够保证某个主题的一个分区上不出现重复消息，它无法实现多个分区的幂等性。其次，它只能实现单会话上的幂等性，不能实现跨会话的幂等性。
7. Kafka 自 0.11 版本开始也提供了对事务的支持，目前主要是在 read committed 隔离级别上做事情。它能保证多条消息原子性地写入到目标分区，同时也能保证 Consumer 只能看到事务成功提交的消息。
8. 事务型 Producer 能够保证将消息原子性地写入到多个分区中。这批消息要么全部写入成功，要么全部失败。另外，事务型 Producer 也不惧进程的重启。Producer 重启回来后，Kafka 依然保证它们发送消息的精确一次处理。
9. 设置事务型 Producer，和幂等性 Producer 一样，开启 enable.idempotence = true。设置 Producer 端参数 transactional. id。最好为其设置一个有意义的名字。
