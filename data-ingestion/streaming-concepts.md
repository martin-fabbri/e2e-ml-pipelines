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








