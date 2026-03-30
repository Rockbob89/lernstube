"""
Task 5: Data Modeling — Solutions
"""

import json


def ecommerce_schema() -> dict:
    """
    Exercise 1: Design a Druid dataSchema for e-commerce order events.

    Return a dict with:
    - "dataSchema": the full dataSchema spec
    - "justification": dict mapping each decision to a reason
    """
    return {
        "dataSchema": {
            "dataSource": "ecommerce-orders",
            "timestampSpec": {},
            "dimensionsSpec": {"dimensions": []},
            "metricsSpec": [],
            "granularitySpec": {},
        },
        "justification": {
            "dimensions": "",
            "metrics": "",
            "rollup": "",
            "segment_granularity": "",
            "dropped_fields": "",
        },
    }


def schema_comparison() -> dict:
    """
    Exercise 2: Two schemas for the same data, optimized differently.

    Return:
    - "schema_a": dataSchema optimized for revenue dashboards
    - "schema_b": dataSchema optimized for per-order drill-down
    - "explanation": why they differ
    """
    return {
        "schema_a": {"dataSchema": {}},
        "schema_b": {"dataSchema": {}},
        "explanation": "",
    }


def cardinality_analysis() -> dict:
    """
    Exercise 3: Handle high-cardinality referrer_url (2M unique values).

    Return:
    - "impact": what happens to Druid with 2M unique dimension values
    - "approach_1": first mitigation strategy
    - "approach_2": second mitigation strategy
    """
    return {
        "impact": "",
        "approach_1": "",
        "approach_2": "",
    }


if __name__ == "__main__":
    print("=== Exercise 1: E-commerce Schema ===")
    result = ecommerce_schema()
    print(json.dumps(result["dataSchema"], indent=2))
    print("Justification:")
    for k, v in result["justification"].items():
        print(f"  {k}: {v}")

    print("\n=== Exercise 2: Schema Comparison ===")
    comp = schema_comparison()
    print(f"Explanation: {comp['explanation']}")

    print("\n=== Exercise 3: Cardinality Analysis ===")
    ca = cardinality_analysis()
    for k, v in ca.items():
        print(f"  {k}: {v}")
