# Task 02: Cluster & Data Structures

## Objective
Understand Hazelcast clustering, partitioning, and core distributed data structures.

## What to Learn
- Cluster formation: multicast, TCP/IP, cloud discovery
- Partitioning: 271 partitions, partition ownership, rebalancing
  ```
  key → hash → partition_id (0-270) → owning member
  Adding a member triggers rebalancing: partitions redistribute so each member owns ~271/N
  ```
- `IMap` — distributed map, near-cache, entry listeners, MapStore
  ```python
  imap = client.get_map("users").blocking()
  imap.put("u1", {"name": "Alice"})
  val = imap.get("u1")  # routed to the member owning partition for "u1"
  ```
- `IQueue` — distributed bounded queue
  ```python
  queue = client.get_queue("jobs").blocking()
  queue.put("task-1")
  job = queue.take()  # blocks until item available
  ```
- `ISet`, `IList` — distributed collections
- `ReplicatedMap` — fully replicated across all members
  ```python
  # ReplicatedMap: every member holds all data — fast reads, more memory
  rmap = client.get_replicated_map("config").blocking()
  rmap.put("timeout", 30)
  ```
- Near-cache: local cache on top of distributed map, invalidation
- Partition awareness: key-based routing

## Exercises

1. **Partition simulator**: Write a function that simulates Hazelcast's consistent hashing. Given N members and a list of keys, assign each key to a partition (0-270), then assign partitions to members. Show rebalancing when a member is added/removed.

2. **Data structure chooser**: Write a function that takes requirements (access pattern, size, consistency needs, read/write ratio) and recommends the best Hazelcast data structure with configuration hints.

3. **Near-cache simulator**: Implement a simplified near-cache that wraps a "remote" dict. Track hit/miss rates, support TTL-based invalidation, and max-size eviction (LRU).
