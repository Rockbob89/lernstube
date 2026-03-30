# Task 03: Distributed Computing

## Objective
Understand Hazelcast's distributed compute capabilities: EntryProcessors, executor service, and pipelines.

## What to Learn
- `EntryProcessor` — execute code on the data-owning member (no network transfer of data)
  ```python
  # Instead of: get(key) → modify locally → put(key)  [3 network hops]
  # EntryProcessor runs the function on the owning member [0 hops for data]
  imap.execute_on_key("user:1", lambda entry: entry.set_value(entry.value() + 1))
  ```
- `IExecutorService` — submit tasks to cluster members
  ```python
  executor = client.get_executor("compute").blocking()
  # Submit to a specific member or round-robin across all
  future = executor.submit_to_all_members(my_callable)
  ```
- Member-targeted vs key-targeted vs all-members execution
- Colocation: running compute where data lives
- Pipeline API for chaining operations
- When to use EntryProcessor vs executor vs Jet

## Exercises

1. **EntryProcessor simulator**: Implement an `EntryProcessor` pattern. Given a distributed map (simulated as a partitioned dict across "nodes"), apply a transformation function on the owning node without transferring the data. Compare with "fetch-modify-put" approach and count network hops.

2. **Executor service**: Build a simplified distributed executor that can submit callables to specific members or round-robin across all members. Track where each task executed and collect results.

3. **Compute colocation analyzer**: Write a function that takes a list of operations (each with a type: "entry-processor", "fetch-modify-put", "executor-targeted", "executor-broadcast") and a simulated cluster topology, and calculates the total network cost (hops) of each strategy. Demonstrate why colocating compute with data is cheaper for large-scale operations.
