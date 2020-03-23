# 【第三期】21 天打卡行动

#21 天打卡# Day28
专栏：kafka 核心技术与实战
时间：2020-03-22
学习：10
学习要点和总结：

一、[10 | 生产者压缩算法面面观](https://time.geekbang.org/column/article/102132)

1. 压缩（compression），它秉承了用时间去换空间的经典 trade-off 思想，具体来说就是用 CPU 时间去换磁盘空间或网络 I/O 传输量，希望以较小的 CPU 开销带来更少的磁盘占用或更少的网络 I/O 传输。
2. 目前 Kafka 共有两大类消息格式，社区分别称之为 V1 版本和 V2 版本。V2 版本是 Kafka 0.11.0.0 中正式引入的。
3. Kafka 的消息层次都分为两层：消息集合（message set）以及消息（message）。一个消息集合中包含若干条日志项（record item），而日志项才是真正封装消息的地方。Kafka 底层的消息日志由一系列消息集合日志项组成。
4. 原来在 V1 版本中，每条消息都需要执行 CRC 校验，但有些情况下消息的 CRC 值是会发生变化的。在 V2 版本中，消息的 CRC 校验工作就被移到了消息集合这一层。
5. 之前 V1 版本中保存压缩消息的方法是把多条消息进行压缩然后保存到外层消息的消息体字段中；而 V2 版本的做法是对整个消息集合进行压缩。显然后者应该比前者有更好的压缩效果。
6. 在 Kafka 中，压缩可能发生在两个地方：生产者端和 Broker 端。生产者程序中配置 compression.type 参数即表示启用指定类型的压缩算法
7. 有两种例外情况就可能让 Broker 重新压缩消息。1. Broker 端指定了和 Producer 端不同的压缩算法。2. Broker 端发生了消息格式转换。
8. Producer 端压缩、Broker 端保持、Consumer 端解压缩。
9. 在 Kafka 2.1.0 版本之前，Kafka 支持 3 种压缩算法：GZIP、Snappy 和 LZ4。从 2.1.0 开始，Kafka 正式支持 Zstandard 算法（简写为 zstd）。它是 Facebook 开源的一个压缩算法，能够提供超高的压缩比（compression ratio）。
10. 在吞吐量方面：LZ4 > Snappy > zstd 和 GZIP；而在压缩比方面，zstd > LZ4 > GZIP > Snappy。具体到物理资源，使用 Snappy 算法占用的网络带宽最多，zstd 最少
11. CPU 资源充足这一条件，如果你的环境中带宽资源有限，那么我也建议你开启压缩。
