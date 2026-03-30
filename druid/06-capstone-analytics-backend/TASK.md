# Task 6: Capstone — Analytics Backend

## Objective
Combine everything: ingest event data into Druid, model it for analytics, and build a set of queries that could power a real-time dashboard.

## Scenario
You are building the analytics backend for a ride-sharing platform. The platform generates ride events with these fields:

```
ride_id, timestamp, city, neighborhood, driver_id, rider_id,
ride_type (standard/premium/pool), distance_km, duration_min,
fare_amount, surge_multiplier, payment_method, rating
```

Volume: ~50M rides/day, 30-day retention.

## Deliverables

1. **Data model** (`model.json`): A complete Druid `dataSchema` with justified choices for dimensions, metrics, rollup, and granularity.

2. **Ingestion spec** (`ingestion.json`): A complete Kafka supervisor spec. Topic: `ride-events`, broker: `kafka.internal:9092`. Include tuning for the given volume.

3. **Query suite** (`queries.sql`): Druid SQL queries for these dashboard panels:
   - Total rides and revenue, last 24h, by city
   - Average fare and duration by ride type, last 7 days
   - Top 10 neighborhoods by ride count, current hour
   - Surge pricing distribution (avg surge multiplier by hour of day), last 30 days
   - Driver performance: top 20 drivers by ride count with average rating > 4.5, last 7 days
   - Real-time: rides per minute for the last 60 minutes

4. **Ops runbook** (`runbook.md`): Short answers (2-3 sentences each):
   - How to handle a Historical node failure
   - How to reindex data after a schema change
   - How to tune for the 50M rides/day volume

## No solution stubs for this task. Build it from scratch.
