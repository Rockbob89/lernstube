"""
Task 5: SQL Warehouses — Solutions (Exercise 3)
"""


def warehouse_sizing() -> list[dict]:
    """
    Exercise 3: Recommend warehouse size and type for each workload.
    """
    return [
        {
            "workload": "Ad-hoc analyst queries (5 concurrent, interactive)",
            "warehouse_type": "",  # serverless or classic
            "size": "",  # Small/Medium/Large/etc
            "auto_stop_minutes": 0,
            "scaling_policy": "",
            "justification": "",
        },
        {
            "workload": "Nightly dashboard refresh (20 dashboards)",
            "warehouse_type": "",
            "size": "",
            "auto_stop_minutes": 0,
            "scaling_policy": "",
            "justification": "",
        },
        {
            "workload": "Real-time operational dashboard (continuous)",
            "warehouse_type": "",
            "size": "",
            "auto_stop_minutes": 0,
            "scaling_policy": "",
            "justification": "",
        },
    ]


def explain_output_guide() -> str:
    """
    Exercise 2c: What to look for in EXPLAIN output.
    Return your analysis guide.
    """
    return ""


if __name__ == "__main__":
    print("=== Exercise 3: Warehouse Sizing ===")
    for config in warehouse_sizing():
        print(f"\n  Workload: {config['workload']}")
        for k, v in config.items():
            if k != "workload":
                print(f"    {k}: {v}")

    print("\n=== Exercise 2c: EXPLAIN Guide ===")
    print(explain_output_guide())
