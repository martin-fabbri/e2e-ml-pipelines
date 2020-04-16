# Apache Kafka as a Stream Processing Tool

* In Kafka, an event describes something that has occurred, as opposed to a request for an action to be performed
* Kafka is distributed by default.
* Fault-tolerant by design, meaning it is hard to lose data if a node is suddenly lost
* Kafka scales from 1 to thousands of nodes
* Kafka provides ordering guarantees for data stored within it, meaning that the order is data is received is the order in which data will be produced to customers
* Commonly used as a data store for popular streaming tools like Apache Spark, Flink and Samza.