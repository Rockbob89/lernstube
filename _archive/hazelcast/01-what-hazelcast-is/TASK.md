# Task 01: What Hazelcast Is

## Objective
Understand what Hazelcast is, how it differs from Redis, and when to use it.

## What to Learn
- Hazelcast as an In-Memory Data Grid (IMDG) vs a simple cache
  ```python
  # Redis: key-value cache — data lives on the server, fetched on demand
  # Hazelcast: data is partitioned across all members AND compute runs where data lives
  # In embedded mode, your app IS a cluster member — no network hop at all
  ```
- Embedded vs client-server vs cloud deployment modes
  ```python
  # Embedded: app process joins the cluster
  import hazelcast
  client = hazelcast.HazelcastClient()  # Python always uses client-server mode
  # Embedded is Java-only; in Python you're always a thin client
  ```
- Hazelcast vs Redis: data partitioning, embedded mode, compute colocation, CP subsystem
- Hazelcast vs Memcached, Ignite, Coherence
- When Hazelcast wins: distributed compute, near-cache, embedded mode, Java-native
- When Redis wins: simplicity, protocol ecosystem, Lua scripting, pub/sub
- Hazelcast Platform = IMDG + Jet (stream processing)

## Exercises

1. **Comparison function**: Write a function that takes two technology names (from a known set: hazelcast, redis, memcached, ignite) and returns a structured comparison across dimensions: data model, clustering, compute, persistence, language support, licensing.

2. **Use case matcher**: Write a function that takes a use case description (as a dict of requirements) and returns the best-fit technology with reasoning. Requirements include: `need_compute` (bool), `embedded_mode` (bool), `data_size_gb` (int), `language` (str), `latency_requirement_ms` (int).

3. **Architecture describer**: Write a function that takes a deployment mode ("embedded", "client-server", "cloud") and returns the architecture details: components, communication pattern, pros, cons.
