# Apache Kafka as a Stream Processing Tool

## Key Concepts
* In Kafka, an event describes something that has occurred, as opposed to a request for an action to be performed
* Kafka is distributed by default.
* Fault-tolerant by design, meaning it is hard to lose data if a node is suddenly lost
* Kafka scales from 1 to thousands of nodes
* Kafka provides ordering guarantees for data stored within it, meaning that the order is data is received is the order in which data will be produced to customers
* Commonly used as a data store for popular streaming tools like Apache Spark, Flink and Samza.

## Industry use cases

* The term _source_ is sometimes used to refer to Kafka clients which are producing data into Kafka, typically in reference to another data store

* The term _sink_ is sometimes used to refer to Kafka clients which are extracting data from Kafka

## Kafka Topics

* Used to organize related events and segment datasets, similar to SQL database tables
* Unlike SQL database tables, Kafka Topics **are not queryable**.
* May be created programmatically, from a CLI or automatically
* All **data** is in key-value form






