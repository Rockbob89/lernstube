# Task 2: Architecture

## Objective
Understand Druid's distributed architecture, node types, data flow, and how segments work.

## What to Learn
- Segments: Druid's fundamental storage unit, immutable, columnar, time-partitioned
  - A segment covers one time interval (e.g., one hour), stored as a set of column files plus an index. Once written, it is never mutated — only replaced.
- Node types and their roles:
  - **Historical**: serves immutable segments from deep storage
  - **Broker**: routes queries, merges results from Historicals and MiddleManagers
  - **Coordinator**: manages segment assignment and balancing across Historicals
  - **Overlord**: manages ingestion tasks
  - **MiddleManager/Peon**: executes ingestion tasks, serves real-time data
  - **Router**: optional query routing (often replaced by load balancer)
- Deep storage (S3, HDFS, local) vs segment cache on Historicals
  - Deep storage is the durable source of truth; Historicals cache hot segments on local SSD. A Historical can reload any segment from deep storage after a restart.
- Metadata store (PostgreSQL/MySQL) and ZooKeeper's role
  - Metadata store tracks which segments exist and their assignment; ZooKeeper coordinates leader election and cluster membership signals between nodes.
- How a query flows from client to result
  - Client -> Broker (parses, prunes segments by time/interval) -> Historicals & MiddleManagers (scan relevant segments in parallel) -> Broker (merges partial results) -> Client

## Exercises

1. **Architecture diagram**: In the solution file, write a function that returns a dict describing the query flow. Map each step from "client sends query" to "client receives result", naming which node handles each step.

2. **Node failure analysis**: For each node type, describe what happens if a single instance goes down. Which failures cause data loss? Which cause query failures? Which are self-healing?

3. **Capacity planning**: Given a cluster with 3 Historicals (each 64GB RAM, 1TB SSD), estimate how much data (in raw event count) the cluster can serve if average segment size is 500MB, segment-to-raw-data ratio is roughly 10:1 compression, and average raw event size is 200 bytes.
