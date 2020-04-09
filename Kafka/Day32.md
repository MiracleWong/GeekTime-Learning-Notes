# 21 天打卡行动

#21 天打卡# Day32
专栏：kafka 核心技术与实战
时间：2020-03-25
学习：13
学习要点和总结：

一、[13 | Java 生产者是如何管理 TCP 连接的？](https://time.geekbang.org/column/article/103844)

Apache Kafka 的所有通信都是基于 TCP 的，而不是于 HTTP 或其他协议的
1 为什采用 TCP?
（1）TCP 拥有一些高级功能，如多路复用请求和同时轮询多个连接的能力。
（2）很多编程语言的 HTTP 库功能相对的比较简陋。
名词解释：
多路复用请求：multiplexing request，是将两个或多个数据合并到底层—物理连接中的过程。TCP 的多路复用请求会在一条物理连接上创建若干个虚拟连接，每个虚拟连接负责流转各自对应的数据流。严格讲：TCP 并不能多路复用，只是提供可靠的消息交付语义保证，如自动重传丢失的报文。

2 何时创建 TCP 连接？
（1）在创建 KafkaProducer 实例时，
A：生产者应用会在后台创建并启动一个名为 Sender 的线程，该 Sender 线程开始运行时，首先会创建与 Broker 的连接。
B：此时不知道要连接哪个 Broker，kafka 会通过 METADATA 请求获取集群的元数据，连接所有的 Broker。
（2）还可能在更新元数据后，或在消息发送时
3 何时关闭 TCP 连接
（1）Producer 端关闭 TCP 连接的方式有两种：用户主动关闭，或 kafka 自动关闭。
A：用户主动关闭，通过调用 producer.close()方关闭，也包括 kill -9 暴力关闭。
B：Kafka 自动关闭，这与 Producer 端参数 connection.max.idles.ms 的值有关，默认为 9 分钟，9 分钟内没有任何请求流过，就会被自动关闭。这个参数可以调整。
C：第二种方式中，TCP 连接是在 Broker 端被关闭的，但这个连接请求是客户端发起的，对 TCP 而言这是被动的关闭，被动关闭会产生大量的 CLOSE_WAIT 连接。
