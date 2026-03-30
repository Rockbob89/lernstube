"""
Task 1: Platform Overview — Solutions
"""


def component_mapping() -> dict[str, str]:
    """
    Exercise 1: Map Databricks components to open-source/cloud-native equivalents.
    """
    return {
        "workspace_notebooks": "",
        "unity_catalog": "",
        "job_clusters": "",
        "dbfs": "",
        "delta_live_tables": "",
        "sql_warehouse": "",
    }


def cluster_configuration() -> dict:
    """
    Exercise 2: Design a cluster config for a nightly ETL job (500GB Parquet).

    Return a dict with config keys and a 'justification' dict.
    """
    return {
        "cluster_type": "",
        "node_type": "",
        "num_workers": 0,
        "autoscaling": {
            "min_workers": 0,
            "max_workers": 0,
        },
        "spot_ratio": "",
        "driver_node_type": "",
        "spark_config": {},
        "justification": {
            "cluster_type": "",
            "node_type": "",
            "autoscaling": "",
            "spot_ratio": "",
        },
    }


def cost_analysis() -> dict:
    """
    Exercise 3: Compare Spark-on-EKS (10x r5.2xlarge) vs Databricks.

    Return:
    - "eks_monthly_cost": estimated EKS cost
    - "databricks_monthly_cost": estimated Databricks cost
    - "cost_breakdown": how you calculated it
    - "justifying_features": list of Databricks features worth the premium
    """
    return {
        "eks_monthly_cost": "",
        "databricks_monthly_cost": "",
        "cost_breakdown": "",
        "justifying_features": [],
    }


if __name__ == "__main__":
    print("=== Exercise 1: Component Mapping ===")
    for component, equivalent in component_mapping().items():
        print(f"  {component} -> {equivalent}")

    print("\n=== Exercise 2: Cluster Configuration ===")
    config = cluster_configuration()
    for k, v in config.items():
        if k != "justification":
            print(f"  {k}: {v}")
    print("  Justifications:")
    for k, v in config["justification"].items():
        print(f"    {k}: {v}")

    print("\n=== Exercise 3: Cost Analysis ===")
    analysis = cost_analysis()
    for k, v in analysis.items():
        print(f"  {k}: {v}")
