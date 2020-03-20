# 【第三期】21 天打卡行动

#21 天打卡# Day27
专栏：kafka 核心技术与实战
时间：2020-03-19
学习：08
学习要点和总结：

一、[07 | 最最最重要的集群参数配置（下）](https://time.geekbang.org/column/article/101763)

1. Topic 级别的参数：

2. (1) 创建 Topic 时进行设置: bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic transaction --partitions 1 --replication-factor 1 --config retention.ms=15552000000 --config max.message.bytes=5242880 (2) 修改 Topic 时设置: bin/kafka-configs.sh --zookeeper localhost:2181 --entity-type topics --entity-name transaction --alter --add-config max.message.bytes=10485760

3. 我个人极其不推荐将 Kafka 运行在 Java 6 或 7 的环境上。
4. KAFKA_HEAP_OPTS：指定堆大小。通用的建议：将你的 JVM 堆大小设置成 6GB 吧。
5. KAFKA_JVM_PERFORMANCE_OPTS：指定 GC 参数。Java8 下，垃圾回收器的设置就用默认的 G1 收集器。

$> export KAFKA_HEAP_OPTS=--Xms6g  --Xmx6g
$> export KAFKA_JVM_PERFORMANCE_OPTS= -server -XX:+UseG1GC -XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:+ExplicitGCInvokesConcurrent -Djava.awt.headless=true
\$> bin/kafka-server-start.sh config/server.properties

7. 系统参数：文件描述符限制：ulimit -n 1000000；文件系统类型：最好为 XFS；swappniess：个人建议将 swappniess 配置成一个接近 0 但不为 0 的值，比如 1；
