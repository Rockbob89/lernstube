# Task 05: Persistence & WAN Replication

## Objective
Understand Hazelcast's persistence mechanisms and WAN replication for multi-datacenter deployments.

## What to Learn
- Hot Restart (Persistence): survive full cluster restarts, store data on disk
- `MapStore` / `MapLoader`: write-through, write-behind to external databases
  ```
  MapStore interface (Java):
    store(key, value)      → called on every put (write-through)
    storeAll(map)          → called in batches (write-behind)
    load(key) → value      → called on cache miss
  write-behind: writes buffered and flushed every N seconds — risk of data loss on crash
  ```
- Write-behind batching and coalescing
  ```
  coalescing: if key "u1" is updated 100x before flush, only the last value is written
  no coalescing: all 100 updates written in order — useful for audit logs
  ```
- WAN Replication: active-passive vs active-active between clusters
- Conflict resolution in active-active: `LATEST_UPDATE`, `HIGHEST_HITS`, custom merge policies
- Consistency tradeoffs: CAP theorem in practice

## Exercises

1. **MapStore simulator**: Implement a `MapStore` pattern with write-through and write-behind modes. In write-behind mode, batch writes and support coalescing (multiple updates to same key = single write).

2. **WAN replication simulator**: Build two simulated clusters. Implement active-passive replication (writes on primary replicate to backup) and active-active with conflict detection. Use timestamps for conflict detection and resolution.

3. **Merge policy engine**: Write a function that takes two conflicting entries (from different clusters) and resolves them using different strategies: latest-update-wins, highest-hits-wins, and a custom merge function.
