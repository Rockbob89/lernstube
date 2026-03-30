# Task 04: Serialization

## Objective
Understand Hazelcast's serialization strategies and their tradeoffs.

## What to Learn
- Why serialization matters in distributed systems: every network transfer and storage operation
- Default Java serialization: slow, bloated, not cross-language
- `IdentifiedDataSerializable` — fast, compact, Java-only
- `Portable` — cross-language, schema evolution, field-level access without deserialization
  ```
  # Portable stores a field index so Hazelcast can read field "age" without deserializing
  # the whole object — useful for queries and map predicates
  ```
- `Compact` (newer) — zero-config, schema evolution, automatic
  ```python
  # Compact: Python client sends schema on first use; no annotation needed
  imap.put("u1", {"name": "Alice", "age": 30})  # schema inferred automatically
  ```
- Custom serializers via `StreamSerializer`
- Performance hierarchy: Compact > IdentifiedDataSerializable > Portable > Java Serializable
- Schema evolution: adding/removing fields without breaking

## Exercises

1. **Serializer comparison**: Write functions that simulate different serialization strategies. Given an object, serialize it as JSON (like default Java serialization — verbose), a compact binary format (like Compact/IdentifiedDataSerializable), and a field-indexed format (like Portable — supports partial deserialization). Compare output sizes.

2. **Schema evolution**: Implement a versioned serializer that handles schema evolution. Write v1 of a User object, then v2 with an added field and a removed field. Demonstrate deserializing v1 data with v2 schema and vice versa.

3. **Serialization benchmark**: Write a benchmarking function that serializes/deserializes an object N times with different strategies and reports throughput and size metrics.
