"""
Task 1: What Druid Is — Solutions

Exercise 1: Classification
Fill in your answers below.
"""


def classify_workloads() -> dict[str, str]:
    """
    Return a dict mapping each workload to "good fit" or "bad fit"
    with a one-sentence reason.
    """
    workloads = {
        "clickstream_analytics_1B_events_day": "",
        "ecommerce_product_catalog_fulltext": "",
        "iot_sensor_timeseries_500k_eps": "",
        "financial_ledger_acid_joins": "",
        "log_aggregation_freetext_alerting": "",
        "adtech_bid_analytics_subsecond_p99": "",
    }
    return workloads


def comparison_matrix() -> list[dict]:
    """
    Exercise 2: Return a list of dicts, one per system.
    Each dict has keys: system, query_latency, ingest_model,
    join_support, storage_model, typical_use_case, operational_complexity.
    """
    systems = [
        {
            "system": "Druid",
            "query_latency": "",
            "ingest_model": "",
            "join_support": "",
            "storage_model": "",
            "typical_use_case": "",
            "operational_complexity": "",
        },
        {
            "system": "ClickHouse",
            "query_latency": "",
            "ingest_model": "",
            "join_support": "",
            "storage_model": "",
            "typical_use_case": "",
            "operational_complexity": "",
        },
        {
            "system": "Elasticsearch",
            "query_latency": "",
            "ingest_model": "",
            "join_support": "",
            "storage_model": "",
            "typical_use_case": "",
            "operational_complexity": "",
        },
        {
            "system": "BigQuery",
            "query_latency": "",
            "ingest_model": "",
            "join_support": "",
            "storage_model": "",
            "typical_use_case": "",
            "operational_complexity": "",
        },
    ]
    return systems


def decision_document() -> str:
    """
    Exercise 3: Return your decision document as a string.
    Scenario: K8s platform, 200M events/day, sub-second dashboard queries.
    Compare Druid vs ClickHouse. Make a recommendation with trade-offs.
    (5-10 sentences)
    """
    return ""


if __name__ == "__main__":
    print("=== Exercise 1: Workload Classification ===")
    for workload, answer in classify_workloads().items():
        print(f"  {workload}: {answer}")

    print("\n=== Exercise 2: Comparison Matrix ===")
    for row in comparison_matrix():
        print(f"  {row['system']}:")
        for k, v in row.items():
            if k != "system":
                print(f"    {k}: {v}")

    print("\n=== Exercise 3: Decision Document ===")
    print(decision_document())
