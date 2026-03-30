"""
Task 4: Querying — Native Query Solutions
"""

import json


def timeseries_query() -> dict:
    """
    Exercise 2a: Native timeseries query.
    Total request count and average response time, HOUR granularity, last 7 days.
    """
    return {
        "queryType": "timeseries",
        "dataSource": "web-access-logs",
        "intervals": [],
        "granularity": "",
        "aggregations": [],
        "postAggregations": [],
    }


def topn_query() -> dict:
    """
    Exercise 2b: Native topN query.
    Top 5 client IPs by request count.
    """
    return {
        "queryType": "topN",
        "dataSource": "web-access-logs",
        "dimension": "",
        "threshold": 0,
        "metric": "",
        "intervals": [],
        "granularity": "",
        "aggregations": [],
    }


def groupby_query() -> dict:
    """
    Exercise 2c: Native groupBy query.
    Request count grouped by method and status_code.
    """
    return {
        "queryType": "groupBy",
        "dataSource": "web-access-logs",
        "dimensions": [],
        "intervals": [],
        "granularity": "",
        "aggregations": [],
    }


def optimization_strategies() -> list[str]:
    """
    Exercise 3: Three strategies to speed up a groupBy on high-cardinality
    'path' dimension (500K unique values, 30s timeout).
    """
    return [
        "",  # Strategy 1
        "",  # Strategy 2
        "",  # Strategy 3
    ]


if __name__ == "__main__":
    print("=== Exercise 2a: Timeseries Query ===")
    print(json.dumps(timeseries_query(), indent=2))

    print("\n=== Exercise 2b: TopN Query ===")
    print(json.dumps(topn_query(), indent=2))

    print("\n=== Exercise 2c: GroupBy Query ===")
    print(json.dumps(groupby_query(), indent=2))

    print("\n=== Exercise 3: Optimization Strategies ===")
    for i, s in enumerate(optimization_strategies(), 1):
        print(f"  {i}. {s}")
