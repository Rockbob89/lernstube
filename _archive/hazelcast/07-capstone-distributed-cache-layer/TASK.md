# Task 07: Capstone — Distributed Cache Layer

## Objective
Add Hazelcast as a caching and compute layer to an existing application. Benchmark it against direct database access.

## What to Build
A Python application (simulated or real) that:
- Has a "database" layer (can be SQLite, a dict, or a mock)
- Adds Hazelcast as a caching layer with read-through/write-through patterns
- Uses near-cache for hot data
- Runs distributed compute (EntryProcessor pattern) for batch operations
- Includes a Jet-style pipeline for aggregation queries

## Requirements
1. Implement the MapStore pattern: cache reads/writes backed by DB
2. Near-cache for frequently accessed keys with TTL
3. At least one EntryProcessor-style operation (modify data without transferring it)
4. A streaming pipeline that aggregates data (e.g., compute stats across all users)
5. Benchmark: measure latency and throughput for cache-hit, cache-miss, and direct-DB paths
6. Write a short report (`REPORT.md`) with benchmark results and architecture decisions

## Deliverables
- `solution.py` with the full implementation
- `REPORT.md` with architecture decisions, benchmark results, and when you would/wouldn't use Hazelcast
- All code should be runnable without a real Hazelcast cluster (use your simulators from previous tasks)

## Evaluation Criteria
- Correct application of MapStore, near-cache, and compute patterns
- Meaningful benchmarks with realistic data volumes
- Clear separation of concerns: DB layer, cache layer, compute layer
- Honest assessment of tradeoffs in the report
