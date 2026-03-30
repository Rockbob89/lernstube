"""
Task 3: Ingestion — Solutions

Build Druid ingestion specs as Python dicts (JSON-serializable).
"""

import json


def batch_ingestion_spec() -> dict:
    """
    Exercise 1: Return a native batch ingestion spec for web access logs.

    Fields: timestamp, method, path, status_code, response_time_ms,
            user_agent, client_ip

    Requirements:
    - Choose dimensions vs metrics appropriately
    - HOUR segment granularity
    - Source: local CSV file at /data/access-logs.csv
    """
    spec = {
        "type": "index_parallel",
        "spec": {
            "dataSchema": {
                "dataSource": "",
                "timestampSpec": {},
                "dimensionsSpec": {"dimensions": []},
                "metricsSpec": [],
                "granularitySpec": {},
            },
            "ioConfig": {},
            "tuningConfig": {},
        },
    }
    return spec


def kafka_ingestion_spec() -> dict:
    """
    Exercise 2: Return a Kafka ingestion (supervisor) spec for the same
    access log data. Kafka topic: web-access-logs, broker: localhost:9092.
    """
    spec = {
        "type": "kafka",
        "spec": {
            "dataSchema": {
                "dataSource": "",
                "timestampSpec": {},
                "dimensionsSpec": {"dimensions": []},
                "metricsSpec": [],
                "granularitySpec": {},
            },
            "ioConfig": {},
            "tuningConfig": {},
        },
    }
    return spec


def rollup_comparison() -> dict[str, dict]:
    """
    Exercise 3: Return two ingestion spec fragments (just the dataSchema part):
    - "with_rollup": rollup enabled, pick a query granularity, define aggregations
    - "without_rollup": rollup disabled

    Include a "tradeoff" key with your explanation.
    """
    return {
        "with_rollup": {
            "dataSchema": {},
        },
        "without_rollup": {
            "dataSchema": {},
        },
        "tradeoff": "",
    }


if __name__ == "__main__":
    print("=== Exercise 1: Batch Ingestion Spec ===")
    print(json.dumps(batch_ingestion_spec(), indent=2))

    print("\n=== Exercise 2: Kafka Ingestion Spec ===")
    print(json.dumps(kafka_ingestion_spec(), indent=2))

    print("\n=== Exercise 3: Rollup Comparison ===")
    result = rollup_comparison()
    print(json.dumps(result["with_rollup"], indent=2))
    print(json.dumps(result["without_rollup"], indent=2))
    print(f"Tradeoff: {result['tradeoff']}")
