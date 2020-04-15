# Stream vs. Batch processing

## Batch Processing

* Runs on a scheduled basis
* May run for a longer period of time and write results to a SQL-like store.
* May analyze all historical data at once.
* Typically works with mutable data and data stores.

## Stream Processing

* Runs at whatever frequency events are generated.
* Typically runs quickly, updating in-memory aggregates
* Stream processing applications may simply emit events themselves, rather than write to an event store.
* Typically analyses trends over a limited period of time due to data volume.
* Typically analyses immutable data and data stores.

Batch and Stream processing are not mutually exclusive. Batch systems can create events to feed into stream processing applications, and similarly, stream processing applications can be part of batch processing analyses.

## Components of a Stream Processing Solution

### Streaming Data Store

* May look like a _message queue_, as is the case with Apache Kafka
* May look like a _SQL store_, as it the case with Apache Cassandra
* Responsible for holding all of the immutable event data in the system
* Provides _guarantee_ that data is stored ordered according to the _time it was produced_
* Provides _guarantee_ that data is produced to consumers in the order it was received
* Provides guarantee that the events it stores are immutable and unchangeable

### Stream Processing Application and Frameworks

* Stream processing applications sit downstream of the data store
* Stream processing applications ingest real-time event data from one or more data streams
* Stream processing applications aggregate, join, and find differences in data from these streams
* Common stream processing applications include:
    * Confluent KSQL
    * Kafka Streams
    * Apache Flink
    * Apache Samza
    * Apache Spark Structure Streaming
    * Faust Python Library

### Benefits of Stream Processing

* Faster for scenarios where a limited set of recent data is needed
* More scalable due to distributed nature of storage
* Provides a useful abstraction that decouples applications from each other
* Allows one set of data to satisfy many use-cases which may not have been predictable when the dataset was originally created
* Built-in ability to replay events and observe exactly what occurred, and in what order, providers more opportunities to recover from error states or dig into how a particular result was arrived at








